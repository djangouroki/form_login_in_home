from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views import View


class Home(View):

    template_name = 'home.html'

    def get(self, request):
        context = {'form': AuthenticationForm()}
        return render(request, self.template_name, context)
