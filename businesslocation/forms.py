from django import forms
from .models import BusinessTrace
import requests
import json

class BusinessTraceForm(forms.ModelForm):
	class Meta:
		model = BusinessTrace
		fields = ("phone_number", 
	"business_name", 
	"street", 
	"zip_code", 
	"city",
	"state",
	"country",
	"longitude",
	"latitude", 
	)
	def clean_latitude(self):
		street = self.cleaned_data.get('street')
		city = self.cleaned_data.get('city')
		state = self.cleaned_data.get('state')
		print(street)
		print(state)
		print(city)
		r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s,+%s,+%s&key=AIzaSyAiiLqBkAzyxCpOhSYel83hCwbArbaQ0Xk' %(street, city, state))
		latitude = str(r.json()['results'][0]['geometry']['location']['lat'])
		print('cleaned_data '+str(latitude))
		return latitude

	def clean_longitude(self):
		street = self.cleaned_data.get('street')
		city = self.cleaned_data.get('city')
		state = self.cleaned_data.get('state')
		r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s,+%s,+%s&key=AIzaSyAiiLqBkAzyxCpOhSYel83hCwbArbaQ0Xk' %(street, city, state))
		longitude= str(r.json()['results'][0]['geometry']['location']['lng'])
		print('cleaned_data '+str(longitude))
		return longitude