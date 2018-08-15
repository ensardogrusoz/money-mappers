import webapp2
import jinja2
import os
from dailyexpenses import Date, Food_Ex, Transportation_Ex, Entertainment_Ex, CssiUser
import json
from datetime import datetime



from google.appengine.ext import ndb

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Login(webapp2.RequestHandler):
    def get(self):
      from google.appengine.api import users
      user = users.get_current_user()
      # If the user is logged in...
      if user:
        first = user.nickname()
        cssi_user = CssiUser.get_by_id(user.user_id())
        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/'))
        # If the user has previously been to our site, we greet them!
        if cssi_user:
          self.response.write('''
              Welcome %s! <br> %s <br>''' % (
                cssi_user.first_name,
                signout_link_html))
        # If the user hasn't been to our site, we ask them to sign up
        else:
          self.response.write('''
              Welcome to our site!  Please sign up! <br>
              <form method="post" action="/mainpage">
              <h3>Enter First Name: </h3><input type="text" name="first_name">
              <h3>Enter Last Name: </h3><input type="text" name="last_name">
              <input type="submit">
              </form><br> %s <br>
              ''' % (signout_link_html))
        cs_user = CssiUser(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            id=user.user_id())
        cs_user.put()
      # Otherwise, the user isn't logged in!
      else:
        self.response.write('''
<<<<<<< HEAD
          Please log in to use our site! <br>
          <a href="%s">Sign in</a>''' % (
            users.create_login_url('/login')))

    def post(self):
      from google.appengine.api import users
      user = users.get_current_user()
      # If the user is logged in...
      if user:
        first = user.nickname()
        cssi_user = CssiUser.get_by_id(user.user_id())
        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/'))
        # If the user has previously been to our site, we greet them!
        if cssi_user:
          self.response.write('''
              Welcome %s! <br> %s <br>''' % (
                cssi_user.first_name,
                signout_link_html))
        # If the user hasn't been to our site, we ask them to sign up
        else:
=======
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
>>>>>>> 403f05464155b0fa8a854bc66ee4ba92ceda3f22
          self.response.write('''
              Welcome to our site!  Please sign up! <br>
              <form method="post" action="/mainpage">
              <h3>Enter First Name: </h3><input type="text" name="first_name">
              <h3>Enter Last Name: </h3><input type="text" name="last_name">
              <input type="submit">
              </form><br> %s <br>
              ''' % (signout_link_html))
        cs_user = CssiUser(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            id=user.user_id())
        cs_user.put()
      # Otherwise, the user isn't logged in!
      else:
        self.response.write('''
          Please log in to use our site! <br>
          <a href="%s">Sign in</a>''' % (
            users.create_login_url('/login')))

class MainPage(webapp2.RequestHandler):
    def get(self):
        from google.appengine.api import users
        user = users.get_current_user()
        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/'))
        # If the user is logged in...
        if user:
          first = user.nickname()
          cssi_user = CssiUser.get_by_id(user.user_id())

          # If the user has previously been to our site, we greet them!
          if cssi_user:
            cs_user = CssiUser(
                first_name=self.request.get('first_name'),
                last_name=self.request.get('last_name'),
                id=user.user_id())
            cs_user.put()
            self.response.write('''
                Welcome %s! <br> %s <br>''' % (
                  cs_user.first_name,
                  signout_link_html))
            main_template = the_jinja_env.get_template('template/mainpage.html')
            self.response.write(main_template.render())
          else:
            fail_template = the_jinja_env.get_template('template/main-fail.html')
            self.response.write(fail_template.render())
        # Otherwise, the user isn't logged in!
        else:
          fail_template = the_jinja_env.get_template('template/main-fail.html')
          self.response.write(fail_template.render())

    def post(self):
        from google.appengine.api import users
        user = users.get_current_user()
        cssi_user = CssiUser.get_by_id(user.user_id())
        cs_user = CssiUser(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            id=user.user_id())
        cs_user.put()
        signout_link_html = '<a href="%s">Sign Out</a>' % (
             users.create_logout_url('/'))
        if cssi_user:
          self.response.write('''
              Welcome %s! <br> %s <br>''' % (
                cs_user.first_name,
                signout_link_html))
        main_template = the_jinja_env.get_template('template/mainpage.html')
        date = self.request.get("date")
        variable_dict = {
            "date": date,
        }
        self.response.write(main_template.render(variable_dict))
        wrappeddate = datetime.strptime(date, "%Y-%m-%d")
        daTe = Date(date = wrappeddate)


