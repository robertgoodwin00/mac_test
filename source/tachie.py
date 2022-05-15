

import os
import pygame


main_directory = os.path.split(os.path.abspath(__file__))[0]
main_dir = os.path.join(main_directory,"../")


#quick function to load an image
def load_image(name, dtype = 0, subdirectory_name = '', subdirectory_name2 = ''):
    directory_name = 'tachie'
   
                
    path = os.path.join(main_dir, directory_name, subdirectory_name, subdirectory_name2, name)  # join path with directory
    #path = os.path.join(directory_name,subdirectory_name,subdirectory_name2,name)
    
    #if os.path.exists(path):
    image = pygame.image.load(path)  #.convert_alpha()
    #else:
    #    image = None
    #    print('error. image ' + path + ' couldnt be loaded')
    
    #if colorkey is not None:
    #    if colorkey is -1:
    #        colorkey = image.get_at((0,0))
    #    image.set_colorkey(colorkey, RLEACCEL)
    return image  
    

def can_load_image(name, dtype = 0, subdirectory_name = '', subdirectory_name2 = ''):
    directory_name = 'tachie'
   

    path = os.path.join(main_dir, directory_name, subdirectory_name, subdirectory_name2, name)  # join path with directory
    #path = os.path.join(directory_name,subdirectory_name,subdirectory_name2,name)

    if os.path.exists(path):
        return True
    return False 




