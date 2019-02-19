from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Car
from .forms import CarForm

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form = CarForm()
	if request.method =="POST":
		form = CarForm(request.POST, request.FILES or None) #request.FILES if we are getting an image files or none"it is optional"
		if form.is_valid():
			form.save()
			messages.success(request, 'successfuly created!')
			return redirect('car-list')
	context = {
	 'form':form,
	}
	return render(request, 'create.html',context)


def car_update(request, car_id):
	car = Car.objects.get(id=car_id)
	form = CarForm(instance= car)
	if request.method =="POST":
		form = CarForm(request.POST, request.FILES or None, instance= car)
		if form.is_valid():
			form.save()
			return redirect('car-list')
			#return redirect(car)
			#this redirect to detail page and it is only work if there is car.get_absolute_url
	context = {
	'form':form,
	'car':car,
	}
	return render(request, 'update.html',context)


def car_delete(request, car_id):
	#Complete Me
	Car.objects.get(id=car_id).delete()
	messages.success(request, 'successfuly deleted!')
	return redirect('car-list')




