from django.shortcuts import render
from django.urls import path
from account.forms import ContactForm
from .utils import send_email_to_admin


# Create your views here.
def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send an email to the admin
            send_email_to_admin(name, email, subject, message)

            # Optionally, save the contact information to a database
            save_contact_info(name, email, subject, message)

            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})




def Contact_success(request):
    return render(request, 'contact_success.html')
