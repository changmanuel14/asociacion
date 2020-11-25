import graphene
import asociados.schema

class Query(asociados.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)