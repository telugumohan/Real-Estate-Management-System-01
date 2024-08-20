from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from .models import Property
from .models import UserProfile
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    name = forms.CharField()
    user_type = forms.ChoiceField(choices=(('customer', 'Customer'), ('agent', 'Agent')), widget=forms.RadioSelect, initial='customer')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        profile = UserProfile(user=user, name=self.cleaned_data['name'], user_type=self.cleaned_data['user_type'])
        profile.save()
        return user





class PropertyForm(forms.ModelForm):
    agent = forms.ModelChoiceField(
        queryset=UserProfile.objects.filter(user_type='agent'),
        empty_label="Select an Agent",
        label="Agent"
    )

    class Meta:
        model = Property
        field = "__all__"
        exclude = ["id", "approved", "seller_name"]


# forms.py


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)
