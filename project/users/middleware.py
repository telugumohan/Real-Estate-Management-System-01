from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

class SessionInvalidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:  # Check if a user is authenticated
            if request.session.get('session_invalid', False):
                messages.error(request, "Your session has expired or you logged out. Please log in again.")
                request.session.flush()
                return redirect(reverse('user_login'))  # Redirect to the login page

        response = self.get_response(request)
        return response
