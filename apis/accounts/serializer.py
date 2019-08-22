from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apis.accounts.models import User, UserProfile
from django.db.transaction import atomic



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ["address"]



class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        self.REQUIRED_FIELD="username","email"
        self.ERRORS =[]
        super().__init__(*args, **kwargs)

    profile = ProfileSerializer()
    email = serializers.EmailField(required=False)
    username = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ['pk','username','email','profile','password','role']
        extra_kwargs = {'password':{'write_only':True}}

    @atomic
    def create(self, validated_data):
        print(validated_data)
        profile_data = validated_data.pop('profile')
        raw_password = validated_data.pop('password')
        for field in self.REQUIRED_FIELD:
            data = validated_data.get(field)
            if not data:
                self.ERRORS.append({field:"{field} field is required.".format(field)})
        if self.ERRORS:
            raise serializers.ValidationError(self.ERRORS)
        
        user = User(**validated_data)
        user.set_password(raw_password)
        user.save()

        UserProfile.objects.create(user=user, **profile_data)
        return user

    @atomic
    def update(self, instance, validated_data):
        profile_instance                =  instance.profile
        profile_data                    =  validated_data.pop("profile")

        instance.first_name             =  validated_data.get("first_name", instance.first_name)
        instance.last_name              =  validated_data.get("last_name", instance.last_name)

        if validated_data.get("password"):
            instance.set_password(validated_data["password"])

        profile_instance.address        =  profile_data.get("address",profile_instance.address)
        profile_instance.profile_pic    =  profile_data.get("profile_pic",profile_instance.profile_pic)
        return instance
