import os
import logging

import webapp2
import jinja2

from google.appengine.api import users

import models

templates = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class EditPage(webapp2.RequestHandler):
	def get(self, path):

		logging.debug(path)

		user = users.get_current_user()

		template_values = {
			"user" : user,
		}

		template = templates.get_template('edit.html')
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
	webapp2.Route(r'/<path:.+?>/edit', handler=EditPage),
	], debug=True)