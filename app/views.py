from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("app:create_profile")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("app:homepage")
	
@login_required
def index(request):
    title = "Neighbourhood"
    business = Business.objects.all().filter
    context = {
        "title": title,
        "business": business
    }
    return render(request, 'main.html', context)

@login_required
def create_profile(request):

    Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/profile/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
    return render(request, 'profilecreate.html', {"u_form": u_form, "p_form": p_form, })

@login_required
def profile(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)


@login_required
def post_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.save()
        return redirect('/')
    else:
        form = PostBusinessForm(auto_id=False)
    return render(request, 'business.html', {"form": form})

@login_required
def announcements(request):
    user = Profile.objects.get(user=request.user.id)
    announcements = Announcements.objects.all().filter(hood=user.hood)
    current_user = request.user
    if request.method == 'POST':
        hood = NeighbourHood.objects.get(name=user.hood)
        form = PostAnnouncement(request.POST, request.FILES)
        if form.is_valid():
            title = form.save(commit=False)
            title.author = current_user
            title.hood = hood
            title.save()
            return redirect('/announce/')
    else:
        form = PostAnnouncement(auto_id=False)
    return render(request, 'announce.html', {"announcements": announcements, "form": form})

@login_required(login_url='/login')
def amenities(request):
    user = Profile.objects.get(user=request.user.id)
    amenities = Amenities.objects.all().filter(hood=user.hood)
    current_user = request.user
    if request.method == 'POST':
        hood = NeighbourHood.objects.get(name=user.hood)
        form = AddAmenity(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.hood = hood
            image.save()
            return redirect('/amenities/')
    else:
        form = AddAmenity(auto_id=False)
    return render(request, 'amenity.html', {"amenities": amenities, "form": form})

def search_results(request):
    if 'businesses' in request.GET and request.GET["businesses"]:
        search_term = request.GET.get('businesses')
        searched_businesses = Business.search_by_name(search_term)
        message = f'{search_term}'

        context = {
            "message": message,
            "businesses": searched_businesses,
        }
        return render(request, 'search.html', context)
    else:
        message = "Search for a business by its name"
        return render(request, 'search.html', {"message": message})