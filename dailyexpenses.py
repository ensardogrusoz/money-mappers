from google.appengine.ext import ndb


class CssiUser(ndb.Model):
  first_name = ndb.StringProperty(required=True)
  last_name = ndb.StringProperty()

class Date(ndb.Model):
    date = ndb.DateProperty(required=True)

class Food_Ex(ndb.Model):
    food = ndb.StringProperty(required=True)
    price1 = ndb.FloatProperty(required=True)
    # ourusers = ndb.KeyProperty(CssiUser, repeated=True)
    # price1 = ndb.IntegerProperty(repeated=True)

class Transportation_Ex(ndb.Model):
    transportation = ndb.StringProperty(required=True)
    price2 = ndb.FloatProperty(required=True)

class Entertainment_Ex(ndb.Model):
    entertainment = ndb.StringProperty(required=True)
    price3 = ndb.FloatProperty(required=True)
    # total = ndb.StringProperty(required=True)
