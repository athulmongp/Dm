from django.shortcuts import render


def TC_dashbord(request):
    return render(request,'TC_dashboard.html')

def TC_current_clients(request):
    return render(request,'TC_current_clients.html')

def TC_current_clients_details(request):
    return render(request,'TC_current_clients_details.html')
