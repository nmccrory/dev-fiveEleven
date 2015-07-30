from apps.data_storage.models import WriteOnly
from django.http import HttpResponse, JsonResponse

import json
from django.shortcuts import render


#takes request and grabs all data from database
def index(request):
	content = {
	'info': WriteOnly.objects.all()
	}

	return render(request, 'mapvisuals/index.html', content)

def toGeo(request):
	data = WriteOnly.objects.all()

	def toGeoJson(data):
		geo = {
			"type": "FeatureCollection",
			"features": [],
		}

		for dat in data:
			geoObj = {
				"type": "Feature",
				"geometry": {
					"type": "Point",
					"coordinates": [dat.latitude, dat.longitude]
				},
				"properties": {
					"numJobs": dat.num_jobs,
					"name": dat.city_name,
					"stateAbbreviation": dat.stateAbbreviation,
					"stateName": dat.stateName,
					"id": 1147394
				}
			}
			geo['features'].append(geoObj)
		return geo

	data = toGeoJson(data)

	return HttpResponse(json.dumps(data), content_type='application/json')


def statedata(request):
	GeoJson = open('/Users/new/Desktop/webdev/Coding Dojo /Group_project/job-visualization/apps/mapvisuals/states.json')
	CityData = WriteOnly.objects.all()
	AllStates = json.load(GeoJson)
	
	for state in AllStates['features']:
	  for city in CityData:
	     if city.stateName == state['properties']['name']:
	        if 'numJobs' in state['properties']:
	           print 'exists'
	           state['properties']['numJobs'] += city.num_jobs
	        else:
	           print 'not exists'
	           state['properties']['numJobs'] = city.num_jobs
	           
	GeoJson = json.dumps(AllStates)
	return HttpResponse(GeoJson , content_type='application/json')
