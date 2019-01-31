from rest_framework import serializers
from users.models import User
from rest_framework.authtoken.models import Token
from users.authenticate import EmailBackend
from django.contrib.auth.password_validation import validate_password



class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='key')
    
    class Meta:
        model = Token
        fields = ("token",)



class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email', 'phone_number','password')

    
    
    @staticmethod
    def validate_password(password):
        """
        Validate password
        """

        validate_password(password)
        return password

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    @staticmethod
    def get_token(user):
        """
        Get or create token
        """

        token, created = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User 
        fields = ('id','username','phone_number','email','first_name','last_name','user_type' , 'token')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('first_name','last_name','user_type' , 'password')


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    default_error_messages = {
        'inactive_account': 'User account is disabled.',
        'invalid_credentials': 'Unable to login with provided credentials.',
    }
    
    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None
        

    def validate(self, attrs):
        self.user = EmailBackend.authenticate(self , username=attrs.get("username"), password=attrs.get("password"))
        
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])

    