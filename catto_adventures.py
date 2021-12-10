import pygame
import sys
pygame.init()
import pygame.freetype
import random
pygame.freetype.init()

winW=900
winH=500
win=pygame.display.set_mode((winW,winH))
pygame.display.set_caption('Catto Adventures')
display_catto_img=pygame.image.load('Assets//catto1L.png')
click_sound=pygame.mixer.Sound("Assets//click.mp3")
eating_sound=pygame.mixer.Sound("Assets//eating_sound.mp3")
hurt_sound=pygame.mixer.Sound("Assets//hurt_sound.mp3")
portal_sound=pygame.mixer.Sound("Assets//portal_sound.mp3")
seacret_sound=pygame.mixer.Sound("Assets//seacret_sound.mp3")
pygame.mixer.music.load("Assets//theme_song.mp3")
pygame.display.set_icon(pygame.transform.scale(display_catto_img,(32,32)))
catto_A1_img=pygame.image.load('Assets//cattoAn1.png')
catto_A2_img=pygame.image.load('Assets//cattoAn2.png')
catto_A3_img=pygame.image.load('Assets//cattoAn3.png')
catto_A4_img=pygame.image.load('Assets//cattoAn4.png')
catto_A1=pygame.transform.scale(catto_A1_img,(128,128))
catto_A2=pygame.transform.scale(catto_A2_img,(128,128))
catto_A3=pygame.transform.scale(catto_A3_img,(128,128))
catto_A4=pygame.transform.scale(catto_A4_img,(128,128))
food_intro_img=pygame.image.load('Assets//food1.png')
food_intro=pygame.transform.scale(food_intro_img,(20,32))
music_cat_img=pygame.image.load('Assets//music_cat.png')
music_cat=pygame.transform.scale(music_cat_img,(32,32))
animation_counter=0
fps=60
fps_intro=7
fps_help=15
cat_W=64
cat_H=64
white=255,255,255
black=0,0,0
gray=120,120,120
red=255,0,0
orange=255,153,51
yellow=255,242,0
green=34,177,76
blue=0,162,232
indigo=63,72,204
violet=163,73,164
brown=185,122,87
light_blue=153,217,234
pink=255,174,201

music_state=True
tile_size=50

roy_img=pygame.image.load('Assets//roygbivbbt.png')
roy=pygame.transform.scale(roy_img,(tile_size,tile_size))

tile1_img=pygame.image.load('Assets//tile1.png')
tile1=pygame.transform.scale(tile1_img,(tile_size,tile_size))

tile2_img=pygame.image.load('Assets//tile2.png')
tile2=pygame.transform.scale(tile2_img,(tile_size,tile_size))

tile3_img=pygame.image.load('Assets//tile3.png')
tile3=pygame.transform.scale(tile3_img,(tile_size,tile_size))

catto1L_img=pygame.image.load('Assets//catto1L.png')
catto2L_img=pygame.image.load('Assets//catto2L.png')
catto3L_img=pygame.image.load('Assets//catto3L.png')

catto1R_img=pygame.image.load('Assets//catto1R.png')
catto2R_img=pygame.image.load('Assets//catto2R.png')
catto3R_img=pygame.image.load('Assets//catto3R.png')

catto1L=pygame.transform.scale(catto1L_img,(cat_W,cat_H))
catto2L=pygame.transform.scale(catto2L_img,(cat_W,cat_H))
catto3L=pygame.transform.scale(catto3L_img,(cat_W,cat_H))

catto1R=pygame.transform.scale(catto1R_img,(cat_W,cat_H))
catto2R=pygame.transform.scale(catto2R_img,(cat_W,cat_H))
catto3R=pygame.transform.scale(catto3R_img,(cat_W,cat_H))

evil_catto_L_img=pygame.image.load('Assets//evil_catto_L.png')
evil_catto_L=pygame.transform.scale(evil_catto_L_img,(cat_W,cat_H)) 
evil_catto_R_img=pygame.image.load('Assets//evil_catto_R.png')
evil_catto_R=pygame.transform.scale(evil_catto_R_img,(cat_W,cat_H))

food1_img=pygame.image.load('Assets//food1.png')
food1=pygame.transform.scale(food1_img,(28,40))

food2_img=pygame.image.load('Assets//food2.png')
food2=pygame.transform.scale(food2_img,(25,40))

food3_img=pygame.image.load('Assets//food3.png')
food3=pygame.transform.scale(food3_img,(28,40))

foodIcon1_img=pygame.image.load('Assets//pr1.png')
foodIcon1=pygame.transform.scale(foodIcon1_img,(21,9))

foodIcon2_img=pygame.image.load('Assets//pr2.png')
foodIcon2=pygame.transform.scale(foodIcon2_img,(21,13))

foodIcon3_img=pygame.image.load('Assets//pr3.png')
foodIcon3=pygame.transform.scale(foodIcon3_img,(21,19))

bg=pygame.image.load('Assets//bg.jpg')
bg2=pygame.image.load('Assets//bg2.jpg')
bg3=pygame.image.load('Assets//bg3.jpg')




path0_img=pygame.image.load('Assets//0path0.png')
path0=pygame.transform.scale(path0_img,(tile_size,tile_size))


path1_img=pygame.image.load('Assets//1path1.png')
path1=pygame.transform.scale(path1_img,(tile_size,tile_size))

path2_img=pygame.image.load('Assets//2path2.png')
path2=pygame.transform.scale(path2_img,(tile_size,tile_size))



portal_img=pygame.image.load('Assets//portal0.png')
portal=pygame.transform.scale(portal_img,(tile_size*2,tile_size*2))

portal_1_img=pygame.image.load('Assets//portal1.png')
portal_1=pygame.transform.scale(portal_1_img,(tile_size*2,tile_size*2))

portal_2_img=pygame.image.load('Assets//portal2.png')
portal_2=pygame.transform.scale(portal_2_img,(tile_size*2,tile_size*2))

portal_3_img=pygame.image.load('Assets//portal3.png')
portal_3=pygame.transform.scale(portal_3_img,(tile_size*2,tile_size*2))

heart_img=pygame.image.load('Assets//heart.png')
heart=pygame.transform.scale(heart_img,(16,16))

flower1_img=pygame.image.load('Assets//flower1.png')
flower1=pygame.transform.scale(flower1_img,(tile_size,tile_size))

flower2_img=pygame.image.load('Assets//flower2.png')
flower2=pygame.transform.scale(flower2_img,(tile_size,tile_size))

flower3_img=pygame.image.load('Assets//flower3.png')
flower3=pygame.transform.scale(flower3_img,(tile_size,tile_size))

flower4_img=pygame.image.load('Assets//flower4.png')
flower4=pygame.transform.scale(flower4_img,(tile_size,tile_size))

flower5_img=pygame.image.load('Assets//flower5.png')
flower5=pygame.transform.scale(flower5_img,(tile_size,tile_size))

flower6_img=pygame.image.load('Assets//flower6.png')
flower6=pygame.transform.scale(flower6_img,(tile_size,tile_size))

flower7_img=pygame.image.load('Assets//flower7.png')
flower7=pygame.transform.scale(flower7_img,(tile_size,tile_size))



velx=3.8 #3.8,3.3,2.8
vely=3.8

velx_456=3.3
vely_456=3.3

velx_789=2.9
vely_789=2.9
GameModeHard=False

count_lives=3 
count_death=0
to_right_1=True
MS_U_1=True
MS_D_1=True
MS_L_1=True
MS_R_1=True
wc_1=1
pc_1=1
ect_1_1=1
ect_1_2=1
ect_1_3=1
Ecat1col_1=False
Ecat2col_1=False
Ecat3col_1=False
Food1col_1=False
Food2col_1=False
Food3col_1=False
Portal_Perms_1=False
Portalcol_1=False
LevelOneCleared=False
camOffx_1=-100
camOffy_1=740



to_right_2=True
MS_U_2=True
MS_D_2=True
MS_L_2=True
MS_R_2=True
wc_2=1
pc_2=1
ect_2_1=1
ect_2_2=1
ect_2_3=1
Ecat1col_2=False
Ecat2col_2=False
Ecat3col_2=False
Food1col_2=False
Food2col_2=False
Food3col_2=False
Portal_Perms_2=False
Portalcol_2=False
LevelTwoCleared=False
camOffx_2=1640
camOffy_2=-300



to_right_3=True
MS_U_3=True
MS_D_3=True
MS_L_3=True
MS_R_3=True
wc_3=1
pc_3=1
ect_3_1=1
ect_3_2=1
ect_3_3=1
Ecat1col_3=False
Ecat2col_3=False
Ecat3col_3=False
Food1col_3=False
Food2col_3=False
Food3col_3=False
Portal_Perms_3=False
Portalcol_3=False
LevelThreeCleared=False
camOffx_3=-350
camOffy_3=-300          




to_right_4=True
MS_U_4=True
MS_D_4=True
MS_L_4=True
MS_R_4=True
wc_4=1
pc_4=1
ect_4_1=1
ect_4_2=1
ect_4_3=1
Ecat1col_4=False
Ecat2col_4=False
Ecat3col_4=False
Food1col_4=False
Food2col_4=False
Food3col_4=False
Portal_Perms_4=False
Portalcol_4=False
LevelFourCleared=False
camOffx_4=200          
camOffy_4=-300    




to_right_5=True
MS_U_5=True
MS_D_5=True
MS_L_5=True
MS_R_5=True
wc_5=1
pc_5=1
ect_5_1=1
ect_5_2=1
ect_5_3=1
Ecat1col_5=False
Ecat2col_5=False
Ecat3col_5=False
Food1col_5=False
Food2col_5=False
Food3col_5=False
Portal_Perms_5=False
Portalcol_5=False
LevelFiveCleared=False
camOffx_5=1700          
camOffy_5=745




to_right_6=True
MS_U_6=True
MS_D_6=True
MS_L_6=True
MS_R_6=True
wc_6=1
pc_6=1
ect_6_1=1
ect_6_2=1
ect_6_3=1
Ecat1col_6=False
Ecat2col_6=False
Ecat3col_6=False
Food1col_6=False
Food2col_6=False
Food3col_6=False
Portal_Perms_6=False
Portalcol_6=False
LevelSixCleared=False
camOffx_6=-350         
camOffy_6=750




to_right_7=True
MS_U_7=True
MS_D_7=True
MS_L_7=True
MS_R_7=True
wc_7=1
pc_7=1
ect_7_1=1
ect_7_2=1
ect_7_3=1
Ecat1col_7=False
Ecat2col_7=False
Ecat3col_7=False
Food1col_7=False
Food2col_7=False
Food3col_7=False
Portal_Perms_7=False
Portalcol_7=False
LevelSevenCleared=False
camOffx_7=675        
camOffy_7=-250 




to_right_8=True
MS_U_8=True
MS_D_8=True
MS_L_8=True
MS_R_8=True
wc_8=1
pc_8=1
ect_8_1=1
ect_8_2=1
ect_8_3=1
Ecat1col_8=False
Ecat2col_8=False
Ecat3col_8=False
Food1col_8=False
Food2col_8=False
Food3col_8=False
Portal_Perms_8=False
Portalcol_8=False
LevelEightCleared=False
camOffx_8=1540        
camOffy_8=-250


GotSeacret=False
s_c=1


to_right_9=True
MS_U_9=True
MS_D_9=True
MS_L_9=True
MS_R_9=True
wc_9=1
pc_9=1
ect_9_1=1
ect_9_2=1
ect_9_3=1
Ecat1col_9=False
Ecat2col_9=False
Ecat3col_9=False
Food1col_9=False
Food2col_9=False
Food3col_9=False
Portal_Perms_9=False
Portalcol_9=False
LevelNineCleared=False
camOffx_9=-275        
camOffy_9=-240 

#GameOver=False
def game_intro():
    global count_death
    global count_lives
    global LevelOneCleared
    global LevelTwoCleared
    global LevelThreeCleared
    global LevelFourCleared
    global LevelFiveCleared
    global LevelSixCleared
    global LevelSevenCleared
    global LevelEightCleared
    global LevelNineCleared
    global GotSeacret

    global Ecat1col_1
    global Ecat2col_1
    global Ecat3col_1
    global Food1col_1
    global Food2col_1
    global Food3col_1
    global Portal_Perms_1
    global Portalcol_1
    global camOffx_1
    global camOffy_1

    global Ecat1col_2
    global Ecat2col_2
    global Ecat3col_2
    global Food1col_2
    global Food2col_2
    global Food3col_2
    global Portal_Perms_2
    global Portalcol_2
    global camOffx_2
    global camOffy_2


    global Ecat1col_3
    global Ecat2col_3
    global Ecat3col_3
    global Food1col_3
    global Food2col_3
    global Food3col_3
    global Portal_Perms_3
    global Portalcol_3
    global camOffx_3
    global camOffy_3

    global Ecat1col_4
    global Ecat2col_4
    global Ecat3col_4
    global Food1col_4
    global Food2col_4
    global Food3col_4
    global Portal_Perms_4
    global Portalcol_4
    global camOffx_4
    global camOffy_4


    global Ecat1col_5
    global Ecat2col_5
    global Ecat3col_5
    global Food1col_5
    global Food2col_5
    global Food3col_5
    global Portal_Perms_5
    global Portalcol_5
    global camOffx_5
    global camOffy_5

    global Ecat1col_6
    global Ecat2col_6
    global Ecat3col_6
    global Food1col_6
    global Food2col_6
    global Food3col_6
    global Portal_Perms_6
    global Portalcol_6
    global camOffx_6
    global camOffy_6

    global Ecat1col_7
    global Ecat2col_7
    global Ecat3col_7
    global Food1col_7
    global Food2col_7
    global Food3col_7
    global Portal_Perms_7
    global Portalcol_7
    global camOffx_7
    global camOffy_7

    global Ecat1col_8
    global Ecat2col_8
    global Ecat3col_8
    global Food1col_8
    global Food2col_8
    global Food3col_8
    global Portal_Perms_8
    global Portalcol_8
    global camOffx_8
    global camOffy_8

    global Ecat1col_9
    global Ecat2col_9
    global Ecat3col_9
    global Food1col_9
    global Food2col_9
    global Food3col_9
    global Portal_Perms_9
    global Portalcol_9
    global camOffx_9
    global camOffy_9
    
    global animation_counter
    global music_state
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit() #quit()
        win.blit(bg2,(0,0))
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if 0+260>mouse[0]>0 and 90+70>mouse[1]>90:
            pygame.draw.rect(win,gray,(0,90,260,70))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
               
                count_lives=3
                count_death=0
                LevelOneCleared=False
                LevelTwoCleared=False
                LevelThreeCleared=False
                LevelFourCleared=False
                LevelFiveCleared=False
                LevelSixCleared=False
                LevelSevenCleared=False
                LevelEightCleared=False
                LevelNineCleared=False
                
                GotSeacret=False

                
                Ecat1col_1=False
                Ecat2col_1=False
                Ecat3col_1=False
                Food1col_1=False
                Food2col_1=False
                Food3col_1=False
                Portal_Perms_1=False
                Portalcol_1=False
                camOffx_1=-100
                camOffy_1=740

                Ecat1col_2=False
                Ecat2col_2=False
                Ecat3col_2=False
                Food1col_2=False
                Food2col_2=False
                Food3col_2=False
                Portal_Perms_2=False
                Portalcol_2=False
                camOffx_2=1640
                camOffy_2=-300

                Ecat1col_3=False
                Ecat2col_3=False
                Ecat3col_3=False
                Food1col_3=False
                Food2col_3=False
                Food3col_3=False
                Portal_Perms_3=False
                Portalcol_3=False
                camOffx_3=-350
                camOffy_3=-300     

                Ecat1col_4=False
                Ecat2col_4=False
                Ecat3col_4=False
                Food1col_4=False
                Food2col_4=False
                Food3col_4=False
                Portal_Perms_4=False
                Portalcol_4=False
                camOffx_4=200          
                camOffy_4=-300

                Ecat1col_5=False
                Ecat2col_5=False
                Ecat3col_5=False
                Food1col_5=False
                Food2col_5=False
                Food3col_5=False
                Portal_Perms_5=False
                Portalcol_5=False
                camOffx_5=1700          
                camOffy_5=745

                Ecat1col_6=False
                Ecat2col_6=False
                Ecat3col_6=False
                Food1col_6=False
                Food2col_6=False
                Food3col_6=False
                Portal_Perms_6=False
                Portalcol_6=False
                camOffx_6=-350         
                camOffy_6=750

                Ecat1col_7=False
                Ecat2col_7=False
                Ecat3col_7=False
                Food1col_7=False
                Food2col_7=False
                Food3col_7=False
                Portal_Perms_7=False
                Portalcol_7=False
                camOffx_7=675        
                camOffy_7=-250

                Ecat1col_8=False
                Ecat2col_8=False
                Ecat3col_8=False
                Food1col_8=False
                Food2col_8=False
                Food3col_8=False
                Portal_Perms_8=False
                Portalcol_8=False
                camOffx_8=1540        
                camOffy_8=-250

                Ecat1col_9=False
                Ecat2col_9=False
                Ecat3col_9=False
                Food1col_9=False
                Food2col_9=False
                Food3col_9=False
                Portal_Perms_9=False
                Portalcol_9=False
                camOffx_9=-275        
                camOffy_9=-240 
                
                main()
            
        else:
            pygame.draw.rect(win,black,(0,90,260,70))


        if 0+205>mouse[0]>0 and 190+70>mouse[1]>190:
            pygame.draw.rect(win,gray,(0,190,205,70))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                help_menu()
        else:
            pygame.draw.rect(win,black,(0,190,205,70))

        if 0+205>mouse[0]>0 and 290+70>mouse[1]>290:
            pygame.draw.rect(win,gray,(0,290,205,70))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                pygame.quit()
        else:
            pygame.draw.rect(win,black,(0,290,205,70))
            


        
            
            
            
        if animation_counter==1 or animation_counter==7:
            win.blit(catto_A1,[600,200])

        if animation_counter==2 or animation_counter==6:
            win.blit(catto_A2,[600,200])

        if animation_counter==3 or animation_counter==5:
            win.blit(catto_A3,[600,200])
        if animation_counter==4:
            win.blit(catto_A4,[600,200])
            



        if animation_counter+1>7:
           animation_counter=1
        else:
            animation_counter=animation_counter+1

        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(0,100),"start",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(0,200),"Help",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(0,300),"Quit",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',40).render_to(win,(390,80),"Catto Adventures",orange)
        win.blit(food_intro,[560,290])
        win.blit(tile1,(540,330))
        win.blit(tile1,(590,330))
        win.blit(tile1,(630,330))
        win.blit(tile1,(680,330))
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(fps_intro)

