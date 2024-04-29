from django.shortcuts import render, redirect,HttpResponseRedirect,reverse
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Project,Data,Gallery,Video
from .forms import SignUpForm,AddRecordForm,ImageUpload,BMI,ImageGallery,VideoUpload
from datetime import datetime
import urllib
import json



def index(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('index')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('index')
	else:
		return render(request,'index.html')


def home(request):
	if request.user.is_authenticated:
		records=Project.objects.all()
		return render(request, 'home.html', {'records':records})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('index')


def logout_user(request):
	logout(request)
	messages.success(request,"You have been logged out ")
	return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Project.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('index')


def delete_record(request,pk):
	if request.user.is_authenticated:
		delete_it = Project.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('index')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('index')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('index')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('index')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Project.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('project')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('index')


def project(request):
	data = Data.objects.all()
	return render(request,'project.html',{'data':data})

def project_detail(request,pk):
    data=Data.objects.get(id=pk)
    return render(request,'detail.html',{'data':data})


# Upload Image
def upload_project(request):
	if request.method == 'POST':
		form = ImageUpload(request.POST, request.FILES)
		if form.is_valid():
			image_file = form.cleaned_data['image']# refersh for clened page
			form.save()
			messages.success(request,'Project upload successfully 👍😎')
			return redirect('project')  # Redirect to a project page
	else:
		form = ImageUpload()
	return render(request, 'upload_image.html', {'form': form})

#delete project

def delete_project(request,pk):
	if request.user.is_authenticated: #check User authurised or Not
		delete_it = Data.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('project')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('project')

# BMI Calculater
def bmi_calculeter(request):
	bmi=None
	interpretation=None
	if request.method == 'POST':
		form = BMI(request.POST)
		if form.is_valid():
			weight = float(form.cleaned_data['weight'])
			height = float(form.cleaned_data['height'])
			# Calculate the BMI
			bmi = round(weight / (height ** 2))
			interpretation=get_bmi_interpretation(bmi)
			form.save()  # Save the form data
			# Create a new empty form
			form = BMI()
	else:
		form = BMI()
	return render(request, 'bmi.html', {'form': form,'bmi':bmi,'interpretation':interpretation})
def get_bmi_interpretation(bmi):
	if bmi < 18.5:
		return 'Underweight'
	elif 18.5 <= bmi < 25:
		return 'Healthy Weight'
	else:
		return 'Overweight'


def gallery(request):
	if request.user.is_authenticated:
		images = Gallery.objects.all()
		if request.method == 'POST':
			form = ImageGallery(request.POST, request.FILES)
			if form.is_valid():
				image_file = form.cleaned_data['image']# refersh for clened page
				form.save()
				messages.success(request,'Image upload successfully 👍😎')
				return redirect( 'gallery')  # Redirect to a project page
		else:
			form = ImageGallery()
		return render(request, 'gallery.html', {'form': form,'images':images,})
	return render(request,'gallery.html')

def gallery_one(request,pk):
	images=Gallery.objects.get(id=pk)
	return render(request, 'one.html', {'images': images})

def delete_gallery(request,pk):
	if request.user.is_authenticated: #check User authurised or Not
		delete_it = Gallery.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Photo Deleted Successfully...")
		return redirect('gallery')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('gallery')
# For Video Gallery
def video_gallery(request):
	if request.user.is_authenticated:
		videos= Video.objects.all()
		if request.method=='POST':
			form=VideoUpload(request.POST or None,request.FILES or None)
			if form.is_valid():
				video_file=form.cleaned_data['video']
				form.save()
				messages.success(request,'Video upload successfully')
				return redirect('video')
		else:
			form=VideoUpload()
		return render(request, 'video_gallery.html', {'form':form,'videos': videos })
	return render(request,'video_gallery.html')

def video_gallery_one(request,pk):
	videos=Video.objects.get(id=pk)
	return render(request, 'video.html', {'videos': videos})


# Weather data
def weather(request):

	if request.method == 'POST':
		city = request.POST['city']
		res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
		json_data = json.loads(res)
		data = {
			"country_code": str(json_data['sys']['country']),
			"coordinate": str(json_data['coord']['lon']) + ' ' +
			str(json_data['coord']['lat']),
			"temp": str(json_data['main']['temp'])+'k',
			"pressure": str(json_data['main']['pressure']),
			"humidity": str(json_data['main']['humidity']),
		}
	else:
		city = ''
		data = {}
	return render(request, 'weather/weather.html', {'city': city, 'data': data})
# chat

def error(request):
	return render(request,'error.html')