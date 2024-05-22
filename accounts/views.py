from .models import MainUser
from .serializers import MainUserSrializers
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.

class MainUserViewset(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSrializers

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance_id = instance.id
            self.perform_destroy(instance)
            return Response(
                {"detail": f"User with ID {instance_id} is successfully deleted."},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )