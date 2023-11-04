from django.db import models
from  Registration_Login.models import EmployeeRegister_Details,BusinessRegister_Details
from DM_Head.models import *


class Leads_assignto_tc(models.Model):
    leadId = models.ForeignKey(Leads, on_delete=models.CASCADE, null=True,default='')
    TC_Id =  models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    Response = models.CharField(max_length=255,default='',null=True,blank=True)
    Reason = models.CharField(max_length=255,default='',null=True,blank=True)
    Assign_Date = models.DateField(auto_now=True,null=True)
    Update_Date = models.DateField(max_length=255,null=True,blank=True,default='')
    Update_Action = models.IntegerField(default=0)
    Status = models.IntegerField(default=0)
    Record = models.FileField(upload_to=r'record',default='')




