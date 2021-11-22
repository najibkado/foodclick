from rest_framework import serializers
from .models import User, Entity, Listing, Giveaway


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, min_length=2)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)


    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email already in use')})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'usermane': ('Username already in use')})

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = [
            'id',
            'user',
            'name',
            'desc',
            'pickup_address',
            'phone',
            'date'
        ]

class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = [
            'id',
            'entity',
            'desc',
            'name'
            'pickup_address',
            'url',
            'quantity',
            'is_active',
            'date'
        ]

class GiveawaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Giveaway
        fields = [
            'id',
            'nin',
            'listing',
            'date'
        ]