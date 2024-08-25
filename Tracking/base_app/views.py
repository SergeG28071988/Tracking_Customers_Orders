from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Resource
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create your views here.
