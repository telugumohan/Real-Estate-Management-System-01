# from django import forms
# from .models import Property
# from ..users.models import UserProfile
#
#
# class PropertyForm(forms.ModelForm):
#     agent = forms.ModelChoiceField(
#         queryset=UserProfile.objects.filter(user_type='agent'),
#         empty_label="Select an Agent",
#         label="Agent"
#     )
#
#     class Meta:
#         model = Property
#         field = "__all__"
#         exclude = ["id", "approved"]