class Expenses(webapp2.RequestHandler):
    def get(self):
        self.response.write("This is the expense page")
    def post(self):
        expense_template = the_jinja_env.get_template('template/expense.html')
        food = self.request.get('user-in-1')
        price1 = self.request.get('user-in-2')
        transportation = self.request.get('user-in-3')
        price2 = self.request.get('user-in-4')
        entertainment = self.request.get('user-in-5')
        price3 = self.request.get('user-in-6')
        foods = Food_Ex.query().fetch()
        trans = Transportation_Ex.query().fetch()
        enter = Entertainment_Ex.query().fetch()
        var_dic={
            "food": food,
            "price1": price1,
            "transportation": transportation,
            "price2": price2,
            "entertainment": entertainment,
            "price3": price3,
            'food_info' : foods,
            'trans_info' : trans,
            'enter_info' : enter,
        }
        self.response.write(expense_template.render(var_dic))
        food_ex = Food_Ex(food = food, price1 = float(price1))
        food_ex.put()
        transport_ex = Transportation_Ex(transportation = transportation, price2 = float(price2))
        transport_ex.put()
        entertain_ex = Entertainment_Ex(entertainment = entertainment, price3 = float(price3))
        entertain_ex.put()



class Home(webapp2.RequestHandler):
    def get(self):
        from google.appengine.api import users
        user = users.get_current_user()
        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/'))
        # If the user is logged in...
        if user:
          first = user.nickname()
          cssi_user = CssiUser.get_by_id(user.user_id())
          if cssi_user:
              cs_user = CssiUser(
                  first_name=self.request.get('first_name'),
                  last_name=self.request.get('last_name'),
                  id=user.user_id())
              cs_user.put()
              home_template = the_jinja_env.get_template('template/welcome.html')
              self.response.write(home_template.render())
          else:
              home_template = the_jinja_env.get_template('template/welcome.html')
              self.response.write(home_template.render())
          # Otherwise, the user isn't logged in!
        else:
          home_template = the_jinja_env.get_template('template/welcome.html')
          self.response.write(home_template.render())

    def post(self):
        from google.appengine.api import users
        user = users.get_current_user()
        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/'))
        # If the user is logged in...
        if user:
          first = user.nickname()
          cssi_user = CssiUser.get_by_id(user.user_id())
          if cssi_user:
            cs_user = CssiUser(
                first_name=self.request.get('first_name'),
                last_name=self.request.get('last_name'),
                id=user.user_id())
            cs_user.put()
            home_template = the_jinja_env.get_template('template/welcome.html')
            self.response.write(home_template.render())
          else:
            home_template = the_jinja_env.get_template('template/welcome.html')
            self.response.write(home_template.render())
      # Otherwise, the user isn't logged in!
        else:
          home_template = the_jinja_env.get_template('template/welcome.html')
          self.response.write(home_template.render())

class Start(webapp2.RequestHandler):
    def get(self):
        start_template = the_jinja_env.get_template('template/main.html')
        self.response.write(start_template.render())

    def post(self):
        start_template = the_jinja_env.get_template('template/main.html')
        self.response.write(start_template.render())

class Monthly(webapp2.RequestHandler):
    def get(self):
        self.response.write("Monthly Expense Page")

    def post(self):
        month_template = the_jinja_env.get_template('template/monthly.html')
        self.response.write(month_template.render())
        
app = webapp2.WSGIApplication([
  ('/', Home),
  ('/login', Login),
  ('/start', Start),
  ('/mainpage', MainPage),
  ('/expense', Expenses),
  ('/monthly', Monthly)
], debug=True)
