from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(ModelSerializer):

  def validate(self,data): 
    print('Validate Data ->', data)
    return data 

    class Meta:
        model = User
    fields = ('id', 'username', 'email', 'password', 'password_confirmation')
