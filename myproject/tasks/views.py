from rest_framework import viewsets
from .models import Task, Service
from .serializers import TaskSerializer, ServiceSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    @action(detail=True, methods=["get"])
    def tarefa(self, request, pk=None):
        servico = self.get_object()
        serializer = ServiceSerializer(servico.tarefa.all(),many=True)
        return Response(serializer.data)
        
        
    
    
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    
    
        
        
        