from rest_framework_simplejwt.views import TokenViewBase
from .serializers import CustomTokenSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Company, Contact
from .serializers import CompanySerializer, ContactSerializer
from .permissions import RoleBasedPermission

class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenSerializer
    

# class CompanyViewSet(viewsets.ModelViewSet):
#     serializer_class = CompanySerializer
#     permission_classes = [IsAuthenticated]

#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name', 'industry', 'country']

#     def get_queryset(self):
#         return Company.objects.filter(
#             organization=self.request.user.organization,
#             is_deleted=False
#         )

#     def perform_create(self, serializer):
#         serializer.save(organization=self.request.user.organization)

#     def perform_destroy(self, instance):
#         instance.is_deleted = True
#         instance.save()
        

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [RoleBasedPermission]

    def get_queryset(self):
        return Company.objects.filter(
            organization=self.request.user.organization,
            is_deleted=False
        )

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        
        
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [RoleBasedPermission]

    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']

    def get_queryset(self):
        return Contact.objects.filter(
            organization=self.request.user.organization,
            is_deleted=False
        )

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()