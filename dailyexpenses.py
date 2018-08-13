from google.appengine.ext import ndb

class Expense(ndb.Model):
    # date = ndb.DateProperty(required=True)
    foods = ndb.StringProperty(required=True)
    price1 = ndb.StringProperty(required=True)
    transportation = ndb.StringProperty(required=True)
    price2 = ndb.StringProperty(required=True)
    entertainment = ndb.StringProperty(required=True)
    price3 = ndb.StringProperty(required=True)
    # total = ndb.StringProperty(required=True)
