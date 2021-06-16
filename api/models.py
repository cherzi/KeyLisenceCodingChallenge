from django.db import models
from django.core.validators import MinLengthValidator


class Key(models.Model):
	name = models.CharField(max_length=8)
	value = models.CharField(max_length=16, unique=True, validators=[MinLengthValidator(4)])
	creationDate = models.DateField(auto_now_add=True)
	expDate = models.DateField()

	def __str__(self):
		return self.name