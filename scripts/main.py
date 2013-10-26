
import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader( 'pages'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())
        #self.response.write(os.path.dirname(__file__))
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