def help_menu():
    global music_state
    global GameModeHard
    hm=True
    while hm:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit() #quit()
        win.blit(bg2,(0,0))
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(0,30),"how to play:",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(40,50),"search the map to find all the food",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(40,70),"avoid being hit by evil cattos",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(40,90),"after all the food has been collected find the portal",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(40,110),"to proceed to the next level",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(40,130),"there is one seacret item hidden somwhere in the game",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(40,150),"you will progressively get slower as you go on",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(40,170),"there are nine levels in total",black)        
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(40,190),"good luck on your adventure, have fun!",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(0,210),"press 'p' to pause the game",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(0,230),"use arrow keys to move",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(0,250),"game mode easy - checkpoints for every 3 levels",black)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(0,270),"game mode hard - no checkpoints, you have 3 lives",black)


        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(200,480),"game made by ladystardustlilith on github",black)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(500,300),"music and sounds",black)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(300,300),"Game Mode",black)
        win.blit(food1,(500,20))
        win.blit(food2,(550,20))
        win.blit(food3,(600,20))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()


        if 0+200>mouse[0]>0 and 390+70>mouse[1]>390:
            pygame.draw.rect(win,gray,(0,390,200,70))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                game_intro()
        else:
            pygame.draw.rect(win,black,(0,390,200,70))


        if 540+50>mouse[0]>540 and 330+50>mouse[1]>330:
            pygame.draw.rect(win,gray,(540,330,50,50))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                if music_state==False:
                    music_state=not music_state
        else:
            pygame.draw.rect(win,black,(540,330,50,50))

        if 645+50>mouse[0]>645 and 330+50>mouse[1]>330:
            pygame.draw.rect(win,gray,(645,330,50,50))
            if click[0]==1:
                if music_state==True:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(click_sound)
                    music_state=not music_state
        else:
            pygame.draw.rect(win,black,(645,330,50,50))



        if 340+50>mouse[0]>340 and 330+50>mouse[1]>330:
            pygame.draw.rect(win,gray,(340,330,50,50))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                GameModeHard=False
        else:
            pygame.draw.rect(win,black,(340,330,50,50))

        if 445+50>mouse[0]>445 and 330+50>mouse[1]>330:
            pygame.draw.rect(win,gray,(445,330,50,50))
            if click[0]==1:
                if music_state==True:
                   pygame.mixer.Sound.play(click_sound)
                GameModeHard=True
        else:
            pygame.draw.rect(win,black,(445,330,50,50))



        if music_state==True:
            win.blit(music_cat,[545,400])
        if music_state==False:
            win.blit(music_cat,[645,400])

        if GameModeHard==False:
            win.blit(music_cat,[345,400])
        if GameModeHard==True:
            win.blit(music_cat,[445,400])
            

        


        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(0,400),"back",white)

        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(550,350),"on",white)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(650,350),"off",white)

        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(345,350),"Easy",white)
        pygame.freetype.Font('Assets//8bit16.ttf',15).render_to(win,(450,350),"Hard",white)
            
        
        

        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(fps_help)
def game_over():
##    global count_lives
  #  global GameOver
    pygame.mixer.music.stop() #?idk
##    global music_state
##    global LevelOneCleared
##    global LevelTwoCleared
##    global LevelThreeCleared
##    global LevelFourCleared
##    global LevelFiveCleared
##    global LevelSixCleared
##    global LevelSevenCleared
##    global LevelEightCleared
##    global LevelNineCleared
##    global GotSeacret
    go=True
    while go:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        win.blit(bg2,(0,0))
        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(220,150),"Game Over!",black)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 150+115>mouse[0]>150 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(150,342,115,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                pygame.quit()
        else:
            pygame.draw.rect(win,black,(150,342,115,40))

        if 600+205>mouse[0]>600 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(600,342,205,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
##                count_lives=3
##                LevelOneCleared=False
##                LevelTwoCleared=False
##                LevelThreeCleared=False
##                LevelFourCleared=False
##                LevelFiveCleared=False
##                LevelSixCleared=False
##                LevelSevenCleared=False
##                LevelEightCleared=False
##                LevelNineCleared=False
##                GotSeacret=False
               # GameOver=False
                game_intro()
        else:
            pygame.draw.rect(win,black,(600,342,205,40))


        pygame.freetype.Font('Assets//8bit16.ttf',40).render_to(win,(150,350),"Quit",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',40).render_to(win,(600,350),"Restart",orange)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(fps_help)
def start_pause(key):
    if key[pygame.K_p]:
        if music_state==True:
            pygame.mixer.Sound.play(click_sound)
        pause()
def pause():
    global music_state
    pause=True
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        win.blit(bg2,(0,0))
        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(300,100),"Paused!",black)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if 50+270>mouse[0]>50 and 242+40>mouse[1]>242:
            pygame.draw.rect(win,gray,(50,242,270,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                game_intro()
        else:
            pygame.draw.rect(win,black,(50,242,270,40))

        if 600+238>mouse[0]>600 and 242+40>mouse[1]>242:
            pygame.draw.rect(win,gray,(600,242,238,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)

                pause=False
        else:
            pygame.draw.rect(win,black,(600,242,238,40))


        if 540+50>mouse[0]>540 and 330+50>mouse[1]>330:
            pygame.draw.rect(win,gray,(540,330,50,50))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                if music_state==False:
                    pygame.mixer.music.play(-1)
                    music_state=not music_state
        else:
            pygame.draw.rect(win,black,(540,330,50,50))

        if 645+50>mouse[0]>645 and 330+50>mouse[1]>330:
            pygame.draw.rect(win,gray,(645,330,50,50))
            if click[0]==1:
                if music_state==True:
                    pygame.mixer.music.stop() 
                    pygame.mixer.Sound.play(click_sound)
                    music_state=not music_state
        else:
            pygame.draw.rect(win,black,(645,330,50,50))

        if music_state==True:
            win.blit(music_cat,[545,400])
        if music_state==False:
            win.blit(music_cat,[645,400])

                  

        

        pygame.freetype.Font('Assets//8bit16.ttf',40).render_to(win,(50,250),"Main Menu",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',40).render_to(win,(600,250),"Continue",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(550,350),"on",white)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(650,350),"off",white)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(500,300),"music and sounds",black)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(fps_help)



def game_completed():
    global GameModeHard
    global music_state
    global GotSeacret
    global count_lives
    global count_death
    pygame.mixer.music.stop() 
    gc=True
    while gc:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        win.blit(bg2,(0,0))
        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(220,30),"Well Done!",black)
        if GameModeHard==True:
            
            if count_lives==1:
                pygame.freetype.Font('Assets//8bit16.ttf',30).render_to(win,(20,120),"you have finished the game with 1 life",black)
            if count_lives!=1:
                pygame.freetype.Font('Assets//8bit16.ttf',30).render_to(win,(20,120),"you have finished the game with "+str(count_lives)+" lives",black)

        if GameModeHard==False:
            if count_death==0:
                pygame.freetype.Font('Assets//8bit16.ttf',30).render_to(win,(235,130),"You haven't died once!",black)
            if count_death==1:
                pygame.freetype.Font('Assets//8bit16.ttf',30).render_to(win,(250,130),"You have died once!",black)
            if count_death!=0 and count_death!=1:
                pygame.freetype.Font('Assets//8bit16.ttf',30).render_to(win,(220,130),"You have died "+str(count_death)+" times",black)
                
                                
        if GotSeacret==True:
            pygame.freetype.Font('Assets//8bit16.ttf',30).render_to(win,(70,190),"you have colected the seacret item!",black)
        if GotSeacret==False:
            pygame.freetype.Font('Assets//8bit16.ttf',30).render_to(win,(20,180),"you have not collected the secret item",black)
            pygame.freetype.Font('Assets//8bit16.ttf',30).render_to(win,(220,220),"better luck next time",black)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 150+115>mouse[0]>150 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(150,342,115,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                pygame.quit()
        else:
            pygame.draw.rect(win,black,(150,342,115,40))

        if 600+265>mouse[0]>600 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(600,342,265,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)

                game_intro()
        else:
            pygame.draw.rect(win,black,(600,342,265,40))


        pygame.freetype.Font('Assets//8bit16.ttf',40).render_to(win,(150,350),"Quit",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',40).render_to(win,(600,350),"Main Menu",orange)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(fps_help)


def game_over_chp_123():
    
    global count_lives
    global LevelOneCleared
    global LevelTwoCleared
    global LevelThreeCleared
    global LevelFourCleared
    global LevelFiveCleared
    global LevelSixCleared
    global LevelSevenCleared
    global LevelEightCleared
    global LevelNineCleared
                
    

                
    global Ecat1col_1
    global Ecat2col_1
    global Ecat3col_1
    global Food1col_1
    global Food2col_1
    global Food3col_1
    global Portal_Perms_1
    global Portalcol_1
    global camOffx_1
    global camOffy_1

    global Ecat1col_2
    global Ecat2col_2
    global Ecat3col_2
    global Food1col_2
    global Food2col_2
    global Food3col_2
    global Portal_Perms_2
    global Portalcol_2
    global camOffx_2
    global camOffy_2

    global Ecat1col_3
    global Ecat2col_3
    global Ecat3col_3
    global Food1col_3
    global Food2col_3
    global Food3col_3
    global Portal_Perms_3
    global Portalcol_3
    global camOffx_3
    global camOffy_3
    
 
    pygame.mixer.music.stop()

    goc=True
    while goc:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        win.blit(bg2,(0,0))
        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(220,150),"Game Over!",black)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 100+135>mouse[0]>100 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(100,342,135,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                game_intro()
        else:
            pygame.draw.rect(win,black,(100,342,135,40))

        if 497+365>mouse[0]>497 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(497,342,365,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                count_lives=3
                
                LevelOneCleared=False
                LevelTwoCleared=False
                LevelThreeCleared=False #svi su false jer krece od 1 lvla 
                LevelFourCleared=False
                LevelFiveCleared=False
                LevelSixCleared=False
                LevelSevenCleared=False
                LevelEightCleared=False
                LevelNineCleared=False
                
                

                
                Ecat1col_1=False
                Ecat2col_1=False
                Ecat3col_1=False
                Food1col_1=False
                Food2col_1=False
                Food3col_1=False
                Portal_Perms_1=False
                Portalcol_1=False
                camOffx_1=-100
                camOffy_1=740

                Ecat1col_2=False
                Ecat2col_2=False
                Ecat3col_2=False
                Food1col_2=False
                Food2col_2=False
                Food3col_2=False
                Portal_Perms_2=False
                Portalcol_2=False
                camOffx_2=1640
                camOffy_2=-300

                Ecat1col_3=False
                Ecat2col_3=False
                Ecat3col_3=False
                Food1col_3=False
                Food2col_3=False
                Food3col_3=False
                Portal_Perms_3=False
                Portalcol_3=False
                camOffx_3=-350
                camOffy_3=-300

                main()

              #  LevelOneCompleted=true i 2 je true i sve na koje zelim su true, i onda main jer u mainu postoji petlja koja ih broji
              #  main()
                
        else:
            pygame.draw.rect(win,black,(497,342,365,40))


        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(100,350),"Main Menu",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(500,350),"return to the checkpoint",orange)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(fps_help)

def game_over_chp_456():

    global count_lives
    global LevelOneCleared
    global LevelTwoCleared
    global LevelThreeCleared
    global LevelFourCleared
    global LevelFiveCleared
    global LevelSixCleared
    global LevelSevenCleared
    global LevelEightCleared
    global LevelNineCleared
                
    global Ecat1col_1
    global Ecat2col_1
    global Ecat3col_1
    global Food1col_1
    global Food2col_1
    global Food3col_1
    global Portal_Perms_1
    global Portalcol_1
    global camOffx_1
    global camOffy_1

    global Ecat1col_2
    global Ecat2col_2
    global Ecat3col_2
    global Food1col_2
    global Food2col_2
    global Food3col_2
    global Portal_Perms_2
    global Portalcol_2
    global camOffx_2
    global camOffy_2

    global Ecat1col_3
    global Ecat2col_3
    global Ecat3col_3
    global Food1col_3
    global Food2col_3
    global Food3col_3
    global Portal_Perms_3
    global Portalcol_3
    global camOffx_3
    global camOffy_3    

                
    global Ecat1col_4
    global Ecat2col_4
    global Ecat3col_4
    global Food1col_4
    global Food2col_4
    global Food3col_4
    global Portal_Perms_4
    global Portalcol_4   
    global camOffx_4
    global camOffy_4

    global Ecat1col_5
    global Ecat2col_5
    global Ecat3col_5
    global Food1col_5
    global Food2col_5
    global Food3col_5
    global Portal_Perms_5
    global Portalcol_5
    global camOffx_5
    global camOffy_5

    global Ecat1col_6
    global Ecat2col_6
    global Ecat3col_6
    global Food1col_6
    global Food2col_6
    global Food3col_6
    global Portal_Perms_6
    global Portalcol_6
    global camOffx_6
    global camOffy_6
    
 
    pygame.mixer.music.stop()

    goc=True
    while goc:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        win.blit(bg2,(0,0))
        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(220,150),"Game Over!",black)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 100+135>mouse[0]>100 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(100,342,135,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                game_intro()
        else:
            pygame.draw.rect(win,black,(100,342,135,40))

        if 497+365>mouse[0]>497 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(497,342,365,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                count_lives=3
                
                LevelOneCleared=True
                LevelTwoCleared=True
                LevelThreeCleared=True#jer se respawna na 4 lvlu
                LevelFourCleared=False
                LevelFiveCleared=False
                LevelSixCleared=False
                LevelSevenCleared=False
                LevelEightCleared=False
                LevelNineCleared=False
                
                Ecat1col_1=False
                Ecat2col_1=False
                Ecat3col_1=False
                Food1col_1=False
                Food2col_1=False
                Food3col_1=False
                Portal_Perms_1=False
                Portalcol_1=False
                camOffx_1=-100
                camOffy_1=740

                Ecat1col_2=False
                Ecat2col_2=False
                Ecat3col_2=False
                Food1col_2=False
                Food2col_2=False
                Food3col_2=False
                Portal_Perms_2=False
                Portalcol_2=False
                camOffx_2=1640
                camOffy_2=-300

                Ecat1col_3=False
                Ecat2col_3=False
                Ecat3col_3=False
                Food1col_3=False
                Food2col_3=False
                Food3col_3=False
                Portal_Perms_3=False
                Portalcol_3=False
                camOffx_3=-350
                camOffy_3=-300
                

                
                Ecat1col_4=False
                Ecat2col_4=False
                Ecat3col_4=False
                Food1col_4=False
                Food2col_4=False
                Food3col_4=False
                Portal_Perms_4=False
                Portalcol_4=False
                camOffx_4=200
                camOffy_4=-300

                Ecat1col_5=False
                Ecat2col_5=False
                Ecat3col_5=False
                Food1col_5=False
                Food2col_5=False
                Food3col_5=False
                Portal_Perms_5=False
                Portalcol_5=False
                camOffx_5=1700
                camOffy_5=745

                Ecat1col_6=False
                Ecat2col_6=False
                Ecat3col_6=False
                Food1col_6=False
                Food2col_6=False
                Food3col_6=False
                Portal_Perms_6=False
                Portalcol_6=False
                camOffx_6=-350
                camOffy_6=750

                main()

              #  LevelOneCompleted=true i 2 je true i sve na koje zelim su true, i onda main jer u mainu postoji petlja koja ih broji
              #  main()
                
        else:
            pygame.draw.rect(win,black,(497,342,365,40))


        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(100,350),"Main Menu",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(500,350),"return to the checkpoint",orange)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(fps_help)



def game_over_chp_789():
    global count_lives
    global LevelOneCleared
    global LevelTwoCleared
    global LevelThreeCleared
    global LevelFourCleared
    global LevelFiveCleared
    global LevelSixCleared
    global LevelSevenCleared
    global LevelEightCleared
    global LevelNineCleared
    global GotSeacret

    global Ecat1col_1
    global Ecat2col_1
    global Ecat3col_1
    global Food1col_1
    global Food2col_1
    global Food3col_1
    global Portal_Perms_1
    global Portalcol_1
    global camOffx_1
    global camOffy_1

    global Ecat1col_2
    global Ecat2col_2
    global Ecat3col_2
    global Food1col_2
    global Food2col_2
    global Food3col_2
    global Portal_Perms_2
    global Portalcol_2
    global camOffx_2
    global camOffy_2


    global Ecat1col_3
    global Ecat2col_3
    global Ecat3col_3
    global Food1col_3
    global Food2col_3
    global Food3col_3
    global Portal_Perms_3
    global Portalcol_3
    global camOffx_3
    global camOffy_3

    global Ecat1col_4
    global Ecat2col_4
    global Ecat3col_4
    global Food1col_4
    global Food2col_4
    global Food3col_4
    global Portal_Perms_4
    global Portalcol_4
    global camOffx_4
    global camOffy_4


    global Ecat1col_5
    global Ecat2col_5
    global Ecat3col_5
    global Food1col_5
    global Food2col_5
    global Food3col_5
    global Portal_Perms_5
    global Portalcol_5
    global camOffx_5
    global camOffy_5

    global Ecat1col_6
    global Ecat2col_6
    global Ecat3col_6
    global Food1col_6
    global Food2col_6
    global Food3col_6
    global Portal_Perms_6
    global Portalcol_6
    global camOffx_6
    global camOffy_6

    global Ecat1col_7
    global Ecat2col_7
    global Ecat3col_7
    global Food1col_7
    global Food2col_7
    global Food3col_7
    global Portal_Perms_7
    global Portalcol_7
    global camOffx_7
    global camOffy_7

    global Ecat1col_8
    global Ecat2col_8
    global Ecat3col_8
    global Food1col_8
    global Food2col_8
    global Food3col_8
    global Portal_Perms_8
    global Portalcol_8
    global camOffx_8
    global camOffy_8

    global Ecat1col_9
    global Ecat2col_9
    global Ecat3col_9
    global Food1col_9
    global Food2col_9
    global Food3col_9
    global Portal_Perms_9
    global Portalcol_9
    global camOffx_9
    global camOffy_9

    pygame.mixer.music.stop()

    goc=True
    while goc:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        win.blit(bg2,(0,0))
        pygame.freetype.Font('Assets//8bit16.ttf',70).render_to(win,(220,150),"Game Over!",black)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 100+135>mouse[0]>100 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(100,342,135,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                game_intro()
        else:
            pygame.draw.rect(win,black,(100,342,135,40))

        if 497+365>mouse[0]>497 and 342+40>mouse[1]>342:
            pygame.draw.rect(win,gray,(497,342,365,40))
            if click[0]==1:
                if music_state==True:
                    
                    pygame.mixer.Sound.play(click_sound)
                count_lives=3
                
                LevelOneCleared=True
                LevelTwoCleared=True
                LevelThreeCleared=True
                LevelFourCleared=True
                LevelFiveCleared=True
                LevelSixCleared=True
                LevelSevenCleared=False#respawn an 7.
                LevelEightCleared=False
                LevelNineCleared=False
                
                Ecat1col_1=False
                Ecat2col_1=False
                Ecat3col_1=False
                Food1col_1=False
                Food2col_1=False
                Food3col_1=False
                Portal_Perms_1=False
                Portalcol_1=False
                camOffx_1=-100
                camOffy_1=740

                Ecat1col_2=False
                Ecat2col_2=False
                Ecat3col_2=False
                Food1col_2=False
                Food2col_2=False
                Food3col_2=False
                Portal_Perms_2=False
                Portalcol_2=False
                camOffx_2=1640
                camOffy_2=-300

                Ecat1col_3=False
                Ecat2col_3=False
                Ecat3col_3=False
                Food1col_3=False
                Food2col_3=False
                Food3col_3=False
                Portal_Perms_3=False
                Portalcol_3=False
                camOffx_3=-350
                camOffy_3=-300
                

                
                Ecat1col_4=False
                Ecat2col_4=False
                Ecat3col_4=False
                Food1col_4=False
                Food2col_4=False
                Food3col_4=False
                Portal_Perms_4=False
                Portalcol_4=False
                camOffx_4=200
                camOffy_4=-300

                Ecat1col_5=False
                Ecat2col_5=False
                Ecat3col_5=False
                Food1col_5=False
                Food2col_5=False
                Food3col_5=False
                Portal_Perms_5=False
                Portalcol_5=False
                camOffx_5=1700
                camOffy_5=745

                Ecat1col_6=False
                Ecat2col_6=False
                Ecat3col_6=False
                Food1col_6=False
                Food2col_6=False
                Food3col_6=False
                Portal_Perms_6=False
                Portalcol_6=False
                camOffx_6=-350
                camOffy_6=750

                Ecat1col_7=False
                Ecat2col_7=False
                Ecat3col_7=False
                Food1col_7=False
                Food2col_7=False
                Food3col_7=False
                Portal_Perms_7=False
                Portalcol_7=False
                camOffx_7=675        
                camOffy_7=-250

                Ecat1col_8=False
                Ecat2col_8=False
                Ecat3col_8=False
                Food1col_8=False
                Food2col_8=False
                Food3col_8=False
                Portal_Perms_8=False
                Portalcol_8=False
                camOffx_8=1540        
                camOffy_8=-250

                Ecat1col_9=False
                Ecat2col_9=False
                Ecat3col_9=False
                Food1col_9=False
                Food2col_9=False
                Food3col_9=False
                Portal_Perms_9=False
                Portalcol_9=False
                camOffx_9=-275        
                camOffy_9=-240 

                main()

              
                
        else:
            pygame.draw.rect(win,black,(497,342,365,40))


        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(100,350),"Main Menu",orange)
        pygame.freetype.Font('Assets//8bit16.ttf',20).render_to(win,(500,350),"return to the checkpoint",orange)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(fps_help)
    
    
def lvl_1(key,c_1):
    global count_death
    global GameModeHard
    global to_right_1
    global wc_1
    global pc_1
    global camOffx_1
    global camOffy_1
    global MS_U_1
    global MS_D_1
    global MS_L_1
    global MS_R_1
    global ect_1_1
    global ect_1_2
    global ect_1_3
    global Ecat1col_1
    global Ecat2col_1
    global Ecat3col_1
    global Food1col_1
    global Food2col_1
    global Food3col_1
    global Portal_Perms_1
    global Portalcol_1
    global LevelOneCleared
    global count_lives
    
    
     
   # global GameOver

    c_1.y=winH-cat_H-tile_size
        
    global music_state 
    
    world_1_data=[
        ['1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['1','fl4','fl1','fl4','fl1','fl4','1','0','0','0','0','0','0','0','0','0','0','fl2','fl2','0','fl2','fl2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['1','fl1','fl4','fl1','fl4','fl1','1','0','0','0','0','0','0','0','0','0','fl2','fl3','fl3','fl2','fl3','fl3','fl2','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0'],
        ['1','fl4','fl1','fl4','fl1','fl4','0','0','0','0','0','0','0','0','0','0','fl2','fl3','fl3','fl3','fl3','fl3','fl2','0','0','0','0','0','0','0','1','fl2','fl2','fl2','fl2','fl2','fl2','fl2','fl2','1','0','0','0','0','0'],
        ['1','fl1','fl4','fl1','fl4','fl1','0','h0','h0','0','0','0','0','0','0','0','0','fl2','fl3','fl3','fl3','fl2','0','0','0','0','0','0','0','0','1','fl2','fl3','0','0','0','0','fl3','fl2','1','0','0','0','0','0'],
        ['1','fl4','fl1','fl4','fl1','fl4','0','h0','h0','0','0','0','0','0','0','0','0','0','fl2','fl3','fl2','0','0','0','0','0','0','0','0','0','1','fl2','fl3','0','p','0','0','fl3','fl2','1','0','0','0','0','0'],
        ['1','fl1','fl4','fl1','fl4','fl1','0','0','h0','0','0','0','0','0','0','0','0','0','0','fl2','0','0','0','0','0','0','0','0','0','0','1','fl2','fl3','0','0','0','0','fl3','fl2','1','0','0','0','0','0'],
        ['1','fl4','fl1','fl4','fl1','fl4','1','0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','0','0','1','fl2','fl2','0','0','0','0','fl2','fl2','1','0','0','0','0','0'],
        ['1','fl1','fl4','fl1','fl4','fl1','1','0','h0','0','0','0','0','0','0','0','h0','h0','0','h0','h0','h0','h0','h0','0','0','0','0','0','0','1','1','1','fl4','fl4','fl4','fl4','1','1','1','0','0','0','0','0'],
        ['1','1','1','1','1','1','1','0','h0','h0','0','0','1','1','1','4','0','5','0','1','1','1','0','0','h0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','h0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','h0','0','0','0','1','1','0','0','1','1','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h0','0','0','1','0','0','0','0','f2','0','0','0','1','0','0','0','h0','0','0','0','1','fl2','fl3','fl2','fl3','1','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','0','h0','0','0','1','fl3','fl2','fl3','fl2','1','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h0','0','0','1','1','1','1','1','1','1','1','1','1','0','0','0','0','h0','0','0','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','h0','h0','0','0','0','0','0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','h0','0','0','0','0','1','1','1','2','0','3','0','1','1','1','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','h0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h0','h0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','h0','0','0','0','7','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h0','0','0','0','0','0','0','1','0','0','0','0','f1','0','0','0','1','0','0','0','0','0','0','0','0','6','0','f3','8','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','0','0','0','0','0','0','0','0','0','0','0']]
            
            
    win.blit(bg,(0,0))
    tile_rects_lvl_1=[]
    ec_lvl_1=[]
    food_lvl_1=[]
    portal_lvl_1=[]
        
    y_1=0
    for row in world_1_data:
        x_1=0
        for tile in row:
            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))   #flowers/misc render
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))

            if tile=='h0':
                win.blit(path0,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                    




                
            if tile=='1':
                win.blit(tile1,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                tile_rects_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size)) #walls

            if tile=='f1' and Food1col_1==False :
                win.blit(food1,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                food_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))
            if tile=='f2' and Food2col_1==False :
                win.blit(food1,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                food_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))#food
            if tile=='f3' and Food3col_1==False :
                win.blit(food1,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                food_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))
                    

            if tile=='p' and pc_1<=8:
                win.blit(portal,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                portal_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))

            if tile=='p' and 8<pc_1<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                portal_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))#portal
                    
            if tile=='p' and 16<pc_1<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                portal_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))

            if tile=='p' and 24<pc_1:
                win.blit(portal_3,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                portal_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))
                
                    
                    
            if tile=='2' and  ect_1_1<=60 and Ecat1col_1==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                ec_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size)) #evil catto #1 lvl 1
            if tile=='3' and  ect_1_1>60 and Ecat1col_1==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                ec_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))

                    

            if tile=='4' and  ect_1_2<=60 and Ecat2col_1==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                ec_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))  #evil catto #2 lvl 1
            if tile=='5' and  ect_1_2>60 and Ecat2col_1==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                ec_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))


                    

            if tile=='6' and  ect_1_3<=45 and Ecat3col_1==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                ec_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))
            if tile=='7' and  90>ect_1_3>45 and Ecat3col_1==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                ec_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))  #evil catto #3 lvl 1
            if tile=='8' and  ect_1_3>90 and Ecat3col_1==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1))
                ec_lvl_1.append(pygame.Rect(x_1*tile_size-camOffx_1,y_1*tile_size-camOffy_1,tile_size,tile_size))

                    
                
                
               
                    
            x_1=x_1+1
        y_1=y_1+1


    if wc_1+1>9:
        wc_1=1
    if ect_1_1+1>120:
        ect_1_1=1
    if ect_1_2+1>120:
        ect_1_2=1
    if ect_1_3+1>135:
        ect_1_3=1
    if pc_1+1>32:
        pc_1=1

               

           

    if to_right_1==True and (wc_1==1 or wc_1==2 or wc_1==3):
        win.blit(catto1R,(c_1.x,winH-cat_H-tile_size))

    if to_right_1==True and (wc_1==4 or wc_1==5 or wc_1==6):
        win.blit(catto2R,(c_1.x,winH-cat_H-tile_size))

    if to_right_1==True and (wc_1==7 or wc_1==8 or wc_1==9):
        win.blit(catto3R,(c_1.x,winH-cat_H-tile_size))


            


    if to_right_1==False and (wc_1==1 or wc_1==2 or wc_1==3):
        win.blit(catto1L,(c_1.x,winH-cat_H-tile_size))

    if to_right_1==False and (wc_1==4 or wc_1==5 or wc_1==6):
        win.blit(catto2L,(c_1.x,winH-cat_H-tile_size))
            
    if to_right_1==False and (wc_1==7 or wc_1==8 or wc_1==9):
        win.blit(catto3L,(c_1.x,winH-cat_H-tile_size))

    hit_list = []
    for i in tile_rects_lvl_1:
        if c_1.colliderect(i):
            hit_list.append(i)

                
          

       # if hit_list != []:
         #   print(hit_list[0][0],hit_list[0][1],MS_U_1)




       
        
    #c_1.left =418 c_1.right=482
            
    #c_1.top=386, c_1.bottom=450

    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    #moving up radi
                MS_U_1=False   
            #else:
              #  MS_U_1=True 

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  #moving down kada se suadri dolje ne moze ici desno 440
                MS_D_1=False
           
            #else:
             #   MS_D_1=True
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:# radi
                MS_L_1=False
               
            #else:
             #   MS_L_1=True
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:#475
                MS_R_1=False
               
                
            #else:
              # MS_R_1=True
        
                
    if hit_list == []:
        MS_U_1=True
        MS_D_1=True
        MS_L_1=True
        MS_R_1=True
    L=[MS_U_1,MS_D_1,MS_L_1,MS_R_1]
    if L==[False,False,False,False]:
        MS_U_1=True

    if L==[False,False,False,True]:
        MS_D_1=True

    if L==[False,False,True,False]:
        MS_D_1=True
 
    
    #print(MS_U_1,MS_D_1,MS_L_1,MS_R_1)
    


    ect_1_1+=1
    ect_1_2+=1
    ect_1_3+=1
    pc_1+=1
                    

    if key[pygame.K_LEFT]  and MS_L_1==True:#and camOffx_1-velx+winW/2>0
        wc_1=wc_1+1
        to_right_1=False
        camOffx_1=camOffx_1-velx
    if key[pygame.K_RIGHT] and MS_R_1==True: #and camOffx_1+velx+winW/2<45*tile_size
        wc_1=wc_1+1
        to_right_1=True
        camOffx_1=camOffx_1+velx
    if key[pygame.K_DOWN] and MS_D_1==True:
        wc_1+=1
        camOffy_1=camOffy_1+vely
    if key[pygame.K_UP] and MS_U_1==True:
        wc_1+=1
        camOffy_1=camOffy_1-vely
        

