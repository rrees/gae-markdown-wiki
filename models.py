
from google.appengine.ext import ndb

class Entry(ndb.Model):
	title = ndb.StringProperty(required=True)
	content = ndb.TextProperty(required=True)
	creator = ndb.UserProperty(required=True)
	created = ndb.DateTimeProperty(auto_now_add=True)
	tags = ndb.StringProperty(repeated=True)
