import webapp2
import jinja2
import os
from dailyexpenses import Date, Food_Ex, Transportation_Ex, Entertainment_Ex, CssiUser
import json
from datetime import datetime


from google.appengine.api import users
from google.appengine.ext import ndb

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Login(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # If the user is logged in...
    if user:
      first_name = user.nickname()
      cssi_user = CssiUser.get_by_id(user.user_id())
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/login'))
      # If the user has previously been to our site, we greet them!
      if cssi_user:
        self.response.write('''
            Welcome %s %s! <br> %s <br>''' % (
              cssi_user.first_name,
              cssi_user.last_name,
              signout_link_html))
      # If the user hasn't been to our site, we ask them to sign up
      else:
        self.response.write('''
            Welcome to our site!  Please sign up! <br>
            <form method="post" action="/mainpage">
            <input type="text" name="first_name">
            <input type="text" name="last_name">
            <input type="submit">
            </form><br> %s <br>
            ''' % (signout_link_html))


    # Otherwise, the user isn't logged in!
    else:
      self.response.write('''
        Please log in to use our site! <br>
        <a href="%s">Sign in</a>''' % (
          users.create_login_url('/login')))



  def post(self):
    user = users.get_current_user()
    if not user:
          self.response.write('''
              Welcome to our site!  Please sign up! <br>
              <form method="post" action="/mainpage">
              <input type="text" name="first_name">
              <input type="text" name="last_name">
              <input type="submit">
              </form><br> %s <br>
              ''' % (signout_link_html))
    cssi_user = CssiUser(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        id=user.user_id())
    cssi_user.put()
    self.response.write('Thanks for signing up, %s!' %
        cssi_user.first_name)

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        cssi_user = CssiUser(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            id=user.user_id())
        cssi_user.put()
        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/login'))

        if user:
            user = users.get_current_user()
            first_name = user.nickname()
            main_template = the_jinja_env.get_template('template/mainpage.html')
            variable_dic={
                "first_name": first_name,
            }
            self.response.write('''
                Welcome %s! <br> %s <br>''' % (
                  cssi_user.first_name,
                  signout_link_html))
            self.response.write(main_template.render(variable_dic))
        if cssi_user:
          self.response.write('''
              Welcome %s %s! <br> %s <br>''' % (
                cssi_user.first_name,
                cssi_user.last_name,
                signout_link_html))
        else:
            self.response.write('''
              Please log in to use this page! <br>
              <a href="%s">Sign in</a>''' % (
                users.create_login_url('/login')))

          # You shouldn't be able to get here without being logged in

    def post(self):
        user = users.get_current_user()
        cssi_user = CssiUser.get_by_id(user.user_id())
        main_template = the_jinja_env.get_template('template/mainpage.html')
        self.response.write('''
            Welcome %s! <br> %s <br>''' % (
              cssi_user.first_name,
              signout_link_html))
        self.response.write(main_template.render())

class Expenses(webapp2.RequestHandler):
    def get(self):
        self.response.write("This is the expense page")
    def post(self):
        expense_template = the_jinja_env.get_template('template/expense.html')
        date = self.request.get("date")
        foodList = []
        food = self.request.get_all('user-in-1')
        while(not food == ''):
            foodList.append(food)
        print(foodList)
        # food_list.append(food)
        price1 = self.request.get_all('user-in-2')
        print price1
        transportation = self.request.get_all('user-in-3')
        price2 = self.request.get('user-in-4')
        entertainment = self.request.get('user-in-5')
        price3 = self.request.get('user-in-6')
        # list = self.request.get('list')
        # list2 = self.request.get('list2')
        # list3 = self.request.get('list3')
        variable_dict={
            # 'food_info': food_list,
            "date": date,
            "food": food,
            "price1": price1,
            "transportation": transportation,
            "price2": price2,
            "entertainment": entertainment,
            "price3": price3,
            # "list": list,
            # "list2": list2,
            # "list3": list3,
        }
        self.response.write(expense_template.render(variable_dict))
        wrappeddate = datetime.strptime(date, "%Y-%m-%d")
        daTe = Date(date = wrappeddate)
        expenses = Food_Ex(foods = food, price1 = price1)
        transport_ex = Transportation_Ex(transportation = transportation, price2 = price2)
        entertain_ex = Entertainment_Ex(entertainment = entertainment, price3 = price3)
        expenses.put()
        transport_ex.put()
        entertain_ex.put()

class Home(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('template/welcome.html')
        self.response.write(home_template.render())

app = webapp2.WSGIApplication([
  ('/', Home),
  ('/login', Login),
  ('/mainpage', MainPage),
  ('/expense', Expenses)
], debug=True)
