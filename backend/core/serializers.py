from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Company, Contact

class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'organization': self.user.organization.name,
            'role': self.user.role,
        }

        return data
    
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['organization', 'created_at']
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['organization', 'created_at']

    # Extra validation (good practice)
    def validate_email(self, value):
        company = self.initial_data.get('company')

        if Contact.objects.filter(email=value, company_id=company).exists():
            raise serializers.ValidationError("Email must be unique within this company")

        return value