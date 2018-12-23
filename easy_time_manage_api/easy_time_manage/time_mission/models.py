from django.db import models
import datatime

class Mission(models.Model):

    mission_name=models.CharField(max_length=20)
    mission_desc=models.CharField(max_length=214)
    mission_content=model.TextField()
    mission_file=models.FileField(upload_to='uploads/%Y/%m/%d')
    mission_image=models.ImageField(upload_to='picture/%Y/%m/%d')
    mission_stime=models.TimeField()
    mission_ftime=models.TimeField()
    
    mission_ctime=models.DateTimeField(auto_now_add=True)
    mission_mtime=models.DateTimeFiled(auto_now=True)

   	@staticmethod
    def get_now_missions():
    	now=datatime.now()
    	return Mission.objects.filter(stime<now).filter(ftime>now)

    @staticmethod
    def get_next_missions():
    	now=datatime.now()
    	return Mission.objects.filter(stime<now+delta_time).filter(stime>now)

    @staticmethod
    def delay_mission(mission_id):
    	now=datatime.now()
    	try:
    		mission=Mission.objects.get(id=mission_id)
    		if mission.stime>now:
    			mission.stime+=delta_time
    		mission.ftime+=delta_time
    		mission.save()
    	except Exception as e:
    		print(e)



# Create your models here.
