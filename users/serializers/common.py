from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        print('Validate Data ->', data)
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirmation')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return user


