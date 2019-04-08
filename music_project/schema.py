import graphene

import main_app.schema


class Query(main_app.schema.Query,graphene.ObjectType):
	pass


schema=graphene.Schema(query=Query)
