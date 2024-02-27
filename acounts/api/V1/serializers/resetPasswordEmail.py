from rest_framework import serializers
from django.shortcuts import get_object_or_404
from ....models import CustomeUser


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.CharField(label=("Email"), write_only=True)

    def validate(self, attrs):
        user = get_object_or_404(CustomeUser, email=attrs.get("email"))
        attrs["user"] = user
        return attrs