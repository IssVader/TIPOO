'''
Created on Nov 15, 2014
@author: Adriel
'''

class LevelType():
	'''
	LevelType
	'''
	basic="Basic"
	intermediate="Intermediate"
	advanced="Advanced"
	Value_English={0:"Basic",1:"Intermediate",2:"Advanced"}
	Value_Spanish={0:"Basico",1:"Intermedio",2:"Avanzado"}

	def get_level_type(self,index):
		return self.Value_Spanish[index]