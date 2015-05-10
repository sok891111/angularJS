from django.db import models

class User(models.Model):
    user_email = models.CharField(max_length=100,primary_key=True)
    user_id = models.CharField(max_length=100,default = None,null=False)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100,null=True, blank=True, default = None)
    user_phone = models.CharField(max_length=100,null=True, blank=True, default = None)
    reg_date = models.DateTimeField('reg date')

    def __getattr__ (self,field):
        return self[field+''];
    def create(data):
    	self.objects.create(user_email=request.POST['userEmail'])
######   Example

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __unicode__ (self):
#     	return self.question_text
    	
# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)