


import os
import pickle
import pygame



from source.tachie import *


def get_font(font_name, font_size):
    source_dir = os.path.split(os.path.abspath(__file__))[0]
    main_dir = os.path.join(source_dir,"../")
    font_path = os.path.join(main_dir,"fonts",font_name)
    #font_path = os.path.join("fonts",font_name)
    font = pygame.font.Font(font_path, font_size)
    return font


main_directory = os.path.split(os.path.abspath(__file__))[0]
main_dir = os.path.join(main_directory,"../")
save_data_path = "save_data"

   

        

pygame.init()


screen = pygame.display.set_mode((900,600))

screen.fill((20, 20, 160))






background_color = (75,75,75)
screen.fill(background_color)
       
          
text_surface = get_font("Vera.ttf", 18).render("test message", False, (250,10,10))
x = 200
screen.blit(text_surface, (x,35))
  




   
tachie = Tachie()
got_tachie = tachie.get_tachie()
source_rect = got_tachie.get_rect()
vertical_offset = 0


screen.blit(got_tachie, (250, 50), source_rect)

text_surface = get_font("VeraSe.ttf",14).render("Another message", True, (160,200,75))
screen.blit(text_surface, (250,120))

pygame.display.flip() # update the whole screen
        
        

        
       
  
                
def main():
	while 1:
		events = pygame.event.get()
		for event in events:

            	    if event.type == pygame.KEYDOWN and event.unicode == 'q':
                		pygame.quit()
                		raise SystemExit            
        
  

 

            
            
            
            