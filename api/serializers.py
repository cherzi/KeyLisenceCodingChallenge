from rest_framework import serializers 
from .models import Key

class KeySerializer(serializers.ModelSerializer):
	value = serializers.ReadOnlyField()
	creationDate = serializers.ReadOnlyField()
	expDate = serializers.ReadOnlyField()

	class Meta:
		model = Key
		fields = '__all__'