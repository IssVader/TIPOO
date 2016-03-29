'''
Created on Dec 10, 2013
Last modified on Nov 15, 2014
@author: Raul, Adriel
'''

class LearningStyle():
    '''
    Learning Style
    '''
    visual="Visual"
    auditory="Auditory"
    kinesthetic="Kinesthetic"
    Value_English={0:"Visual",1:"Auditory",2:"Kinesthetic"}
    Value_Spanish={0:"Visual",1:"Auditivo",2:"Kinestesico"}
    styles=[visual,auditory,kinesthetic]

    def get_learning_style(self, index):
    	return self.Value_Spanish[index]