# one of thse objects contains all data for showing an npc on screen visual novel style
# the get_tachie() method near the end is called from scenery.py and roster.py (and elsewhere I think)
class Tachie():
    def __init__(self, is_male = False):
        self.pose = 'a'
        self.horizontal_flip = True
        self.skinColor = 2
        self.heightAdjust = 0
        self.clothesID = 99
        #self.clothesColor = ColorData()
        self.clothesColorIndex = -1
        self.last_worn_clothesID = 99
        
        self.headID = 100
        
        self.hairBackID = 100
        self.hairFrontID = 100
        self.hairColor = ColorData()
        
        self.eyesID = 99
        self.eyesOpenID = 99 # used only for characters whose eyes are usually shut
        self.eyesID_contemplative = 99 # shut eyes used for around 50% of characters
        self.eyesColor = ColorData()
        
        self.faceID = 99  # mouth and eyebrows that combine for an expression
        self.faceID_surprised = 99
        self.faceID_happy = 99
        self.faceID_unhappy = 99
        self.faceID_contemplative = 99
        
        self.accessoryClothesID = 0
        self.accessoryClothesColor = ColorData()
        self.accessoryHeadID = 0
        self.accessoryHeadColor = ColorData()
        self.accessoryBodyID = 0
        self.accessoryBodyColor = ColorData()
        
        self.setAll(False)
        
        self.own_clothesID = self.clothesID
        self.own_clothesColorIndex = self.clothesColorIndex
       
       
    def isGlasses(self):
        s = self.accessoryHeadID
        if self.gender == 'female' and s == 125:
            return True
        elif self.gender == 'male' and (s == 105 or s == 110 or s ==115):
            return True
        return False
    
    def isTie(self):
        c = self.clothesID
        if self.gender == 'male' and c >= 105 and c <= 117:
            return True
        elif self.gender == 'female' and (c == 167 or c == 168):
            return True
        return False
    
    def isNecklace(self):
        b = self.accessoryBodyID
        c = self.clothesID
        if self.gender == 'female' and (b == 100 or c == 245 or c == 206):
            return True
        return False
            
    def isHairAccessory(self):
        s = self.accessoryHeadID
        if self.gender == 'female' and (s == 100 or s == 105 or s == 110 or s == 120 or s == 130):
            return True
        return False
        
    def isBelt(self):
        c = self.clothesID
        if self.gender == 'male' and (c == 100 or c == 111 or c == 114 or c == 115 or c == 126 or c == 128):
            return True
        return False
        
    def isGloves(self):
        b = self.accessoryBodyID
        c = self.clothesID
        if self.gender == 'female' and (c == 240 or c == 245 or b == 110):
            return True
        return False

    
    def change_clothes(self, clothesID, is_male, color_index = -1):
        self.clothesID = clothesID
        if color_index != -1:
            self.clothesColorIndex = color_index
    
        # handle cases where we don't have all poses (female only since male only has one pose)
        
    
    # set the tachie's body, face, hair, clothes, colors, etc 
    def setAll(self, is_male = True):
        self.gender = 'male' if is_male else 'female'
        self.skinColor = 5 
        if self.skinColor > 8: # make lighter colors more prevalent
            self.skinColor -= 9
        
        height_type = 0
        # more tall heights than short heights. for males 0-5 with 5 (short) being rarer. for females 0-8, with 7 being rarer, 8 very rare
        height_type = 2

        #height_adjust = (height_type * 5) + (height_type * height_type)    # 0, 6, 14, 24, 36, 50
        self.heightAdjust = (height_type * 4) + (height_type * height_type)    # 0, 5, 12, 21, 32, 45, 60, 77, 96
        

        self.headID = 100 #id_data.random_headID(is_male)
        self.hairBackID = 100 #id_data.random_hairBackID(is_male) 
        self.hairFrontID = 100 #id_data.random_hairFrontID(is_male)
        #self.eyesID = 100 #id_data.random_eyesID(is_male)
        #self.faceID = 100 #id_data.random_faceID(is_male, self.skinColor)
        self.clothesID = 100 #id_data.random_clothesID(is_male) 
        
        self.change_clothes(self.clothesID, is_male)
            

        self.set_clothesColor(is_male)
        #self.set_accessoryHead()
        #self.set_accessoryClothes()
        #self.set_accessoryBody()
        

    
    
    # reassign eyes and face based on character traits
    def set_eyes_and_face(self, is_male, traits):
        id_data = ID_Data()
        self.eyesID, self.eyesOpenID = id_data.reassigned_eyesID(is_male, traits)
        self.faceID = id_data.reassigned_faceID(is_male, self.skinColor, traits)
        self.faceID_surprised = id_data.random_faceID_surprised(is_male, self.faceID)
        self.faceID_happy = id_data.random_faceID_happy(is_male, self.faceID)
        self.faceID_unhappy = id_data.random_faceID_unhappy(is_male, self.faceID)
        self.faceID_contemplative, self.eyesID_contemplative = id_data.random_faceID_and_eyesID_contemplative(is_male, self.faceID, self.eyesID)
    
    def load_hairBack(self):   
        hairBack = RandomColorSurface()
        #load hair_back       
        not_yet_found = True
        while not_yet_found:
            not_yet_found = False
            file_name = str(self.hairBackID) + '.png'
            
            try:
                if can_load_image(file_name, 3, self.gender, 'hair_back'):
                    hairBack.surf = load_image(file_name, 3, self.gender, 'hair_back')
                else:
                    self.hairBackID += 1
                    if self.hairBackID > 299:
                        self.hairBackID = 100                    
                    not_yet_found = True
            except pygame.error:
                #print('Cannot load clothes image:', file_name)
                pass
                #self.hairBackID += 1
                #if self.hairBackID > 299:
                #    self.hairBackID = 100                    
                #not_yet_found = True
                
        hairBack.colorize(self.hairColor)
        return hairBack
                
     
    def load_hairFront(self):
        hairFront = RandomColorSurface()   
        # load hair_front
        not_yet_found = True
        while not_yet_found:
            not_yet_found = False
            file_name = str(self.hairFrontID) + '.png'
            
            try:
                if can_load_image(file_name, 3, self.gender, 'hair_front'):
                    hairFront.surf = load_image(file_name, 3, self.gender, 'hair_front')
                else:
                    self.hairFrontID += 1
                    if self.hairFrontID > 299:
                        self.hairFrontID = 100                    
                    not_yet_found = True
            except pygame.error:
                #print('Cannot load clothes image:', file_name)
                pass
                #self.hairFrontID += 1
                #if self.hairFrontID > 299:
                #    self.hairFrontID = 100                    
                #not_yet_found = True
                
        hairFront.colorize(self.hairColor)
        return hairFront
        
    
    def load_eyesBack(self, expression = 0):
        #log('loading eyes back with expression=' + str(expression),3)
        eyesBack = RandomColorSurface()   
        # load eyes
        not_yet_found = True
        while not_yet_found:
            not_yet_found = False
            
            # use eyesOpenID for surprised and happy and sad expressions, only for special (closed) eyes
            if (expression == 1 or expression == 2 or expression == 3) and \
             self.eyesID != self.eyesOpenID:
                eyes_id = self.eyesOpenID
            elif expression == 4:
                eyes_id = self.eyesID_contemplative
            else:
                eyes_id = self.eyesID
            #log('eyes_id=' + str(eyes_id))    
            file_name = str(eyes_id) + '.png'
            
            try:
                if can_load_image(file_name, 3, self.gender, 'eyes_back'):
                    eyesBack.surf = load_image(file_name, 3, self.gender, 'eyes_back')
                else:
                    self.eyesID += 1
                    if self.eyesID > 299:
                        self.eyesID = 100  
                    not_yet_found = True
            except pygame.error:
                #print('Cannot load clothes image:', file_name)
                pass
                #self.eyesID += 1
                #if self.eyesID > 299:
                #    self.eyesID = 100  
                #not_yet_found = True
        
        return eyesBack
        
        
    def load_eyesFront(self, expression = 0):
        #log('loading eyes front with expression=' + str(expression),3)
        eyesFront = RandomColorSurface()   
        # load front eyes
        # use eyesOpenID for surprised and happy and sad expressions, only for special (closed) eyes
        if (expression == 1 or expression == 2 or expression == 3) and \
         self.eyesID != self.eyesOpenID:
            eyes_id = self.eyesOpenID
        elif expression == 4:
            eyes_id = self.eyesID_contemplative  
        else:
            eyes_id = self.eyesID
                
        file_name = str(eyes_id) + '.png'            
        try:
            # try to load the same ID. if it doesn't exist don't load anything
            if can_load_image(file_name, 3, self.gender, 'eyes_front'):
                eyesFront.surf = load_image(file_name, 3, self.gender, 'eyes_front')
            else:
                eyesFront.surf = pygame.Surface((1,1), pygame.SRCALPHA, 32)
        except pygame.error:
            pass
            # no front eyes matching back eyes so just make an empty surface
            #eyesFront.surf = pygame.Surface((1,1), pygame.SRCALPHA, 32)
        
        #print('eyesFrontID = ' + str(self.eyesFrontID))
        eyesFront.colorize(self.eyesColor, True)
        return eyesFront
     
    
    def load_face(self, expression = 0): #surprised = False):
        # load face
        #log('loading face with expression=' + str(expression),3)
        not_yet_found = True
        while not_yet_found:
            not_yet_found = False
   
            #idd = self.faceID_surprised if surprised else self.faceID  # load face
            if expression == 0: # normal
                idd = self.faceID 
            elif expression == 1: # surprised
                idd = self.faceID_surprised
            elif expression == 2: # happy
                idd = self.faceID_happy
            elif expression == 3: # unhappy
                idd = self.faceID_unhappy
            elif expression == 4: # contemplative
                idd = self.faceID_contemplative
                
            file_name = str(idd) + '.png'
            
            try:
                if can_load_image(file_name, 3, self.gender, 'face'):
                    face = load_image(file_name, 3, self.gender, 'face')
                else:
                    self.faceID += 1
                    if self.faceID > 699:
                        self.faceID = 100  
                    not_yet_found = True
            except pygame.error:
                pass
                #self.faceID += 1
                #if self.faceID > 699:
                #    self.faceID = 100  
                #not_yet_found = True
    
        # some mouths don't look good on dark skin unless we change them
        if self.skinColor == 7:
            face.fill((100, 100, 100, 100), special_flags=pygame.BLEND_SUB) 
        #elif self.skinColor == 8:
        #    face.fill((50, 50, 50, 100), special_flags=pygame.BLEND_ADD) 
        
        return face
        
  
        #clothes = load_image(str(self.clothes_id) + pose + '.png', 3, gender, 'clothes')
        
    
    def load_clothes(self, force_clothes = -1, xray_on = False):
        # load clothes
        #clothes = RandomColorSurface()   
        not_yet_found = True
        
        while not_yet_found:
            not_yet_found = False
            
            if xray_on:
                file_name = '50.png'
            elif force_clothes == -1:
                file_name = str(self.clothesID) + self.pose + '.png'
             
                self.last_worn_clothesID = self.clothesID
            else:
                file_name = str(force_clothes) + self.pose + '.png'
      
                self.last_worn_clothesID = force_clothes
    
            
            try:
                if can_load_image(file_name, 3, self.gender, 'clothes'):
                    clothes = load_image(file_name, 3, self.gender, 'clothes')
                else:
                    self.clothesID += 1
                    if self.clothesID > 299:
                        self.clothesID = 100                    
                    not_yet_found = True
            except pygame.error:
                pass
                #self.clothesID += 1
                #if self.clothesID > 299:
                #    self.clothesID = 100                    
                #not_yet_found = True
           
        
           
        # transform clothes color 
             
        if self.clothesColorIndex == 1:
            clothes.fill((190, 100, 0, 100), special_flags=pygame.BLEND_MULT)  # dark yellow/brown/green
        elif self.clothesColorIndex == 2:
            clothes.fill((100, 30, 0, 100), special_flags=pygame.BLEND_ADD) # slightly reddish
        elif self.clothesColorIndex == 3:
            clothes.fill((160, 50, 90, 100), special_flags=pygame.BLEND_MULT) # dark purple
            clothes.fill((200, 200, 200, 100), special_flags=pygame.BLEND_MULT)  
        elif self.clothesColorIndex == 4:
            clothes.fill((160, 100, 30, 100), special_flags=pygame.BLEND_SUB) # dark blue
        elif self.clothesColorIndex == 5:
            clothes.fill((20, 160, 20, 100), special_flags=pygame.BLEND_SUB) # deep pink/purple
        elif self.clothesColorIndex == 6:
            clothes.fill((0, 150, 180, 100), special_flags=pygame.BLEND_SUB) # red  
        elif self.clothesColorIndex == 7:
            clothes.fill((80, 20, 150, 100), special_flags=pygame.BLEND_SUB) # green
        elif self.clothesColorIndex == 8:           
            clothes.fill((10, 80, 160, 100), special_flags=pygame.BLEND_SUB) # orange/brown/green
        elif self.clothesColorIndex == 9:
            clothes.fill((160, 0, 50, 100), special_flags=pygame.BLEND_ADD) # light pink
        elif self.clothesColorIndex == 10:
            clothes.fill((10, 20, 100, 100), special_flags=pygame.BLEND_ADD) # light blue
        elif self.clothesColorIndex == 11:
            clothes.fill((30, 80, 20, 100), special_flags=pygame.BLEND_ADD) # light green/cyan
        elif self.clothesColorIndex == 12:
            clothes.fill((100, 100, 160, 100), special_flags=pygame.BLEND_SUB) # black/green 
        elif self.clothesColorIndex == 13:
            clothes.fill((30, 160, 160, 100), special_flags=pygame.BLEND_SUB) # black/red
        elif self.clothesColorIndex == 14:
            clothes.fill((40, 100, 160, 100), special_flags=pygame.BLEND_SUB) # black/tan
        elif self.clothesColorIndex == 15:            
            clothes.fill((70, 60, 50, 100), special_flags=pygame.BLEND_ADD) # slightly lighter 
        elif self.clothesColorIndex == 16:
            clothes.fill((0, 120, 190, 100), special_flags=pygame.BLEND_SUB) # red/brown/orange    
        elif self.clothesColorIndex == 17:
            clothes.fill((0, 200, 90, 100), special_flags=pygame.BLEND_SUB) # bright red/pink/purple
        elif self.clothesColorIndex == 18:
            clothes.fill((70, 130, 200, 100), special_flags=pygame.BLEND_SUB) # black/brown                
        elif self.clothesColorIndex == 19:
            clothes.fill((120, 40, 0, 100), special_flags=pygame.BLEND_ADD) # lighter
        elif self.clothesColorIndex == 20:           
            clothes.fill((80, 20, 0, 100), special_flags=pygame.BLEND_ADD) # grey
            clothes.fill((70, 70, 70, 100), special_flags=pygame.BLEND_MULT)
        elif self.clothesColorIndex == 21:           
            clothes.fill((30, 0, 80, 100), special_flags=pygame.BLEND_ADD) # brown grey
            clothes.fill((70, 60, 60, 100), special_flags=pygame.BLEND_MULT)
        elif self.clothesColorIndex == 22:
            clothes.fill((40, 30, 20, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((50, 50, 50, 100), special_flags=pygame.BLEND_MULT) # dark grey
        elif self.clothesColorIndex == 23:            
            clothes.fill((20, 10, 20, 100), special_flags=pygame.BLEND_MULT) # almost black
        elif self.clothesColorIndex == 24:
            clothes.fill((0, 150, 180, 100), special_flags=pygame.BLEND_SUB)  
            clothes.fill((120, 120, 120, 100), special_flags=pygame.BLEND_MULT) # dark red/brown
        elif self.clothesColorIndex == 25:
            clothes.fill((0, 50, 100, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((180, 80, 0, 100), special_flags=pygame.BLEND_ADD) # light yellow/orange 
        elif self.clothesColorIndex == 26:
            clothes.fill((0, 120, 30, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((60, 30, 100, 100), special_flags=pygame.BLEND_ADD) # light purple/pink
        elif self.clothesColorIndex == 27:
            clothes.fill((100, 50, 50, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((50, 100, 100, 100), special_flags=pygame.BLEND_ADD) # cyan
        elif self.clothesColorIndex == 28:
            clothes.fill((30, 150, 150, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((20, 0, 0, 100), special_flags=pygame.BLEND_ADD) # light red
        elif self.clothesColorIndex == 29:
            clothes.fill((80, 120, 150, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((10, 20, 10, 100), special_flags=pygame.BLEND_ADD) # not sure but looks good   
        elif self.clothesColorIndex == 30:
            clothes.fill((60, 100, 130, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((30, 0, 30, 100), special_flags=pygame.BLEND_ADD) # not sure but looks good 
        elif self.clothesColorIndex == 31:
            clothes.fill((150, 150, 150, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((30, 30, 30, 100), special_flags=pygame.BLEND_ADD) # dark blue grey
        elif self.clothesColorIndex == 32:
            clothes.fill((100, 100, 150, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((30, 30, 0, 100), special_flags=pygame.BLEND_ADD) # interesting shade of green
        elif self.clothesColorIndex == 33:
            clothes.fill((150, 200, 200, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((10, 10, 10, 100), special_flags=pygame.BLEND_ADD) # blackish red
        elif self.clothesColorIndex == 34:
            clothes.fill((170, 190, 180, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((10, 0, 10, 100), special_flags=pygame.BLEND_ADD) # blackish blue
        elif self.clothesColorIndex == 35:
            clothes.fill((40, 30, 20, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((150, 100, 110, 100), special_flags=pygame.BLEND_ADD) # whitish blue
        elif self.clothesColorIndex == 36:
            clothes.fill((0, 20, 40, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((100, 50, 10, 100), special_flags=pygame.BLEND_MULT) # dark brown
        elif self.clothesColorIndex == 37:
            clothes.fill((0, 40, 60, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((220, 150, 100, 100), special_flags=pygame.BLEND_MULT) 
            clothes.fill((160, 50, 10, 100), special_flags=pygame.BLEND_ADD) # super orange
        elif self.clothesColorIndex == 38:
            clothes.fill((0, 50, 100, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((180, 80, 0, 100), special_flags=pygame.BLEND_ADD)   
            clothes.fill((140, 80, 10, 100), special_flags=pygame.BLEND_ADD) # super yellow
        elif self.clothesColorIndex == 39:
            clothes.fill((20, 30, 50, 100), special_flags=pygame.BLEND_SUB) 
            clothes.fill((180, 110, 100, 100), special_flags=pygame.BLEND_ADD) # whitish red
        
        #log('clothesColorIndex=' + str(self.clothesColorIndex),6)
        
        return clothes
    
    
    def set_clothesColor(self, is_male):            
        looking_for_good_color = True
        #self.clothesID = 174
        while(looking_for_good_color):
            clothes_color = 20
            if clothes_color == 1:
                if (is_male and (False)) or (not is_male and
                    (self.clothesID == 120 or self.clothesID == 180 or self.clothesID == 240 or self.clothesID == 245)):
                    continue
            elif clothes_color == 2:
                if (is_male and (self.clothesID == 130 or self.clothesID == 131 or self.clothesID == 135)) or (not is_male and
                    (self.clothesID == 120 or self.clothesID == 125 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 170 or self.clothesID == 171 or self.clothesID == 175 or self.clothesID == 176 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 230 or self.clothesID == 255)):
                    continue
            elif clothes_color == 3:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 220)):
                    continue
            elif clothes_color == 4:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 155)):
                    continue
            elif clothes_color == 5:
                pass
            elif clothes_color == 6:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 206)):
                    continue
            elif clothes_color == 7:
                pass
            elif clothes_color == 8:           
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 8 or self.clothesID == 120)):
                    continue
            elif clothes_color == 9:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 120 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 175 or self.clothesID == 176 or self.clothesID == 180 or self.clothesID == 181)):
                    continue
            elif clothes_color == 10:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 171 or self.clothesID == 250)):
                    continue
            elif clothes_color == 11:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 120 or self.clothesID == 121 or self.clothesID == 122 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 172 or self.clothesID == 173 or self.clothesID == 290)):
                    continue
            elif clothes_color == 12:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101)) or (not is_male and 
                    (self.clothesID == 110 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 255)):
                    continue
            elif clothes_color == 13:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101)) or (not is_male and
                    (self.clothesID == 155 or self.clothesID == 156)):
                    continue
            elif clothes_color == 14:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101)) or (not is_male and 
                    (self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 180 or self.clothesID == 255)):
                    continue
            elif clothes_color == 15:            
                if (is_male and (self.clothesID == 130 or self.clothesID == 131)) or (not is_male and 
                    (self.clothesID == 120 or self.clothesID == 121 or self.clothesID == 122 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 170 or self.clothesID == 171 or self.clothesID == 173 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 230)):
                    continue
            elif clothes_color == 16:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 120)):
                    continue
            elif clothes_color == 17:
                pass
            elif clothes_color == 18:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101)) or (not is_male and 
                    (self.clothesID == 110 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 175 or self.clothesID == 200 or self.clothesID == 201 or self.clothesID == 255)):
                    continue
            elif clothes_color == 19:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or (self.clothesID >= 114 and self.clothesID <= 117) or self.clothesID == 130 or self.clothesID == 131)) or (not is_male and 
                    (self.clothesID == 101 or self.clothesID == 120 or self.clothesID == 121 or self.clothesID == 122 or self.clothesID == 142 or self.clothesID == 155 or self.clothesID == 156 or (self.clothesID >= 170 and self.clothesID <= 173) or self.clothesID == 175 or self.clothesID == 176 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 190 or self.clothesID == 191 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 225 or self.clothesID == 230 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 20:           
                if (is_male and (self.clothesID == 110 or self.clothesID == 111 or self.clothesID == 113 or self.clothesID == 114)) or (not is_male and 
                    (self.clothesID == 120 or self.clothesID == 121 or self.clothesID == 122 or self.clothesID == 130 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 206 or self.clothesID == 230 or self.clothesID == 225 or self.clothesID == 245 or self.clothesID == 255 or self.clothesID == 290)):
                    continue
            elif clothes_color == 21:           
                if (is_male and ((self.clothesID >= 110 and self.clothesID == 113) or self.clothesID == 120)) or (not is_male and 
                    (self.clothesID == 110 or self.clothesID == 112 or self.clothesID == 120 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 165 or self.clothesID == 172 or self.clothesID == 185 or self.clothesID == 206 or self.clothesID == 225 or self.clothesID == 240 or self.clothesID == 255 or self.clothesID == 260 or self.clothesID == 290)):
                    continue
            elif clothes_color == 22:
                if (is_male and (self.clothesID == 100 or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 130 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 175 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 225 or self.clothesID == 230 or self.clothesID == 290)):
                    continue
            elif clothes_color == 23:            
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or self.clothesID == 105 or self.clothesID == 106 or self.clothesID == 107 or self.clothesID == 108 or (self.clothesID >= 110 and self.clothesID <= 117) or self.clothesID == 120 or self.clothesID == 125 or self.clothesID == 126 or self.clothesID == 127 or self.clothesID == 128 or self.clothesID == 130 or self.clothesID == 131 or self.clothesID == 135 or self.clothesID == 137 or self.clothesID == 140)) or (not is_male and 
                    (self.clothesID == 100 or self.clothesID == 101 or self.clothesID == 105 or self.clothesID == 106 or self.clothesID == 107 or self.clothesID == 110 or self.clothesID == 112 or self.clothesID == 113 or self.clothesID == 115 or self.clothesID == 116 or self.clothesID == 120 or self.clothesID == 121 or self.clothesID == 122  or self.clothesID == 125 or self.clothesID == 130 or self.clothesID == 131 or self.clothesID == 135 or self.clothesID == 142 or self.clothesID == 150 or self.clothesID == 151 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 165 or self.clothesID == 166 or self.clothesID == 167 or self.clothesID == 168 or self.clothesID == 170 or self.clothesID == 171 or self.clothesID == 172 or self.clothesID == 173 or self.clothesID == 175 or self.clothesID == 176 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 200 or self.clothesID == 201 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 220 or self.clothesID == 225 or self.clothesID == 230 or self.clothesID == 235 or self.clothesID == 245 or self.clothesID == 250 or self.clothesID == 255 or self.clothesID == 260)):
                    continue
            elif clothes_color == 24:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101)) or (not is_male and 
                    (self.clothesID == 106)):
                    continue
            elif clothes_color == 25:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 120 or self.clothesID == 135 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 171 or self.clothesID == 173 or self.clothesID == 174 or self.clothesID == 175 or self.clothesID == 176 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 190 or self.clothesID == 191 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 225 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 26:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 135 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 230)):
                    continue
            elif clothes_color == 27:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 175 or self.clothesID == 176 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182)):
                    continue
            elif clothes_color == 28:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101)) or (not is_male and 
                    (self.clothesID == 206)):
                    continue
            elif clothes_color == 29:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or (self.clothesID >= 114 and self.clothesID <= 117) or self.clothesID == 120 or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 155 or self.clothesID ==156 or self.clothesID == 160 or self.clothesID == 165 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 200 or self.clothesID == 225 or self.clothesID == 230)):
                    continue
            elif clothes_color == 30:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or (self.clothesID >= 114 and self.clothesID <= 117) or self.clothesID == 120 or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 230 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 31:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or (self.clothesID >= 114 and self.clothesID <= 117) or (self.clothesID >= 125 and self.clothesID <= 128) or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 100 or self.clothesID == 101 or self.clothesID == 105 or self.clothesID == 106 or self.clothesID == 110 or self.clothesID == 112 or self.clothesID == 113 or self.clothesID == 135 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 165 or self.clothesID == 166 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 200 or self.clothesID == 201 or self.clothesID == 220 or self.clothesID == 230 or self.clothesID == 235 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 32:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or (self.clothesID >= 114 and self.clothesID <= 117) or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 110 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 165 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 191 or self.clothesID == 200 or self.clothesID == 201 or self.clothesID == 220 or self.clothesID == 230 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 33:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or (self.clothesID >= 105 and self.clothesID <= 108) or self.clothesID == 114 or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 100 or self.clothesID == 101 or self.clothesID == 105 or self.clothesID == 106 or self.clothesID == 107 or self.clothesID == 110 or self.clothesID == 112 or self.clothesID == 113 or self.clothesID == 135 or self.clothesID == 136 or self.clothesID == 150 or self.clothesID == 151 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 165 or self.clothesID == 167 or self.clothesID == 168 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 200 or self.clothesID == 201 or self.clothesID == 205 or self.clothesID == 230 or self.clothesID == 235 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 34:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or (self.clothesID >= 105 and self.clothesID <= 108) or self.clothesID == 120)) or (not is_male and 
                    (self.clothesID == 101 or self.clothesID == 105 or self.clothesID == 106 or self.clothesID == 110 or self.clothesID == 112 or self.clothesID == 113 or self.clothesID == 133 or self.clothesID == 135 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 165 or self.clothesID == 167 or self.clothesID == 168 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 190 or self.clothesID == 191 or self.clothesID == 200 or self.clothesID == 201 or self.clothesID == 205 or self.clothesID == 230 or self.clothesID == 235 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 35:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or self.clothesID == 110 or self.clothesID == 111 or self.clothesID == 112 or self.clothesID == 113 or self.clothesID == 114 or self.clothesID == 115 or self.clothesID == 116 or self.clothesID == 117 or self.clothesID == 120 or self.clothesID == 130 or self.clothesID == 131 or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 106 or self.clothesID == 115 or self.clothesID == 116 or self.clothesID == 120 or self.clothesID == 121 or self.clothesID == 122 or self.clothesID == 125 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 171 or self.clothesID == 170 or self.clothesID == 174 or self.clothesID == 175 or self.clothesID == 176 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 190 or self.clothesID == 191 or self.clothesID == 200 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 220 or self.clothesID == 225 or self.clothesID == 230 or self.clothesID == 255 or self.clothesID == 290)):
                    continue
            elif clothes_color == 36:
                if (is_male and (False)) or (not is_male and 
                    (self.clothesID == 115 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 230)):
                    continue
            elif clothes_color == 37:
                if (is_male and (self.clothesID == 100 or self.clothesID == 101 or (self.clothesID >= 114 and self.clothesID <= 117) or self.clothesID == 120 or self.clothesID == 130 or self.clothesID == 131)) or (not is_male and 
                    (self.clothesID == 100 or self.clothesID == 120 or self.clothesID == 135 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 175 or self.clothesID == 176 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 190 or self.clothesID == 191 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 230 or self.clothesID == 245 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 38:
                if (is_male and (self.clothesID == 100 or (self.clothesID >= 110 and self.clothesID <= 117) or self.clothesID == 120 or self.clothesID == 125 or self.clothesID == 126 or self.clothesID == 127 or self.clothesID == 130 or self.clothesID == 131 or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 100 or self.clothesID == 120 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 170 or self.clothesID == 171 or self.clothesID == 175 or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 220 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
            elif clothes_color == 39:
                if (is_male and (self.clothesID == 100 or (self.clothesID >= 110 and self.clothesID <= 117) or self.clothesID == 120 or self.clothesID == 125 or self.clothesID == 126 or self.clothesID == 130 or self.clothesID == 131 or self.clothesID == 135)) or (not is_male and 
                    (self.clothesID == 100 or self.clothesID == 113 or self.clothesID == 115 or self.clothesID == 116 or self.clothesID == 120 or self.clothesID == 121 or self.clothesID == 122 or self.clothesID == 125 or self.clothesID == 126 or self.clothesID == 136 or self.clothesID == 137 or self.clothesID == 140 or self.clothesID == 142 or self.clothesID == 155 or self.clothesID == 156 or self.clothesID == 160 or self.clothesID == 167 or self.clothesID == 168 or (self.clothesID >= 170 and self.clothesID <= 176) or self.clothesID == 180 or self.clothesID == 181 or self.clothesID == 182 or self.clothesID == 190 or self.clothesID == 191 or self.clothesID == 205 or self.clothesID == 206 or self.clothesID == 211 or self.clothesID == 220 or self.clothesID == 225 or self.clothesID == 230 or self.clothesID == 245 or self.clothesID == 250 or self.clothesID == 255)):
                    continue
             
            looking_for_good_color = False
            #found_good_color = CheckColor(clothes_color, self.clothesID, self.isMale)
            
        self.clothesColorIndex = clothes_color  
        #log('clothes color = ' + str(clothes_color) + ' for clothesID = ' + str(self.clothesID),6) 
    
    
   
    
   
    
          
    def load_body(self):      
        # body must be loaded after clothes (but blitted before) because clothes_id may be incremented for testing
        # there is no body ID because it is the same as the clothesID
        try:
            bodyID = 100
                
            file_name = str(bodyID) + self.pose + '.png'
            #print('loading ' + file_name + ' body')
            if can_load_image(file_name, 3, self.gender, 'body'):
                body = load_image(file_name, 3, self.gender, 'body')
            else:
                # if the file doesn't exist just load the default body
                file_name = '105' + self.pose + '.png' if self.gender == 'female' else '100.png'
                body = load_image('105' + self.pose + '.png', 3, self.gender, 'body')  
                
        except pygame.error:
            # if the file doesn't exist just load the default body
            pass
            #file_name = '105' + self.pose + '.png' if self.gender == 'female' else '100.png'
            #print('loading ' + file_name + ' body instead')
            #body = load_image('105' + self.pose + '.png', 3, self.gender, 'body')  
        
        # 0=pale, 1=pinkish, 2=normal, 3=slight tan, 4=sunburn, 5=tanned, 6=dark, 7=very dark   
        if self.skinColor == 0: 
            body.fill((40, 30, 30, 100), special_flags=pygame.BLEND_ADD)  # pale skin
        elif self.skinColor == 1: 
            body.fill((20, 0, 20, 100), special_flags=pygame.BLEND_ADD)  # pinkish skin
        elif self.skinColor == 3: 
            body.fill((250, 240, 215, 100), special_flags=pygame.BLEND_MULT)  # slightly tanned skin
        elif self.skinColor == 4: 
            body.fill((250, 210, 190, 100), special_flags=pygame.BLEND_MULT)  # sunburned skin
        elif self.skinColor == 5: 
            body.fill((230, 200, 160, 100), special_flags=pygame.BLEND_MULT)  # tanned skin
        elif self.skinColor == 6: 
            body.fill((200, 180, 140, 100), special_flags=pygame.BLEND_MULT)  # dark skin
        elif self.skinColor == 7: 
            body.fill((100, 90, 80, 100), special_flags=pygame.BLEND_MULT)  # very dark skin
        elif self.skinColor == 8: 
            body.fill((40, 30, 40, 100), special_flags=pygame.BLEND_MULT)  # black skin
        
        #print('loaded clothes ' + file_name)
        return body


    # face_only is used only to determine whether to do the log line
    def load_head(self, is_male, player_relationship_title = 0, face_only = False):
        # load head
        headID  = self.headID
        if is_male and player_relationship_title == 13:
            headID = 111
        elif not is_male:
            if player_relationship_title == 5:
                headID = 110
            elif player_relationship_title == 13:
                headID = 111
        
        head = load_image(str(headID) + '.png', 3, self.gender, 'head')
        
        if self.skinColor == 0: 
            head.fill((40, 30, 30, 100), special_flags=pygame.BLEND_ADD)  # pale skin
        elif self.skinColor == 1: 
            head.fill((20, 0, 20, 100), special_flags=pygame.BLEND_ADD)  # pinkish skin
        elif self.skinColor == 3: 
            head.fill((250, 240, 215, 100), special_flags=pygame.BLEND_MULT)  # slightly tanned skin
        elif self.skinColor == 4: 
            head.fill((250, 210, 190, 100), special_flags=pygame.BLEND_MULT)  # sunburned skin
        elif self.skinColor == 5: 
            head.fill((230, 200, 160, 100), special_flags=pygame.BLEND_MULT)  # tanned skin
        elif self.skinColor == 6: 
            head.fill((200, 180, 140, 100), special_flags=pygame.BLEND_MULT)  # dark skin
        elif self.skinColor == 7: 
            head.fill((100, 90, 80, 100), special_flags=pygame.BLEND_MULT)  # very dark skin
        elif self.skinColor == 8: 
            head.fill((40, 30, 40, 100), special_flags=pygame.BLEND_MULT)  # black skin
        
        
        
            
        
        return head
             
        
        # hair_back
        #hair_front = load_image(str(hair_front_id) + '.png', 3, self.gender, 'hair_front')
        
        
        #body = pygame.transform.scale(body, (450, 550))
        #hair_back = pygame.transform.scale(hair_back, (450, 550))
        
        #hair_front = pygame.transform.scale(hair_front, (450, 550))
        #clothes = pygame.transform.scale(clothes, (450, 550))
        
           
   

        #hair_color_adjust = (250, 150, 70, 100) # brown
         
        
        #hair_front = self.hairColor.colorize(hair_front)
        #hair_back = self.hairColor.colorize(hair_back)
        
        
        
        
        
        #clothes.colorize(self.clothesColor)
        
        #r3 = random.randint(0, 5) + r
        #g3 = random.randint(0, 100) + g
        #b3 = random.randint(0, 150) + b
        #hair_color_adjust = (r3, g3, b3, 100)
        
        #hair_front.fill(hair_color_adjust, special_flags=3)
        #hair_back.fill(hair_color_adjust, special_flags=3)
        
        #print('hair color = ' + str(hair_color_adjust) + ' with blend type MULT')
        
       
        
        #hair_color_blend_type = pygame.BLEND_SUB  #pygame.BLEND_MULT

        
        #hair_back.fill((60, 60, 60, 100), special_flags=pygame.BLEND_MULT) # black hair
        #hair_front.fill((60, 60, 60, 100), special_flags=pygame.BLEND_MULT) # black hair
        #hair_front.fill((60, 0, 60, 100), special_flags=pygame.BLEND_ADD) # colored hair
        #hair_front.fill((110, 110, 110, 100), special_flags=pygame.BLEND_SUB) # dark colored hair
        #hair_front.fill((220, 130, 0, 100), special_flags=pygame.BLEND_ADD) # blonde hair
        
        #hair_front.fill(hair_color_adjust, special_flags=hair_color_blend_type) # brown hair
        #hair_back.fill(hair_color_adjust, special_flags=hair_color_blend_type) # brown hair
        
        #hair_front.fill((30, 30, 30, 100), special_flags=pygame.BLEND_SUB) # dark colored hair
        #hair_back.fill((120, 120, 120, 100), special_flags=pygame.BLEND_ADD)
        
         # + str(hair_color_blend_type))
        # BLEND_ADD is 1, BLEND_SUB is 2, BLEND_MULT is 3, 
        
        #clothes.fill((100, 30, 0, 100), special_flags=pygame.BLEND_ADD) # slightly reddish clothes
        #clothes.fill((200, 200, 200, 100), special_flags=pygame.BLEND_MULT)  # dark clothes
        #clothes.fill((180, 120, 50, 100), special_flags=pygame.BLEND_MULT)  #  brown/green clothes
        #clothes.fill((160, 50, 90, 100), special_flags=pygame.BLEND_MULT) # purple clothes (combine with above for dark red)
        
        
        #clothes.fill((190, 120, 30, 100), special_flags=pygame.BLEND_ADD) # yellow clothes (too bright!)
        
        
        
            #if not found_good_color:
            #    print('REJECTING this clothing color combination')
           
           

    def get_tachie(self, face_only = False, is_male = False, player_relationship_title = 0, expression = 0, force_clothes = -1, xray_on = False):
        
        # load the images
        #expression = 4
        hairBack = self.load_hairBack()
        hairFront = self.load_hairFront()
        eyesBack = self.load_eyesBack(expression)
        eyesFront = self.load_eyesFront(expression)
        face = self.load_face(expression)
        head = self.load_head(is_male, player_relationship_title, face_only)
        clothes = self.load_clothes(force_clothes, xray_on)
        body = self.load_body() 
        
 
        source_rect = body.get_rect()
        source_rect = pygame.Rect(source_rect.left, source_rect.top, source_rect.width, source_rect.height - self.heightAdjust)
        
        
        tachie_surface = pygame.Surface((source_rect.width,source_rect.height), pygame.SRCALPHA, 32)
        
        
        head_horizontal_offset = 0
        head_vertical_offset = 0

        # because the base female head was too large, make it smaller and adjust the position for head and head parts
        if self.gender == 'female':
            hairBack.surf = pygame.transform.scale(hairBack.surf, (464, 564))
            head = pygame.transform.scale(head, (464, 564))
            hairFront.surf = pygame.transform.scale(hairFront.surf, (464, 564))
            eyesBack.surf = pygame.transform.scale(eyesBack.surf, (464, 564))
            eyesFront.surf = pygame.transform.scale(eyesFront.surf, (464, 564))
            face = pygame.transform.scale(face, (464, 564))
            # don't do this for scarf, but do it for hair beads, glasses, hair extensions etc
            head_horizontal_offset = 23
            head_vertical_offset = 17
        
        
        # surfaces must be blitted in this order
        tachie_surface.blit(hairBack.surf, (head_horizontal_offset, head_horizontal_offset), source_rect)
        
        tachie_surface.blit(body, (0,0), source_rect)

        
        tachie_surface.blit(clothes, (0,0), source_rect)
        
        tachie_surface.blit(head, (head_horizontal_offset, head_vertical_offset), source_rect)
        
        tachie_surface.blit(eyesBack.surf, (head_horizontal_offset, head_vertical_offset), source_rect)
        tachie_surface.blit(eyesFront.surf, (head_horizontal_offset, head_vertical_offset), source_rect)
        tachie_surface.blit(face, (head_horizontal_offset, head_vertical_offset), source_rect)
        
        
            
        tachie_surface.blit(hairFront.surf, (head_horizontal_offset, head_vertical_offset), source_rect)
        
        if self.horizontal_flip:
            tachie_surface = pygame.transform.flip(tachie_surface, True, False)
        
        return tachie_surface
       
       

class RandomColorSurface():
    def __init__(self):
        #super().__init__()
        self.surf = None
        
    # make colored version of this surface using ColorData object
    # eyesFront should be darker, as well as scarf accessory
    # one hair accessory should be a little darker
    def colorize(self, colordata, darker = False, littledarker = False):
       
        add_r, add_g, add_b = colordata.add_r, colordata.add_g, colordata.add_b
        sub_r, sub_g, sub_b = colordata.sub_r, colordata.sub_g, colordata.sub_b
        
        if True:           
            color_adjust = (add_r, add_g, add_b, 100)       
            self.surf.fill(color_adjust, special_flags = pygame.BLEND_ADD)
            #hair_back.fill(hair_color_adjust, special_flags = pygame.BLEND_ADD)    
            #print('color = ' + str(color_adjust) + ' with blend type ADD')
        

            color_adjust = (sub_r, sub_g, sub_b, 100)
            self.surf.fill(color_adjust, special_flags = pygame.BLEND_SUB)
            #hair_back.fill(hair_color_adjust, special_flags = pygame.BLEND_SUB)
            #print('color = ' + str(color_adjust) + ' with blend type SUB')
            
      
       
class ColorData():
    def __init__(self): 
    
        self.add_before_subtract = True  # adding before subtracting results in lighter colors
        self.add_r, self.add_g, self.add_b = 0, 0, 0  # rgb values for adding
        self.sub_r, self.sub_g, self.sub_b = 0, 0, 0  # rgb values for subtracting
        
        self.assign_color()

    
    def assign_color(self):
        if True:
            self.add_before_subtract = True
            # images start with a blue base, and we want red to have a bias anyway, so values are not even
            self.add_r = 150   
            self.add_g = 100
            self.add_b = 100
            
            self.sub_r = 25
            self.sub_g = 75
            self.sub_b = 75
            
        
            
            