##    pygame.draw.rect(win,white,c_1,2)
##    for i in hit_list:
##        pygame.draw.rect(win,red,i,2)
##   
##    for i in tile_rects_lvl_1:                  #HITBOXES
##        pygame.draw.rect(win,orange,i,2)
##    for i in hit_list:
##        pygame.draw.rect(win,red,i,2)
##            
    ec_hit_list = []
    for i in ec_lvl_1:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
        
    if ec_hit_list != []:
        if 90>ec_hit_list[0][0]-camOffx_1>-90 and -20>ec_hit_list[0][1]-camOffy_1>-220:
            Ecat1col_1=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
                
        if 90>ec_hit_list[0][0]-camOffx_1>-90 and  430>ec_hit_list[0][1]-camOffy_1>240:
            Ecat2col_1=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
           
        if -550>ec_hit_list[0][0]-camOffx_1>-900  and -160>ec_hit_list[0][1]-camOffy_1>-410:
            Ecat3col_1=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
               
            


    food_hit_list = []
    for i in food_lvl_1:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:

        if 100>food_hit_list[0][0]-camOffx_1>-60 and -210>food_hit_list[0][1]-camOffy_1>-290:
            Food1col_1=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
                
        if 100>food_hit_list[0][0]-camOffx_1>-90 and 240>food_hit_list[0][1]-camOffy_1>90:
            Food2col_1=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)

        if -640>food_hit_list[0][0]-camOffx_1>-820 and -210>food_hit_list[0][1]-camOffy_1>-320:
            Food3col_1=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
           # print(food_hit_list[0][0]-camOffx_1,food_hit_list[0][1]-camOffy_1)
            
       
            
          

    COL_STATES_lives=[Ecat1col_1,Ecat2col_1,Ecat3col_1]
    count_lives_1=count_lives
    for i in COL_STATES_lives:
        if i==True:
            count_lives_1-=1
       # print(count_lives)
    if count_lives_1==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_123()
        
      
    if count_lives_1==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_1==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_1==1:
        win.blit(heart,(418,380))

        
    portal_hit_list = []
    for i in portal_lvl_1:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_1==True:
        LevelOneCleared=True
        count_lives=count_lives_1
        if music_state==True:
            pygame.mixer.Sound.play(portal_sound)
       

    COL_STATES_food=[Food1col_1,Food2col_1,Food3col_1]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1: 
        win.blit(foodIcon1,(418,372)) 
    if count_food==2 :
        win.blit(foodIcon1,(418,372))
        win.blit(foodIcon1,(438,372))
    if count_food==3 :
        win.blit(foodIcon1,(418,372))
        win.blit(foodIcon1,(438,372))
        win.blit(foodIcon1,(458,372))
        Portal_Perms_1=True
    if Portal_Perms_1==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_1==True: 
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal",black)
            
            
            
              
    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 1",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 1 - checkpoint level 1",black)
        
            
            
    pygame.display.update()
