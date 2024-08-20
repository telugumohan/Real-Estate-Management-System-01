from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to a thank-you page here
            return render(request, 'contact/thank.html')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {'form': form})
