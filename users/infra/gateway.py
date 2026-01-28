from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from ..services.erros import *

EMAIL = settings.EMAIL_HOST_USER

class EmailSender:
    def __init__(self):
        self.email = 'email'
    def send_email(self,email,code):
        title = "Código de verificação"
        from_email = EMAIL
        to = [email]

        html_content = render_to_string("./apps/email.html", {'code': code})
        text_content = f"Seu codigo de verificação e: {code}"

        msg = EmailMultiAlternatives(title, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        try:
            msg.send()
        except Exception:
            raise EmailSendError()
    