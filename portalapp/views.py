from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from portalapp.models import CustomUser
from .models import Flight
from django.contrib import messages
from .models import Flight
from .forms import FlightForm,ContactFormForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactFormForm()
    return render(request, 'contact_form.html', {'form': form})
# Create your views here.
def home(request):
    return render(request, 'index.html')

def manage(request):
    return render(request, 'manage.html')

def signup1(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return render(request, 'signup1.html', {'error': "Passwords don't match"})
        else:
            request.session['uname'] = uname
            request.session['email'] = email
            request.session['pass1'] = pass1
            return redirect('signup2')
    return render(request, 'signup1.html')
 
def signup2(request):
    if request.method=='POST':
        uname = request.session.get('uname')
        email = request.session.get('email')
        pass1 = request.session.get('pass1')

        fname=request.POST.get('first-name')
        lname=request.POST.get('last-name')
        dob=request.POST.get('dob')
        addr=request.POST.get('straddr')
        towncity=request.POST.get('towncity')
        state=request.POST.get('state')
        country=request.POST.get('country')
        pin=request.POST.get('pin')
        telno=request.POST.get('telno')
        
        my_user = CustomUser.objects.create_user(username=uname, email=email, password=pass1, fname=fname, lname=lname, dob=dob, addr=addr,towncity=towncity, state=state, country=country, pin=pin, telno=telno)
        my_user.save()
        return redirect('login')
    return render(request, 'signup2.html')
 
def Login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': "Username or Password is incorrect"})
    return render (request,'login.html')

def Logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'profile.html')

def flightstatus(request):
    return render(request, 'flightstatus.html')

def checkin(request):
    return render(request, 'checkin.html')

def admin_dashboard(request):
    flights = Flight.objects.all()  
    form = FlightForm()
    return render(request, 'admin.html', {'form': form,'flights': flights})

def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flight added successfully!')
            return redirect('admin_dashboard')
    else:
        form = FlightForm()
    return render(request, 'admin.html', {'form': form})

def update_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flight updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'update_flight.html', {'form': form, 'flight': flight})

def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.delete()
        messages.success(request, 'Flight deleted successfully!')
        return redirect('admin_dashboard')
    return render(request, 'delete_flight.html', {'flight': flight})

def search_flights(request):
    flights = None
    if request.method == 'GET' and request.GET:
        departure = request.GET.get('departure')
        arrival = request.GET.get('arrival')
        departure_date = request.GET.get('departure_date')
        
        flights = Flight.objects.filter(departure=departure, arrival=arrival, departure_date=departure_date)
    return render(request, 'search_flight.html', {'flights': flights})

def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == 'POST':
        num_passengers = int(request.POST.get('num_passengers', 1))  # Default to 1 passenger if not specified
        total_amount = (flight.price) * (num_passengers)

        # Store necessary data in session for future reference (like booking confirmation)
        request.session['flight_id'] = flight.id
        request.session['num_passengers'] = num_passengers
        request.session['total_amount'] = total_amount

        # Redirect to the booking invoice page to confirm details and proceed to payment
        return redirect('booking_invoice')  # Redirect to booking_invoice view

    context = {
        'flight': flight,
    }
    return render(request, 'book_flight.html', context)

def booking_invoice(request,flight_id):
    # Retrieve booking details from session
    num_passengers = request.session.get('num_passengers', 1)
    total_amount = request.session.get('total_amount', 0)
    
    # Retrieve flight object
    flight = get_object_or_404(Flight, id=flight_id)

    context = {
        'flight': flight,
        'num_passengers': num_passengers,
        'total_amount': total_amount,
    }
    return render(request, 'payment.html', context)
