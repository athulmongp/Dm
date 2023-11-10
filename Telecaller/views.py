from django.shortcuts import render,redirect
from Registration_Login.models import *
from .models import *
from django.core import serializers
from django.db.models import Q
from django.utils import timezone
from datetime import date, datetime,timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count


def count_weekdays(start_date, end_date):
    current_date = start_date
    weekdays_count = 0

    # Iterate through each date within the range
    while current_date <= end_date:
        # Check if the current date is a weekday (Monday to Saturday)
        if current_date.weekday() < 6:
            weekdays_count += 1
        
        # Move to the next day
        current_date += timedelta(days=1)

    return weekdays_count

def TC_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details,Status =1,Update_Action=0)
        data1 = Leads_assignto_tc.objects.filter(TC_Id=dash_details,Status =0,Update_Action=0)
        data2 = Leads_assignto_tc.objects.filter(TC_Id=dash_details,Status =1,Update_Action=1)
        
        
        l=len(data)+len(data1)
        l2=len(data2)

        
        
        content = {'emp_dash':emp_dash,'dash_details':dash_details,'l':l,'l2':l2} 

        return render(request,'TC_dashboard.html',content)

    else:
            return redirect('/')

    

def TC_current_clients(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data =  Leads_assignto_tc.objects.filter(TC_Id=dash_details,Update_Action=0)

        print(data)
        

        client = WorkRegister.objects.all()
        
       
        
        content = {'emp_dash':emp_dash,'dash_details':dash_details,'data':data,'client':client}

        return render(request,'TC_current_clients.html',content)

    else:
            return redirect('/')
    

def TC_current_clients_details(request,id):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        
        
    
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details.id,leadId__lead_work_regId__clientId=id,Update_Action=0)
        print(emp_id)
       
        
       
        
        content = {'emp_dash':emp_dash,'dash_details':dash_details,'data':data}

        return render(request,'TC_current_clients_details.html',content)

    else:
            return redirect('/')
    
def TC_update_Clients_Response(request,id):
     if request.method == 'POST':
          response=request.POST['Response']
          reason=request.POST['Reason']
          record=request.FILES.get('record')
          next_date=request.POST['nud']
          ud=date.today()
          tc = Leads_assignto_tc.objects.get(id=id)
          if next_date != '':
              tc.Next_update_date=next_date

          
          

          tc.Response = response
          tc.Reason = reason
          tc.Update_Date=ud
          
          
          tc.save()
          if  record!='': 
            tcr=Leads_Call_Record(Leads_assignto_tc_id=tc,Record=record)
            tcr.save()
          
          if  response != 'waiting':
              data = Leads_assignto_tc.objects.filter(id=id).update(Update_Action = 1) 
          
          return redirect('TC_ongoing_leads',tc.client_id.id)
     
def TC_previous_clients(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data = Leads_assignto_tc.objects.filter(TC_Id= dash_details.id,Update_Action=1)
        print(data)
        

        client = WorkRegister.objects.all()
        
       
        
        content = {'emp_dash':emp_dash,'dash_details':dash_details,'data':data,'client':client}

        return render(request,'TC_previous_clients.html',content)

    else:
            return redirect('/')     
         
    
def TC_previous_clients_details(request,id):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        
        
    
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details.id,leadId__lead_work_regId__clientId=id,Update_Action=1)
        print(emp_id)
       
        
       
        
        content = {'emp_dash':emp_dash,'dash_details':dash_details,'data':data}

        return render(request,'TC_previous_clients_details.html',content)

    else:
            return redirect('/') 

