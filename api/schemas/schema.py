import graphene
from api.service.case_service import CaseService

class Case(graphene.ObjectType):
    uuid = graphene.Int(required=True)
    country = graphene.String()
    gender = graphene.String()
    age = graphene.String()
    is_dead = graphene.Boolean()


class Query(graphene.ObjectType):
    case = graphene.Field(Case, uuid=graphene.Int())

    def resolve_case(self, info, uuid):
        print(uuid)
        result = CaseService.get_case(CaseService, uuid)
        return Case(
            uuid=result[0],
            country=result[1],
            gender=result[2],
            age=result[3],
            is_dead=result[4]
        )

schema = graphene.Schema(query=Query)