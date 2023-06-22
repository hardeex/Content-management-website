from django.core.mail import send_mail
from django.conf import settings

def send_email_to_admin(name, email, subject, message):
    #recipient_list = [settings.ADMIN_EMAIL]  # Replace with the admin's email address
    recipient_list = [settings.webmasterjdd@gmail.com]  
    message_text = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
    send_mail('New Contact Form Submission', message_text, email, recipient_list)