def lvl_2(key,c_1):
    global count_death
    global GameModeHard
    global to_right_2
    global MS_U_2
    global MS_D_2
    global MS_L_2
    global MS_R_2
    global wc_2
    global pc_2
    global ect_2_1
    global ect_2_2
    global ect_2_3
    global Ecat1col_2
    global Ecat2col_2
    global Ecat3col_2
    global Food1col_2
    global Food2col_2
    global Food3col_2
    global Portal_Perms_2
    global Portalcol_2
    global LevelTwoCleared
    global camOffx_2
    global camOffy_2
    
    global count_lives 
  
    c_1.y=winH-cat_H-tile_size
   # global GameOver
    global music_state     
    world_2_data=[
        ['0','3','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','fl5','fl5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','h0','h0','0','0','0','0','0','0','0','0','0','0','0','fl5','fl2','fl2','fl5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','1','2','0','1','0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','fl5','fl2','fl2','fl5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','h0','h0','0','0','0'],
        ['0','0','1','0','0','1','0','0','0','0','h0','0','0','0','0','0','0','0','0','fl5','fl2','fl2','fl5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','h0','0','0','0','0','0'],
        ['0','0','1','0','0','1','0','0','0','0','h0','h0','h0','0','0','0','0','0','0','fl5','fl2','fl2','fl5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0'],
        ['1','1','1','0','0','1','1','1','0','0','0','0','h0','0','0','0','0','0','0','0','fl5','fl5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0','1','0','0','0','0','h0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0','1','0','0','0','0','h0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0'],
        ['1','0','0','f1','0','0','0','1','0','0','0','0','h0','h0','0','0','1','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0','1','0','0','0','0','0','h0','0','0','1','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0'],
        ['1','1','1','1','1','1','1','1','0','0','0','h0','h0','h0','0','0','1','0','0','1','1','1','1','6','0','7','0','1','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0'],
        ['0','0','fl7','fl6','fl6','fl7','0','0','0','0','0','h0','0','0','0','0','1','0','0','1','0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0'],
        ['0','0','fl6','fl6','fl6','fl6','0','0','0','0','0','h0','0','0','0','0','1','4','0','1','0','0','1','0','0','0','0','1','0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','0'],
        ['0','0','fl6','fl6','fl6','fl6','h0','h0','h0','h0','h0','h0','0','0','0','5','0','0','0','0','0','0','1','0','f2','0','0','1','0','h0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0'],
        ['0','0','fl7','fl6','fl6','fl7','0','0','0','0','h0','0','0','0','0','0','0','0','h0','0','0','0','1','0','0','0','0','1','0','0','h0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','h0','h0','0','0','0','0','0','0','h0','0','0','1','1','1','1','1','1','0','0','0','h0','0','1','1','1','1','1','0','h0','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1','1','1','0','0','h0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','h0','0','1','fl5','fl2','fl5','1','0','h0','1','fl7','fl6','fl7','1'],
        ['1','fl5','fl6','0','0','0','0','fl5','fl6','1','0','0','h0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','h0','h0','h0','h0','0','1','fl2','fl5','fl2','1','0','h0','1','fl6','fl7','fl6','1'],
        ['1','fl6','fl5','0','p','0','0','fl6','fl5','1','0','0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','h0','h0','h0','0','0','0','0','0','1','fl5','fl2','fl5','0','0','h0','0','fl7','fl6','fl7','1'],
        ['1','fl5','fl6','0','0','0','0','fl5','fl6','1','0','0','h0','0','0','0','0','0','0','0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','1','fl2','fl5','fl2','0','0','h0','0','fl6','fl7','fl6','1'],
        ['1','fl6','fl5','0','0','0','0','fl6','fl5','1','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl5','fl2','fl5','0','0','0','0','fl7','fl6','fl7','1'],
        ['1','fl5','fl6','0','0','0','0','fl5','fl6','1','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','f3','fl5','fl2','0','0','0','0','fl6','fl7','fl6','1'],
        ['1','1','1','0','0','0','0','1','1','1','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl5','fl2','fl5','1','0','0','1','fl7','fl6','fl7','1'],
        ['0','0','0','0','0','0','fl7','fl7','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl2','fl5','fl2','1','0','0','1','fl6','fl7','fl6','1'],
        ['0','0','0','0','0','0','fl7','fl7','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','0','0','1','1','1','1','1']]

    win.blit(bg,(0,0))
    tile_rects_lvl_2=[]
    food_lvl_2=[]
    ec_lvl_2=[]
    portal_lvl_2=[]
    y_1=0
    for row in world_2_data:
        x_1=0
        for tile in row:

            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))   #flowers/misc render
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))

                        
            if tile=='fl5':
                win.blit(flower5,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))

                        
            if tile=='fl6':
                win.blit(flower6,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))

                        
            if tile=='fl7':
                win.blit(flower7,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))

            if tile=='h0':
                win.blit(path0,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                    





            


            
            if tile=='1':
                win.blit(tile1,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                tile_rects_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))

                
            if tile=='f1' and Food1col_2==False :
                win.blit(food1,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                food_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))
            if tile=='f2' and Food2col_2==False :
                win.blit(food1,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                food_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))
            if tile=='f3' and Food3col_2==False :
                win.blit(food1,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                food_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))


            if tile=='p' and pc_2<=8:
                win.blit(portal,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                portal_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))

            if tile=='p' and 8<pc_2<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                portal_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))
                
            if tile=='p' and 16<pc_2<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                portal_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))

            if tile=='p' and 24<pc_2:
                win.blit(portal_3,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                portal_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))




            if tile=='2' and  ect_2_1<=45 and Ecat1col_2==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                ec_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size)) #1st catto evil
            if tile=='3' and  ect_2_1>45 and Ecat1col_2==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                ec_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))



            
            if tile=='4' and  ect_2_2<=45 and Ecat2col_2==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                ec_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size)) #2nd catto evil
            if tile=='5' and  ect_2_2>45 and Ecat2col_2==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                ec_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))


            if tile=='6' and  ect_2_3<=60 and Ecat3col_2==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                ec_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size)) #3rd catto evil
            if tile=='7' and  ect_2_3>60 and Ecat3col_2==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2))
                ec_lvl_2.append(pygame.Rect(x_1*tile_size-camOffx_2,y_1*tile_size-camOffy_2,tile_size,tile_size))



            
            
            x_1=x_1+1
        y_1=y_1+1

    if pc_2+1>32:
        pc_2=1

    if ect_2_1+1>135:
        ect_2_1=1
    if ect_2_2+1>135:
        ect_2_2=1
    if ect_2_3+1>120:
        ect_2_3=1


    if wc_2+1>9:
        wc_2=1


       

    if to_right_2==True and (wc_2==1 or wc_2==2 or wc_2==3):
        win.blit(catto1R,(c_1.x,c_1.y))

    if to_right_2==True and (wc_2==4 or wc_2==5 or wc_2==6):
        win.blit(catto2R,(c_1.x,c_1.y))

    if to_right_2==True and (wc_2==7 or wc_2==8 or wc_2==9):
        win.blit(catto3R,(c_1.x,c_1.y))


        


    if to_right_2==False and (wc_2==1 or wc_2==2 or wc_2==3):
        win.blit(catto1L,(c_1.x,c_1.y))

    if to_right_2==False and (wc_2==4 or wc_2==5 or wc_2==6):
        win.blit(catto2L,(c_1.x,c_1.y))
        
    if to_right_2==False and (wc_2==7 or wc_2==8 or wc_2==9):
        win.blit(catto3L,(c_1.x,c_1.y))

    hit_list = []
    for i in tile_rects_lvl_2:
        if c_1.colliderect(i):
            hit_list.append(i)


    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    
                MS_U_2=False   
            
              

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  
                MS_D_2=False
           
            
             
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:
                MS_L_2=False
               
            
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:
                MS_R_2=False
               
                
                
    if hit_list == []:
        MS_U_2=True
        MS_D_2=True
        MS_L_2=True
        MS_R_2=True
    L=[MS_U_2,MS_D_2,MS_L_2,MS_R_2]
    if L==[False,False,False,False]:
        MS_U_2=True
    if L==[False,False,False,True]:
        MS_D_2=True
    if L==[False,False,True,False]:
        MS_D_2=True


    #ect_2_1    
    #ect_2_2
    #...
    pc_2+=1
    ect_2_1+=1
    ect_2_2+=1
    ect_2_3+=1

    
    if key[pygame.K_LEFT] and camOffx_2-velx+winW/2>0 and MS_L_2==True:
        wc_2=wc_2+1
        to_right_2=False
        camOffx_2=camOffx_2-velx
    if key[pygame.K_RIGHT] and camOffx_2+velx+winW/2<45*tile_size and MS_R_2==True:
        wc_2=wc_2+1
        to_right_2=True
        camOffx_2=camOffx_2+velx
    if key[pygame.K_DOWN] and MS_D_2==True:
        wc_2+=1
        camOffy_2=camOffy_2+vely
    if key[pygame.K_UP] and MS_U_2==True:
        wc_2+=1
        camOffy_2=camOffy_2-vely






    ec_hit_list = []
    for i in ec_lvl_2:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
    
    if ec_hit_list != []:
        if 900>ec_hit_list[0][0]-camOffx_2>700 and 860>ec_hit_list[0][1]-camOffy_2>690:
            Ecat1col_2=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
                
        if 690>ec_hit_list[0][0]-camOffx_2>610 and 760>ec_hit_list[0][1]-camOffy_2>590:
            Ecat1col_2=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
        if 200>ec_hit_list[0][0]-camOffx_2>-10 and 130>ec_hit_list[0][1]-camOffy_2>30:
            Ecat2col_2=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)    
        if -10>ec_hit_list[0][0]-camOffx_2>-90 and 270>ec_hit_list[0][1]-camOffy_2>80:
            Ecat2col_2=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)    

        if -310>ec_hit_list[0][0]-camOffx_2>-490 and 350>ec_hit_list[0][1]-camOffy_2>200:
            Ecat3col_2=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

            




      #  print(ec_hit_list[0][0]-camOffx_2,ec_hit_list[0][1]-camOffy_2)




    food_hit_list = []
    for i in food_lvl_2:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:
        if 800>food_hit_list[0][0]-camOffx_2>620 and 490>food_hit_list[0][1]-camOffy_2>350:
            Food1col_2=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -260>food_hit_list[0][0]-camOffx_2>-420 and 240>food_hit_list[0][1]-camOffy_2>90:
            Food2col_2=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)    
        if -860>food_hit_list[0][0]-camOffx_2>-930 and -170>food_hit_list[0][1]-camOffy_2>-330:
            Food3col_2=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)    
        #print(food_hit_list[0][0]-camOffx_2,food_hit_list[0][1]-camOffy_2)


    
      




    COL_STATES_lives=[Ecat1col_2,Ecat2col_2,Ecat3col_2]
    count_lives_2=count_lives
    for i in COL_STATES_lives:
        if i==True:
            count_lives_2-=1
    if count_lives_2==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_123()
       
    if count_lives_2==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_2==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_2==1:
        win.blit(heart,(418,380))
     
    portal_hit_list = []
    for i in portal_lvl_2:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_2==True:
        LevelTwoCleared=True
        count_lives=count_lives_2
        if music_state==True:
            pygame.mixer.Sound.play(portal_sound)

        

    COL_STATES_food=[Food1col_2,Food2col_2,Food3col_2]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1:
        win.blit(foodIcon1,(418,372)) 
    if count_food==2:
        win.blit(foodIcon1,(418,372))
        win.blit(foodIcon1,(438,372))
    if count_food==3:
        win.blit(foodIcon1,(418,372))
        win.blit(foodIcon1,(438,372))
        win.blit(foodIcon1,(458,372))
        Portal_Perms_2=True
    if Portal_Perms_2==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_2==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal",black)
       
       

    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 2",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 2 - checkpoint level 1",black)    


    
    pygame.display.update()    





def lvl_3(key,c_1):
    global count_death
    global GameModeHard
    global to_right_3
    global MS_U_3
    global MS_D_3
    global MS_L_3
    global MS_R_3
    global wc_3
    global pc_3
    global ect_3_1
    global ect_3_2
    global ect_3_3
    global Ecat1col_3
    global Ecat2col_3
    global Ecat3col_3
    global Food1col_3
    global Food2col_3
    global Food3col_3
    global Portal_Perms_3
    global Portalcol_3
    global LevelThreeCleared
    global camOffx_3
    global camOffy_3

    global count_lives 
  
    c_1.y=winH-cat_H-tile_size
    #global GameOver
    global music_state
    world_3_data=[
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','0','0','0','0','0','0','0','0','0','0','0','0','0','fl7','fl7','0','0','0','0','0'],
        ['0','0','0','h0','0','0','0','0','0','0','0','0','fl6','fl7','fl6','fl6','0','0','0','0','0','0','0','0','0','0','0','h0','h0','h0','0','0','0','0','0','0','0','0','0','fl5','0','0','0','0','0'],
        ['0','0','0','h0','0','0','0','0','0','0','0','fl7','fl7','fl6','0','0','0','0','0','0','0','0','0','0','1','2','0','1','0','0','h0','h0','h0','0','0','0','0','0','0','0','fl5','p','0','0','0'],
        ['0','0','0','0','h0','0','0','fl6','fl7','fl7','fl7','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','1','0','0','0','0','h0','0','0','0','0','0','0','0','fl7','0','0','0','0'],
        ['0','0','fl6','fl6','fl7','fl7','fl7','fl7','fl6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','1','0','0','0','0','h0','0','0','0','0','0','0','0','0','fl7','0','0','0'],
        ['fl7','fl7','fl7','fl7','fl6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','0','0','1','1','1','0','0','0','h0','0','0','0','0','0','0','0','fl7','0','0','0'],
        ['fl7','fl6','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl6','fl6','fl6','fl6','fl6','1','0','0','0','h0','0','0','0','0','0','0','0','0','fl7','0','0'],
        ['0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl6','f1','fl6','fl6','fl6','1','0','0','0','0','h0','0','0','0','0','0','0','0','0','fl7','0'],
        ['0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl6','fl6','fl6','fl6','fl6','1','0','0','0','0','h0','0','0','0','0','0','0','0','0','fl7','0'],
        ['0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','fl7'],
        ['0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','1','fl5','fl1','fl5','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','1','fl1','fl5','fl1','1','0','0','0','0','0','0','h0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','1','fl5','fl1','fl5','0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','1','fl1','fl5','fl1','0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','h0','h0','h0','0','0','0','0','0','1','fl5','fl1','fl5','0','h0','h0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','1','fl1','fl5','fl1','0','0','0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
        ['0','0','0','0','0','0','0','0','0','0','h0','h0','0','0','0','1','fl5','fl1','fl5','1','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['1','1','1','1','1','1','1','1','1','1','0','h0','0','0','0','1','fl1','fl5','fl1','1','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['1','0','0','0','0','0','0','0','0','1','0','h0','0','0','0','1','1','1','1','1','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','1','0','0','0','f3','0','0','0','0','1'],
        ['1','0','0','0','f2','0','0','0','0','1','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['1','0','0','0','0','0','0','0','0','1','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','h0','h0','h0','h0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['1','1','1','4','0','5','0','1','1','1','0','h0','0','0','0','0','0','0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','h0','h0','h0','0','0','0','1','1','1','6','0','7','0','1','1','1'],
        ['0','0','0','0','0','0','0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0']]

    win.blit(bg,(0,0))
    tile_rects_lvl_3=[]
    food_lvl_3=[]
    ec_lvl_3=[]
    portal_lvl_3=[]
    y_1=0
    for row in world_3_data:
        x_1=0
        for tile in row:
            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))   
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))

                        
            if tile=='fl5':
                win.blit(flower5,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))

                        
            if tile=='fl6':
                win.blit(flower6,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))

                        
            if tile=='fl7':
                win.blit(flower7,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))

            if tile=='h0':
                win.blit(path0,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))

           









            
            if tile=='1':
                win.blit(tile1,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                tile_rects_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))






            if tile=='f1' and Food1col_3==False :
                win.blit(food1,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                food_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))
            if tile=='f2' and Food2col_3==False :
                win.blit(food1,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                food_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))
            if tile=='f3' and Food3col_3==False :
                win.blit(food1,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                food_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))




            
            if tile=='p' and pc_3<=8:
                win.blit(portal,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                portal_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))

            if tile=='p' and 8<pc_3<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                portal_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))
                
            if tile=='p' and 16<pc_3<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                portal_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))

            if tile=='p' and 24<pc_3:
                win.blit(portal_3,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                portal_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))








            if tile=='2' and  ect_3_1<=60 and Ecat1col_3==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                ec_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size)) #1st catto evil
            if tile=='3' and  ect_3_1>60 and Ecat1col_3==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                ec_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))



            if tile=='4' and  ect_3_2<=60 and Ecat2col_3==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                ec_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size)) #1st catto evil
            if tile=='5' and  ect_3_2>60 and Ecat2col_3==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                ec_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))

            if tile=='6' and  ect_3_3<=60 and Ecat3col_3==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                ec_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size)) #1st catto evil
            if tile=='7' and  ect_3_3>60 and Ecat3col_3==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3))
                ec_lvl_3.append(pygame.Rect(x_1*tile_size-camOffx_3,y_1*tile_size-camOffy_3,tile_size,tile_size))


            
                    








                
            x_1=x_1+1
        y_1=y_1+1

    if pc_3+1>32:
        pc_3=1
        
    if ect_3_1+1>120:
        ect_3_1=1

    if ect_3_2+1>120:
        ect_3_2=1

    if ect_3_3+1>120:
        ect_3_3=1




    if wc_3+1>9:
        wc_3=1


       

    if to_right_3==True and (wc_3==1 or wc_3==2 or wc_3==3):
        win.blit(catto1R,(c_1.x,c_1.y))

    if to_right_3==True and (wc_3==4 or wc_3==5 or wc_3==6):
        win.blit(catto2R,(c_1.x,c_1.y))

    if to_right_3==True and (wc_3==7 or wc_3==8 or wc_3==9):
        win.blit(catto3R,(c_1.x,c_1.y))


        


    if to_right_3==False and (wc_3==1 or wc_3==2 or wc_3==3):
        win.blit(catto1L,(c_1.x,c_1.y))

    if to_right_3==False and (wc_3==4 or wc_3==5 or wc_3==6):
        win.blit(catto2L,(c_1.x,c_1.y))
        
    if to_right_3==False and (wc_3==7 or wc_3==8 or wc_3==9):
        win.blit(catto3L,(c_1.x,c_1.y))

    hit_list = []
    for i in tile_rects_lvl_3:
        if c_1.colliderect(i):
            hit_list.append(i)



    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    
                MS_U_3=False   
            
              

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  
                MS_D_3=False
           
            
             
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:
                MS_L_3=False
               
            
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:
                MS_R_3=False
               
                
                
    if hit_list == []:
        MS_U_3=True
        MS_D_3=True
        MS_L_3=True
        MS_R_3=True
    L=[MS_U_3,MS_D_3,MS_L_3,MS_R_3]
    if L==[False,False,False,False]:
        MS_U_3=True
    if L==[False,False,False,True]:
        MS_D_3=True
    if L==[False,False,True,False]:
        MS_D_3=True

    
    #ect_2_1    
    #ect_2_2
    #...
    ect_3_1+=1
    ect_3_2+=1
    ect_3_3+=1
    pc_3+=1

        
    if key[pygame.K_LEFT] and camOffx_3-velx+winW/2>0 and MS_L_3==True:
        wc_3=wc_3+1
        to_right_3=False
        camOffx_3=camOffx_3-velx
    if key[pygame.K_RIGHT] and camOffx_3+velx+winW/2<45*tile_size and MS_R_3==True:
        wc_3=wc_3+1
        to_right_3=True
        camOffx_3=camOffx_3+velx
    if key[pygame.K_DOWN] and MS_D_3==True:
        wc_3+=1
        camOffy_3=camOffy_3+vely
    if key[pygame.K_UP] and MS_U_3==True:
        wc_3+=1
        camOffy_3=camOffy_3-vely




    ec_hit_list = []
    for i in ec_lvl_3:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
    
    if ec_hit_list != []:
        if -250>ec_hit_list[0][0]-camOffx_3>-460 and 820>ec_hit_list[0][1]-camOffy_3>640:
            Ecat1col_3=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
        if -410>ec_hit_list[0][0]-camOffx_3>-490 and 710>ec_hit_list[0][1]-camOffy_3>530:
            Ecat1col_3=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)


        if 690>ec_hit_list[0][0]-camOffx_3>510 and -290>ec_hit_list[0][1]-camOffy_3>-470:
            Ecat2col_3=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        if -1060>ec_hit_list[0][0]-camOffx_3>-1240 and -290>ec_hit_list[0][1]-camOffy_3>-470:
            Ecat3col_3=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
            
       # print(ec_hit_list[0][0]-camOffx_3,ec_hit_list[0][1]-camOffy_3)



    food_hit_list = []
    for i in food_lvl_3:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:
        if -290>food_hit_list[0][0]-camOffx_3>-470 and 490>food_hit_list[0][1]-camOffy_3>330:
            Food1col_3=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if 760>food_hit_list[0][0]-camOffx_3>580 and -170>food_hit_list[0][1]-camOffy_3>-320:
            Food2col_3=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -990>food_hit_list[0][0]-camOffx_3>-1170 and -110>food_hit_list[0][1]-camOffy_3>-270:
            Food3col_3=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
       # print(food_hit_list[0][0]-camOffx_3,food_hit_list[0][1]-camOffy_3)



    
             

    COL_STATES_lives=[Ecat1col_3,Ecat2col_3,Ecat3col_3]
    count_lives_3=count_lives 
    for i in COL_STATES_lives:
        if i==True:
            count_lives_3-=1
    if count_lives_3==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_123()
        
        
    if count_lives_3==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_3==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_3==1:
        win.blit(heart,(418,380))
    

    portal_hit_list = []
    for i in portal_lvl_3:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_3==True:
        LevelThreeCleared=True
        count_lives=count_lives_3
        if music_state==True:
                pygame.mixer.Sound.play(portal_sound)


    COL_STATES_food=[Food1col_3,Food2col_3,Food3col_3]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1:
        win.blit(foodIcon1,(418,372)) 
    if count_food==2:
        win.blit(foodIcon1,(418,372))
        win.blit(foodIcon1,(438,372))
    if count_food==3:
        win.blit(foodIcon1,(418,372))
        win.blit(foodIcon1,(438,372))
        win.blit(foodIcon1,(458,372))
        Portal_Perms_3=True
    if Portal_Perms_3==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_3==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal",black)
       
       
    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 3",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 3 - checkpoint level 1",black)




        


      

    pygame.display.update()



