from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model
User = get_user_model()

#def login_reg_view(request):
#    #template = loader.get_template('login_register/templates/test.html')
#    return render(request, 'login_register/templates/test.html')


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

