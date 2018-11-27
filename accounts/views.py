from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(TemplateView):
    template_name='accounts/mypage.html'


# Create your views here.
