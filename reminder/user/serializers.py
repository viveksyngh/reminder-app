from rest_framework import serializers

from .models import User, Account


class UserSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)

        if self.context['request'].method not in ['POST']:
            self.fields.pop("password")


    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'email',
                  'mobile_number', 'password', 'secondary_email')
        extra_kwargs = {'password' : 
                            { 'write_only': True}
                       }
        read_only_fields = ('pk',)

    def get_extra_kwargs(self):
        extra_kwargs = super(UserSerializer, self).get_extra_kwargs()
        action = self.context['view'].action

        if action in ['update', 'partial_update']:
            kwargs = extra_kwargs.get('username', {})
            kwargs['read_only'] = True
            extra_kwargs['username'] = kwargs
            
            kwargs = extra_kwargs.get("mobile_number", {})
            kwargs['read_only'] = True
            extra_kwargs['mobile_number'] = kwargs
            
            kwargs = extra_kwargs.get("password", {})
            extra_kwargs["password"] = kwargs

        return extra_kwargs
    
    def create(self, validated_data):
        user = User(username=validated_data['username'],
                    email=validated_data['email'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    mobile_number=validated_data['mobile_number']
                   )
        user.set_password(validated_data['password'])
        if validated_data['secondary_email']:
            user.secondary_email = validated_data['secondary_email']
        user.save()
        return user

    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name",
                                                 instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.secondary_email = validated_data.get("secondary_email",
                                             instance.secondary_email)
        if validated_data.get("password"):
            instance.set_password(validated_data["password"])
        instance.save()
        return instance


class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("password" ,)
        extra_kwargs = {
                            "password" : {
                                "write_only": True 
                            }
        }

    def update(self, instance, validated_data):
        if validated_data.get("password"):
            instance.set_password(validated_data["password"])
        instance.save()
        return instance


class UserAccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "mobile_number",)


class AccountSerializer(serializers.ModelSerializer):
    
    user = UserAccountSerializer()

    class Meta:
        model = Account
        fields = ('account_id', 'account_type', "address", "user")


