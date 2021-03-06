from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import status

from general.models import Appointment, Ad
from .serializers import *
from . import permissions as custom_permissions

from django.contrib.auth.models import User


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = [custom_permissions.AppointmentAccept]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AppointmentSerializerPOST
        else:
            return AppointmentSerializer

    def perform_update(self, serializer):
        pk = serializer.instance.id
        appointment = Appointment.objects.get(id=pk)
        ad = appointment.ad
        non_confirmed_appointments = ad.appointment_set.exclude(id=pk)
        for non_confirmed_appointment in non_confirmed_appointments:
            non_confirmed_appointment.delete()

        ad.is_availible = False
        serializer.save(author=self.request.user, is_confirmed=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, is_confirmed=False)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [custom_permissions.IsAuthorOrReadOnly]

    def update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, is_availible=True)


class TutorAdViewSet(AdViewSet):
    queryset = Ad.objects.all().filter(ad_type="T")


class StudentAdViewSet(AdViewSet):
    queryset = Ad.objects.all().filter(ad_type="L")
