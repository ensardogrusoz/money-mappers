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

class CssiUser(ndb.Model):
  """CssiUser stores information about a logged-in user.

  The AppEngine users api stores just a couple of pieces of
  info about logged-in users: a unique id and their email address.

  If you want to store more info (e.g. their real name, high score,
  preferences, etc, you need to create a Datastore model like this
  example).
  """
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
