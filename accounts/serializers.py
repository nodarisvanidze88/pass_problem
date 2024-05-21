from .models import MainUser
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from django.contrib.auth.hashers import make_password



class MainUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['id', 'username', 'first_name', 'last_name', 'status', 'email',
                  'registration_date', 'address1', 'address2', 'country', 'city',
                  'zip_num', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        
        user = super().create(validated_data)
        
        if password:
            user.set_password(password)
        user.save()
        return user

    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError("Password must be provided.")
        return value





# class MainUserSrializers(CountryFieldMixin, serializers.ModelSerializer):
#     class Meta:
#         model = MainUser
#         fields = ['id', 
#                   'username',
#                   'first_name',
#                   'last_name',
#                   'status',
#                   'email',
#                   'registration_date',
#                   'address1','address2',
#                   'country',
#                   'city',
#                   'zip_num',
#                   'phone_number']
#         extra_kwargs = {'password':{'write_only':True}}

#         def create(self, validated_data):
#             password = validated_data.pop('password', None)
#             user = MainUser(**validated_data)
#             if password:
#                 user.set_password(password)
#             user.save()
#             return user