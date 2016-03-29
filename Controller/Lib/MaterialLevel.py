'''
Created on Dec 12, 2013

@author: Raul
'''

class MaterialLevel():
    '''
    Material Level
    '''
    basic="0"#"Basic"
    medium="1"#"Medium"
    advance="2"#"Advance"
    levels=[basic,medium,advance]
    
    def get_lang_level(self,lang,name):
        chp = self.get_material_level("uni").index(name)
        return self.get_material_level(lang)[int(chp)]
    
    def get_uni_level(self,lang,level):
        lvl = self.get_material_level(lang).index(str(level))
        return self.get_material_level("uni")[lvl]

    def get_material_level(self,lang):
    
        def spanish():
            material_level=["B&aacute;sico","Intermedio","Avanzado"]
            return material_level
        
        def uni():             
            material_level=["0","1","2"]
            return material_level
        
        level_lang={"spanish":spanish,
                       "uni":uni
                       }
        
        return level_lang[lang]()