def lvl_4(key,c_1):
    global count_death
    global GameModeHard
    global to_right_4
    global MS_U_4
    global MS_D_4
    global MS_L_4
    global MS_R_4
    global wc_4
    global pc_4
    global ect_4_1
    global ect_4_2
    global ect_4_3
    global Ecat1col_4
    global Ecat2col_4
    global Ecat3col_4
    global Food1col_4
    global Food2col_4
    global Food3col_4
    global Portal_Perms_4
    global Portalcol_4
    global LevelFourCleared
    global camOffx_4 
    global camOffy_4

    global count_lives 
    c_1.y=winH-cat_H-tile_size

    #global GameOver
    global music_state


    world_4_data=[
        ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','fl2','fl2','fl2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['1','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','fl2','fl2','fl2','fl2','fl2','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
        ['1','0','0','0','0','0','0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','fl2','fl2','fl2','fl2','fl2','fl2','fl2','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['1','0','0','0','1','1','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','fl2','fl2','fl2','fl2','fl2','fl2','fl2','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['1','0','f1','0','1','0','3','0','0','0','0','h0','0','0','0','0','0','0','0','0','fl2','fl2','fl2','fl2','fl2','fl2','fl2','0','0','0','0','0','0','0','0','1','0','0','0','f3','0','0','0','0','1'],
        ['1','0','0','0','1','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','fl2','fl2','fl2','fl2','fl2','0','0','0','0','0','0','0','0','0','1','fl7','fl7','0','0','0','0','0','0','1'],
        ['1','0','0','0','1','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','fl2','fl2','fl2','0','0','0','0','0','0','0','0','0','0','1','fl7','fl7','0','0','0','0','0','0','1'],
        ['1','1','1','1','1','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['0','0','0','0','0','0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0','1'],
        ['0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','1'],
        ['0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','h0','0','0','0','0','0','0','0','0','1','0','0','1'],
        ['0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','h0','h0','h0','0','0','0','0','0','0','1','0','0','1'],
        ['0','0','0','0','0','h0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','5','0','0','h0','0','0','0','0','0','0','0','h0','h0','0','0','0','0','0','1','0','0','1'],
        ['0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','h0','h0','h0','0','0','1','0','0','1'],
        ['0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','0','1','4','0','1','0','1','1','1','1','0','0','0','0','0','h0','0','0','1','6','0','1'],
        ['0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl5','fl6','1','0','1','0','0','1','0','1','fl5','fl6','1','0','0','0','0','0','h0','0','0','0','0','0','7'],
        ['0','0','0','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl5','1','0','1','0','0','1','0','1','fl6','fl5','1','0','0','0','0','0','h0','h0','h0','0','0','0','0'],
        ['fl3','fl3','fl3','0','0','h0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl5','fl6','1','0','1','0','0','1','0','1','f2','fl6','1','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','fl3','fl3','fl3','fl3','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl5','1','1','1','0','0','1','1','1','fl6','fl5','1','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h0','fl3','fl3','0','0','0','0','0','0','0','0','0','0','0','1','fl5','fl6','0','0','0','0','0','0','0','0','fl5','fl6','1','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','p','0','0','0','fl3','fl3','fl3','fl3','0','0','0','0','0','0','0','1','fl6','fl5','0','0','0','0','0','0','0','0','fl6','fl5','1','0','0','0','0','0','0','fl6','fl6','fl6','fl6','fl6','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','fl3','fl3','0','0','0','0','0','0','1','fl5','fl6','0','0','0','0','0','0','0','0','fl5','fl6','1','0','0','0','0','0','0','fl6','fl6','fl6','fl6','fl6','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','fl3','fl3','0','0','0','0','0','1','fl6','fl5','1','1','1','1','1','1','1','1','fl6','fl5','1','0','0','0','0','0','0','fl6','fl6','fl6','fl6','fl6','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','fl3','fl3','fl3','0','0','1','fl5','fl6','1','0','0','0','0','0','0','1','fl5','fl6','1','0','0','0','0','0','0','fl6','fl6','fl6','fl6','fl6','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','fl3','fl3','1','1','1','1','0','0','0','0','0','0','1','1','1','1','0','0','0','0','0','0','fl6','fl6','fl6','fl6','fl6','0']]
    
    win.blit(bg2,(0,0))
    tile_rects_lvl_4=[]
    food_lvl_4=[]
    ec_lvl_4=[]
    portal_lvl_4=[]
    y_1=0
    for row in world_4_data:
        x_1=0
        for tile in row:
            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))   
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))

                        
            if tile=='fl5':
                win.blit(flower5,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))

                        
            if tile=='fl6':
                win.blit(flower6,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))

                        
            if tile=='fl7':
                win.blit(flower7,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))

            if tile=='h0':
                win.blit(path1,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))

            




            

            
            if tile=='1':
                win.blit(tile2,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                tile_rects_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))



            
            if tile=='f1' and Food1col_4==False :
                win.blit(food2,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                food_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))
            if tile=='f2' and Food2col_4==False :
                win.blit(food2,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                food_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))
            if tile=='f3' and Food3col_4==False :
                win.blit(food2,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                food_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))



            if tile=='p' and pc_4<=8:
                win.blit(portal,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                portal_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))

            if tile=='p' and 8<pc_4<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                portal_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))
                
            if tile=='p' and 16<pc_4<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                portal_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))

            if tile=='p' and 24<pc_4:
                win.blit(portal_3,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                portal_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))




                



            if tile=='2' and  ect_4_1<=45 and Ecat1col_4==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                ec_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size)) #1st catto evil
            if tile=='3' and  ect_4_1>45 and Ecat1col_4==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                ec_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))



            if tile=='4' and  ect_4_2<=45 and Ecat2col_4==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                ec_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size)) #1st catto evil
            if tile=='5' and  ect_4_2>45 and Ecat2col_4==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                ec_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))

            if tile=='6' and  ect_4_3<=45 and Ecat3col_4==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                ec_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size)) #1st catto evil
            if tile=='7' and  ect_4_3>45 and Ecat3col_4==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4))
                ec_lvl_4.append(pygame.Rect(x_1*tile_size-camOffx_4,y_1*tile_size-camOffy_4,tile_size,tile_size))

                
            x_1=x_1+1
        y_1=y_1+1

    if pc_4+1>32:
        pc_4=1


    if wc_4+1>9:
        wc_4=1

            
    if ect_4_1+1>135:
        ect_4_1=1

    if ect_4_2+1>135:
        ect_4_2=1

    if ect_4_3+1>135:
        ect_4_3=1
        



    if to_right_4==True and (wc_4==1 or wc_4==2 or wc_4==3):
        win.blit(catto1R,(c_1.x,c_1.y))

    if to_right_4==True and (wc_4==4 or wc_4==5 or wc_4==6):
        win.blit(catto2R,(c_1.x,c_1.y))

    if to_right_4==True and (wc_4==7 or wc_4==8 or wc_4==9):
        win.blit(catto3R,(c_1.x,c_1.y))


        


    if to_right_4==False and (wc_4==1 or wc_4==2 or wc_4==3):
        win.blit(catto1L,(c_1.x,c_1.y))

    if to_right_4==False and (wc_4==4 or wc_4==5 or wc_4==6):
        win.blit(catto2L,(c_1.x,c_1.y))
        
    if to_right_4==False and (wc_4==7 or wc_4==8 or wc_4==9):
        win.blit(catto3L,(c_1.x,c_1.y))




    hit_list = []
    for i in tile_rects_lvl_4:
        if c_1.colliderect(i):
            hit_list.append(i)


    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    
                MS_U_4=False   
            
              

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  
                MS_D_4=False
           
            
             
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:
                MS_L_4=False
               
            
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:
                MS_R_4=False
               
                
                
    if hit_list == []:
        MS_U_4=True
        MS_D_4=True
        MS_L_4=True
        MS_R_4=True
    L=[MS_U_4,MS_D_4,MS_L_4,MS_R_4]
    if L==[False,False,False,False]:
        MS_U_4=True
    if L==[False,False,False,True]:
        MS_D_4=True
    if L==[False,False,True,False]:
        MS_D_4=True


    

    ect_4_1+=1
    ect_4_2+=1
    ect_4_3+=1
    pc_4+=1
    

    if key[pygame.K_LEFT] and camOffx_4-velx_456+winW/2>0 and MS_L_4==True:
        wc_4=wc_4+1
        to_right_4=False
        camOffx_4=camOffx_4-velx_456
    if key[pygame.K_RIGHT] and camOffx_4+velx_456+winW/2<45*tile_size and MS_R_4==True:
        wc_4=wc_4+1
        to_right_4=True
        camOffx_4=camOffx_4+velx_456
    if key[pygame.K_DOWN] and MS_D_4==True:
        wc_4+=1
        camOffy_4=camOffy_4+vely_456
    if key[pygame.K_UP] and MS_U_4==True:
        wc_4+=1
        camOffy_4=camOffy_4-vely_456

    ec_hit_list = []
    for i in ec_lvl_4:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
    
    if ec_hit_list != []:
        if 680>ec_hit_list[0][0]-camOffx_4>440 and 730>ec_hit_list[0][1]-camOffy_4>490:
            Ecat1col_4=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        if -200>ec_hit_list[0][0]-camOffx_4>-490 and 270>ec_hit_list[0][1]-camOffy_4>-20:
            Ecat2col_4=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)


        if -1260>ec_hit_list[0][0]-camOffx_4>-1390 and 170>ec_hit_list[0][1]-camOffy_4>-60:
            Ecat3col_4=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)


        
        #print(ec_hit_list[0][0]-camOffx_4,ec_hit_list[0][1]-camOffy_4)



    food_hit_list = []
    for i in food_lvl_4:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:
        if 840>food_hit_list[0][0]-camOffx_4>690 and 690>food_hit_list[0][1]-camOffy_4>530:
            Food1col_4=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -660>food_hit_list[0][0]-camOffx_4>-720 and 40>food_hit_list[0][1]-camOffy_4>-110:
            Food2col_4=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -990>food_hit_list[0][0]-camOffx_4>-1160 and 690>food_hit_list[0][1]-camOffy_4>530:
            Food3col_4=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)

        

        #print(food_hit_list[0][0]-camOffx_4,food_hit_list[0][1]-camOffy_4)
    

                     
    COL_STATES_lives=[Ecat1col_4,Ecat2col_4,Ecat3col_4]
    count_lives_4=count_lives
    for i in COL_STATES_lives:
        if i==True:
            count_lives_4-=1
    if count_lives_4==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_456()
        
        
    if count_lives_4==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_4==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_4==1:
        win.blit(heart,(418,380))
        
    portal_hit_list = []
    for i in portal_lvl_4:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_4==True:
        LevelFourCleared=True
        count_lives=count_lives_4
        if music_state==True:
                pygame.mixer.Sound.play(portal_sound)

    

    COL_STATES_food=[Food1col_4,Food2col_4,Food3col_4]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1:
        win.blit(foodIcon2,(416,365)) 
    if count_food==2:
        win.blit(foodIcon2,(416,365))
        win.blit(foodIcon2,(438,365))
    if count_food==3:
        win.blit(foodIcon2,(416,365))
        win.blit(foodIcon2,(438,365))
        win.blit(foodIcon2,(460,365))
        Portal_Perms_4=True
    if Portal_Perms_4==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_4==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal",black)
       
       
    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 4",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 4 - checkpoint level 4",black)  


   

    pygame.display.update()

def lvl_5(key,c_1):
    global count_death
    global GameModeHard
    global to_right_5
    global MS_U_5
    global MS_D_5
    global MS_L_5
    global MS_R_5
    global wc_5
    global pc_5
    global ect_5_1
    global ect_5_2
    global ect_5_3
    global Ecat1col_5
    global Ecat2col_5
    global Ecat3col_5
    global Food1col_5
    global Food2col_5
    global Food3col_5
    global Portal_Perms_5
    global Portalcol_5
    global LevelFiveCleared
    global camOffx_5         
    global camOffy_5

    global count_lives  
    c_1.y=winH-cat_H-tile_size
    global music_state
    #global GameOver
    world_5_data=[
        ['1','1','1','1','1','0','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1'],
        ['1','fl6','fl7','fl6','1','0','1','fl6','fl7','fl6','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','fl6','fl5','fl6','0','0','0','1'],
        ['1','fl3','fl3','fl3','1','0','1','fl3','fl3','fl3','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','fl5','fl6','fl5','0','f2','0','1'],
        ['1','f1','fl7','fl6','1','0','1','fl6','fl7','fl6','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','fl6','fl5','fl6','0','0','0','1'],
        ['1','fl3','fl3','fl3','1','1','1','fl3','fl3','fl3','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','fl5','fl6','fl5','0','0','0','1'],
        ['1','fl6','fl7','fl6','0','0','0','fl6','fl7','fl6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0','1','1','1','1','1','1','1'],
        ['1','fl3','fl3','fl3','0','0','0','fl3','fl3','fl3','0','0','2','0','h','h','h','h','h','h','h','h','h','h','h','h','h','h','0','4','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0'],
        ['1','fl6','fl7','fl6','0','0','0','fl6','fl7','fl6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0'],
        ['1','fl3','fl3','fl3','1','1','1','fl3','fl3','fl3','1','1','1','3','0','0','0','0','0','0','0','0','0','0','0','0','0','h','h','5','0','0','0','0','fl3','fl3','0','0','1','0','0','0','0','0','0'],
        ['1','fl6','fl7','fl6','1','0','1','fl6','fl7','fl6','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','fl3','fl3','0','0','1','0','0','0','0','0','0'],
        ['1','fl3','fl3','fl3','1','0','1','fl3','fl3','fl3','1','0','0','0','0','0','0','0','0','0','fl7','fl7','fl7','0','0','0','0','h','0','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0'],
        ['1','fl6','fl7','fl6','1','0','1','fl6','fl7','fl6','1','0','0','0','0','0','0','0','fl7','fl7','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['1','1','1','1','1','0','1','1','1','1','1','0','0','0','0','0','0','0','0','0','fl7','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['fl5','fl2','fl5','fl2','0','0','0','0','0','0','0','0','0','0','0','0','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','0','fl7','fl7','0','0','0','0'],
        ['fl5','fl2','fl5','fl2','0','0','0','0','0','0','0','0','0','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','fl7','fl7','0','0','0','0'],
        ['fl5','fl2','fl5','fl2','0','0','0','0','0','h','h','h','h','h','0','0','0','0','0','0','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0'],
        ['fl5','fl2','fl5','fl2','0','0','h','h','h','h','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','1','f3','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0'],
        ['1','1','1','0','0','h','0','1','1','1','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0'],
        ['1','fl7','fl7','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','1','0','fl5','fl5','fl5','1','1','1','1','1','1','0','0','0','0','0','0','h','0','0','0','0','0','0','0'],
        ['1','fl7','fl7','0','p','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','1','0','fl2','fl2','fl2','0','0','0','0','0','0','0','0','0','0','0','0','h','h','h','h','h','h','h','0'],
        ['1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','1','0','fl5','fl5','fl5','0','0','0','0','0','6','0','h','h','h','h','h','h','0','0','0','0','0','h','0'],
        ['1','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','1','0','fl2','fl2','fl2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0'],
        ['1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','7','0','0','0','0','0','0','0','0','0','0','0','0','0']]


    

    win.blit(bg2,(0,0))
    tile_rects_lvl_5=[]
    food_lvl_5=[]
    ec_lvl_5=[]
    portal_lvl_5=[]
    y_1=0
    for row in world_5_data:
        x_1=0
        for tile in row:
            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))   
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))

                        
            if tile=='fl5':
                win.blit(flower5,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))

                        
            if tile=='fl6':
                win.blit(flower6,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))

                        
            if tile=='fl7':
                win.blit(flower7,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))


            
            if tile=='h':#promijenila sam render slovo prije je bilo h0
                win.blit(path1,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))




            
            if tile=='1':
                win.blit(tile2,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                tile_rects_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))







            if tile=='f1' and Food1col_5==False :
                win.blit(food2,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                food_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))
            if tile=='f2' and Food2col_5==False :
                win.blit(food2,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                food_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))
            if tile=='f3' and Food3col_5==False :
                win.blit(food2,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                food_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))



            if tile=='p' and pc_5<=8:
                win.blit(portal,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                portal_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))

            if tile=='p' and 8<pc_5<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                portal_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))
                
            if tile=='p' and 16<pc_5<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                portal_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))

            if tile=='p' and 24<pc_5:
                win.blit(portal_3,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                portal_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))








            if tile=='2' and  ect_5_1<=45 and Ecat1col_5==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                ec_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size)) #1st catto evil
            if tile=='3' and  ect_5_1>45 and Ecat1col_5==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                ec_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))



            if tile=='4' and  ect_5_2<=53 and Ecat2col_5==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                ec_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size)) #1st catto evil
            if tile=='5' and  ect_5_2>53 and Ecat2col_5==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                ec_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))

            if tile=='6' and  ect_5_3<=45 and Ecat3col_5==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                ec_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size)) #1st catto evil
            if tile=='7' and  ect_5_3>45 and Ecat3col_5==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5))
                ec_lvl_5.append(pygame.Rect(x_1*tile_size-camOffx_5,y_1*tile_size-camOffy_5,tile_size,tile_size))
            x_1=x_1+1
        y_1=y_1+1

    if pc_5+1>32:
        pc_5=1




    
    if wc_5+1>9:
        wc_5=1

    if ect_5_1>105:
        ect_5_1=1

    if ect_5_2>106:
        ect_5_2=1

    if ect_5_3>105:
        ect_5_3=1

        
    


       

    if to_right_5==True and (wc_5==1 or wc_5==2 or wc_5==3):
        win.blit(catto1R,(c_1.x,c_1.y))

    if to_right_5==True and (wc_5==4 or wc_5==5 or wc_5==6):
        win.blit(catto2R,(c_1.x,c_1.y))

    if to_right_5==True and (wc_5==7 or wc_5==8 or wc_5==9):
        win.blit(catto3R,(c_1.x,c_1.y))


        


    if to_right_5==False and (wc_5==1 or wc_5==2 or wc_5==3):
        win.blit(catto1L,(c_1.x,c_1.y))

    if to_right_5==False and (wc_5==4 or wc_5==5 or wc_5==6):
        win.blit(catto2L,(c_1.x,c_1.y))
        
    if to_right_5==False and (wc_5==7 or wc_5==8 or wc_5==9):
        win.blit(catto3L,(c_1.x,c_1.y))





    hit_list = []
    for i in tile_rects_lvl_5:
        if c_1.colliderect(i):
            hit_list.append(i)



    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    
                MS_U_5=False   
            
              

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  
                MS_D_5=False
           
            
             
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:
                MS_L_5=False
               
            
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:
                MS_R_5=False
               
                
                
    if hit_list == []:
        MS_U_5=True
        MS_D_5=True
        MS_L_5=True
        MS_R_5=True
    L=[MS_U_5,MS_D_5,MS_L_5,MS_R_5]
    if L==[False,False,False,False]:
        MS_U_5=True
    if L==[False,False,False,True]:
        MS_D_5=True
    if L==[False,False,True,False]:
        MS_D_5=True


    

