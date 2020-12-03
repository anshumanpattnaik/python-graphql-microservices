from mongoengine import Document
from mongoengine.fields import (
    ListField, DecimalField, IntField,ReferenceField, StringField,
)

class States(Document):
    meta = {'collection': 'states'}
    key = StringField()
    name = StringField()
    address = StringField()
    latitude = DecimalField()
    longitude = DecimalField()
    confirmed = IntField()
    deaths = IntField()
    recovered = IntField()

class Statistics(Document):
    meta = {'collection': 'statistics'}
    country = StringField()
    code = StringField()
    flag = StringField()
    coordinates = ListField(DecimalField())
    confirmed = IntField()
    deaths = IntField()
    recovered = IntField()
    states = ListField(ReferenceField(States))

class TotalCases(Document):
    meta = {'collection': 'total_cases'}
    total_confirmed = IntField()
    total_deaths = IntField()
    total_recovered = IntField()
    last_date_updated = StringField()

class Subscriber(Document):
    meta = {'collection': 'subscriber'}
    email = StringField()