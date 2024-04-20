import logging

# Create your views here.
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Patient
from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return render(request, "patient/dashboard.html")


def display_patients(request):
    items = Patient.objects.filter(doctor=request.user.id)
    context = {
        'items': items,
        'header': 'Patient Progress Tracker',
    }
    logging.info(items)
    return render(request, "patient/dashboard.html", context)


def view_patient(request, patient_username):
    patient = Patient.objects.get(user__username=patient_username)
    context = {
        'item': patient,
        'header': patient_username,
    }
    return render(request, "patient/patient_detail.html", context)
