from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # Для валидации пароля
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, required=True)  # Роль пользователя

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'phone_number', 'role')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return data

    def create(self, validated_data):
        # Убираем 'password2' из данных, чтобы избежать ошибки
        validated_data.pop('password2', None)

        # Хэширование пароля
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Неверные учетные данные.")
            if not user.is_active:
                raise serializers.ValidationError("Пользователь неактивен.")
        else:
            raise serializers.ValidationError("Необходимо указать 'username' и 'password'.")

        data['user'] = user
        return data