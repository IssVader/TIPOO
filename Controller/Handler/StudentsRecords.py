'''
Created on Mar 15, 20156

@author: Brandon Ramirez Ayala
'''
import os
import time
import json
import jinja2
import copy
import time
import datetime
from RequestManager import RequestManagement as request_management
from Controller.Lib.UserType import UserType as user_type
from Controller.Management.MaterialManagement.VideoMaterialManagement import VideoMaterialManagement as video_material_management
from Controller.Management.CollegeManagement.SubjectManagement import SubjectManagement as subject_management
from Controller.Management.CollegeManagement.TopicManagement import TopicManagement as topic_management
from Controller.Management.UserManagement import TutorManagement as tutor_management
from Controller.Management.UserManagement import StudentManagement as student_management
from Model.UserTracking.Session import Session as session
from Model.UserTracking.Action import Action as action


JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname('View/')))
students_records_template = JINJA_ENVIRONMENT.get_template('students_records_template.tmp')

class StudentsRecords(request_management):
    
    def get(self):
        user = self.get_user_type()                    
        if user == user_type.visitor:
        	self.redirect('/')
        	return 0
        elif user == user_type.student:
        	self.redirect('/')
        	return 1
        elif user == user_type.tutor:
            template_values = {}
            list_data = session().get_all_sessions()
            
            data_sessions = {}
            list_data_sessions = []
            for l  in list_data:
                student = student_management().get_student( l.user.key().id() )
                data_sessions['name'] = student.first
                data_sessions['last'] = student.last
                data_sessions['email'] = student.email
                data_sessions['sex'] = student.sex
                data_sessions['bday'] = student.bday
                data_sessions['learning_style'] = student.learning_style
                data_sessions['time_init'] = datetime.datetime.fromtimestamp(l.time_init).strftime('%Y-%m-%d %H:%M:%S')
                data_sessions['time_end'] = datetime.datetime.fromtimestamp(l.time_end).strftime('%Y-%m-%d %H:%M:%S')
                data_sessions['time_conected'] = datetime.datetime.fromtimestamp(l.time_conected).strftime('%H:%M:%S')
                data_sessions['number_clicks'] = action().count_events_between_dates(l.time_init,l.time_end,'click',l.user)
                data_sessions['number_scrolls'] = action().count_events_between_dates(l.time_init,l.time_end,'scroll',l.user)
                list_data_sessions.append(data_sessions.copy())

             
            
            
            template_values = {'list_data_sessions':list_data_sessions}
            self.response.write(students_records_template.render(template_values))
            
            return 2
        else:
        	return 3

    def post(self):
    	print("never get here")