def TC_profile(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        
        
        content = {'emp_dash':emp_dash,'dash_details':dash_details} 

        return render(request,'TC_profile.html',content)

    else:
            return redirect('/')    

    
def TC_profile_detailsUpdate(request):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        # Details Save -----------------

        if request.POST:
             
             emp_obj = EmployeeRegister_Details.objects.get(id=dash_details.id)

             emp_obj.emp_name = request.POST['empname']
             emp_obj.emp_contact_no = request.POST['contactno']
             emp_obj.emp_email = request.POST['empEmail']
             emp_obj.emp_address1 = request.POST['add1']
             emp_obj.emp_address2 = request.POST['add2']
             emp_obj.emp_address3 = request.POST['add3']
             emp_obj.emp_pin = request.POST['pincode']
             emp_obj.emp_location = request.POST['loc']
             emp_obj.emp_district = request.POST['empdist']
             emp_obj.emp_state = request.POST['empState']

             if request.FILES.get('empProfile'):
                emp_obj.emp_profile = request.FILES.get('empProfile')

             else:
                emp_obj.emp_profile =  emp_obj.emp_profile 

             if request.FILES.get('empResume'):
                emp_obj.emp_file = request.FILES.get('empResume')

             else:
                emp_obj.emp_file =  emp_obj.emp_file 

             emp_obj.save()
             success_text = 'Profile Details Updated.'
             success = True

             dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        
             content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'success_text':success_text,
                    'success':success}

        else:
            error_text = 'Profile Details Updated.'
            error = True
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error_text':error_text,
                    'error':error}

        return render(request,'TC_profile.html',content)

    else:
            return redirect('/')
    

# Remove Profile Image ---------------

def TC_profileImage_remove(request):
    emp_id = request.POST.get('emp_id')
    dash_details = EmployeeRegister_Details.objects.get(id=emp_id)
    dash_details.emp_profile = ''
    dash_details.save()
    return JsonResponse({'message': 'Received emp_id: ' + emp_id})
     
# End ------------------------------------------------     
    

def TC_leave(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

       
        
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        #Head Leave --------
        leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')

    
       
        if request.POST:
             
            leave_obj = EmployeeLeave()
            leave_obj.start_date = request.POST['fromDate']
            leave_obj.end_date = request.POST['toDate']
            leave_obj.leave_type = request.POST['type_select']
            leave_obj.leave_reason = request.POST['reason_content']
            leave_obj.leave_request_file = request.FILES.get('leave_requestFile')
            leave_obj.emp_id = dash_details
            leave_obj.leave_apply_date = date.today()

            # day calculation
                
            start_date_str = request.POST['fromDate']
            end_date_str = request.POST['toDate'] 

            # Convert the date strings to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

            # Calculate the difference in days
            weekdays_count = (count_weekdays(start_date, end_date))
                
            leave_obj.no_of_days = weekdays_count
            leave_obj.save()
                
            success=True
            success_text = 'Leave applied successfully, waiting for approvel.'

            leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
            

            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'success':success,
                    'success_text':success_text,'leave_data':leave_data}

        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'leave_data':leave_data}

        return render(request,'TC_leave.html',content)

    else:
            return redirect('/')

def TC_leave_search(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

       
        
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        #Head Leave --------
        leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')

       
        if request.POST:
             
            if request.POST['d1'] and request.POST['d2']:

                date1 = request.POST['d1'] 
                date2 = request.POST['d2']
                
                leave_data = EmployeeLeave.objects.filter(emp_id=dash_details,start_date__gte=date1,end_date__lte=date2)

                content = {'emp_dash':emp_dash,
                            'dash_details':dash_details,
                            'notifications':notifications,
                            'leave_data':leave_data
                            }    
             
            
        return render(request,'TC_leave.html',content)

    else:
            return redirect('/')    




# Action Taken -------------------

def TC_actionTaken(request):

    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        team = Allocation_Details.objects.filter(allocat_to=dash_details)
        team_ids = [t.allocatEmp_id_id for t in team]

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        employees = EmployeeRegister_Details.objects.filter(id__in=team_ids)
        action_taken_data = ActionTaken.objects.filter(act_from_id=dash_details.id).order_by('-id')
        tc_action_taken_data = ActionTaken.objects.filter(act_emp_id=dash_details).order_by('-id')

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data,
                   'tc_action_taken_data':tc_action_taken_data}

        return render(request,'TC_actionTaken.html',content)

    else:
            return redirect('/')

# Feedback -------------------------

