from django.core.mail import send_mail
from django.conf import settings

def send_email_to_admin(name, email, subject, message):
    recipient_list = [settings.ADMINS[0][1]]  # Use the admin's email address from the ADMINS setting
    message_text = f"Name: {name}\nEmail: {email}\nSubject:  {subject}\nMessage: \n\n{message}\n"
    send_mail('JDD: New Contact Form Submission', message_text, email, recipient_list)
