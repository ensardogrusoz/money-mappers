import webapp2
import jinja2
import os
from dailyexpenses import Expense
import json
from datetime import datetime


from google.appengine.api import users
from google.appengine.ext import ndb

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



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

class MainHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # If the user is logged in...
    if user:
      email_address = user.nickname()
      cssi_user = CssiUser.get_by_id(user.user_id())
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/'))
      # If the user has previously been to our site, we greet them!
      if cssi_user:
        self.response.write('''
            Welcome %s %s (%s)! <br> %s <br>''' % (
              cssi_user.first_name,
              cssi_user.last_name,
              email_address,
              signout_link_html))
      # If the user hasn't been to our site, we ask them to sign up
      else:
        self.response.write('''
            Welcome to our site, %s!  Please sign up! <br>
            <form method="post" action="/">
            <input type="text" name="first_name">
            <input type="text" name="last_name">
            <input type="submit">
            </form><br> %s <br>
            ''' % (email_address, signout_link_html))
    # Otherwise, the user isn't logged in!
    else:
      self.response.write('''
        Please log in to use our site! <br>
        <a href="%s">Sign in</a>''' % (
          users.create_login_url('/')))

  def post(self):
    user = users.get_current_user()
    if not user:
      # You shouldn't be able to get here without being logged in
      self.error(500)
      return
    cssi_user = CssiUser(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        id=user.user_id())
    cssi_user.put()
    self.response.write('Thanks for signing up, %s!' %
        cssi_user.first_name)

class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = the_jinja_env.get_template('template/mainpage.html')
        self.response.write(main_template.render())

    def post(self):
        main_template = the_jinja_env.get_template('template/mainpage.html')
        self.response.write(main_template.render())

class Expenses(webapp2.RequestHandler):
    def get(self):
        self.response.write("This is the expense page")
    def post(self):
        expense_template = the_jinja_env.get_template('template/expense.html')
        date = self.request.get("date")
        food = self.request.get('user-in-1')
        price1 = self.request.get('user-in-2')
        transportation = self.request.get('user-in-3')
        price2 = self.request.get('user-in-4')
        entertainment = self.request.get('user-in-5')
        price3 = self.request.get('user-in-6')
        variable_dict={
            "date": date,
            "food": food,
            "price1": price1,
            "transportation": transportation,
            "price2": price2,
            "entertainment": entertainment,
            "price3": price3,
        }
        self.response.write(expense_template.render(variable_dict))
        wrappeddate = datetime.strptime(date, "%Y-%m-%d")
        expenses = Expense(date = wrappeddate, foods = food, price1 = price1, transportation = transportation, price2 = price2, entertainment = entertainment, price3 = price3)
        expenses.put()

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/mainpage', MainPage),
  ('/expense', Expenses)
], debug=True)
