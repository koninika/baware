from django.shortcuts import render
from django.http import HttpResponse
from baware.website.models import *
from geocodelocation import getlat

class Crime(object):
	def __init__(self, crime, count):
		self.crime = crime
		self.count = count
      
def sort(d):
	for key1 in d.keys():
		for key2 in d.keys():
			if d[key1] > d[key2]:
				d[key1], d[key2] = d[key2], d[key1]
				
	return d
      
def home(request):
	if request.method == 'GET':
		return render(request, "postform.html")
	 	
	elif request.method == 'POST':
		coord = getlat(request.POST['addr'])
		addr = request.POST['addr']
 		p = policeData.objects.filter(Latitude__range=(coord[0]-0.01,coord[0]+0.01), Longitude__range=(coord[1]-0.01,coord[1]+0.01))
 		crimes = {}
 		for i in p:
 			crimes[i.Event_Clearance_Group] = 0
 		total = 0
 		for i in p:
 			crimes[i.Event_Clearance_Group] += 1
 			total +=1
 	return render(request, "query.html", {'crimes':sort(crimes), 'address': addr,'total': total})
