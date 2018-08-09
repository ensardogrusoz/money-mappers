import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/mainpage', MainPage)
    # ('/data', DatabaseHandler),
    # ('/trivia', Trivia)
], debug=True)
