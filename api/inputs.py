import graphene

class CreateToolInstalledSensorInput(graphene.InputObjectType):
    r_toolmodule_id = graphene.UUID(required=True)
    r_toolsensortype_id = graphene.UUID(required=True)
    record_point = graphene.Float()