##    ect_4_1+=1
##    ect_4_2+=1
##    ect_4_3+=1
##    pc_4+=1
    ect_5_1+=1
    ect_5_2+=1
    ect_5_3+=1
    pc_5+=1    

    if key[pygame.K_LEFT] and camOffx_5-velx_456+winW/2>0 and MS_L_5==True:
        wc_5=wc_5+1
        to_right_5=False
        camOffx_5=camOffx_5-velx_456
    if key[pygame.K_RIGHT] and camOffx_5+velx_456+winW/2<45*tile_size and MS_R_5==True:
        wc_5=wc_5+1
        to_right_5=True
        camOffx_5=camOffx_5+velx_456
    if key[pygame.K_DOWN] and MS_D_5==True:
        wc_5+=1
        camOffy_5=camOffy_5+vely_456
    if key[pygame.K_UP] and MS_U_5==True:
        wc_5+=1
        camOffy_5=camOffy_5-vely_456


    ec_hit_list = []
    for i in ec_lvl_5:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
    
    if ec_hit_list != []:
        if 357>ec_hit_list[0][0]-camOffx_5>91 and 576>ec_hit_list[0][1]-camOffy_5>293:
           Ecat1col_5=True
           if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)


        if -488>ec_hit_list[0][0]-camOffx_5>-699 and 478>ec_hit_list[0][1]-camOffy_5>293:
           Ecat2col_5=True
           if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        if -545>ec_hit_list[0][0]-camOffx_5>-812 and -220>ec_hit_list[0][1]-camOffy_5>-525:
           Ecat3col_5=True
           if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        
        #print(ec_hit_list[0][0]-camOffx_5,ec_hit_list[0][1]-camOffy_5)

    food_hit_list = []
    for i in food_lvl_5:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:
        if 800>food_hit_list[0][0]-camOffx_5>723 and 745>food_hit_list[0][1]-camOffy_5>570:
           Food1col_5=True
           if music_state==True:
                pygame.mixer.Sound.play(eating_sound)

        if -1135>food_hit_list[0][0]-camOffx_5>-1310 and 780>food_hit_list[0][1]-camOffy_5>620:
           Food2col_5=True
           if music_state==True:
                pygame.mixer.Sound.play(eating_sound)

        if -205>food_hit_list[0][0]-camOffx_5>-275 and -25>food_hit_list[0][1]-camOffy_5>-170:
           Food3col_5=True
           if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
           
       # print(food_hit_list[0][0]-camOffx_5,food_hit_list[0][1]-camOffy_5)


   

    COL_STATES_lives=[Ecat1col_5,Ecat2col_5,Ecat3col_5]
    count_lives_5=count_lives 
 
    for i in COL_STATES_lives:
        if i==True:
            count_lives_5-=1
    if count_lives_5==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_456()
        
        
    if count_lives_5==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_5==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_5==1:
        win.blit(heart,(418,380))
    
    portal_hit_list = []
    for i in portal_lvl_5:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_5==True:
        LevelFiveCleared=True
        count_lives=count_lives_5
        if music_state==True:
                pygame.mixer.Sound.play(portal_sound)

    COL_STATES_food=[Food1col_5,Food2col_5,Food3col_5]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1:
        win.blit(foodIcon2,(416,365)) 
    if count_food==2:
        win.blit(foodIcon2,(416,365))
        win.blit(foodIcon2,(438,365))
    if count_food==3:
        win.blit(foodIcon2,(416,365))
        win.blit(foodIcon2,(438,365))
        win.blit(foodIcon2,(460,365))
        Portal_Perms_5=True
    if Portal_Perms_5==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_5==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal",black)
       
       
    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 5",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 5 - checkpoint level 4",black)     







            
    
    pygame.display.update()

def lvl_6(key,c_1):
    global count_death
    global GameModeHard
    global to_right_6
    global MS_U_6
    global MS_D_6
    global MS_L_6
    global MS_R_6
    global wc_6
    global pc_6
    global ect_6_1
    global ect_6_2
    global ect_6_3
    global Ecat1col_6
    global Ecat2col_6
    global Ecat3col_6
    global Food1col_6
    global Food2col_6
    global Food3col_6
    global Portal_Perms_6
    global Portalcol_6
    global LevelSixCleared
    global camOffx_6        
    global camOffy_6

    global count_lives  
    c_1.y=winH-cat_H-tile_size
    global music_state
    #global GameOver
    world_6_data=[
        ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0'],
        ['1','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl2','fl2','fl2','fl2','fl2','fl2','fl2','fl2','fl2','fl2','1','0','0','0','0','0','0','0','0'],
        ['1','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl2','0','0','0','p','0','0','0','0','fl2','1','0','0','0','0','0','0','0','0'],
        ['1','f1','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl2','0','0','0','0','0','0','0','0','fl2','1','0','0','0','0','0','0','0','0'],
        ['1','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl2','fl2','fl2','0','0','0','0','fl2','fl2','fl2','1','0','0','0','0','0','0','0','0'],
        ['1','0','0','1','0','0','0','0','0','0','0','0','5','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','0','0','0','0','1','1','1','1','0','0','0','0','0','0','0','0'],
        ['1','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl1','fl5','fl1','0','0','0','0','fl5','fl1','fl5','1','0','0','0','0','0','0','0','0'],
        ['1','0','0','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl5','fl1','fl5','0','0','0','0','fl1','fl5','fl1','1','0','0','0','0','0','0','0','0'],
        ['1','0','0','3','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl1','fl5','fl1','0','0','0','0','fl5','fl1','fl5','1','0','0','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0','0','0','0','0','0','0','h','h','0','0','0','0','0','0','0','0','0','0','1','1','1','1','0','0','0','0','1','1','1','1','0','0','0','0','0','0','0','0'],
        ['1','1','1','0','0','1','1','1','1','1','1','1','0','0','h','0','0','0','0','fl7','fl7','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','1','2','0','1','0','0','0','0','0','0','0','0','h','0','0','0','0','fl7','fl7','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','1','0','0','1','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','1','1','1','1','0','0','0','0','0','0','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h','h','h','h','h','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','h','0','0','h','h','h','0','0','0','0','0','0','0','0','0'],
        ['0','0','h','h','h','h','0','0','0','0','0','0','0','0','1','fl6','fl1','fl6','fl1','fl6','1','fl1','fl1','fl1','fl1','fl1','1','0','0','0','h','0','0','0','0','h','h','h','h','0','0','0','0','0','0'],
        ['0','0','h','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl1','fl6','fl1','fl6','1','fl7','fl7','fl7','fl7','fl7','1','0','0','0','h','0','0','0','0','0','0','0','0','h','h','h','0','0','0'],
        ['0','0','h','0','0','0','0','0','0','0','0','0','0','0','6','fl6','fl1','fl6','fl1','fl6','1','fl1','fl1','fl1','fl1','fl1','0','0','0','0','h','0','0','0','0','0','0','fl7','fl7','fl7','fl7','fl7','fl7','fl7','fl7'],
        ['0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','fl6','fl1','fl6','fl1','fl6','1','fl7','fl7','fl7','fl7','fl7','0','h','h','h','h','0','0','0','0','0','0','fl5','fl5','fl5','fl5','fl5','fl5','fl5','fl5'],
        ['0','0','h','h','h','h','h','h','h','h','h','h','h','0','7','fl6','fl1','fl6','fl1','f2','1','fl1','fl1','fl1','fl1','fl1','0','0','0','0','0','0','0','0','0','0','0','fl7','fl7','fl7','fl7','fl7','fl7','fl7','fl7'],
        ['0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','fl6','fl1','fl6','fl1','fl6','1','fl7','fl7','fl7','fl7','fl7','0','0','0','0','0','0','0','0','0','0','0','fl5','fl5','fl5','fl5','fl5','fl5','fl5','fl5'],
        ['0','0','h','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl1','fl6','fl1','fl6','1','fl1','fl1','fl1','fl1','fl1','1','0','0','0','0','0','0','0','0','0','0','fl7','fl7','fl7','fl7','fl7','fl7','fl7','fl7'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl1','fl6','fl1','fl6','1','fl7','fl7','fl7','fl7','fl7','1','0','0','0','0','0','0','0','0','0','0','fl5','fl5','fl5','fl5','fl5','f3','fl5','fl5'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','fl7','fl7','fl7','fl7','fl7','fl7','fl7','fl7']]

    win.blit(bg2,(0,0))
    tile_rects_lvl_6=[]
    food_lvl_6=[]
    ec_lvl_6=[]
    portal_lvl_6=[]
    y_1=0
    for row in world_6_data:
        x_1=0
        for tile in row:
            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))   
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))

                        
            if tile=='fl5':
                win.blit(flower5,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))

                        
            if tile=='fl6':
                win.blit(flower6,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))

                        
            if tile=='fl7':
                win.blit(flower7,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))


            
            if tile=='h':#promijenila sam render slovo prije je bilo h0
                win.blit(path1,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))




            
            if tile=='1':
                win.blit(tile2,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                tile_rects_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))


            if tile=='f1' and Food1col_6==False :
                win.blit(food2,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                food_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))
            if tile=='f2' and Food2col_6==False :
                win.blit(food2,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                food_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))
            if tile=='f3' and Food3col_6==False :
                win.blit(food2,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                food_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))



            if tile=='p' and pc_6<=8:
                win.blit(portal,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                portal_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))

            if tile=='p' and 8<pc_6<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                portal_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))
                
            if tile=='p' and 16<pc_6<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                portal_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))

            if tile=='p' and 24<pc_6:
                win.blit(portal_3,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                portal_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))








            if tile=='2' and  ect_6_1<=53 and Ecat1col_6==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                ec_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size)) #1st catto evil
            if tile=='3' and  ect_6_1>53 and Ecat1col_6==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                ec_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))



            if tile=='4' and  ect_6_2<=45 and Ecat2col_6==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                ec_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size)) #1st catto evil
            if tile=='5' and  ect_6_2>45 and Ecat2col_6==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                ec_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))

            if tile=='6' and  ect_6_3<=53 and Ecat3col_6==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                ec_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size)) #1st catto evil
            if tile=='7' and  ect_6_3>53 and Ecat3col_6==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6))
                ec_lvl_6.append(pygame.Rect(x_1*tile_size-camOffx_6,y_1*tile_size-camOffy_6,tile_size,tile_size))
                
            x_1=x_1+1
        y_1=y_1+1


    if wc_6+1>9:
        wc_6=1

    
    if ect_6_1>106:
        ect_6_1=1

    if ect_6_2>105:
        ect_6_2=1

    if ect_6_3>106:
        ect_6_3=1
        
    if pc_6+1>32:
        pc_6=1


       

    if to_right_6==True and (wc_6==1 or wc_6==2 or wc_6==3):
        win.blit(catto1R,(c_1.x,c_1.y))

    if to_right_6==True and (wc_6==4 or wc_6==5 or wc_6==6):
        win.blit(catto2R,(c_1.x,c_1.y))

    if to_right_6==True and (wc_6==7 or wc_6==8 or wc_6==9):
        win.blit(catto3R,(c_1.x,c_1.y))


        


    if to_right_6==False and (wc_6==1 or wc_6==2 or wc_6==3):
        win.blit(catto1L,(c_1.x,c_1.y))

    if to_right_6==False and (wc_6==4 or wc_6==5 or wc_6==6):
        win.blit(catto2L,(c_1.x,c_1.y))
        
    if to_right_6==False and (wc_6==7 or wc_6==8 or wc_6==9):
        win.blit(catto3L,(c_1.x,c_1.y))




    hit_list = []
    for i in tile_rects_lvl_6:
        if c_1.colliderect(i):
            hit_list.append(i)



    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    
                MS_U_6=False   
            
              

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  
                MS_D_6=False
           
            
             
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:
                MS_L_6=False
               
            
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:
                MS_R_6=False
               
                
                
    if hit_list == []:
        MS_U_6=True
        MS_D_6=True
        MS_L_6=True
        MS_R_6=True
    L=[MS_U_6,MS_D_6,MS_L_6,MS_R_6]
    if L==[False,False,False,False]:
        MS_U_6=True
    if L==[False,False,False,True]:
        MS_D_6=True
    if L==[False,False,True,False]:
        MS_D_6=True
    


    ect_6_1+=1
    ect_6_2+=1
    ect_6_3+=1
    pc_6+=1    

    if key[pygame.K_LEFT] and camOffx_6-velx_456+winW/2>0 and MS_L_6==True:
        wc_6=wc_6+1
        to_right_6=False
        camOffx_6=camOffx_6-velx_456
    if key[pygame.K_RIGHT] and camOffx_6+velx_456+winW/2<45*tile_size and MS_R_6==True:
        wc_6=wc_6+1
        to_right_6=True
        camOffx_6=camOffx_6+velx_456
    if key[pygame.K_DOWN] and MS_D_6==True:
        wc_6+=1
        camOffy_6=camOffy_6+vely_456
    if key[pygame.K_UP] and MS_U_6==True:
        wc_6+=1
        camOffy_6=camOffy_6-vely_456


    ec_hit_list = []
    for i in ec_lvl_6:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
    
    if ec_hit_list != []:

        if 811>ec_hit_list[0][0]-camOffx_6>580 and 380>ec_hit_list[0][1]-camOffy_6>144:
           Ecat1col_6=True
           if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
        if 405>ec_hit_list[0][0]-camOffx_6>192 and 627>ec_hit_list[0][1]-camOffy_6>294:
           Ecat2col_6=True
           if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)


        if 263>ec_hit_list[0][0]-camOffx_6>38 and -120>ec_hit_list[0][1]-camOffy_6>-306:
           Ecat3col_6=True
           if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        
##        print(ec_hit_list[0][0]-camOffx_6,ec_hit_list[0][1]-camOffy_6)


    food_hit_list = []
    for i in food_lvl_6:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:
        if 790>food_hit_list[0][0]-camOffx_6>728 and 740>food_hit_list[0][1]-camOffy_6>580:
           Food1col_6=True
           if music_state==True:
                pygame.mixer.Sound.play(eating_sound)

        if 11>food_hit_list[0][0]-camOffx_6>-90 and -107>food_hit_list[0][1]-camOffy_6>-234:
           Food2col_6=True
           if music_state==True:
                pygame.mixer.Sound.play(eating_sound)

        if -1140>food_hit_list[0][0]-camOffx_6>-1310 and -260>food_hit_list[0][1]-camOffy_6>-426:
           Food3col_6=True
           if music_state==True:
                pygame.mixer.Sound.play(eating_sound)

           
        #print(food_hit_list[0][0]-camOffx_6,food_hit_list[0][1]-camOffy_6)

    COL_STATES_lives=[Ecat1col_6,Ecat2col_6,Ecat3col_6]
    count_lives_6=count_lives 
    for i in COL_STATES_lives:
        if i==True:
            count_lives_6-=1
    if count_lives_6==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_456()
        
        
    if count_lives_6==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_6==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_6==1:
        win.blit(heart,(418,380))
    
    portal_hit_list = []
    for i in portal_lvl_6:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_6==True:
        LevelSixCleared=True
        count_lives=count_lives_6
        if music_state==True:
                pygame.mixer.Sound.play(portal_sound)


    COL_STATES_food=[Food1col_6,Food2col_6,Food3col_6]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1:
        win.blit(foodIcon2,(416,365)) 
    if count_food==2:
        win.blit(foodIcon2,(416,365))
        win.blit(foodIcon2,(438,365))
    if count_food==3:
        win.blit(foodIcon2,(416,365))
        win.blit(foodIcon2,(438,365))
        win.blit(foodIcon2,(460,365))
        Portal_Perms_6=True
    if Portal_Perms_6==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_6==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal",black)
       
       
    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 6",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 6 - checkpoint level 4",black)     


   


    pygame.display.update()

