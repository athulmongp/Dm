from django.shortcuts import render,redirect
from Registration_Login.models import *
from .models import *


def TC_dashbord(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        
        
        content = {'emp_dash':emp_dash,'dash_details':dash_details} 

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
        data = Leads_assignto_tc.objects.filter(TC_Id= dash_details.id)
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
        
        
    
        data = Leads_assignto_tc.objects.filter(TC_Id=dash_details.id,leadId__lead_work_regId__clientId=id)
        print(emp_id)
       
        
       
        
        content = {'emp_dash':emp_dash,'dash_details':dash_details,'data':data}

        return render(request,'TC_current_clients_details.html',content)

    else:
            return redirect('/')
    
