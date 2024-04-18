import graphene


# для добавления toolinstalledsensor указывается
# id toolmodule и id toolsensortype, record_point
class CreateToolInstalledSensorInput(graphene.InputObjectType):
    r_toolmodule_id = graphene.UUID(required=True)
    r_toolsensortype_id = graphene.UUID(required=True)
    record_point = graphene.Float()

# изменение поля record_point по id toolinstalledsensor
class UpdateToolInstalledSensorInput(graphene.InputObjectType):
    id = graphene.UUID(required=True)
    record_point = graphene.Float(required=True)

# удаление объекта ToolInstalledSensor по id
class DeleteToolInstalledSensorInput(graphene.InputObjectType):
    id = graphene.UUID(required=True)

# все параметры опциональны, кроме r_module_type_id, sn, dbsn, dbtname.
# они должны указываться при создании toolmodule обязательно
# TODO: проверить добавление в базу данных изображения image с фронта
class CreateToolModuleInput(graphene.InputObjectType):
    r_module_type_id = graphene.UUID(required=True)
    sn = graphene.String(required=True)
    dbsn = graphene.String(required=True)
    dbtname = graphene.String(required=True)
    dbdate = graphene.Date()
    dbversion = graphene.String()
    dbcomment = graphene.String()
    dbtlength = graphene.Float()
    dbtweight = graphene.Float()
    dbtmax_od = graphene.Float()
    dbtmax_od_collapsed = graphene.Float()
    dbtmax_od_opened = graphene.Float()
    dbtimage_h_shift = graphene.Float()
    dbtimage_h_scale = graphene.Float()
    dbtimage_h_y1 = graphene.Float()
    dbtimage_h_y2 = graphene.Float()
    dbtcomp_str = graphene.Float()
    image = graphene.String()
