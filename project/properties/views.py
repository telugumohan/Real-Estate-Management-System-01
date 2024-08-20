# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from .models import Property
# from .forms import PropertyForm
# from django.db.models import Q
# from django.shortcuts import get_object_or_404, redirect
# from .models import Property
#
# from django.shortcuts import render
# from .models import Property
# def approve_property(request, property_id):
#     # Make sure the user is an agent
#     if not request.user.user_type == 'agent':
#         return redirect('homepage')  # Redirect to the home page or another appropriate page
#
#     property = get_object_or_404(Property, id=property_id)
#
#     # Check if the property is not already approved
#     if not property.approved:
#         property.approved = True
#         property.save()
#
#     return redirect('homepage')
#
#
# def sell(request):
#     form = PropertyForm(request.POST, request.FILES)
#     if request.method == "POST":
#
#         print('inside post')
#         if form.is_valid():
#             form.save()
#             return render(request, 'properties/success.html')
#     # else:
#     #     form = UserRegForm()
#     return render(request, 'properties/sell.html', {'form': form})
#
# from django.db.models import Q
# from .models import Property
#
# def luxury_estate(request):
#     properties = Property.objects.filter(property_category='luxury', approved=True)
#     return render(request, 'properties/property_list.html', {'properties': properties})
#
# def oceanfront_retreats(request):
#     properties = Property.objects.filter(property_category='oceanfront', approved=True)
#     return render(request, 'properties/property_list.html', {'properties': properties})
#
# def urban_living(request):
#     properties = Property.objects.filter(property_category='urban', approved=True)
#     return render(request, 'properties/property_list.html', {'properties': properties})
#
# def countryside_escapes(request):
#     properties = Property.objects.filter(property_category='countryside', approved=True)
#     return render(request, 'properties/property_list.html', {'properties': properties})
#
# def property_search(request):
#     search_query = request.GET.get('search_query', '')
#     location_filter = request.GET.get('location', '')
#     category_filter = request.GET.get('category', '')
#     features_filter = request.GET.get('features', '')
#
#     # Use Q objects to perform an OR search across multiple fields and filter by 'approved'
#     properties = Property.objects.filter(
#         Q(property_title__icontains=search_query) |
#         Q(property_location__icontains=search_query) |
#         Q(property_category__icontains=search_query) |
#         Q(property_features__icontains=search_query),
#         approved=True
#     )
#
#     return render(request, 'properties/search_results.html', {'properties': properties, 'search_query': search_query})
#
#
#
#
# def agent_properties(request):
#     # Assuming you have a custom user model 'UserProfile' for agents
#     if request.user.is_authenticated and request.user.user_type == 'agent':
#         agent_properties = Property.objects.filter(agent=request.user.userprofile, approved=True)
#         return render(request, 'properties/agent_properties.html', {'agent_properties': agent_properties})
#     else:
#         # Handle the case when the user is not an agent
#         return redirect('homepage')  # You can create a custom error template
