'''
Last Modified on Mar 20, 2015
@author: Thomas, Raul
'''
from google.appengine.ext import db
from Model.Intelligent.IntelligentType import IntelligentType
from Model.User.Student import Student as Student
from Model.Subject.Subject import Subject
from Model.UserTracking.Action import Action
import time

class Session(db.Model):
	'''
	StudentRecords
	'''
	time_init = db.FloatProperty()
	time_end = db.FloatProperty()
	time_conected = db.FloatProperty()
	user = db.ReferenceProperty(Student)

	def get_all_sessions(self):
		query_str = "SELECT * FROM Session "
		return db.GqlQuery(query_str).fetch(limit=50)
		