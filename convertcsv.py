import csv
from MySQLdb import connect

conn = connect("localhost", "root", "root", "policedb")
cursor = conn.cursor();
csvdata = csv.reader(file('policedata.csv'))

flag = False

for row in csvdata:
	if flag==False:
		flag=True
		continue
	
	cursor.execute('Insert into website_policedata(ID, \
	CAD_Event_Number, General_Offense_Number, Event_Clearance_Code, Event_Clearance_Description, Event_Clearance_SubGroup, Event_Clearance_Group, Event_Clearance_Date, Hundred_Block_Location, District_Sector, Zone_Beat, Census_Tract, Longitude, Latitude, Incident_Location, Initial_Type_Description, Initial_Type_Subgroup, Initial_Type_Group,	At_Scene_Time)' \
	'Values(%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s","%s","%s")', row)

conn.commit()
conn.close()
print "done"
