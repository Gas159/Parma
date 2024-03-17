from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # fields = []  # fields = '__all__'
        # fields = ['first_name', 'last_name']  # fields = '__all__'
        fields = ['first_name', 'last_name', 'email']  # fields = '__all__'
        ordering = ['-date_joined']
