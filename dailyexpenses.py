from google.appengine.ext import ndb

class Date(ndb.Model):
    date = ndb.DateProperty(required=True)
    
class Food_Ex(ndb.Model):
    foods = ndb.StringProperty(required=True)
    price1 = ndb.StringProperty(required=True)

class Transportation_Ex(ndb.Model):
    transportation = ndb.StringProperty(required=True)
    price2 = ndb.StringProperty(required=True)

class Entertainment_Ex(ndb.Model):
    entertainment = ndb.StringProperty(required=True)
    price3 = ndb.StringProperty(required=True)
    # total = ndb.StringProperty(required=True)
