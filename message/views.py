from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import MessageSerializer
from rest_framework.views import APIView
from .models import Message
import logging
from django.utils import timezone
from login.models import User

logger = logging.getLogger(__name__)

# Create your views here.
class retrieveMessageView(generics.ListAPIView):
	"""
	A view that returns the count of active users in JSON.
	"""
	renderer_classes = (JSONRenderer, )
	queryset = Message.objects.order_by('read_msg_yn','-send_date')
	# authentication_classes = (authentication.TokenAuthentication,)

	def post(self, *args, **kwargs):
		return self.list(*args, **kwargs)

	def get(self, *args, **kwargs):
		return self.list(*args, **kwargs)

	def list(self, request):
		try:
			user_email = request.session['user'].get('user_email')
			queryset = Message.objects.filter(rcv=user_email).order_by('read_msg_yn','-send_date')
			serializer = MessageSerializer(queryset, many=True)
			data = JSONRenderer().render(serializer.data)
			logger.info("QUERY>> %s" % queryset.query)
			return Response(data,content_type="application/json; charset=utf-8")
		except Exception, why:
			logger.error(why)
			return Response({'result':'error' },status=400)


class CreateMessageView(APIView):

	def get(self, request, *args, **kwargs):
		return Response({'result':'Not Found' }, status=404)

	def post(self, request, *args, **kwargs):
		try:
			data = request.DATA
			user =User.objects.get(pk=request.session['user'].get('user_email'))
			message = Message.objects.create(
				send=request.session['user'].get('user_email'),
				rcv=data['rcv'],
				content=data['content'],
				msg_type=data['msg_type'],
				read_msg_yn='N',
				send_date=timezone.now(),
				user=user
				)
			message.clean()
			message.save()
			serializer = MessageSerializer(message)

			return Response(serializer.data, status=201)	
		except Exception, why:
			logger.error(why)
			return Response({'result':'create Error' }, status=400)