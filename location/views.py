from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from location.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from geopy.distance import geodesic
from django.http import JsonResponse

# Create your views here.


# @login_required(login_url="index")
def contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            name = request.POST['name']
            email = request.POST['email']
            website = request.POST['website']
            message = request.POST['message']

            ch = Contact(name=name, email=email,
                         website=website, message=message)
            ch.save()
            print(name)
            return redirect('index')
        else:
            messages.error(request, 'Register First')
            return redirect('register')
    else:
        return render(request, 'contact.html')


def location(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
            user_name = current_user.username
            lat = request.POST.get('latitude')
            lng = request.POST.get('longitude')

            # GPT Code
            # location, created = Location.objects.get_or_create(username=user_name)
            # location.lat = lat
            # location.lng = lng
            # location.save()

            # GPT Code 2
            location = Location.objects.filter(username=user_name).first()

            # If the location doesn't exist, create a new one
            if not location:
                location = Location(username=user_name)

            location.lat = lat
            location.lng = lng
            location.save()

            # Manish Code
            # if Location.objects.filter(username=user_name):

            #     location, created = Location.objects.get_or_create(
            #         username=user_name)

            #     location.lat = lat
            #     location.lng = lng
            #     location.save()

            # else:
            #     first_create = Location(username=user_name, lat=lat, lng=lng)
            #     first_create.save()

            print(location)
            return redirect('location')
        else:
            messages.error(request, 'Register First')
            return redirect('register')
    else:
        return render(request, 'location.html')


def track(request):
    # print(request.POST)
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_user = request.user
            current_user_location = Location.objects.filter(
                username=current_user.username).first()
            target_user_location = Location.objects.filter(
                username='vishal').first()

            if current_user_location and target_user_location:
                current_user_coords = (
                    current_user_location.lat, current_user_location.lng)
                target_user_coords = (target_user_location.lat,
                                      target_user_location.lng)

                distance = geodesic(current_user_coords,
                                    target_user_coords).meters

                if distance <= 40:
                    # messages.error(request, 'Vehicle is NearBy')
                    return JsonResponse({'message': 'Vehicle is NearBy'})
                else:
                    # messages.error(request, 'Not NearBY')
                    return JsonResponse({'message': 'Vehicle is not NearBy'})

        else:
            return render(request, "track.html")
    else:
        messages.error(request, 'Register first to Track')
        return redirect('register')
