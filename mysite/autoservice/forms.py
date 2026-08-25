from django.contrib.auth.models import User
from .models import OrderComment, Profile, Order
from django import forms

class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ['content']

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


class UserOrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'deadline', 'status']
        widgets = {"deadline": forms.DateTimeInput(attrs={"type": "datetime-local"})}

