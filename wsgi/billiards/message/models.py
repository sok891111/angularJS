from django.db import models
from login.models import User

class Message(models.Model):
	index = models.AutoField(primary_key=True)
	send = models.CharField(max_length=100, null=False)
	rcv = models.CharField(max_length=100, null=False)
	content = models.CharField(max_length=500, default = None)
	msg_type = models.CharField(max_length=10, default = None)
	read_msg_yn = models.BooleanField(default=True)
	send_date = models.DateTimeField('send date')
	user = models.ForeignKey(User)