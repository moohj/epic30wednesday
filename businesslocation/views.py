from django.shortcuts import render
from .models import BusinessTrace
from .forms import BusinessTraceForm

# Create your views here.
def index(request):
	form = BusinessTraceForm(request.POST or None)
	if form.is_valid():
		print('its valid')
		instance = form.save(commit = False)
		instance.save()
	else:
		print('not valid')
	context = {
	"form":form,
	}
	return render(request,'businesslocation/index.html',context)