def lvl_7(key,c_1):
    global count_death
    global GameModeHard
    global to_right_7
    global MS_U_7
    global MS_D_7
    global MS_L_7
    global MS_R_7
    global wc_7
    global pc_7
    global ect_7_1
    global ect_7_2
    global ect_7_3
    global Ecat1col_7
    global Ecat2col_7
    global Ecat3col_7
    global Food1col_7
    global Food2col_7
    global Food3col_7
    global Portal_Perms_7
    global Portalcol_7
    global LevelSevenCleared
    global camOffx_7       
    global camOffy_7

    global count_lives 
  
    c_1.y=winH-cat_H-tile_size
    global music_state
    #global GameOver
    world_7_data=[
        ['1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1'],
        ['1','0','0','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','0','0','0','0','1'],
        ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
        ['1','0','0','0','0','0','0','0','0','3','0','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','0','5','0','0','0','0','0','0','0','0','0','1'],
        ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
        ['1','0','0','0','0','1','1','1','1','1','1','0','0','0','0','0','0','0','0','fl3','fl3','0','h','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','0','0','0','0','1'],
        ['1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','fl3','fl3','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','1'],
        ['1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','fl3','fl3','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','1'],
        ['1','f1','0','fl5','fl5','1','0','0','0','0','0','0','0','0','0','0','0','0','0','fl3','fl3','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','f2','1'],
        ['1','0','0','fl5','fl5','1','0','0','0','0','0','0','0','0','0','0','0','0','0','fl3','fl3','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl3','fl3','0','0','1'],
        ['1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl3','fl3','0','0','1'],
        ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','h','h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','0','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','h','0','0','0','1','1','1','1','1','1','0','0','0','0','1','1','1','1','1','1','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1'],
        ['0','0','0','0','0','h','0','0','0','1','fl7','fl7','fl7','fl7','1','0','0','0','0','1','fl6','fl5','fl6','fl5','1','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl7','fl6','1'],
        ['0','0','0','0','0','h','0','0','0','1','fl1','fl1','fl1','fl1','1','0','0','0','0','1','fl6','fl5','fl6','fl5','1','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl7','fl6','1'],
        ['0','0','0','h','h','h','0','0','0','1','fl7','fl7','fl7','fl7','1','1','1','1','1','1','fl6','fl5','fl6','f3','1','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','fl6','fl7','fl6','1'],
        ['0','0','h','h','0','0','0','0','0','1','fl1','fl1','fl1','fl1','0','0','0','0','0','0','fl6','fl5','fl6','fl5','1','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','fl6','fl7','fl6','1'],
        ['0','0','h','0','0','0','0','0','0','1','fl7','fl7','fl7','fl7','0','0','0','0','0','0','fl6','fl5','fl6','fl5','1','0','0','h','h','h','h','h','h','h','h','h','h','h','h','h','0','fl6','fl7','fl6','1'],
        ['p','0','0','fl3','fl3','0','0','0','0','1','fl1','fl1','fl1','fl1','0','0','0','0','0','0','fl6','fl5','fl6','fl5','1','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','fl6','fl7','fl6','1'],
        ['0','0','0','fl3','fl3','0','0','0','0','1','1','1','1','1','1','0','0','0','0','1','1','1','1','1','1','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl7','fl6','1'],
        ['0','0','0','fl3','fl3','0','0','0','0','0','0','0','0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl7','fl6','1'],
        ['0','0','0','fl3','fl3','0','0','0','0','0','0','0','0','0','1','6','0','7','0','1','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1']]

    win.blit(bg3,(0,0))
    tile_rects_lvl_7=[]
    food_lvl_7=[]
    ec_lvl_7=[]
    portal_lvl_7=[]
    y_1=0
    for row in world_7_data:
        x_1=0
        for tile in row:
            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))   
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))

                        
            if tile=='fl5':
                win.blit(flower5,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))

                        
            if tile=='fl6':
                win.blit(flower6,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))

                        
            if tile=='fl7':
                win.blit(flower7,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))


            
            if tile=='h':#promijenila sam render slovo prije je bilo h0
                win.blit(path2,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))





            
            if tile=='1':
                win.blit(tile3,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                tile_rects_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))

                

            if tile=='f1' and Food1col_7==False :
                win.blit(food3,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                food_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))
            if tile=='f2' and Food2col_7==False :
                win.blit(food3,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                food_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))
            if tile=='f3' and Food3col_7==False :
                win.blit(food3,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                food_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))



            if tile=='p' and pc_7<=8:
                win.blit(portal,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                portal_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))

            if tile=='p' and 8<pc_7<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                portal_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))
            
            if tile=='p' and 16<pc_7<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                portal_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))

            if tile=='p' and 24<pc_7:
                win.blit(portal_3,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                portal_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))



            

            if tile=='2' and  ect_7_1<=54 and Ecat1col_7==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                ec_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size)) 
            if tile=='3' and  ect_7_1>54 and Ecat1col_7==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                ec_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))



            if tile=='4' and  ect_7_2<=54 and Ecat2col_7==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                ec_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size)) 
            if tile=='5' and  ect_7_2>54 and Ecat2col_7==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                ec_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))

            if tile=='6' and  ect_7_3<=54 and Ecat3col_7==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                ec_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size)) 
            if tile=='7' and  ect_7_3>54 and Ecat3col_7==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7))
                ec_lvl_7.append(pygame.Rect(x_1*tile_size-camOffx_7,y_1*tile_size-camOffy_7,tile_size,tile_size))
                
            x_1=x_1+1
        y_1=y_1+1

    if wc_7+1>9:
        wc_7=1

    
    if ect_7_1>108:
        ect_7_1=1

    if ect_7_2>108:
        ect_7_2=1

    if ect_7_3>108:
        ect_7_3=1
        
    if pc_7+1>32:
        pc_7=1


       

    if to_right_7==True and (wc_7==1 or wc_7==2 or wc_7==3):
        win.blit(catto1R,(c_1.x,c_1.y))

    if to_right_7==True and (wc_7==4 or wc_7==5 or wc_7==6):
        win.blit(catto2R,(c_1.x,c_1.y))

    if to_right_7==True and (wc_7==7 or wc_7==8 or wc_7==9):
        win.blit(catto3R,(c_1.x,c_1.y))


        


    if to_right_7==False and (wc_7==1 or wc_7==2 or wc_7==3):
        win.blit(catto1L,(c_1.x,c_1.y))

    if to_right_7==False and (wc_7==4 or wc_7==5 or wc_7==6):
        win.blit(catto2L,(c_1.x,c_1.y))
        
    if to_right_7==False and (wc_7==7 or wc_7==8 or wc_7==9):
        win.blit(catto3L,(c_1.x,c_1.y))




    hit_list = []
    for i in tile_rects_lvl_7:
        if c_1.colliderect(i):
            hit_list.append(i)



    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    
                MS_U_7=False   
            
              

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  
                MS_D_7=False
           
            
             
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:
                MS_L_7=False
               
            
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:
                MS_R_7=False
               
                
                
    if hit_list == []:
        MS_U_7=True
        MS_D_7=True
        MS_L_7=True
        MS_R_7=True
    L=[MS_U_7,MS_D_7,MS_L_7,MS_R_7]
    if L==[False,False,False,False]:
        MS_U_7=True
    if L==[False,False,False,True]:
        MS_D_7=True
    if L==[False,False,True,False]:
        MS_D_7=True


    ect_7_1+=1
    ect_7_2+=1
    ect_7_3+=1
    pc_7+=1    

    if key[pygame.K_LEFT] and camOffx_7-velx_789+winW/2>0 and MS_L_7==True:
        wc_7=wc_7+1
        to_right_7=False
        camOffx_7=camOffx_7-velx_789
    if key[pygame.K_RIGHT] and camOffx_7+velx_789+winW/2<45*tile_size and MS_R_7==True:
        wc_7=wc_7+1
        to_right_7=True
        camOffx_7=camOffx_7+velx_789
    if key[pygame.K_DOWN] and MS_D_7==True:
        wc_7+=1
        camOffy_7=camOffy_7+vely_789
    if key[pygame.K_UP] and MS_U_7==True:
        wc_7+=1
        camOffy_7=camOffy_7-vely_789

    ec_hit_list = []
    for i in ec_lvl_7:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
    
    if ec_hit_list != []:
        if 515>ec_hit_list[0][0]-camOffx_7>285 and 730>ec_hit_list[0][1]-camOffy_7>545:
            Ecat1col_7=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        if -740>ec_hit_list[0][0]-camOffx_7>-1000 and 730>ec_hit_list[0][1]-camOffy_7>545:
            Ecat2col_7=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        if 210>ec_hit_list[0][0]-camOffx_7>-120 and -300>ec_hit_list[0][1]-camOffy_7>-530:
            Ecat3col_7=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        
       # print(ec_hit_list[0][0]-camOffx_7,ec_hit_list[0][1]-camOffy_7)    
    
    food_hit_list = []
    for i in food_lvl_7:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:
        if 790>food_hit_list[0][0]-camOffx_7>720 and 500>food_hit_list[0][1]-camOffy_7>320:
            Food1col_7=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -1180>food_hit_list[0][0]-camOffx_7>-1290 and 500>food_hit_list[0][1]-camOffy_7>320:
            Food2col_7=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -180>food_hit_list[0][0]-camOffx_7>-300 and -5>food_hit_list[0][1]-camOffy_7>-180:
            Food3col_7=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        #print(food_hit_list[0][0]-camOffx_7,food_hit_list[0][1]-camOffy_7)    


    COL_STATES_lives=[Ecat1col_7,Ecat2col_7,Ecat3col_7]
    count_lives_7=count_lives 
    
    for i in COL_STATES_lives:
        if i==True:
            count_lives_7-=1
    if count_lives_7==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_789()
        
        
    if count_lives_7==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_7==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_7==1:
        win.blit(heart,(418,380))
    
    portal_hit_list = []
    for i in portal_lvl_7:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_7==True:
        LevelSevenCleared=True
        count_lives=count_lives_7
        if music_state==True:
                pygame.mixer.Sound.play(portal_sound)

    COL_STATES_food=[Food1col_7,Food2col_7,Food3col_7]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1:
        win.blit(foodIcon3,(416,360)) 
    if count_food==2:
        win.blit(foodIcon3,(416,360))
        win.blit(foodIcon3,(438,360))
    if count_food==3:
        win.blit(foodIcon3,(416,360))
        win.blit(foodIcon3,(438,360))
        win.blit(foodIcon3,(460,360))
        Portal_Perms_7=True
    if Portal_Perms_7==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_7==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal",black)
       
       
    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 7",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 7 - checkpoint level 7",black)     



    pygame.display.update()


def lvl_8(key,c_1):
    global count_death
    global GameModeHard
    global to_right_8
    global MS_U_8
    global MS_D_8
    global MS_L_8
    global MS_R_8
    global wc_8
    global pc_8
    global ect_8_1
    global ect_8_2
    global ect_8_3
    global Ecat1col_8
    global Ecat2col_8
    global Ecat3col_8
    global Food1col_8
    global Food2col_8
    global Food3col_8
    global Portal_Perms_8
    global Portalcol_8
    global LevelEightCleared
    global camOffx_8        
    global camOffy_8
    
    global GotSeacret
    global s_c
    
    global count_lives 
  
    c_1.y=winH-cat_H-tile_size
    global music_state
    #global GameOver
    world_8_data=[
        ['1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','p','0','fl3','fl3','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['1','fl3','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['1','f1','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','0','0','0','0','0','fl7','fl7','0','0','h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['1','fl3','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','0','0','0','0','0','fl7','fl7','0','0','0','0','0','0','0','0','h','0','0','h','h','h','h','0','0','0','0','0','0','0','0','0'],
        ['1','1','1','0','0','0','0','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','h','h','h','h','0','0','0','0','0','0'],
        ['0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0'],
        ['0','0','1','0','0','0','0','1','0','0','0','0','0','0','fl3','fl3','fl3','fl3','fl3','fl3','fl3','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0'],
        ['1','1','1','0','0','0','0','1','1','1','0','0','0','0','fl3','fl3','fl3','S','fl3','fl3','fl3','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['1','fl3','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','fl3','fl3','fl3','fl3','fl3','fl3','fl3','0','0','0','0','0','0','0','0','h','0','0','0','0','1','1','1','6','0','0','7','0','1','1','1'],
        ['1','fl3','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','1','0','0','0','0','0','0','0','0','0','1'],
        ['1','fl3','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','1','fl6','fl6','0','0','0','0','0','0','0','1'],
        ['1','1','1','0','0','0','0','1','1','1','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','0','h','0','0','0','0','1','fl6','fl6','0','0','0','0','0','0','0','1'],
        ['0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl6','fl6','fl6','fl6','fl6','fl6','1','0','h','0','0','0','0','1','fl6','fl6','0','0','0','0','0','0','f3','1'],
        ['0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','1','fl6','fl6','fl6','fl6','fl6','fl6','fl6','1','0','h','0','0','0','0','1','0','0','0','0','0','0','0','0','0','1'],
        ['1','1','1','0','0','0','0','1','1','1','0','0','0','0','0','0','0','0','0','1','fl6','fl6','fl6','fl6','fl6','fl6','fl6','1','0','h','0','0','0','0','1','0','0','0','0','0','0','0','0','0','1'],
        ['1','fl3','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','0','0','0','0','0','1','1','1','0','0','0','1','1','1','0','h','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1'],
        ['1','fl3','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','h','0','0','0','0','1','0','0','0','0','1','fl7','fl7','fl7','fl7','1'],
        ['1','fl3','fl7','0','0','0','0','fl7','fl3','1','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','h','0','0','0','0','1','0','0','0','0','1','fl5','fl5','fl5','fl5','1'],
        ['1','1','1','0','0','0','0','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','h','0','0','0','0','4','0','0','0','0','1','fl7','fl7','fl7','fl7','1'],
        ['0','0','1','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','1','fl5','fl5','fl5','fl5','1'],
        ['0','0','1','2','0','3','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','h','h','h','h','h','h','h','h','0','5','0','0','0','0','1','fl7','fl7','fl7','fl7','1'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','fl5','fl5','0','f2','1','fl5','fl5','fl5','fl5','1'],
        ['0','0','0','0','h','0','0','0','0','0','0','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','fl5','fl5','0','0','1','fl7','fl7','fl7','fl7','1'],
        ['0','0','0','0','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','1','fl5','fl5','fl5','fl5','1'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1']]

    win.blit(bg3,(0,0))
    tile_rects_lvl_8=[]
    food_lvl_8=[]
    ec_lvl_8=[]
    portal_lvl_8=[]
    seacret=[]
    y_1=0
    for row in world_8_data:
        x_1=0
        for tile in row:
            if tile=='S' and GotSeacret==False:
                win.blit(roy,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                seacret.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))

            
            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))   
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))

                        
            if tile=='fl5':
                win.blit(flower5,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))

                        
            if tile=='fl6':
                win.blit(flower6,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))

                        
            if tile=='fl7':
                win.blit(flower7,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))

            if tile=='h':
                win.blit(path2,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                
                
            if tile=='1':
                win.blit(tile3,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                tile_rects_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))


            if tile=='f1' and Food1col_8==False :
                win.blit(food3,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                food_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))
            if tile=='f2' and Food2col_8==False :
                win.blit(food3,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                food_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))
            if tile=='f3' and Food3col_8==False :
                win.blit(food3,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                food_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))


            if tile=='p' and pc_8<=8:
                win.blit(portal,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                portal_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))

            if tile=='p' and 8<pc_8<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                portal_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))
            
            if tile=='p' and 16<pc_8<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                portal_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))

            if tile=='p' and 24<pc_8:
                win.blit(portal_3,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                portal_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))



            

            if tile=='2' and  ect_8_1<=56 and Ecat1col_8==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                ec_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size)) 
            if tile=='3' and  ect_8_1>56 and Ecat1col_8==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                ec_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))



            if tile=='4' and  ect_8_2<=54 and Ecat2col_8==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                ec_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size)) 
            if tile=='5' and  ect_8_2>54 and Ecat2col_8==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                ec_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))

            if tile=='6' and  ect_8_3<=54 and Ecat3col_8==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                ec_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size)) 
            if tile=='7' and  ect_8_3>54 and Ecat3col_8==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8))
                ec_lvl_8.append(pygame.Rect(x_1*tile_size-camOffx_8,y_1*tile_size-camOffy_8,tile_size,tile_size))
                
            x_1=x_1+1
        y_1=y_1+1


    if wc_8+1>9:
        wc_8=1

    if ect_8_1>112:
        ect_8_1=1

    if ect_8_2>108:
        ect_8_2=1

    if ect_8_3>108:
        ect_8_3=1
        
    if pc_8+1>32:
        pc_8=1


       

    if to_right_8==True and (wc_8==1 or wc_8==2 or wc_8==3):
        win.blit(catto1R,(c_1.x,c_1.y))

    if to_right_8==True and (wc_8==4 or wc_8==5 or wc_8==6):
        win.blit(catto2R,(c_1.x,c_1.y))

    if to_right_8==True and (wc_8==7 or wc_8==8 or wc_8==9):
        win.blit(catto3R,(c_1.x,c_1.y))


        


    if to_right_8==False and (wc_8==1 or wc_8==2 or wc_8==3):
        win.blit(catto1L,(c_1.x,c_1.y))

    if to_right_8==False and (wc_8==4 or wc_8==5 or wc_8==6):
        win.blit(catto2L,(c_1.x,c_1.y))
        
    if to_right_8==False and (wc_8==7 or wc_8==8 or wc_8==9):
        win.blit(catto3L,(c_1.x,c_1.y))




    hit_list = []
    for i in tile_rects_lvl_8:
        if c_1.colliderect(i):
            hit_list.append(i)



    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    
                MS_U_8=False   
            
              

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  
                MS_D_8=False
           
            
             
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:
                MS_L_8=False
               
            
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:
                MS_R_8=False
               
                
                
    if hit_list == []:
        MS_U_8=True
        MS_D_8=True
        MS_L_8=True
        MS_R_8=True
    L=[MS_U_8,MS_D_8,MS_L_8,MS_R_8]
    if L==[False,False,False,False]:
        MS_U_8=True
    if L==[False,False,False,True]:
        MS_D_8=True
    if L==[False,False,True,False]:
        MS_D_8=True
    


    ect_8_1+=1
    ect_8_2+=1
    ect_8_3+=1
    pc_8+=1    

    if key[pygame.K_LEFT] and camOffx_8-velx_789+winW/2>0 and MS_L_8==True:
        wc_8=wc_8+1
        to_right_8=False
        camOffx_8=camOffx_8-velx_789
    if key[pygame.K_RIGHT] and camOffx_8+velx_789+winW/2<45*tile_size and MS_R_8==True:
        wc_8=wc_8+1
        to_right_8=True
        camOffx_8=camOffx_8+velx_789
    if key[pygame.K_DOWN] and MS_D_8==True:
        wc_8+=1
        camOffy_8=camOffy_8+vely_789
    if key[pygame.K_UP] and MS_U_8==True:
        wc_8+=1
        camOffy_8=camOffy_8-vely_789


    ec_hit_list = []
    for i in ec_lvl_8:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
    
    if ec_hit_list != []:
        if 820>ec_hit_list[0][0]-camOffx_8>480 and -125>ec_hit_list[0][1]-camOffy_8>-330:
            Ecat1col_8=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        if -740>ec_hit_list[0][0]-camOffx_8>-960 and -120>ec_hit_list[0][1]-camOffy_8>-305:
            Ecat2col_8=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)

        
        if -915>ec_hit_list[0][0]-camOffx_8>-1250 and 470>ec_hit_list[0][1]-camOffy_8>275:
            Ecat3col_8=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
            
        
        #print(ec_hit_list[0][0]-camOffx_8,ec_hit_list[0][1]-camOffy_8)    

    food_hit_list = []
    for i in food_lvl_8:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:
        if 790>food_hit_list[0][0]-camOffx_8>720 and 780>food_hit_list[0][1]-camOffy_8>620:
            Food1col_8=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -935>food_hit_list[0][0]-camOffx_8>-1045 and -152>food_hit_list[0][1]-camOffy_8>-330:
            Food2col_8=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -1180>food_hit_list[0][0]-camOffx_8>-1290 and 300>food_hit_list[0][1]-camOffy_8>115:
            Food3col_8=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
   

        #print(food_hit_list[0][0]-camOffx_8,food_hit_list[0][1]-camOffy_8)  


    COL_STATES_lives=[Ecat1col_8,Ecat2col_8,Ecat3col_8]
    count_lives_8=count_lives 

    for i in COL_STATES_lives:
        if i==True:
            count_lives_8-=1
    if count_lives_8==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_789()
        
    if count_lives_8==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_8==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_8==1:
        win.blit(heart,(418,380))
    
    portal_hit_list = []
    for i in portal_lvl_8:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_8==True:
        LevelEightCleared=True
        count_lives=count_lives_8
        if music_state==True:
                pygame.mixer.Sound.play(portal_sound)

    COL_STATES_food=[Food1col_8,Food2col_8,Food3col_8]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1:
        win.blit(foodIcon3,(416,360)) 
    if count_food==2:
        win.blit(foodIcon3,(416,360))
        win.blit(foodIcon3,(438,360))
    if count_food==3:
        win.blit(foodIcon3,(416,360))
        win.blit(foodIcon3,(438,360))
        win.blit(foodIcon3,(460,360))
        Portal_Perms_8=True
    if Portal_Perms_8==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_8==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal",black)
       
       
    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 8",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 8 - checkpoint level 7",black)     

    seacret_hit_list = []
    for i in seacret:
        if c_1.colliderect(i):
            seacret_hit_list.append(i)

    if seacret_hit_list != []:
        GotSeacret=True
        if music_state==True:
            pygame.mixer.Sound.play(seacret_sound)
    
    if GotSeacret==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,445),"secret achievement unlocked:",black)
        if s_c+1>96:
            s_c=1
        if s_c<=8:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",red)
        if 8<s_c<=16:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",orange)
        if 16<s_c<=24:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",yellow)
        if 24<s_c<=32:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",green)
        if 32<s_c<=40:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",blue)
        if 40<s_c<=48:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",indigo)
        if 48<s_c<=56:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",violet)
        if 56<s_c<=64:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",black)
        if 64<s_c<=72:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",brown)
        if 72<s_c<=80:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",light_blue)
        if 80<s_c<=88:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",pink)
        if 88<s_c<=96:
            pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(200,445),"roygbivbbt",white)
        s_c+=1
            
   

    pygame.display.update()



