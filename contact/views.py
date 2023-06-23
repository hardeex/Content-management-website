from django.shortcuts import render, redirect
from account.forms import ContactForm
from .utils import send_email_to_admin


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
            # save_contact_info(name, email, subject, message)

            # Set a success message in the session
            request.session['contact_success'] = True

            return redirect('contact:contact')  # Redirect to the same page
    else:
        form = ContactForm()

    # Check if a success message is present in the session
    contact_success = request.session.pop('contact_success', False)

    return render(request, 'contact.html', {'form': form, 'contact_success': contact_success})


