from rest_framework import serializers
from .models import zira
from rest_framework.serializers import HyperlinkedIdentityField

class AddZiraSerializer(serializers.ModelSerializer):
	class Meta:
		model = zira
		fields = ('ticket_num','issue_description','uploaded_by')
		depth = 1

class SearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = zira
		fields = ('ticket_num',)
		depth = 1