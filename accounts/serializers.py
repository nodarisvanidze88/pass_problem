from .models import MainUser
from rest_framework import serializers
from django_countries.fields import Country

class CountryField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Country(data)
class MainUserSrializers(serializers.ModelSerializer):
    country = CountryField(required=False)
    class Meta:
        model = MainUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'required': False},
            'user_permissions': {'required': False}
        }

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        user_permissions = validated_data.pop('user_permissions', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        if groups is not None:
            instance.groups.set(groups)
        if user_permissions is not None:
            instance.user_permissions.set(user_permissions)
        return instance
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        user_permissions = validated_data.pop('user_permissions', None)

        user = MainUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()

        if groups is not None:
            user.groups.set(groups)

        if user_permissions is not None:
            user.user_permissions.set(user_permissions)

        return user