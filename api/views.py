from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import KeySerializer
from .models import *

import datetime
import random
import string
import re


@api_view(['GET'])
def keyList(request):
	keys = Key.objects.all()
	serializer = KeySerializer(keys, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def keyDetail(request, pk):
	key = Key.objects.get(id=pk)
	serializer = KeySerializer(key, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def keyCreate(request):

	serializer = KeySerializer(data=request.data)
	
	today = datetime.date.today()
	expDate = today.replace(year=today.year + 1)

	if serializer.is_valid():
		value = generateKey(serializer.validated_data['name'])
		serializer.save(expDate=expDate, value=value)

	return Response(serializer.data)


@api_view(['DELETE'])
def keyDelete(request, pk):
	key = Key.objects.get(id=pk)
	key.delete()

	return Response('Deleted!')


def generateKey(name):
	#name.replace(" ", "")
	name = re.sub(r"\s+", "", name)
	value = ''.join(random.choices(string.ascii_uppercase + string.digits, k = (16-len(name))))
	value = name + value
	random.shuffle(list(value))
	return ''.join(value);
