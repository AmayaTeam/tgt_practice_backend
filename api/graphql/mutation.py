import graphene
import graphql_jwt

from api.graphql.mutations.tool_installed_sensor import (
    CreateToolInstalledSensor,
    UpdateToolInstalledSensor,
    DeleteToolInstalledSensor,
)
from api.graphql.mutations.tool_module import (
    CreateToolModule,
    UpdateToolModule,
    DeleteToolModule,
)
from api.graphql.mutations.tool_module_group import (
    CreateToolModuleGroup,
    UpdateToolModuleGroup,
    DeleteToolModuleGroup,
)


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_tool_installed_sensor = CreateToolInstalledSensor.Field()
    update_tool_installed_sensor = UpdateToolInstalledSensor.Field()
    delete_tool_installed_sensor = DeleteToolInstalledSensor.Field()

    create_tool_module = CreateToolModule.Field()
    update_tool_module = UpdateToolModule.Field()
    delete_tool_module = DeleteToolModule.Field()

    create_tool_module_group = CreateToolModuleGroup.Field()
    update_tool_module_group = UpdateToolModuleGroup.Field()
    delete_tool_module_group = DeleteToolModuleGroup.Field()
