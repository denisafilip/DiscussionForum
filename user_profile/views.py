from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Statistics
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            birth_date = request.POST['birth_date']
            age = request.POST['age']
            country = request.POST['country']
            city = request.POST['city']

            if len(username) > 15:
                messages.error(request, "Username must be under 15 characters.")
                return redirect('/register/')
            if not username.isalnum():
                messages.error(request, "Username must contain only letters and numbers.")
                return redirect('/register/')
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect('/register/')

            user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name)
            Profile.objects.create(user=user, birth_date=birth_date, age=age, country=country, city=city)
            Statistics.objects.create(user=user)
            return render(request, 'login.html')
    else:
        form = ProfileForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            stats, created = Statistics.objects.get_or_create(user=user)
            request.session['post_count'] = stats.post_count
            request.session['reply_count'] = stats.reply_count
            request.session['visit_count'] = stats.visit_count

            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/myprofile/")
        else:
            messages.error(request, "Invalid Credentials")
        alert = True
        return render(request, 'login.html', {'alert': alert})
    return render(request, "login.html")


def user_logout(request):
    stats = Statistics.objects.filter(user=request.user).first()
    stats.post_count += request.session['post_count']
    stats.reply_count += request.session['reply_count']
    stats.visit_count += request.session['visit_count']
    stats.save()
    Statistics.objects.filter(pk=stats.id).update(visit_count=stats.visit_count,
                                                  post_count=stats.post_count,
                                                  reply_count=stats.reply_count)
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login/')


@login_required(login_url='/login')
def my_profile(request):
    if request.method == "POST":
        user = request.user
        profile = Profile.objects.filter(user=user).first()
        profile.save()
        form = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "profile.html", {'obj': obj,
                                                    'profile': profile})
    else:
        form = ProfileForm()
    return render(request, "profile.html", {'form': form})
