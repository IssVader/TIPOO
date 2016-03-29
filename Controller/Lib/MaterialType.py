'''
Created on Dec 13, 2013

@author: Raul
'''

class MaterialType():
    '''
    Material Type
    '''
    video="0"
    text="1"    
    supported_materials=[video,text]
    
    def get_uni_type(self,lang,name):
        t = self.get_chapters(lang).index(name)
        return self.get_chapters("uni")[t]
    
    def get_material_type(self,lang):
        
        def spanish():
            material_type=["video","texto"]
            return material_type
            
        def uni():             
            material_type=["0","1"]
            return material_type
        
        material_lang={"spanish":spanish,
                       "uni":uni
                       }
        
        return material_lang[lang]()