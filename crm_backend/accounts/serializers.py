from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        data['user'] = {
            'id': user.id,
            'email': user.email,
            'role': user.role,
        }

        data['organization'] = {
            'id': user.organization.id,
            'name': user.organization.name,
            'subscription_plan': user.organization.subscription_plan,
        }

        return data