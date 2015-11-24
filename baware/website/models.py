from django.db import models
from django.contrib import admin

# Create your models here.
class policeData(models.Model): 
	CAD_CDW_ID 				    = models.IntegerField(default=0, max_length = 10)
	CAD_Event_Number 			= models.IntegerField(max_length = 15)
	General_Offense_Number 		= models.IntegerField(max_length = 20)
	Event_Clearance_Code 		= models.IntegerField(max_length = 5)
	Event_Clearance_Description	= models.CharField(max_length = 100)
	Event_Clearance_SubGroup	= models.CharField(max_length = 100)
	Event_Clearance_Group		= models.CharField(max_length = 100)
	Event_Clearance_Date		= models.DateTimeField()
	Hundred_Block_Location		= models.CharField(max_length = 100)
	District_Sector				= models.CharField(max_length = 5)	
	Zone_Beat					= models.CharField(max_length = 5)	
	Census_Tract				= models.DecimalField(max_digits=12, decimal_places=6)
	Longitude					= models.DecimalField(max_digits=16, decimal_places=12)
	Latitude					= models.DecimalField(max_digits=16, decimal_places=12)
	Incident_Location			= models.CharField(max_length = 40)
	Initial_Type_Description	= models.CharField(max_length = 120)
	Initial_Type_Subgroup		= models.CharField(max_length = 120)	
	Initial_Type_Group			= models.CharField(max_length = 120)	
	At_Scene_Time				= models.DateTimeField()

admin.site.register(policeData)
