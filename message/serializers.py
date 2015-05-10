from .models import Message
from rest_framework import serializers

class MessageSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Message
		fields = ('index','send','rcv','content','msg_type','read_msg_yn','send_date')

 