from django.core.mail import send_mail

from celery import shared_task

from config.settings.development import DEFAULT_FROM_EMAIL


@shared_task
def send_enquiry_email_task(data):

    subject = data["subject"]
    name = data["name"]
    email = data["email"]
    message = data["message"]
    from_email = data["email"]
    recipient_list = [DEFAULT_FROM_EMAIL]

    mail_sent = send_mail(
        subject, 
        message, 
        from_email, 
        recipient_list, 
        fail_silently=True
    )

    return mail_sent

