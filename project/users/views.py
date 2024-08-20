from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.db.models import Q
from .models import Property
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from .models import Property
from django.shortcuts import render
from .models import Property
def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')  # Replace 'home' with your desired URL name
    else:
        form = UserRegistrationForm()
    return render(request, 'users/user_register.html', {'form': form})

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        if request.session.get('session_invalid', False):
            messages.error(request, "Your session has expired or you logged out. Please log in again.")
            return redirect(reverse('user_login') + "?logout=true") # Redirect to the login page
        username = request.POST.get('username')  # Use 'get' method to safely access form data
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('homepage')  # Replace 'home' with your actual homepage URL name
        else:
            # Handle authentication error, e.g., display an error message
            return render(request, 'users/user_login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'users/user_login.html')

def logout_view(request):
    request.session['session_invalid'] = True
    logout(request)
    return redirect(reverse('user_login') + "?logout=true")  # Replace 'home' with your desired URL name




@login_required
def approve_property(request, property_id):
    # Make sure the user is an agent
 # Redirect to the home page or another appropriate page

    property = get_object_or_404(Property, id=property_id)

    # Check if the property is not already approved
    if not property.approved:
        property.approved = True
        property.save()

    return redirect('homepage')

@login_required
def sell(request):
    form = PropertyForm(request.POST, request.FILES)
    if request.method == "POST":

        print('inside post')
        if form.is_valid():
            propert = form.save(commit=False)
            # Set the seller_name to the user's username
            propert.seller_name = request.user.username
            propert.save()
            form.save()
            return render(request, 'users/success.html')
    # else:
    #     form = UserRegForm()
    return render(request, 'users/sell.html', {'form': form})


@login_required()
def luxury_estate(request):
    properties = Property.objects.filter(property_category='luxury', approved=True)
    return render(request, 'users/property_list.html', {'properties': properties})

@login_required
def oceanfront_retreats(request):
    properties = Property.objects.filter(property_category='oceanfront', approved=True)
    return render(request, 'users/property_list.html', {'properties': properties})

@login_required()
def urban_living(request):
    properties = Property.objects.filter(property_category='urban', approved=True)
    return render(request, 'users/property_list.html', {'properties': properties})

@login_required
def countryside_escapes(request):
    properties = Property.objects.filter(property_category='countryside', approved=True)
    return render(request, 'users/property_list.html', {'properties': properties})

@login_required
def property_search(request):
    search_query = request.GET.get('search_query', '')
    location_filter = request.GET.get('location', '')
    category_filter = request.GET.get('category', '')
    features_filter = request.GET.get('features', '')

    # Use Q objects to perform an OR search across multiple fields and filter by 'approved'
    properties = Property.objects.filter(
        Q(property_title__icontains=search_query) |
        Q(property_location__icontains=search_query) |
        Q(property_category__icontains=search_query) |
        Q(property_features__icontains=search_query),
        approved=True
    )

    return render(request, 'users/search_results.html', {'properties': properties, 'search_query': search_query})




from django.shortcuts import render
from .models import Property

@login_required()
def agent_properties(request):
    if request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.user_type == 'agent':
        properties = Property.objects.filter(agent=request.user.userprofile, approved=False)
        return render(request, 'users/agent_properties.html', {'properties': properties})
    else:
        # Handle the case when the user is not an agent or doesn't have a userprofile
        return redirect('homepage')  # You can create a custom error template
  # You can create a custom error template



@login_required
def owner_properties(request):
    properties = Property.objects.filter(
        seller_name=request.user.username
    )
    return render(request, 'users/owner_properties.html', {'properties': properties})

    # if request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.user_type == 'customer':
    #     # Filter properties based on the owner's user type and seller_name
    #     properties = Property.objects.filter(
    #         agent__user_type='customer',
    #         seller_name=request.user.username
    #     )
    #     return render(request, 'users/owner_properties.html', {'properties': properties})
    # else:
    #     # Handle the case when the user is not a customer or doesn't have a userprofile
    #     return redirect('homepage')  # You can create a custom error template