def TC_feedback(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1)

        feedback_data = Feedback.objects.filter(feedback_emp_id__in=employees).exclude(
            Q(feedback_emp_id=dash_details) | Q(feedback_emp_id=None)).order_by('-id')


        # Saveing Feedback 
        if request.POST:

            feedback_obj = Feedback()
            feedback_obj.feedback_emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['to_id']))
            feedback_obj.from_id = dash_details.id
            feedback_obj.from_name = dash_details.emp_name
            feedback_obj.feedback_content = request.POST['feedback_content']
            feedback_obj.feedback_date = date.today()
            feedback_obj.save()

            success=True
            success_text = 'Feedback add successfully.'

            feedback_data =Feedback.objects.filter(feedback_emp_id__in=employees).exclude(
            Q(feedback_emp_id=dash_details) | Q(feedback_emp_id=None)).order_by('-id')

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,

                   'employees':employees,
                   'feedback_data':feedback_data,
                   'success':success,
                   'success_text':success_text}
        
        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,

                   'employees':employees,
                   'feedback_data':feedback_data}

        return render(request,'TC_feedback.html',content)

    else:
            return redirect('/')

def TC_feedback_Typechange(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        # employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1)

        selected_value = request.GET.get('value')
    
        if selected_value == '1':
            feedback_data =Feedback.objects.filter(from_id=dash_details.id)
        else:
            feedback_data =Feedback.objects.filter(feedback_emp_id=dash_details).order_by('-id')
        
        data_list = []
        for feedback in feedback_data:
            data = {
                'feedback_date': feedback.feedback_date,
               
                'from_name': feedback.from_name,
                
                'to_name': feedback.feedback_emp_id.emp_name,
                'feedback_content': feedback.feedback_content
            }
            data_list.append(data)
        
        return JsonResponse(data_list, safe=False)

def TC_complaints(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1)
        complaints_data = Complaints.objects.filter(complaint_emp_id=dash_details).order_by('status')

        
     

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'complaints_data':complaints_data,
                   'employees':employees,
                  }

        return render(request,'TC_complaints.html',content)

    else:
            return redirect('/')  
def TC_complaint_add(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)
         # Notification-----------
        # notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1)
        complaints_data = Complaints.objects.filter(complaint_emp_id__in=employees).order_by('status')
        if request.POST:
            emp_id= request.POST['to_id']
            emp= EmployeeRegister_Details.objects.get(id=emp_id)
            complaint=request.POST['complaint_content']
            complaint_date = date.today()
             
            data = Complaints(complaint_emp_id=emp,compaint_content=complaint,complaint_date=complaint_date) 
            data.save()

            success=True
            success_text = 'Response add successfully.'
           

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   
                   'complaints_data':complaints_data,
                   'employees':employees,
                   'success':success,
                   'success_text':success_text}
            return render(request,'TC_complaints.html',content)
        
def TC_leads(request,id):  
     if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)  
        id = id 
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'id':id
                  }
     return render(request,'TC_leads.html',content)     

def TC_newleads(request,id):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)  
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details,Update_Action=0,Status=0,client_id=id)
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'data':data,
                  }
    return render(request,'TC_newleads.html',content)   

def TC_newleads_accept(request,id):
    data=Leads_assignto_tc.objects.get(id=id)
    status = Leads_assignto_tc.objects.filter(id=id).update(Status = 1)
    return redirect('TC_newleads',data.client_id.id)

def TC_ongoing_leads(request,id):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)  
        
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details,Update_Action=0,Status=1,client_id=id)
        record =  Leads_Call_Record.objects.all()
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'data':data,
                   'record':record
                  }
    return render(request,'TC_ongoing_leads.html',content) 

def TC_waiting_leads(request,id):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)  
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details,Response='waiting',client_id=id)
        record =  Leads_Call_Record.objects.all()
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'data':data,
                   'record':record,
                  }
    return render(request,'TC_waiting_leads.html',content) 

def TC_rejected_leads(request,id):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)  
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details,Response='Not intrest',client_id=id)
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'data':data,
                  }
    return render(request,'TC_rejected_leads.html',content) 

def TC_completed_leads(request,id):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        print(dash_details.id)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)  
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details,Update_Action=1,Status=1,client_id=id)
        record =  Leads_Call_Record.objects.all()
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'data':data,
                   'record':record
                  }
    return render(request,'TC_completed_leads.html',content) 






           
