from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def home(request):
    if not request.session.get('user'):
        return redirect('login')

    username = request.session.get('user')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')
    else:
        form = FeedbackForm()

    return render(request, 'index.html', {
        'form': form,
        'username': username
    })

    return render(request, 'index.html', {'form': form})
def view_feedbacks(request):
    feedbacks = Feedback.objects.order_by('-submitted_at')
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})

from .forms import SignupForm, LoginForm
from .models import User

# SIGNUP VIEW
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# LOGIN VIEW
def login_view(request):
    error = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username, password=password)
                request.session['user'] = user.username
                return redirect('home')
            except User.DoesNotExist:
                error = "Invalid username or password"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error': error})


# LOGOUT
def logout_view(request):
    request.session.flush()
    return redirect('login')

def view_feedbacks(request):
    if not request.session.get('user'):
        return redirect('login')

    feedbacks = Feedback.objects.order_by('-submitted_at')
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})


