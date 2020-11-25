import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from asociados.models import Asociado, Especialidad, Subespecialidad

class EspecialidadNode(DjangoObjectType):
    class Meta:
        model = Especialidad
        filter_fields = ['categoria', 'asociados']
        interfaces = (relay.Node, )

class SubespecialidadNode(DjangoObjectType):
    class Meta:
        model = Subespecialidad
        filter_fields = ['categoria', 'asociados']
        interfaces = (relay.Node, )

class AsociadoNode(DjangoObjectType):
    class Meta:
        model = Asociado
        filter_fields = {
            'nombre': ['exact', 'icontains', 'istartswith'],
            'apellido': ['exact', 'icontains', 'istartswith'],
            'fecha_nacimiento': ['exact', 'icontains'],
            'fecha_renMem': ['exact', 'icontains'],
            'telefono': ['exact'],
            'correo': ['exact'],
            'direccion': ['exact'],
            'especialidad': ['exact'],
            'especialidad__categoria': ['exact'],
            'subespecialidad': ['exact'],
            'subespecialidad__categoria': ['exact'],
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    
    especialidad = relay.Node.Field(EspecialidadNode)
    all_especialidades = DjangoFilterConnectionField(EspecialidadNode)

    subespecialidad = relay.Node.Field(SubespecialidadNode)
    all_subespecialidades = DjangoFilterConnectionField(SubespecialidadNode)

    asociado = relay.Node.Field(AsociadoNode)
    all_asociados = DjangoFilterConnectionField(AsociadoNode)