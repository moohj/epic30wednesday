from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class BusinessTrace(models.Model):
	"""record and manipulate data for address"""
	"""default={
	"street":'',
	"zip":"",
	"city":"",
	"state":"",
	"country":"",
	"longitude":"",
	"latitude":"",
	}
	set_defaults()"""

	phone_number = PhoneNumberField(default='+12129321090')
	business_name = models.CharField(max_length=120, default='Manhattan')
	street = models.CharField(max_length=120, default='1855 7th ave')
	zip_code = models.CharField(max_length=5, default='10026')
	city = models.CharField(max_length=120, default='new York')
	state = models.CharField(max_length=120, default='NY')
	country = models.CharField(max_length=120, default='United States')
	longitude = models.CharField(max_length=120, default='United States')
	latitude = models.CharField(max_length=120, default='United States')

	def __str__(self):
		return self.business_name



	
	def validate_city():
		pass

	def validate_zip():
		pass

	"""def set_defaults():"""

		




		