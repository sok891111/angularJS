from .models import Notice,Message
from rest_framework import serializers

 
class NoticeSerializer(serializers.HyperlinkedModelSerializer):
	## XXX : authenicate
	# owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Notice
		fields = ('index', 'contents' , 'writer' , 'reg_date')


 