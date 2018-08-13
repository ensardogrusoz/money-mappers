from google.appengine.ext import ndb

class Date(ndb.Model):
    date = ndb.DateProperty(required=True)

class Food_Ex(ndb.Model):
    foods = ndb.StringProperty(repeated=True)
    price1 = ndb.IntegerProperty(repeated=True)

class Transportation_Ex(ndb.Model):
    transportation = ndb.StringProperty(required=True)
    price2 = ndb.IntegerProperty(required=True)

class Entertainment_Ex(ndb.Model):
    entertainment = ndb.StringProperty(required=True)
    price3 = ndb.IntegerProperty(required=True)
    # total = ndb.StringProperty(required=True)
