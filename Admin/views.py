from django.shortcuts import render,redirect
from Registration_Login.models import *



def admin_dashboard(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details,emp_active_status=0)
        
        content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'employees':employees}

        return render(request,'AD_dashboard.html',content)

    else:
            return redirect('/')
    
    
#Appove Login 

def admin_login_approve(request,pk):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)

        employees_obj = EmployeeRegister_Details.objects.get(id=pk)
        employees_obj.emp_active_status = 1
        employees_obj.save()

        log_obj = LogRegister_Details.objects.get(id=employees_obj.logreg_id.id)
        log_obj.active_status=1
        log_obj.save()

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details,emp_active_status=0)
        
        content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'employees':employees}

        return render(request,'AD_dashboard.html',content)

    else:
            return redirect('/')


def admin_login_reject(request,pk):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)

        employees_obj = EmployeeRegister_Details.objects.get(id=pk)
        employees_obj.emp_active_status = 0
        employees_obj.save()

        log_obj = LogRegister_Details.objects.get(id=employees_obj.logreg_id.id)
        log_obj.active_status=2
        log_obj.save()

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details,emp_active_status=0)
        
        content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'employees':employees}

        return render(request,'AD_dashboard.html',content)

    else:
            return redirect('/')

# Department ---------------------

def admin_department(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)
        departments = DepartmentRegister_details.objects.filter(brd_id=dash_details)

        if request.POST:
             
            depart_obj = DepartmentRegister_details()
            depart_obj.dept_name = request.POST['department_name']
            depart_obj.dept_content = request.POST['department_discription']
            depart_obj.dept_active_status = 1
            depart_obj.brd_id = dash_details
            depart_obj.save()

            success = True
            success_text = 'New department created successfully '

            departments = DepartmentRegister_details.objects.filter(brd_id=dash_details)

        
            content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'success':success,
                   'success_text':success_text,
                   'departments':departments}
        else:
             
            content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                    'departments':departments}

        return render(request,'AD_department.html',content)

    else:
            return redirect('/')
    


# Designation ----------------------------

def admin_designation(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)

        departments = DepartmentRegister_details.objects.filter(brd_id=dash_details,dept_active_status=1)
        designations = DesignationRegister_details.objects.filter(dept_id__in=departments)

        if request.POST:
            
            desidnation_obj = DesignationRegister_details()

            desidnation_obj.desig_name = request.POST['designation_name']
            desidnation_obj.desig_content = request.POST['designation_discription']
            desidnation_obj.desig_brd_id = dash_details
            desidnation_obj.dept_id =  DepartmentRegister_details.objects.get(id=int(request.POST['deparmentId'])) 
            desidnation_obj.desig_active_status = 1
            desidnation_obj.dashboard_id = request.POST['dashboardId'] 
            desidnation_obj.save()

            success = True
            success_text = 'New designation add successfully '
            designations = DesignationRegister_details.objects.filter(dept_id__in=departments)

            content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'departments':departments,
                   'designations':designations,
                   'success':success,
                   'success_text':success_text
                   }

        else:
            
            content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'departments':departments,
                   'designations':designations
                   }

        return render(request,'AD_designation.html',content)

    else:
            return redirect('/')
     



def admin_logout(request):
    request.session.pop('admin_id', None)
    return redirect('login_page')
     


