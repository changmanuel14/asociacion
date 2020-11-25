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


class CreateAsociado(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()
        fecha_nacimiento = graphene.types.datetime.DateTime()
        fecha_renMem = graphene.types.datetime.DateTime()
        telefono = graphene.Int()
        direccion = graphene.String()
        correo = graphene.String()
        especialidad = graphene.List(graphene.ID)
        subespecialidad = graphene.List(graphene.ID)

    asociado = graphene.Field(AsociadoNode)

    def mutate(self, info, nombre=None, apellido=None, fecha_nacimiento=None, fecha_renMem=None, telefono=None, direccion=None, correo=None, especialidad=None, subespecialidad=None):
        asociado = Asociado.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            fecha_renMem=fecha_renMem,
            telefono=telefono,
            direccion=direccion,
            correo=correo
        )

        if especialidad is not None:
            especialidad_set = []
            for especialidad_id in especialidad:
                especialidad_object = Especialidad.objects.get(pk=especialidad_id)
                especialidad_set.append(especialidad_object)
            asociado.especialidad.set(especialidad_set)

        if subespecialidad is not None:
            subespecialidad_set = []
            for subespecialidad_id in subespecialidad:
                subespecialidad_object = Subespecialidad.objects.get(pk=subespecialidad_id)
                subespecialidad_set.append(subespecialidad_object)
            asociado.subespecialidad.set(subespecialidad_set)
            
        asociado.save()

        return CreateAsociado(
            asociado=asociado
        )

class UpdateAsociado(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()
        fecha_nacimiento = graphene.types.datetime.DateTime()
        fecha_renMem = graphene.types.datetime.DateTime()
        telefono = graphene.Int()
        direccion = graphene.String()
        correo = graphene.String()
        especialidad = graphene.List(graphene.ID)
        subespecialidad = graphene.List(graphene.ID)

    asociado = graphene.Field(AsociadoNode)

    def mutate(self, info, id, nombre=None, apellido=None, fecha_nacimiento=None, fecha_renMem=None, telefono=None,direccion=None, correo=None, especialidad=None, subespecialidad=None):
        asociado = Asociado.objects.get(pk=id)
        asociado.nombre=nombre if nombre is not None else asociado.nombre,
        asociado.apellido=apellido if apellido is not None else asociado.apellido,
        asociado.fecha_nacimiento=fecha_nacimiento if fecha_nacimiento is not None else asociado.fecha_nacimiento,
        asociado.fecha_renMem=fecha_renMem if fecha_renMem is not None else asociado.fecha_renMem,
        asociado.telefono=telefono if telefono is not None else asociado.telefono,
        asociado.direccion=direccion if direccion is not None else asociado.direccion,
        asociado.correo=correo if correo is not None else asociado.correo

        if especialidad is not None:
            especialidad_set = []
            for especialidad_id in especialidad:
                especialidad_object = Especialidad.objects.get(pk=especialidad_id)
                especialidad_set.append(especialidad_object)
            asociado.especialidad.set(especialidad_set)

        if subespecialidad is not None:
            subespecialidad_set = []
            for subespecialidad_id in subespecialidad:
                subespecialidad_object = Subespecialidad.objects.get(pk=subespecialidad_id)
                subespecialidad_set.append(subespecialidad_object)
            asociado.subespecialidad.set(subespecialidad_set)
            
        asociado.save()

        return UpdateAsociado(
            asociado=asociado
        )

class DeleteAsociado(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    asociado = graphene.Field(AsociadoNode)

    def mutate(self, info, id):
        asociado = Asociado.objects.get(pk=id)
        if asociado is not None:
            asociado.delete()
        return DeleteAsociado(asociado=asociado)

class Mutation(graphene.ObjectType):
    create_asociado = CreateAsociado.Field()
    update_asociado = UpdateAsociado.Field()
    delete_asociado = DeleteAsociado.Field() 