def lvl_9(key,c_1):
    global count_death
    global GameModeHard
    global to_right_9
    global MS_U_9
    global MS_D_9
    global MS_L_9
    global MS_R_9
    global wc_9
    global pc_9
    global ect_9_1
    global ect_9_2
    global ect_9_3
    global Ecat1col_9
    global Ecat2col_9
    global Ecat3col_9
    global Food1col_9
    global Food2col_9
    global Food3col_9
    global Portal_Perms_9
    global Portalcol_9
    global LevelNineCleared
    global camOffx_9        
    global camOffy_9

    global count_lives 
  
    c_1.y=winH-cat_H-tile_size
    global music_state
    #global GameOver
    world_9_data=[
        ['0','0','fl3','fl3','fl3','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','fl3','0','0','0','fl3','0','0','0','0','0','0','0','0','0','0','0','1','fl5','f2','fl5','fl5','0','0','fl6','fl6','fl6','fl6','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['fl3','0','0','0','0','0','fl3','0','0','0','0','0','0','0','0','0','0','1','fl6','fl6','fl6','fl6','0','0','fl5','fl5','fl5','fl5','1','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0'],
        ['fl3','0','0','h','h','0','fl3','0','0','0','0','0','0','0','0','0','0','1','fl5','fl5','fl5','fl5','0','0','fl6','fl6','fl6','fl6','1','0','0','0','0','0','0','1','fl7','fl5','fl7','fl5','fl7','fl5','1','0','0'],
        ['fl3','0','0','0','h','h','fl3','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','0','0','1','1','1','1','1','0','0','0','0','0','0','1','fl7','fl5','fl7','fl5','fl7','fl5','1','0','0'],
        ['0','fl3','0','0','0','fl3','0','h','h','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','1','0','0','0','0','0','0','0','0','0','0','1','fl7','fl5','fl7','fl5','fl7','fl5','1','0','0'],
        ['0','0','fl3','fl3','fl3','0','0','0','h','h','h','h','0','0','0','0','0','0','0','0','0','1','0','0','1','0','0','0','0','0','0','0','0','0','0','1','fl7','fl5','fl7','fl5','fl7','fl5','1','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','h','h','h','h','0','0','1','1','1','1','1','0','0','1','1','1','1','1','0','0','0','0','0','0','1','1','1','0','0','1','1','1','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','4','0','0','0','0','0','0','fl7','fl1','fl7','fl1','1','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','fl7','fl1','fl7','fl1','1','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','h','h','5','0','0','0','0','0','0','fl7','fl1','fl7','fl1','1','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0'],
        ['1','1','1','1','1','1','1','1','1','1','0','0','0','0','h','0','0','0','0','0','0','0','0','0','fl7','fl1','fl7','fl1','1','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0'],
        ['1','fl6','fl6','fl6','fl6','fl6','1','fl5','fl5','1','0','0','0','0','h','0','0','1','1','1','1','1','0','0','1','1','1','1','1','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0'],
        ['1','f1','fl7','fl7','fl7','fl7','1','fl5','fl5','1','0','0','0','0','h','0','0','0','0','0','0','1','0','0','1','0','0','0','0','0','0','0','h','h','h','h','h','h','h','h','h','h','h','0','0'],
        ['1','fl6','fl6','fl6','fl6','fl6','0','0','0','2','0','0','0','0','h','0','0','0','0','0','0','1','0','0','1','0','0','0','0','0','0','0','h','0','0','0','h','0','0','0','0','0','h','0','0'],
        ['1','fl7','fl7','fl7','fl7','fl7','0','0','0','0','0','0','0','0','h','0','0','1','1','1','1','1','0','0','1','1','1','1','1','0','0','0','h','0','0','1','6','0','1','0','0','1','7','0','1'],
        ['1','fl6','fl6','fl6','fl6','fl6','0','0','0','3','0','h','h','h','h','0','0','1','fl5','fl5','fl5','fl5','0','0','fl6','fl6','fl6','fl6','1','0','0','0','h','0','0','1','0','0','1','0','0','1','0','0','1'],
        ['1','fl7','fl7','fl7','fl7','fl7','0','0','0','0','0','0','0','0','h','0','0','1','fl6','fl6','fl6','fl6','0','0','fl5','fl5','fl5','fl5','1','0','0','0','h','0','0','1','0','0','1','0','0','1','0','0','1'],
        ['1','fl6','fl6','fl6','fl6','fl6','1','fl5','fl5','1','0','0','0','0','h','0','0','1','fl5','fl5','fl5','fl5','0','0','fl6','fl6','fl6','fl6','1','0','0','0','h','0','0','1','0','0','1','0','0','1','0','0','1'],
        ['1','fl7','fl7','fl7','fl7','fl7','1','fl5','fl5','1','0','0','0','0','h','0','0','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','h','0','0','1','0','0','1','1','1','1','0','0','1'],
        ['1','1','1','1','1','1','1','1','1','1','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','1','fl7','fl7','0','0','0','0','0','0','1'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','h','h','h','0','0','1','fl7','fl7','0','f3','0','0','0','0','1'],
        ['0','0','0','0','fl6','fl6','0','0','0','0','0','0','0','0','h','0','0','0','0','0','0','0','0','0','0','0','h','h','h','h','h','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['0','p','0','0','fl6','fl6','0','0','0','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','1'],
        ['0','0','0','h','h','h','h','h','h','h','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1']]

    win.blit(bg3,(0,0))
    tile_rects_lvl_9=[]
    food_lvl_9=[]
    ec_lvl_9=[]
    portal_lvl_9=[]
    y_1=0
    for row in world_9_data:
        x_1=0
        for tile in row:
            if tile=='fl1':
                win.blit(flower1,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))

            if tile=='fl2':
                win.blit(flower2,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                   
            if tile=='fl3':
                win.blit(flower3,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))   
                    
            if tile=='fl4':
                win.blit(flower4,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))

                        
            if tile=='fl5':
                win.blit(flower5,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))

                        
            if tile=='fl6':
                win.blit(flower6,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))

                        
            if tile=='fl7':
                win.blit(flower7,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))

            if tile=='h':
                win.blit(path2,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                


            
            if tile=='1':
                win.blit(tile3,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                tile_rects_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))



                
            if tile=='f1' and Food1col_9==False :
                win.blit(food3,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                food_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))
            if tile=='f2' and Food2col_9==False :
                win.blit(food3,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                food_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))
            if tile=='f3' and Food3col_9==False :
                win.blit(food3,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                food_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))


            if tile=='p' and pc_9<=8:
                win.blit(portal,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                portal_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))

            if tile=='p' and 8<pc_9<=16:
                win.blit(portal_1,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                portal_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))
            
            if tile=='p' and 16<pc_9<=24:
                win.blit(portal_2,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                portal_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))

            if tile=='p' and 24<pc_9:
                win.blit(portal_3,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                portal_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))



            

            if tile=='2' and  ect_9_1<=54 and Ecat1col_9==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                ec_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size)) 
            if tile=='3' and  ect_9_1>54 and Ecat1col_9==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                ec_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))



            if tile=='4' and  ect_9_2<=54 and Ecat2col_9==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                ec_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size)) 
            if tile=='5' and  ect_9_2>54 and Ecat2col_9==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                ec_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))

            if tile=='6' and  ect_9_3<=54 and Ecat3col_9==False:
                win.blit(evil_catto_R,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                ec_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size)) 
            if tile=='7' and  ect_9_3>54 and Ecat3col_9==False:
                win.blit(evil_catto_L,(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9))
                ec_lvl_9.append(pygame.Rect(x_1*tile_size-camOffx_9,y_1*tile_size-camOffy_9,tile_size,tile_size))
            x_1=x_1+1
        y_1=y_1+1

    if wc_9+1>9:
        wc_9=1

    if ect_9_1>108:
        ect_9_1=1

    if ect_9_2>108:
        ect_9_2=1

    if ect_9_3>108:
        ect_9_3=1
        
    if pc_9+1>32:
        pc_9=1


       

    if to_right_9==True and (wc_9==1 or wc_9==2 or wc_9==3):
        win.blit(catto1R,(c_1.x,c_1.y))

    if to_right_9==True and (wc_9==4 or wc_9==5 or wc_9==6):
        win.blit(catto2R,(c_1.x,c_1.y))

    if to_right_9==True and (wc_9==7 or wc_9==8 or wc_9==9):
        win.blit(catto3R,(c_1.x,c_1.y))


        


    if to_right_9==False and (wc_9==1 or wc_9==2 or wc_9==3):
        win.blit(catto1L,(c_1.x,c_1.y))

    if to_right_9==False and (wc_9==4 or wc_9==5 or wc_9==6):
        win.blit(catto2L,(c_1.x,c_1.y))
        
    if to_right_9==False and (wc_9==7 or wc_9==8 or wc_9==9):
        win.blit(catto3L,(c_1.x,c_1.y))




    hit_list = []
    for i in tile_rects_lvl_9:
        if c_1.colliderect(i):
            hit_list.append(i)



    if hit_list != []:
        for i in range(len(hit_list)):
           
            if hit_list[i][1]<355 and key[pygame.K_UP]:    
                MS_U_9=False   
            
              

            if hit_list[i][1]>420 and key[pygame.K_DOWN]:  
                MS_D_9=False
           
            
             
            if hit_list[i][0]<375 and key[pygame.K_LEFT]:
                MS_L_9=False
               
            
            if hit_list[i][0]>475 and key[pygame.K_RIGHT]:
                MS_R_9=False
               
                
                
    if hit_list == []:
        MS_U_9=True
        MS_D_9=True
        MS_L_9=True
        MS_R_9=True
    L=[MS_U_9,MS_D_9,MS_L_9,MS_R_9]
    if L==[False,False,False,False]:
        MS_U_9=True
    if L==[False,False,False,True]:
        MS_D_9=True
    if L==[False,False,True,False]:
        MS_D_9=True

    


    ect_9_1+=1
    ect_9_2+=1
    ect_9_3+=1
    pc_9+=1    

    if key[pygame.K_LEFT] and camOffx_9-velx_789+winW/2>0 and MS_L_9==True:
        wc_9=wc_9+1
        to_right_9=False
        camOffx_9=camOffx_9-velx_789
    if key[pygame.K_RIGHT] and camOffx_9+velx_789+winW/2<45*tile_size and MS_R_9==True:
        wc_9=wc_9+1
        to_right_9=True
        camOffx_9=camOffx_9+velx_789
    if key[pygame.K_DOWN] and MS_D_9==True:
        wc_9+=1
        camOffy_9=camOffy_9+vely_789
    if key[pygame.K_UP] and MS_U_9==True:
        wc_9+=1
        camOffy_9=camOffy_9-vely_789

    ec_hit_list = []
    for i in ec_lvl_9:
        if c_1.colliderect(i):
            ec_hit_list.append(i)
    
    if ec_hit_list != []:
        if 515>ec_hit_list[0][0]-camOffx_9>280 and 130>ec_hit_list[0][1]-camOffy_9>-115:
            Ecat1col_9=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
        if 105>ec_hit_list[0][0]-camOffx_9>-102 and 405>ec_hit_list[0][1]-camOffy_9>190:
            Ecat2col_9=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
        if -950>ec_hit_list[0][0]-camOffx_9>-1340 and 127>ec_hit_list[0][1]-camOffy_9>-76:
            Ecat3col_9=True
            if music_state==True:
                pygame.mixer.Sound.play(hurt_sound)
           
        #print(ec_hit_list[0][0]-camOffx_9,ec_hit_list[0][1]-camOffy_9)  

    food_hit_list = []
    for i in food_lvl_9:
        if c_1.colliderect(i):
            food_hit_list.append(i)

    if food_hit_list != []:
        if 795>food_hit_list[0][0]-camOffx_9>725 and 230>food_hit_list[0][1]-camOffy_9>70:
            Food1col_9=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -5>food_hit_list[0][0]-camOffx_9>-175 and 730>food_hit_list[0][1]-camOffy_9>669:
            Food2col_9=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
        if -990>food_hit_list[0][0]-camOffx_9>-1170 and -170>food_hit_list[0][1]-camOffy_9>-336:
            Food3col_9=True
            if music_state==True:
                pygame.mixer.Sound.play(eating_sound)
       

        #print(food_hit_list[0][0]-camOffx_9,food_hit_list[0][1]-camOffy_9)  

    COL_STATES_lives=[Ecat1col_9,Ecat2col_9,Ecat3col_9]
    count_lives_9=count_lives  
    
    for i in COL_STATES_lives:
        if i==True:
            count_lives_9-=1
    if count_lives_9==0:
        if GameModeHard==True:
            game_over()
        if GameModeHard==False:
            count_death+=1
            game_over_chp_789()
        
    if count_lives_9==3:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
        win.blit(heart,(458,380))
    if count_lives_9==2:
        win.blit(heart,(418,380))
        win.blit(heart,(438,380))
    if count_lives_9==1:
        win.blit(heart,(418,380))
    
    portal_hit_list = []
    for i in portal_lvl_9:
        if c_1.colliderect(i):
            portal_hit_list.append(i)

    if portal_hit_list != [] and Portal_Perms_9==True:
        LevelNineCleared=True
        count_lives=count_lives_9
        if music_state==True:
                pygame.mixer.Sound.play(portal_sound)


    COL_STATES_food=[Food1col_9,Food2col_9,Food3col_9]
    count_food=0
    for i in COL_STATES_food:
        if i == True:
            count_food+=1
    if count_food==1:
        win.blit(foodIcon3,(416,360)) 
    if count_food==2:
        win.blit(foodIcon3,(416,360))
        win.blit(foodIcon3,(438,360))
    if count_food==3:
        win.blit(foodIcon3,(416,360))
        win.blit(foodIcon3,(438,360))
        win.blit(foodIcon3,(460,360))
        Portal_Perms_9=True
    if Portal_Perms_9==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">colect all the food "+str(count_food)+"/3",black)
    if Portal_Perms_9==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,475),">find the portal - finish the game!",black)
       
       
    if GameModeHard==True:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 9",black)
    if GameModeHard==False:
        pygame.freetype.Font('Assets//8bit16.ttf',10).render_to(win,(0,460),"level 9 - checkpoint level 7",black)     
  
    pygame.display.update()
    
def main():
    global LevelOneCleared
    global LevelTwoCleared
    global LevelThreeCleared
    global LevelFourCleared
    global LevelFiveCleared
    global LevelSixCleared
    global LevelSevenCleared
    global LevelEightCleared
    global LevelNineCleared
##    global GameOver
    clock=pygame.time.Clock()    
    run=True
    c_1=pygame.Rect(winW/2-cat_W/2,winH-cat_H-tile_size,cat_W,cat_H)  

  
   
    if music_state==True:
        pygame.mixer.music.play(-1)    
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False



                
        COMPLETED_LEVELS=[LevelOneCleared,LevelTwoCleared,LevelThreeCleared,LevelFourCleared,LevelFiveCleared,LevelSixCleared,LevelSevenCleared,LevelEightCleared,LevelNineCleared]
        PASS=0
        for i in COMPLETED_LEVELS:
            if i==True:
                PASS+=1
        if PASS==0 :
            key=pygame.key.get_pressed()
            lvl_1(key,c_1)                         

        if PASS==1:
            key=pygame.key.get_pressed()
            lvl_2(key,c_1)
        if PASS==2:
            key=pygame.key.get_pressed()
            lvl_3(key,c_1)
        if PASS==3:
            key=pygame.key.get_pressed()
            lvl_4(key,c_1)
        if PASS==4:
            key=pygame.key.get_pressed()
            lvl_5(key,c_1)
        if PASS==5:
            key=pygame.key.get_pressed()
            lvl_6(key,c_1)
        if PASS==6:
            key=pygame.key.get_pressed()
            lvl_7(key,c_1)
        if PASS==7:
            key=pygame.key.get_pressed()
            lvl_8(key,c_1)
        if PASS==8:
            key=pygame.key.get_pressed()
            lvl_9(key,c_1)
        if PASS==9:
            game_completed()
            
        key=pygame.key.get_pressed()
        start_pause(key)
        
    




##        key=pygame.key.get_pressed()     #TESTIRANJE !!!!!!!!!!!!!!!
##        lvl_8(key,c_1)  
##        
##       


     



      
            
    pygame.quit()
    sys.exit()
game_intro()

