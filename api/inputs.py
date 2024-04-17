import graphene

class CreateToolInstalledSensorInput(graphene.InputObjectType):
    # для добавления toolinstalledsensor указывается
    # id toolmodule и id toolsensortype, record_point
    r_toolmodule_id = graphene.UUID(required=True)
    r_toolsensortype_id = graphene.UUID(required=True)
    record_point = graphene.Float()

class UpdateToolInstalledSensorInput(graphene.InputObjectType):
    # изменение поля record_point по id toolinstalledsensor
    id = graphene.UUID(required=True)
    record_point = graphene.Float(required=True)

class DeleteToolInstalledSensorInput(graphene.InputObjectType):
    # удаление объекта ToolInstalledSensor по id
    id = graphene.UUID(required=True)
