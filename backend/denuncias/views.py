from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import DenunciaAmbiental
from .serializers import DenunciaSerializer

class DenunciaViewSet(viewsets.ModelViewSet):
    queryset = DenunciaAmbiental.objects.all()
    serializer_class = DenunciaSerializer

    # Esta función es la magia: abre la puerta solo para crear denuncias
    def get_permissions(self):
        if self.action == 'create':
            # Permite a los ciudadanos (sin login) enviar el formulario (POST)
            return [AllowAny()]
        # Exige login a los técnicos para ver, editar o borrar las denuncias
        return [IsAuthenticated()]