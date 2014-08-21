import os

import webapp2
import jinja2

templates = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class FrontPage(webapp2.RequestHandler):
	def get(self):

		template_values = {}

		template = templates.get_template('index.html')
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler=FrontPage),
	], debug=True)