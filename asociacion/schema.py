import graphene
import asociados.schema

class Query(asociados.schema.Query, graphene.ObjectType):
    pass

class Mutation(asociados.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)