from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=10, choices=(('customer', 'Customer'), ('agent', 'Agent')))
    def __str__(self):
        return self.user.username



from django.contrib.auth.models import User  # Import the user model used in your project



# Define choices for property categories
PROPERTY_CATEGORIES = (
    ('luxury', 'Luxury Estate'),
    ('oceanfront', 'Oceanfront Retreats'),
    ('urban', 'Urban Living Gems'),
    ('countryside', 'Countryside Escapes'),
)


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    property_title = models.CharField(max_length=200)
    property_description = models.TextField()
    property_type = models.CharField(max_length=50)
    property_category = models.CharField(max_length=20, choices=PROPERTY_CATEGORIES, default='luxury')
    property_price = models.DecimalField(max_digits=10, decimal_places=2)
    property_location = models.CharField(max_length=100)
    property_features = models.TextField(blank=True, null=True)
    seller_name = models.CharField(max_length=100)
    seller_email = models.EmailField()
    seller_phone = models.CharField(max_length=15)
    property_images = models.ImageField(upload_to='property_images/', blank=True, null=True)

    approved = models.BooleanField(default=False)  # New field for property approval
    agent = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='agent_properties')

    def __str__(self):
        return self.property_title
