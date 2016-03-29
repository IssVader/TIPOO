'''
Created on 22/01/2014
Last Modified on Nov 13, 2014
@author: Raul, Adriel
'''
import time
import datetime
from Controller.Handler.RequestManager import RequestManagement as request_management
from Controller.Handler.UserSession import UserSession as user_session
from Model.UserTracking.Session import Session as session
from Controller.Management.UserManagement import StudentManagement as student_management
from Controller.Lib.UserType import UserType as user_type
#from tipoo.Lib.UserType import UserType as user_type



class Logout(request_management):
    '''
    Home
    '''
    def get(self):
        user = self.get_user_type()                    
        if user == user_type.visitor:                    
            self.redirect('/')
            return 0
        elif user == user_type.student:
            '''
            user_id=self.get_user_id()
            self.response.write(user_id)
            self.response.write('<br>')
            '''
            
            s = session()
            student_id = self.session['user-id']
            user = student_management().get_student(student_id)
            
            
            s.user = user
            s.time_init = self.session['user-time']
            s.time_end = time.time()
            s.time_conected = s.time_end - self.session['user-time'] 
            s.put()
            
            
            user_session().close(self.session)
            
            '''
            #self.response.write(logout)
            #if str(user_id) == str(logout):
            #for s in self.session.keys():
            #    self.session[s]=None
                #self.response.write(self.session[s])
                #self.response.write('<br/>')
            #self.session['user']=None
            #self.session['user-id']=None
            '''
            
            self.redirect('/')


            return 1

        elif user == user_type.tutor:

            user_session().close(self.session)
    
            self.redirect('/')

            return 2        