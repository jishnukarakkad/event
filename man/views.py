from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import BookingForm, FeedbackForm, ContactForm  
from .models import Events, Booking, Feedback 
from django.contrib.auth import logout 
from django.contrib import messages
from .models import Profile, Booking  # Ensure the Profile model is imported

# Home page
def index(request):
    return render(request, 'index.html')

# Event listing page
def events(request):
    events = Events.objects.all()
    return render(request, 'events.html', {'events': events})

# Feedback page
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_feedback')  # Redirect to feedback view after success
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback.html', {'form': form})

# View to display all feedback submissions
def view_feedback(request):
    feedback_list = Feedback.objects.all().order_by('-submitted_at')
    return render(request, 'view_feedback.html', {'feedback_list': feedback_list})

# Contact page
def contacts(request):
    return render(request, 'contacts.html')

# Booking confirmation page
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from .models import Booking

def confirmation(request, booking_id):
    # Retrieve the booking object or return a 404 if not found
    booking = get_object_or_404(Booking, id=booking_id)

    # Prepare email details
    subject = 'Your Ticket Confirmation'
    to_email = booking.email  # Recipient's email
    
    # Render the email template with the context
    email_content = render_to_string('ticket_email.html', {
        'booking': booking,
        'user_email': booking.email
    })

    # Send the email
    try:
        email = EmailMultiAlternatives(subject, '', 'testing450439@gmail.com', [to_email])  # Replace with your email
        email.attach_alternative(email_content, "text/html")  # Attach the HTML content
        email.send(fail_silently=False)
        messages.success(request, 'A confirmation email has been sent to your email address.')
    except Exception as e:
        messages.error(request, f'Error sending email: {e}')

    return render(request, 'confirmation.html', {
        'booking': booking,
        'user_email': booking.email
    })


# Ticket email page
def ticket_email(request):
    return render(request, 'ticket_email.html')

def contact_success(request):
    return render(request, 'contact_success.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(request.GET.get('next', 'index'))  # Redirect to the next page or index
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Book an event
@login_required
def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Handle email sending, etc.
            return redirect('confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    events = Events.objects.all()
    return render(request, 'bookings.html', {'form': form, 'events': events})

# Create a new view to handle the login redirect from bookings
def redirect_to_login(request):
    messages.info(request, "Please log in to view the bookings.")  # Set the message
    return redirect('login')

def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {'form': form})

@login_required
def profile(request):
    # Retrieve bookings for the logged-in user
    bookings = Booking.objects.filter(user=request.user)

    # Pass the user information to the template
    return render(request, 'profile.html', {'bookings': bookings, 'user': request.user})

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('index') 

def about(request):
    return render(request,'about.html')

def welcome_view(request):
    return render(request, 'welcome.html')






