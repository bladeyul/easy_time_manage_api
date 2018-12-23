from django.shortcuts import render
from .models import Mission

# Create your views here.
def now_mission(request):
	if request.method=='GET':
		mission_lists=Mission.get_now_missions()

def next_mission(request):
	if request.method=='GET':
		mission_lists=Mission.get_next_missions()

def delay_mission(request):
	if request.method=='POST':
		data=request.POST
		mission_id=data['mission_id']
		Mission.delay_mission(mission_id)
