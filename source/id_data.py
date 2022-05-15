
import random

# temporary object to hold ID data for tachie set methods
# is deleted at the end of populate

class ID_Data():
    def __init__(self):
        
        #self.female_head = [100,101,102,103]
        
        self.male_hairBack = [100,101,105,106,110,115,116,120,125,130,135,140]
        self.female_hairBack = [100,105,110,114,115,120,121,125,126,130,135, \
         140,141,145,146,150,151,155,160,165,170,171,172,175,180,185,186, \
         190,191,195,196,200,205,206,207,210,211,212]
         
        self.male_hairFront = [100,105,106,110,115,120,125,130,135,140]
        self.female_hairFront = [100,105,110,115,120,125,130,135]
        
        self.male_eyes = [100,105,110,125,130,135,150,155,160]
        self.male_eyesAlternative = [180,182,192]  # 185 funny sad eyes
        self.male_eyesContemplative = [181,183,193]
        self.female_eyes = [100,105,110,125,130,135,170,175,180]
        self.female_eyesAlternative = [120,145,160]
        self.female_eyesContemplative = [115,140,185]
           
        self.male_face = [100,106,116,121,140,146,156,166,190,196]
        #self.male_faceSpecial = []
        self.male_face_surprised_even = [150,160,170,176,226]
        self.male_face_surprised_odd = [135]
        self.male_face_happy_even = [110,200,236]
        self.male_face_happy_odd = [131]
        self.male_face_unhappy_even = [180,186,206,220,230]
        self.male_face_unhappy_odd = [125]
        self.male_face_contemplative_even = [210,216]
        self.male_face_contemplative_odd = [125] # same as for unhappy_odd
        
        
        self.female_face = [100,101,105,106,135,136,140,141, \
         145,146,170,171,175,176, \
         235,236,245,246,250,251,255,256,260,261,265,266, \
         275,276,285,286,290,291,295,296, \
         320,321]
        #self.female_faceSpecial = [130,131] 
        self.female_face_surprised_even = [156,220,300,306,316]  # 120,121 is x-shaped mouth
        self.female_face_surprised_odd = [155,221,301,305,315] 
        self.female_face_happy_even = [110,116,126,240] # 130, 131 is puppy mouth
        self.female_face_happy_odd = [111,115,125,241]
        self.female_face_unhappy_even = [150,160,166,180,186,190,196,200,206,210,216,270]
        self.female_face_unhappy_odd = [151,161,165,181,185,191,195,201,205,211,215,271]
        self.female_face_contemplative_even = [226,230,280,326,310]
        self.female_face_contemplative_odd = [225,231,281,325,311]
        
         
        self.male_clothes = [100,101,105,106,107,108,110,111,112,113,114, \
         115,116,117,120,125,126,127,128,130,131,135,136,137,140,145,146,147]
        self.female_clothes = [100,101,102,105,106,107,110,112,113,115,116, \
         120,121,122,123,125,126,127,130,131,135,136,140,142,146,150,155,156,157,
         160,165,166,167,168,170,171,172,173,174,175,176,180,181,182,185, \
         190,191,200,201,205,206,220,230,235,236,237,240, \
         251,252,260,290,291,292]

  
    def random_headID(self, is_male):
        if is_male:
            return 100 #101 if random.randint(0,9)==0 else 100
        else:   
            return 101 if random.randint(0,7)==0 else 100
        #j = random.randint(0,len(self.female_head)-1)
        #return self.female_head[j]
        
  
    def random_hairBackID(self, is_male):
        chosen = False
        if is_male:
            while not chosen:
                j = random.randint(0,len(self.male_hairBack)-1)
                idd = self.male_hairBack[j]
                
                if idd ==140 and random.randint(0,2) != 0:
                    continue  # long hair should be rarer
                
                chosen = True
        else:
            while not chosen:
                j = random.randint(0,len(self.female_hairBack)-1)
                idd = self.female_hairBack[j]
                
                #if idd == 51 and random.randint(0,1) != 0:
                #    continue  # wild hair should be rarer
                chosen = True
        return idd

    def random_hairFrontID(self, is_male):
        chosen = False
        if is_male:
            while not chosen:
                j = random.randint(0,len(self.male_hairFront)-1)
                idd = self.male_hairFront[j]
                
                chosen = True
        else:
            while not chosen:
                j = random.randint(0,len(self.female_hairFront)-1)
                idd = self.female_hairFront[j]

                chosen = True
        return idd

    def random_eyesID(self, is_male):
        chosen = False
        if is_male:
            while not chosen:
                j = random.randint(0,len(self.male_eyes)-1)
                idd = idd2 = self.male_eyes[j]
                
                '''if random.randint(0,9) == 0:
                    j = random.randint(0,len(self.male_eyesSpecial)-1)
                    idd = self.male_eyesSpecial[j]  # special eyes'''
                if random.randint(0,9) == 0: # closed amused eyes
                    j = random.randint(0,len(self.male_eyesAlternative)-1)
                    idd = self.male_eyesAlternative[j] 
                chosen = True
            
        else:
            while not chosen:
                j = random.randint(0,len(self.female_eyes)-1)
                idd = idd2 = self.female_eyes[j]
                
                '''if random.randint(0,9) == 0:
                    j = random.randint(0,len(self.female_eyesSpecial)-1)
                    idd = self.female_eyesSpecial[j] # special eyes'''
                if random.randint(0,9) == 0: # closed amused eyes
                    j = random.randint(0,len(self.female_eyesAlternative)-1)
                    idd = self.female_eyesAlternative[j] 
                chosen = True
                
        return idd, idd2
        

        
    def random_faceID(self, is_male, skin_color):
        chosen = False
        
        if is_male:
            while not chosen:
                j = random.randint(0,len(self.male_face)-1)
                idd = self.male_face[j]
                
                '''if random.randint(0,49) == 0:
                    j = random.randint(0,len(self.male_faceSpecial)-1)
                    idd = self.male_faceSpecial[j]  # special face'''
                
                chosen = True
        else:
            while not chosen:
                j = random.randint(0,len(self.female_face)-1)
                idd = self.female_face[j]
                
                '''if random.randint(0,9) == 0:
                    j = random.randint(0,len(self.female_faceSpecial)-1)
                    idd = self.female_faceSpecial[j]  # special face'''
                
                # some mouths clash with the darkest skin
                if idd == 311 and skin_color == 8:
                    continue
                
                chosen = True
        return idd 
        
    def random_faceID_surprised(self, is_male, faceID):
        if is_male:
            if faceID % 2 == 0:
                j = random.randint(0,len(self.male_face_surprised_even)-1)
                idd = self.male_face_surprised_even[j] # even is lighter eyebrows
            else:
                j = random.randint(0,len(self.male_face_surprised_odd)-1)
                idd = self.male_face_surprised_odd[j] # odd is darker eyebrows
        else:
            if faceID % 2 == 0:
                j = random.randint(0,len(self.female_face_surprised_even)-1)
                idd = self.female_face_surprised_even[j]
            else:
                j = random.randint(0,len(self.female_face_surprised_odd)-1)
                idd = self.female_face_surprised_odd[j]
        return idd 
        
    def random_faceID_happy(self, is_male, faceID):
        if is_male:
            if faceID % 2 == 0:
                j = random.randint(0,len(self.male_face_happy_even)-1)
                idd = self.male_face_happy_even[j]
            else:
                j = random.randint(0,len(self.male_face_happy_odd)-1)
                idd = self.male_face_happy_odd[j]
        else:
            if faceID % 2 == 0:
                j = random.randint(0,len(self.female_face_happy_even)-1)
                idd = self.female_face_happy_even[j]
            else:
                j = random.randint(0,len(self.female_face_happy_odd)-1)
                idd = self.female_face_happy_odd[j]
        return idd 
        
    def random_faceID_unhappy(self, is_male, faceID):
        if is_male:
            if faceID % 2 == 0:
                j = random.randint(0,len(self.male_face_unhappy_even)-1)
                idd = self.male_face_unhappy_even[j]
            else:
                j = random.randint(0,len(self.male_face_unhappy_odd)-1)
                idd = self.male_face_unhappy_odd[j]
        else:
            if faceID % 2 == 0:
                j = random.randint(0,len(self.female_face_unhappy_even)-1)
                idd = self.female_face_unhappy_even[j]
            else:
                j = random.randint(0,len(self.female_face_unhappy_odd)-1)
                idd = self.female_face_unhappy_odd[j]
        return idd 
    
    def random_faceID_and_eyesID_contemplative(self, is_male, faceID, eyesID):
        face, eyes = faceID, eyesID
        # change the face or the eyes, not both
        if random.randint(0,1) == 0: 
            # change the eyes to be shut
            if is_male:
                j = random.randint(0,len(self.male_eyesContemplative)-1)
                eyes = self.male_eyesContemplative[j]
            else:
                j = random.randint(0,len(self.female_eyesContemplative)-1)
                eyes = self.female_eyesContemplative[j]
        else:
            # change the face
            if is_male:
                if faceID % 2 == 0:
                    j = random.randint(0,len(self.male_face_contemplative_even)-1)
                    face = self.male_face_contemplative_even[j]
                else:
                    j = random.randint(0,len(self.male_face_contemplative_odd)-1)
                    face = self.male_face_contemplative_odd[j]
            else:
                if faceID % 2 == 0:
                    j = random.randint(0,len(self.female_face_contemplative_even)-1)
                    face = self.female_face_contemplative_even[j]
                else:
                    j = random.randint(0,len(self.female_face_contemplative_odd)-1)
                    face = self.female_face_contemplative_odd[j]
    
        return face, eyes   

    def random_clothesID(self, is_male):
        chosen = False
        if is_male:
            while not chosen:
                j = random.randint(0,len(self.male_clothes)-1)
                idd = self.male_clothes[j]
                
                chosen = True
        else:
            while not chosen:
                j = random.randint(0,len(self.female_clothes)-1)
                idd = self.female_clothes[j]

                chosen = True
        return idd 



    # reassign eyes based on traits, since some combinations don't work well
    def reassigned_eyesID(self, is_male, traits):
        #print('eyesID=' + str(cur_id))

        if is_male:
            if 30 in traits:
                self.male_eyes.remove(100)
            if 30 in traits or 32 in traits or 40 in traits or 66 in traits:
                self.male_eyes.remove(105)
            if 27 in traits or 30 in traits or 32 in traits or 40 in traits or 62 in traits:
                self.male_eyes.remove(110)
            if 27 in traits or 85 in traits:
                self.male_eyes.remove(125)
            if 32 in traits:
                self.male_eyes.remove(135)
            if 85 in traits:
                self.male_eyes.remove(150)
            #if 13 in traits or 15 in traits or 21 in traits or 25 in traits or 29 in traits or 33 in traits \
            # or 37 in traits or 43 in traits or 47 in traits or 48 in traits or 52 in traits or 61 in traits \
            # or 63 in traits or 71 in traits or 82 in traits:
            #    self.male_eyesSpecial.remove(180)
            #if 15 in traits or 32 in traits or 47 in traits or 71 in traits:
            #    self.male_eyesSpecial.remove(181)
            #if 32 in traits:
            #    self.male_eyesSpecial.remove(182)
            #if 32 in traits or 47 in traits or 65 in traits:
            #    self.male_eyesSpecial.remove(183)
            if False:
                self.male_eyesSpecial.remove(185) # comical black flat eyes
            #if 32 in traits or 71 in traits:
            #    self.male_eyesSpecial.remove(192)
            #if 32 in traits or 47 in traits or 65 in traits or 71 in traits:    
            #    self.male_eyesSpecial.remove(193)
        
        else:
            if 27 in traits or 57 in traits or 85 in traits:
                self.female_eyes.remove(105)
            #if 13 in traits or 15 in traits or 21 in traits or 47 in traits or 65 in traits \
            # or 75 in traits or 77 in traits:
            #    self.female_eyesSpecial.remove(115)
            #if 15 in traits or 21 in traits:
            #    self.female_eyesSpecial.remove(120)
            #if 27 in traits or 57 in traits or 85 in traits:
            if 13 in traits or 29 in traits or 65 in traits or 75 in traits or 77 in traits:
                self.female_eyes.remove(135)
            #if 13 in traits or 15 in traits or 21 in traits or 29 in traits or 32 in traits \
            # or 47 in traits or 65 in traits or 75 in traits or 77 in traits or 81 in traits:
            #    self.female_eyesSpecial.remove(140)
            #if 58 in traits or 68 in traits or 74 in traits or 82 in traits:
            #    self.female_eyesSpecial.remove(145)
            #if 32 in traits:    
            #    self.female_eyesSpecial.remove(160)
            if 27 in traits:
                self.female_eyes.remove(170)
            if 77 in traits:
                self.female_eyes.remove(175)
            if 65 in traits:
                self.female_eyes.remove(180)
            #if 13 in traits or 15 in traits or 21 in traits or 29 in traits or 47 in traits:
            #    self.female_eyesSpecial.remove(185)
               
                
        idd, idd2 = self.random_eyesID(is_male) # set eyes
        return idd, idd2
    
    
    # reassign face based on traits, since some combinations don't work well    
    def reassigned_faceID(self, is_male, skin_color, traits):
        #print('faceID=' + str(cur_id))

        if is_male:
            #if 12 in traits or 70 in traits or 85 in traits:
            #    self.male_face.remove(105)
            #    self.male_face.remove(106)
            #if 12 in traits or 38 in traits or 46 in traits or 62 in traits or 64 in traits:
            #    self.male_face.remove(110)
            #    self.male_face.remove(111)
            #if 40 in traits or 48 in traits:
            #    self.male_face.remove(115)
            #    self.male_face.remove(116)
            #if 47 in traits or 77 in traits:
            #    self.male_face.remove(120)
            #    self.male_face.remove(121)
            #if 21 in traits or 32 in traits or 66 in traits:
            #    self.male_face.remove(125)
            #    self.male_face.remove(126)
            #if 77 in traits:
            #    self.male_face.remove(130)
            #    self.male_face.remove(131)
            if False:
                self.male_faceSpecial.remove(135) # surprised open mouth. what to do with it?
                self.male_faceSpecial.remove(136)
            #if 32 in traits or 66 in traits:
            #    self.male_face.remove(140)
            #    self.male_face.remove(141)
            if False:
                self.male_faceSpecial.remove(150) # angry mouth open. what to do?
            #if 27 in traits or 33 in traits or 61 in traits:
            #    self.male_face.remove(155)
            #    self.male_face.remove(156)
            if False:
                self.male_faceSpecial.remove(160) # another surprised open mouth
                self.male_faceSpecial.remove(161)
            #if 27 in traits or 33 in traits or 47 in traits or 57 in traits or 65 in traits or 75 in traits or 77 in traits:
            #    self.male_face.remove(165)
            #    self.male_face.remove(166)
            if False:
                self.male_faceSpecial.remove(170) # a very surprised open mouth
                self.male_faceSpecial.remove(171)
            if False:
                self.male_faceSpecial.remove(175) # a worried face with mouth open
                self.male_faceSpecial.remove(176)
            #if 33 in traits or 61 in traits or 67 in traits or 75 in traits or 77 in traits:
            #    self.male_face.remove(180)
            #    self.male_face.remove(181)
            #if 47 in traits or 65 in traits or 77 in traits:
            #    self.male_face.remove(185)
            #if 46 in traits:
            #    self.male_face.remove(190)
            #    self.male_face.remove(191)
            #if 28 in traits or 39 in traits or 85 in traits:
            #    self.male_face.remove(195)
            #    self.male_face.remove(196)
            #if 28 in traits or 39 in traits or 61 in traits or 85 in traits:
            #    self.male_face.remove(200)
            #    self.male_face.remove(201)
            #if 27 in traits or 33 in traits or 61 in traits:
            #    self.male_face.remove(205)
            #    self.male_face.remove(206)
            #if 11 in traits or 15 in traits or 29 in traits or 47 in traits or 65 in traits or 75 in traits or 77 in traits:
            #    self.male_face.remove(210)
            #    self.male_face.remove(211)
            #if 11 in traits or 15 in traits or 21 in traits or 29 in traits or 47 in traits or 65 in traits or 75 in traits \
            # or 77 in traits:
            #    self.male_face.remove(215)
            #    self.male_face.remove(216)
            #if 15 in traits or 29 in traits or 47 in traits or 65 in traits or 75 in traits or 77 in traits:
            #    self.male_face.remove(220)
            #    self.male_face.remove(221)
            if False:
                self.male_faceSpecial.remove(225) # angry with mouth open again
                self.male_faceSpecial.remove(226)
            #if 15 in traits or 21 in traits or 29 in traits or 47 in traits or 65 in traits or 75 in traits \
            # or 77 in traits:
            #    self.male_face.remove(230)
            #    self.male_face.remove(231)
            if 17 in traits or 26 in traits or 31 in traits or 38 in traits or 42 in traits or 46 in traits \
             or 52 in traits or 58 in traits or 64 in traits or 68 in traits or 74 in traits or 82 in traits:
                pass
                #self.male_faceSpecial.remove(235) # goofy tongue out
                #self.male_faceSpecial.remove(236)
            
        else:
            if 49 in traits:
                self.female_face.remove(100) 
                self.female_face.remove(101)
            if 12 in traits or 46 in traits or 49 in traits or 85 in traits:
                self.female_face.remove(105) 
                self.female_face.remove(106)
            #if 12 in traits or 46 in traits or 49 in traits or 59 in traits or 85 in traits:
            #    self.female_face.remove(110) 
            #    self.female_face.remove(111)
            #if 12 in traits or 28 in traits or 36 in traits or 46 in traits or 49 in traits or 59 in traits \
            # or 85 in traits:
            #    self.female_face.remove(115) 
            #    self.female_face.remove(116)
            if False:
                self.female_faceSpecial.remove(120) # mouth has an x shape
                self.female_faceSpecial.remove(121)
            #if 17 in traits or 26 in traits or 31 in traits or 38 in traits or 42 in traits or 46 in traits \
            # or 52 in traits or 58 in traits or 64 in traits or 68 in traits or 74 in traits or 82 in traits:
            #    self.female_faceSpecial.remove(125) # tongue sticking out
            #    self.female_faceSpecial.remove(126)
            if False:
                self.female_faceSpecial.remove(130) # dog mouth
                self.female_faceSpecial.remove(131)
            if 15 in traits or 21 in traits or 29 in traits or 47 in traits or 65 in traits or 77 in traits:
                self.female_face.remove(135) 
                self.female_face.remove(136)
            if 65 in traits:
                self.female_face.remove(140) 
                self.female_face.remove(141)
            if 27 in traits or 85 in traits:
                self.female_face.remove(145) 
                self.female_face.remove(146)
            #if 27 in traits or 33 in traits or 63 in traits or 75 in traits or 85 in traits:
            #    self.female_face.remove(150) 
            #    self.female_face.remove(151)
            if False:
                self.female_faceSpecial.remove(155) # wide surprised mouth
                self.female_faceSpecial.remove(156)
            #if 15 in traits or 25 in traits or 37 in traits or 47 in traits or 61 in traits or 65 in traits \
            # or 75 in traits or 77 in traits:
            #    self.female_face.remove(160) 
            #    self.female_face.remove(161)
            #if 7 in traits or 15 in traits or 21 in traits or 25 in traits or 37 in traits or 47 in traits \
            # or 61 in traits or 65 in traits or 75 in traits or 77 in traits:
            #    self.female_face.remove(165) 
            #    self.female_face.remove(166)
            if 47 in traits or 61 in traits or 77 in traits:
                self.female_face.remove(170) 
                self.female_face.remove(171)
            if 12 in traits or 20 in traits or 27 in traits or 33 in traits or 49 in traits \
             or 59 in traits or 70 in traits or 85 in traits:
                self.female_face.remove(175) 
                self.female_face.remove(176)
            #if 15 in traits or 21 in traits or 33 in traits or 43 in traits or 47 in traits or 61 in traits \
            # or 65 in traits or 75 in traits or 77 in traits:
            #    self.female_face.remove(180) 
            #    self.female_face.remove(181)
            #if 15 in traits or 20 in traits or 21 in traits or 27 in traits or 33 in traits or 43 in traits \
            # or 47 in traits or 61 in traits or 65 in traits or 75 in traits or 77 in traits or 81 in traits:
            #    self.female_face.remove(185) # mouth open and dismayed
            #    self.female_face.remove(186)
            #if 21 in traits or 33 in traits or 47 in traits or 61 in traits or 65 in traits \
            # or 75 in traits or 77 in traits:
            #    self.female_face.remove(190) 
            #    self.female_face.remove(191)
            if False:
                self.female_faceSpecial.remove(195) # sad lips
                self.female_faceSpecial.remove(196)
            #if 7 in traits or 11 in traits or 15 in traits or 20 in traits or 21 in traits \
            # or 27 in traits or 29 in traits or 33 in traits or 37 in traits or 43 in traits \
            # or 47 in traits or 52 in traits or 59 in traits or 61 in traits or 63 in traits \
            # or 65 in traits or 67 in traits or 75 in traits or 77 in traits or 81 in traits or 85 in traits:
            #    self.female_face.remove(200) # sad eyebrows no mouth
            #    self.female_face.remove(201)
            #if 20 in traits or 27 in traits or 33 in traits or 37 in traits or 43 in traits \
            # or 47 in traits or 59 in traits or 61 in traits or 65 in traits or 67 in traits \
            # or 75 in traits or 77 in traits:
            #    self.female_face.remove(205)
            #    self.female_face.remove(206)
            #if 61 in traits or 65 in traits or 77 in traits:
            #    self.female_face.remove(210) # sad eyebrows no mouth
            #    self.female_face.remove(211)
            #if 15 in traits or 20 in traits or 27 in traits or 33 in traits or 37 in traits \
            # or 52 in traits or 59 in traits or 61 in traits or 65 in traits or 77 in traits:
            #    self.female_face.remove(215) # sad eyebrows no mouth
            #    self.female_face.remove(216)
            if False:
                self.female_faceSpecial.remove(220) # another wide mouth
                self.female_faceSpecial.remove(221)
            #if 21 in traits or 29 in traits or 37 in traits or 47 in traits or 61 in traits \
            # or 65 in traits or 69 in traits or 75 in traits or 77 in traits:
            #    self.female_face.remove(225) 
            #    self.female_face.remove(226)
            #if 15 in traits or 21 in traits or 33 in traits or 37 in traits or 47 in traits \
            # or 61 in traits or 65 in traits or 75 in traits or 77 in traits:
            #    self.female_face.remove(230) 
            #    self.female_face.remove(231)
            if 65 in traits:
                self.female_face.remove(235) 
                self.female_face.remove(236)
            #if 59 in traits:
            #    self.female_face.remove(240) 
            #    self.female_face.remove(241)
            if 65 in traits or 77 in traits:
                self.female_face.remove(245) 
                self.female_face.remove(246)
            #if 15 in traits or 21 in traits or 29 in traits or 47 in traits or 65 in traits \
            # or 77 in traits:
            #    self.female_face.remove(250) 
            #    self.female_face.remove(251)
            if 36 in traits or 40 in traits or 66 in traits:
                self.female_face.remove(255) 
                self.female_face.remove(256)
            if 36 in traits or 40 in traits or 66 in traits:
                self.female_face.remove(260) 
                self.female_face.remove(261)
            if 13 in traits or 21 in traits or 29 in traits or 47 in traits or 65 in traits \
             or 75 in traits or 77 in traits:
                self.female_face.remove(265) 
                self.female_face.remove(266)
            #if 13 in traits or 15 in traits or 21 in traits or 29 in traits or 25 in traits \
            # or 29 in traits or 33 in traits or 37 in traits or 47 in traits or 61 in traits \
            # or 65 in traits or 69 in traits or 75 in traits or 77 in traits or 81 in traits:
            #    self.female_face.remove(270) 
            #    self.female_face.remove(271)
            if 65 in traits or 77 in traits:
                self.female_face.remove(275) 
                self.female_face.remove(276)
            if False:
                self.female_faceSpecial.remove(280) # critical sad lips
                self.female_faceSpecial.remove(281)
            if 11 in traits or 13 in traits or 15 in traits or 21 in traits or 29 in traits \
             or 47 in traits or 65 in traits or 75 in traits or 77 in traits or 81 in traits:
                self.female_face.remove(285) 
                self.female_face.remove(286)
            if 77 in traits:
                self.female_face.remove(290) 
                self.female_face.remove(291)
            if 34 in traits:
                self.female_face.remove(295) 
                self.female_face.remove(296)
            #if 65 in traits or 77 in traits:
            #    self.female_face.remove(300) 
            #    self.female_face.remove(301)
            if False:
                self.female_faceSpecial.remove(305) # happy wide mouth
                self.female_faceSpecial.remove(306)
            #if 15 in traits or 21 in traits or 47 in traits or 65 in traits or 75 in traits \
            # or 77 in traits or 81 in traits:
            #    self.female_face.remove(310) 
            #    self.female_face.remove(311)
            if False:
                self.female_faceSpecial.remove(315) # sad mouth
                self.female_faceSpecial.remove(316)
            if 65 in traits or 77 in traits:
                self.female_face.remove(320) 
                self.female_face.remove(321)
            if False:
                self.female_faceSpecial.remove(325) # sad dog mouth
                self.female_faceSpecial.remove(326) 

        
        cur_id = self.random_faceID(is_male, skin_color) # set face
        return cur_id
    
    
    #self.female_faceSpecial = [120,121,125,126,130,131,155,156,195,196, \
    #     220,221,280,281,305,306,315,316,325,326]
         
         
         
         
         
         
        