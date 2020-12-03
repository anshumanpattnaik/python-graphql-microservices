import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import States as StatesModel
from models import Statistics as StatisticsModel
from models import TotalCases as TotalCasesModel
from models import Subscriber as SubscriberModel


class States(MongoengineObjectType):

    class Meta:
        model = StatesModel
        interfaces = (Node,)


class Statistics(MongoengineObjectType):

    class Meta:
        model = StatisticsModel
        interfaces = (Node,)


class TotalCases(MongoengineObjectType):

    class Meta:
        model = TotalCasesModel
        interfaces = (Node,)


class Subscriber(MongoengineObjectType):

    class Meta:
        model = SubscriberModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_statistics = MongoengineConnectionField(Statistics)
    all_states = MongoengineConnectionField(States)
    all_total_cases = MongoengineConnectionField(TotalCases)
    all_subscriber = MongoengineConnectionField(Subscriber)


class fetchByCountryName(graphene.Mutation):
    class Arguments:
        country = graphene.String(required=True)

    statistics = graphene.Field(lambda: Statistics)

    def mutate(self, info, country):
        country_statistics = StatisticsModel.objects.get(country=country)
        return fetchByCountryName(statistics=country_statistics)


class Mutation(graphene.ObjectType):
    fetch_by_country_name = fetchByCountryName.Field()


schema = graphene.Schema(
    query=Query, types=[States, Statistics, TotalCases, Subscriber], mutation=Mutation)
