from .models import Signup
from rest_framework import serializers

class signup_serializer(serializers.ModelSerializer):
    class Meta:
        model=Signup
        fields = "__all__"