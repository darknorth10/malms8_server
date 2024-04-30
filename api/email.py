from djoser import email
from djoser import utils
from djoser.conf import settings
from django.contrib.auth.tokens import default_token_generator

class ActivationEmail(email.ActivationEmail):
    template_name = './api/ActivateEmail.html'

    def get_context_data(self):
        context = super().get_context_data()
        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        context["site_name"] = "MALMS8"
        context["domain"] = "localhost:5173"
        
        return context

class ConfirmationEmail(email.ConfirmationEmail):
    template_name = './api/ConfirmationEmail.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context["site_name"] = "MALMS8"
        return context