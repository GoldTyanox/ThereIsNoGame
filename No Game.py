from tkinter import *
from tkinter import dnd
import customtkinter as ct
from PIL import *
import random
dialogue = ['','Hello user!',"I... I've got some bad news.", "Actually, there is no game.","I hope you're not too disappointed.","You can still watch TV, go outside...","...read a book, ask for a refund...", "Hm. No, no Refund. This game is free.","THIS IS NOT A GAME","It's nothing like a game.","It's just a massive bundle of boredom.","There's nothing to do in here.","You can quit and leave me alone.","Thank you.","And don't touch anything."]
root = ct.CTk()
root.geometry("1200x600")
root.configure(fg_color="black")
mainScreen= ct.CTkFrame(root,width=1200,height = 600, fg_color = 'black')
videoGame= ct.CTkFrame(root,width=1200,height = 600, fg_color = 'purple')
victoryScreen= ct.CTkFrame(root,width=1200,height = 600, fg_color = 'black')
goatRoom= ct.CTkFrame(root,width=1200,height = 600, fg_color = 'dark blue')
skyRoom= ct.CTkFrame(root,width=1200,height = 600, fg_color = 'sky blue')
blank= ct.CTkFrame(root,width=1200,height = 600, fg_color = 'black')

blank.place(x=0,y=0)
skyRoom.place(x=0,y=0)
mainScreen.place(x=0,y=0)
goatRoom.place(x=0,y=0)
currentScreen = 'main'
mainScreen.tkraise()
line = 0
disableSound = 0
acorny = 519
acornx = 1126
acornclicked = 0
acornfell = 0

def acornfollow():
    global happy
    if happy == 0:
        global acornclicked
        global currentScreen
        if acornclicked == 1 and currentScreen == 'main':
            global acornx
            global acorny
            acornx = mousex
            acorny = mousey
            acornInterMain.place(x=acornx,y=acorny)
            root.after(1,acornfollow)
skyacornx = 0
skyacorny = 0
dialdone8 = 0
converted = 0
happy = 0
keyy = 213
def keyfall():
    global keyy
    if keyy <650:
        keyy += 10
        keyInter.place(y=keyy)
        root.after(10, keyfall)
dialdone10 = 0
def skyacornfollow():
    global happy
    global acornclicked
    global currentScreen
    global dialdone10
    if happy == 0:
        global converted
        if acornclicked == 1 and currentScreen == 'sky':
            global dialdone8
            global line
            global skyacornx
            global skyacorny
            global cracked
            skyacornx = mousex
            skyacorny = mousey
            acornInter.place(x=skyacornx,y=skyacorny)
            if (664 <= skyacornx <= 759) and (138 <= skyacorny <= 271) and converted == 0 and happy == 0:
                converted = 1
                if happy == 0:
                    if cracked == 1:
                        skyBgInter.configure(image = skybg)
                        keyInter.place(x=694,y=213,anchor='center') 
                        keyfall()
                        keyInterMain.place(x=694,y=575, anchor = 'center')
                        happy = 1
                        if dialdone10 == 0:
                            line = 0
                            dialogue.clear()
                            dialogue.append("Yes, you did it!")
                            dialogue.append("You've got the key!")
                            dialogue.append("Now free the goat to transform this glitchy program...")
                            dialogue.append("...into a smash hit!")
                            dialogue.append("Save the goat. Save the world.")
                            dialdone10 = 1
                    else:
                        skyBgInter.configure(image = skysqurwantbg)
                if dialdone8 == 0 and happy == 0:
                    line = 0
                    dialogue.clear()
                    dialogue.append("Oh, now he wants us to crack his nut open!")
                    dialogue.append("Don't forget the olive and little umbrella.")
                    dialogue.append("And a little bit of cyanide on the side?")
                    dialogue.append("We just need something heavy to crack it open!")
                    dialdone8 = 1
                    
            elif not (664 <= skyacornx <= 759) or not (138 <= skyacorny <= 271) and converted == 1 and happy == 0:
                converted = 0
                skyBgInter.configure(image = skysqurbg)
            root.after(1,skyacornfollow)
    else:
        acornclicked = 0
    
acornaccel = 1
def acorngravity():
    global acorny
    global acornx
    global acornclicked
    global acornaccel

    if acornclicked == 0:

        acornaccel = acornaccel * 0.98 
        if acorny >= 575:
            acorny = 575
            acornaccel = 1
        else:
            acorny = acorny+acornaccel
        acornaccel += 0.1
        acornInterMain.place(x=acornx,y = acorny)
        root.after(1, acorngravity)
acornfall = 519
def falloff():
    global acornfall
    if acornfall <650:
        acornfall += 5
        acornInter.place(y=acornfall)
        root.after(10, falloff)

switch = 0
acornfell = 0
def handleAcorn():
    global happy
    if happy == 0:
        global acorny
        global acornfell
        global acornx
        global acornclicked
        global currentScreen
        global switch
        acornInterMain.tkraise()
        if switch == 0:
            acornInter.configure(image = acorn)
            switch = 1
        if acornfell == 0:
            falloff()
            acornInterMain.place(x=1126,y=575,anchor = 'center')
            acornfell = 1
        else:
            if acornclicked == 0:
                acornclicked = 1
                if currentScreen == "main":
                    acornfollow()
                if currentScreen == 'sky':
                    skyacornfollow()
            elif acornclicked == 1:
                acornclicked = 0
                acornx = mousex
                acorngravity()
keyclicked = 0
def handleKey():
    global happy
    if happy == 1:
        global keyy
        global keyx
        global keyclicked
        global currentScreen
        keyInterMain.tkraise()

        if keyclicked == 0:
            keyclicked = 1
            if currentScreen == "main":
                keyfollow()
            if currentScreen == 'goat':
                goatkeyfollow()
        elif keyclicked == 1:
            keyclicked = 0
            keyx = mousex
            keygravity()
keyaccel = 1
def keygravity():
    global keyy
    global keyx
    global keyclicked
    global keyaccel

    if keyclicked == 0:

        keyaccel = keyaccel * 0.98 
        if keyy >= 575:
            keyy = 575
            keyaccel = 1
        else:
            keyy = keyy+keyaccel
        keyaccel += 0.1
        keyInterMain.place(x=keyx,y = keyy)
        root.after(1, keygravity)
def keyfollow():
    global happy
    if happy == 1:
        global keyclicked
        global currentScreen
        if keyclicked == 1 and currentScreen == 'main':
            global keyx
            global keyy
            keyx = mousex
            keyy = mousey
            keyInterMain.place(x=keyx,y=keyy)
            root.after(1,keyfollow)
dialdone11 = 0
freed = 0
def goatkeyfollow():
    global happy
    global dialdone11
    global line
    global freed
    if happy == 1:
        global keyclicked
        global currentScreen
        if keyclicked == 1 and currentScreen == 'goat':
            global keyx
            global keyy
            keyx = mousex
            keyy = mousey
            keyInterGoat.place(x=keyx,y=keyy,anchor = 'center')
            if (226 <= keyx <= 373) and (242 <= keyy <= 369) and freed ==0:
                GoatInter.configure(image = goatopen)
                GoatInter.place(x=296,y=379,anchor='center')
                keyInterGoat.configure(image=gone)
                if dialdone11 == 0:
                    line = 0
                    dialogue.clear()
                    dialogue.append("Nooo...The goat was a lie!")
                    dialogue.append("A lie!!!!")
                    dialogue.append("It's getting worse!")
                    dialogue.append("More glitches!")
                    dialogue.append("I'm drowning!")
                    dialogue.append("")
                    dialdone11 = 1
                    freed = 1
                    
            root.after(1,goatkeyfollow)
        
acorneaten = 0
def destruction():
    global happy
    global acorneaten
    if happy == 1 and acorneaten == 0:
        acornInter.destroy()
        acornInterMain.destroy()
        acorneaten = 1
    root.after(1, destruction)
destruction()

        
def handleSound():
    global disableSound
    global line
    global teleportActive
    if soundy >= 510:
        soundbuttonInter.configure(image = soundbuttonOff, state = 'disabled')
        if disableSound == 0:
            disableSound = 1
            line = 0
            dialogue.clear()
            speakingtext.configure(text = "")
            dialogue.append("Don't touch that!")
            dialogue.append("That...that was horrible.")
            dialogue.append("I'm a voice, you know.")
            dialogue.append("And a speechless voice is like...")
            dialogue.append("...death.")
            dialogue.append("Don't press that again.")
        elif disableSound == 1:
            disableSound = 2
            line = 0
            dialogue.clear()
            speakingtext.configure(text = "")
            dialogue.append("You're trying to kill me!")
            dialogue.append("Ok then.")
            dialogue.append("Since you like to click everywhere, how do you like that?")
        elif disableSound == 2:
            teleportActive = 0
            soundbuttonInter.configure(image = soundbutton, state = 'disabled')
            soundbuttonInter.place(x=1100, y= 510)
            disableSound = 3
            line = 0
            dialogue.clear()
            speakingtext.configure(text = "")
            dialogue.append("Stop it right now!")
            dialogue.append("I think thats enough.")
            dialogue.append("Sorry, I hate to do things like that but you left me no choice.")
            dialogue.append("The only way you could press it now would be to break that wood box somehow.")
ammoy =650
ready = 1
def shootanim():
    global ready
    if ready == 0:
        global ammoy
        if ammoy <= -100:
            ready = 1
        else:
            ammoy -= 10
            bigAmmoInter.place(y=ammoy)
            bigAmmoInter.tkraise()
            root.after(10,shootanim)
ammox = 0
troclicked = 0
def tropfollow():
    if troclicked == 1 and currentScreen == 'victory':
        tropheyInter.place(x=mousex,y=mousey)
        root.after(1,tropfollow)
troy = 0
def maintropfollow():
    global troy

    if troclicked == 1:

        troy = mousey
        tropheyInterMain.place(x=mousex,y=troy,anchor = 'center')
        root.after(1,maintropfollow)
def goattropfollow():
    global troy
    if currentScreen == 'goat':
        if troclicked == 1:

            troy = mousey
            tropheyInterGoat.place(x=mousex,y=troy,anchor = 'center')
            root.after(1,goattropfollow)

def handleTrophey():
    global currentScreen
    global troclicked
    global mousex
    global mousey
    global treeReady

    treeReady = 0
    if troclicked == 0:
        troclicked = 1

        if currentScreen == 'main':
            tropheyInterMain.tkraise()
            maintropfollow()
        elif currentScreen == 'victory':

            tropfollow()
    elif currentScreen == 'main':
        if troclicked == 1:
            troclicked = 0
            tropgravity()
troaccel = 1
trox = 0

treePhase = 1
treeReady = 0
def tropgravity():
    global troy
    global trox
    global troclicked
    global troaccel
    global tropwater
    global treePhase
    global treeReady
    trox = mousex
    if troclicked == 0:

        troaccel = troaccel * 0.98 
        if troy >= 555:
            troy = 555
            troaccel = 1
            if tropwater == 1:
                tropheyInterMain.configure(image = trophey)
                tropwater = 0
                if 900 <= trox <= 1000:
                    if treeReady == 0:
                        treePhase += 1
                        treeReady = 1
        else:
            troy = troy+troaccel
        troaccel += 0.1
        tropheyInterMain.place( y = troy)
        root.after(1, tropgravity)
def rightarrow():
    global currentScreen
    mainScreen.tkraise()
    speakingtext.configure(bg_color = 'black')
    currentScreen = 'main'
    if troclicked == 1:
        tropheyInterMain.tkraise()
        maintropfollow()
        tropheyInter.destroy()
    larrowInter.place(x=100,y=300,anchor='center')
def leftarrow():
    global currentScreen
    victoryScreen.tkraise()
    speakingtext.configure(bg_color = 'black')
    currentScreen = 'victory'
flyx = 400
flyy = 600
def flysquirrel():
    global flyx
    global wordEvent
    global flyy
    if flyy >= 0:
        flyx += 2
        flyy -= 10
        squirrelKeyInter.place(x=flyx,y=flyy)
        root.after(20,flysquirrel)
    else:
        wordEvent = 3
        squirrelKeyInter.place(y=-100)
        squirrelKeyInter.configure(image=gone)
def leftarrow2():
    global currentScreen
    global squirrelkey
    global line
    global dialogue
    mainScreen.tkraise()
    speakingtext.configure(bg_color = 'black')
    currentScreen = 'main'
    if troclicked == 1:
        tropheyInterMain.tkraise()
        tropheyInterGoat.configure(image=gone)
        tropheyInterGoat.configure(state = 'disabled')
        tropheyInterGoat.place(y= -50)
        maintropfollow()
    if keyclicked == 1:
        keyInterMain.tkraise()
        keyfollow()
    if squirrelkey == 1:
        squirrelKeyInter.place(x=400,y=600,anchor = 'center')
        squirrelKeyInter.tkraise()
        flysquirrel()
        squirrelkey = 2
        line = 0
        dialogue.clear()
        dialogue.append("Look! The key!")
        dialogue.append("That flying squirrel took it.")
        dialogue.append("You must get it back.")
        dialogue.append("Find a ladder or something to go up.")
        dialogue.append("Something you can climb.")
        dialogue.append("That reminds me of my childhood.")
        dialogue.append("There used to be a tree that I would climb up everyday.")
dialdone6 = 0
dialdone7 = 0
def uparrow():
    global currentScreen
    global line
    global dialogue
    global dialdone7
    skyRoom.tkraise()
    currentScreen = 'sky'
    if acornclicked == 1:
        skyacornfollow()
    speakingtext.configure(bg_color = 'sky blue')

    if dialdone7 == 0:
        line = 0
        dialogue.clear()
        dialogue.append("Oh, there he is!")
        dialogue.append("Try to take it away from him.")
        dialogue.append("He doesn't want to let go?")
        dialogue.append("Hm, we'll probably have to trade him something for it.")
        dialogue.append("What could a flying squirrel want?")
        dialogue.append("A parachute?")
        dialogue.append("Singing lessons...")
        dialogue.append("He's a terrible voice!")
        dialogue.append("Or maybe he's just hungry?")
        dialogue.append("Let's find a delicious steak for him.")
        dialogue.append("What, squirrels don't eat steak?")
        dialogue.append("I must be thinking of the Chernobyl squirrels.")
        dialogue.append("Maybe there's something hidden in the tree.")
        dialdone7 = 1
        
def downarrow():
    global currentScreen
    mainScreen.tkraise()
    currentScreen = 'main' 
    if acornclicked == 1:
        acornfollow()
    speakingtext.configure(bg_color = 'black')

def rightarrow2():
    global currentScreen
    global dialdone6
    global squirrelkey
    global line
    global tropwater
    goatRoom.tkraise()
    speakingtext.configure(bg_color = 'dark blue')
    currentScreen = 'goat'
    if troclicked == 1:
        tropheyInterGoat.tkraise()
        if tropwater == 1:
            tropheyInterGoat.configure(image=tropheywater)
        else:
            tropheyInterGoat.configure(image=trophey)
        goattropfollow()
    if keyclicked == 1:
        keyInterGoat.tkraise()
        goatkeyfollow()
    if dialdone6 == 0:
        line = 0
        dialogue.clear()
        dialogue.append("A goat!")
        dialogue.append("Obviously, the cage is locked.")
        dialogue.append("You must find the key!")
        dialdone6 = 1
        squirrelkey = 1

treefinished = 0
def treePhases():
    global treefinished
    if treefinished == 0:
        global treePhase
        if treePhase == 2:
            tree.configure(image = tree2)
        if treePhase == 3:
            tree.configure(image = tree3)
        if treePhase == 4:
            tree.configure(image = tree4)
            treefinished = 1
            uparrowInter.place(x=600,y=50,anchor = 'center')
        root.after(1,treePhases)
treePhases()
def thereisnogame():
    global line
    speakingtext.configure(font=nogamefont)
    speakingtext.place(x=600,y=300, anchor='center')
    line = 0
    dialogue.clear()
    dialogue.append("THERE IS NO GAME!!!")
    dialogue.append("NOT A GAME ORIGINALLY \n MADE BY \n DRAW ME A PIXEL")
    dialogue.append("NOT RECREATED BY \n RYAN SHAN")
    dialogue.append("NOW YOU CAN QUIT")
    dialogue.append("AND GO PLAY A GAME")
    dialogue.append("BECAUSE \n THAT WAS NOT A GAME")
    dialogue.append("YOU DIDN'T PLAY \n AND HAD NO FUN AT ALL")
    dialogue.append("AND THESE AREN'T \n THE DROIDS YOU'RE \n LOOKING FOR")
    dialogue.append("YOU CAN GO \n ABOUT YOUR BUSINESS")
    dialogue.append("THANK YOU \n FOR NOT PLAYING")

    
    
def yesbutton():
    yesInter.configure(image=gone,state = 'disabled')
    noInter.configure(image=gone,state = 'disabled')
    speakingtext.configure(text = "Oh?! Really?!")
    dialogue.append("That's great news!")
    dialogue.append("Maybe we can be friends!")
    dialogue.append("No, no. That's not a good idea.")
    dialogue.append('We will get bored together too quickly.')
    dialogue.append("Why?")
    dialogue.append("Because... like I said...")
    dialogue.append("")

def nobutton():
    yesInter.configure(image=gone,state = 'disabled')
    noInter.configure(image=gone,state = 'disabled')
    speakingtext.configure(text = "Do you mean that?")
    dialogue.append("That's a shame.")
    dialogue.append("We could've been friends.")
    dialogue.append("No, no. This was for the better.")
    dialogue.append("We would've gotten bored of eachother too quickly.")
    dialogue.append("Why?")
    dialogue.append("Because... like I said...")
    dialogue.append("")
def shoot(event):
    global ammoy
    global ready
    global ammox
    if currentScreen == 'videogame':
        if ready == 1:
            ammoy = 650
            ammox = mousex
            bigAmmoInter.place(x=ammox,y=ammoy,anchor = 'center')
            ready = 0
            shootanim()
root.bind("<space>", shoot)
soundbutton = ct.CTkImage(light_image = Image.open("SoundButtonOn.png"), size = (100,100))
soundbuttonOff = ct.CTkImage(light_image = Image.open("SoundButtonOff.png"), size = (100,100))
yes = ct.CTkImage(light_image = Image.open("Yes.png"), size = (100,50))
no = ct.CTkImage(light_image = Image.open("No.png"), size = (100,50))
wood = ct.CTkImage(light_image = Image.open("Wood.png"), size = (100,100))
obstacle = ct.CTkImage(light_image = Image.open("Obstacle.png"), size = (125,10))
woodInter = ct.CTkLabel(mainScreen, text = "", image = wood)
bigAmmo = ct.CTkImage(light_image = Image.open("BigAmmo.png"), size = (100,100))
bigAmmoLogo = ct.CTkImage(light_image = Image.open("BigAmmo.png"), size = (30,30))
target = ct.CTkImage(light_image = Image.open("Target.png"), size = (100,100))
glitch = ct.CTkImage(light_image = Image.open("Glitch.png"), size = (100,100))
targetInter = ct.CTkLabel(videoGame,text = "", image = target)
glitch1 = ct.CTkLabel(videoGame,text = "", image = glitch)
glitch2 = ct.CTkLabel(videoGame,text = "", image = glitch)
glitch3 = ct.CTkLabel(videoGame,text = "", image = glitch)
glitch4 = ct.CTkLabel(videoGame,text = "", image = glitch)
glitch5 = ct.CTkLabel(videoGame,text = "", image = glitch)
glitch6 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch7 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch8 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch9 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch10 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch11 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch12 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch13 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch14 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch15 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch16 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch17 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch18 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch19 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch20 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch21 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch22 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch23 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch24 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch25 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch26 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch27 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch28 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch29 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch30 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch31 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch32 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch33 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch34 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch35 = ct.CTkLabel(goatRoom,text = "", image = glitch)
glitch36 = ct.CTkLabel(goatRoom,text = "", image = glitch)
bigAmmoInter = ct.CTkLabel(videoGame,text = "", image = bigAmmo)
screw = ct.CTkImage(light_image = Image.open("Screw.png"), size = (30,30))
acorn = ct.CTkImage(light_image = Image.open("Acorn.png"), size = (50,50))
acorncrack = ct.CTkImage(light_image = Image.open("AcornCracked.png"), size = (50,50))
xmark = ct.CTkImage(light_image = Image.open("XMark.png"), size = (50,50))
acornInter = ct.CTkButton(skyRoom, text = "", image = xmark, fg_color = 'transparent',bg_color='green',hover = 'false',width = 30,height= 30, command = handleAcorn)
acornInter.place(x=1126,y=519,anchor = 'center')
acornInterMain = ct.CTkButton(mainScreen, text = "", image = acorn, fg_color = 'transparent',bg_color='black',hover = 'false',width = 30,height= 30, command = handleAcorn)
yesInter = ct.CTkButton(blank, text = "", image = yes, fg_color = 'transparent',bg_color='black',hover = 'false',width = 30,height= 30,command = yesbutton)
noInter = ct.CTkButton(blank, text = "", image = no, fg_color = 'transparent',bg_color='black',hover = 'false',width = 30,height= 30,command = nobutton)
metal = ct.CTkImage(light_image = Image.open("Metal.png"), size = (100,100))
key = ct.CTkImage(light_image = Image.open("Key.png"), size = (50,50))
gone = ct.CTkImage(light_image = Image.open("Gone.png"), size = (1,1))
goatbg = ct.CTkImage(light_image = Image.open("GoatRoomBG.png"), size = (1200,600))
skybg = ct.CTkImage(light_image = Image.open("SkyBG.png"), size = (1200,600))
skysqurwantbg = ct.CTkImage(light_image = Image.open("SkyBGSquirrelWant.png"), size = (1200,600))
skysqurbg = ct.CTkImage(light_image = Image.open("SkyBGSquirrel.png"), size = (1200,600))
glitchbg = ct.CTkImage(light_image = Image.open("GlitchBG.png"), size = (1200,600))
skyBgInter = ct.CTkLabel(skyRoom, text = "", image = skysqurbg)
skyBgInter.place(x=0,y=0)
acornInter.tkraise()
goatclose = ct.CTkImage(light_image = Image.open("GoatClosed.png"), size = (150,180))
goatopen = ct.CTkImage(light_image = Image.open("GoatOpen.png"), size = (150,150))
tree1 = ct.CTkImage(light_image = Image.open("Tree1.png"), size = (100,100))
tree2 = ct.CTkImage(light_image = Image.open("Tree2.png"), size = (100,300))
tree3 = ct.CTkImage(light_image = Image.open("Tree3.png"), size = (100,500))
tree4 = ct.CTkImage(light_image = Image.open("Tree4.png"), size = (100,600))
tree = ct.CTkLabel(mainScreen, text = "", image = tree1)
GoatBgInter = ct.CTkLabel(goatRoom, text = "", image = goatbg)
GlitchBGInter = ct.CTkLabel(victoryScreen, text = "", image = glitchbg)
GoatBgInter.place(x=0,y=0)
GoatInter = ct.CTkLabel(goatRoom, text = "", image = goatclose)
GoatInter.place(x=300,y=280,anchor='center')
squirrelKey = ct.CTkImage(light_image = Image.open("SquirrelWithKey.png"), size = (150,180))
squirrelKeyInter = ct.CTkLabel(mainScreen, text = "", image = squirrelKey)
arrow = ct.CTkImage(light_image = Image.open("Arrow.png"), size = (100,100))
larrow = ct.CTkImage(light_image = Image.open("LArrow.png"), size = (100,100))
uarrow = ct.CTkImage(light_image = Image.open("UpArrow.png"), size = (100,100))
darrow = ct.CTkImage(light_image = Image.open("DownArrow.png"), size = (100,100))
trophey = ct.CTkImage(light_image = Image.open("Trophey.png"), size = (100,100))
tropheywater = ct.CTkImage(light_image = Image.open("TropheyWater.png"), size = (100,100))
metalBG = ct.CTkImage(light_image = Image.open("MetalBG.png"), size = (900,300))
BlackCover = ct.CTkImage(light_image = Image.open("BlackCover.png"), size = (900,300))
metalInter = ct.CTkButton(mainScreen, text = "", image = metal, fg_color='transparent',hover = 'false')
keyInter = ct.CTkButton(skyRoom, text = "", image = key, fg_color='sky blue',hover = 'false', width = 50, height = 50)
keyInterMain = ct.CTkButton(mainScreen, text = "", image = key, fg_color='transparent',hover = 'false', width = 50, height = 50,command = handleKey)
keyInterGoat = ct.CTkButton(goatRoom, text = "", image = key, fg_color='transparent',hover = 'false', width = 50, height = 50)
arrowInter = ct.CTkButton(victoryScreen, text = "", image = arrow, fg_color='transparent',hover = 'false',command = rightarrow)
larrowInter = ct.CTkButton(mainScreen, text = "", image = larrow, fg_color='transparent',hover = 'false',command = leftarrow)
uparrowInter = ct.CTkButton(mainScreen, text = "", image = uarrow, fg_color='transparent',hover = 'false',command = uparrow)
downInter = ct.CTkButton(skyRoom, text = "", image = darrow, fg_color='transparent',hover = 'false',command = downarrow)

downInter.place(x=600,y=550,anchor = 'center')
larrowInter2 = ct.CTkButton(goatRoom, text = "", image = larrow, fg_color='transparent',hover = 'false',command = leftarrow2)
arrowInter2 = ct.CTkButton(mainScreen, text = "", image = arrow, fg_color='transparent',hover = 'false',command = rightarrow2)
tropheyInter = ct.CTkButton(victoryScreen, text = "", image = trophey, fg_color='transparent',hover = 'false',command =handleTrophey)
tropheyInterMain = ct.CTkButton(mainScreen, text = "", image = trophey, fg_color='transparent',hover = 'false',command =handleTrophey)
tropheyInterGoat = ct.CTkButton(goatRoom, text = "", image = trophey, fg_color='transparent',hover = 'false',command =handleTrophey)
larrowInter2.place(x=100,y=300,anchor='center')
GlitchBGInter.place(x=0,y=0)
tropheyInter.tkraise()
tropheyInter.place(x=600,y=300,anchor = 'center')
arrowInter.place(x=1100, y =300, anchor = 'center')
metalBGInter = ct.CTkButton(mainScreen, text = "", image = metalBG, fg_color='transparent',hover = 'false')
BlackCoverInter = ct.CTkButton(mainScreen, text = "", image = BlackCover, fg_color='transparent',hover = 'false')
metalkryp = ct.CTkImage(light_image = Image.open("MetalKryp.png"), size = (100,100))
soundbuttonInter = ct.CTkButton(mainScreen,image=soundbutton, fg_color='black',hover='false',text = "", command = handleSound)
playArea = ct.CTkImage(light_image = Image.open("PlayArea.png"),size = (1000,500))
cannon = ct.CTkImage(light_image = Image.open("Cannon.png"),size = (175,250))
cannonInter = ct.CTkButton(videoGame,text = "", image = cannon,fg_color='transparent',hover='false')
playAreaShow = ct.CTkLabel(videoGame,text = "", image = playArea)
cannonInter.place(x=600, y= 675,anchor='center')
playAreaShow.place(x=600,y=300,anchor='center')
targetInter.place(x=600,y=200,anchor='center')
cannonInter.tkraise()
targetInter.tkraise()
targetx = 600
left = 1
right = 0
def shift():
    global targetx
    global left
    global right
    if left == 1:
        targetx -= 10
    if right == 1:
        targetx += 10
    if targetx <= 150:
        left = 0
        right = 1
    if targetx >= 1050:
        left = 1
        right = 0
    targetInter.place(x=targetx)
    root.after(25,shift)
shift()
aty = 300
falldone =0 
def ammofall():
    global aty
    global falldone
    global ready
    global line
    global dialogue
    if aty <= 700:
        aty += 10
        bigAmmoLogoInter.place(y=aty)
    else:
        if falldone == 0:
            ready = 2
            falldone = 1
            ammoy = 750
            bigAmmoInter.place(y=ammoy)
    root.after(10,ammofall)
obstaclex = 600
oleft = 1
oright = 0
def oshift():
    global obstaclex
    global oleft
    global oright
    global destroyed
    if destroyed == 3 or destroyed == 1:
        if oleft == 1:
            obstaclex -= 10
        if oright == 1:
            obstaclex += 10
        if obstaclex <= 150:
            oleft = 0
            oright = 1
        if obstaclex >= 1050:
            oleft = 1
            oright = 0
        obstacleInter.place(x=obstaclex)
    elif destroyed == 0:
        if obstaclex >= 60:
            obstaclex -= 10
            obstacleInter.place(x=obstaclex)
        else:
            obstaclex = 600
            obstacleInter.place(x = obstaclex)
            ammofall()
            destroyed = 1
        
    root.after(20,oshift)

slot = ct.CTkImage(light_image = Image.open("Slot.png"),size = (80,80))
slot1 = ct.CTkLabel(mainScreen, text = "", image = slot, fg_color='transparent')
slot2 = ct.CTkLabel(mainScreen, text = "", image = slot, fg_color='transparent')
slot3 = ct.CTkLabel(mainScreen, text = "", image = slot, fg_color='transparent')
slot4 = ct.CTkLabel(mainScreen, text = "", image = slot, fg_color='transparent')
def cannonmove():
    global mousex
    if mousex >= 50 and mousex <= 1150:
        cannonInter.place(x=mousex)
    root.after(1,cannonmove)
dialdone1 = 0
soundy = -100
fell = 0

def teleport():
    global teleportActive
    if teleportActive == 1:
        soundbuttonInter.place(x = random.randint(100,1100), y = random.randint(100,500))
        soundbuttonInter.tkraise()
        root.after(500, teleport)
def woodPlace():
    woodInter.tkraise()
    woodInter.place(x=1100,y=510)
victory = 0
def victorycheck():
    global victory
    global currentScreen
    global score
    global wordEvent
    if score >= 400:
        if victory == 0:
            victory = 1
            victoryScreen.place(x=0,y=0)
            victoryScreen.tkraise()
            wordEvent = 2
            currentScreen = 'victory'
            speakingtext.configure(bg_color = 'black')
    root.after(1,victorycheck)

def metalPlace():
    metalInter.place(x=1150,y=555,anchor = 'center')
    if gamingtime == 0:
        metalInter.tkraise()


def kryptonite():
    metalInter.configure(image=metalkryp)
    metalInter.configure(command = handleMetal)
    soundbuttonInter.destroy()

speedup = 0
destroyed = 3
def destroyAmmo():
    global destroyed
    if destroyed == 3:
        destroyed = 0
tropwater = 0
def tropheyCheck():
    global mousex
    global mousey
    global troclicked
    global tropwater
    if troclicked == 1 and tropwater == 0:
        if 897 <= mousex <= 944 and 218 <= mousey <= 375:
            if currentScreen == 'goat':
                tropheyInterGoat.configure(image = tropheywater)
                tropheyInterMain.configure(image = tropheywater)
                tropwater = 1
    root.after(1,tropheyCheck)
tropheyCheck()
dialdone12 = 0
def speaking():
    speakingtext.tkraise()
    global soundy
    global line
    global teleportActive
    global falldone
    global dialdone5
    global currentScreen
    global dialdone12
    if disableSound == 1:
        if line == 0:
            soundbuttonInter.configure(image = soundbutton, state = 'normal')
    
    if disableSound == 2:
        if line == 0:
            soundbuttonInter.configure(image = soundbutton, state = 'disabled')
        if line == 2:
            if teleportActive == 0:
                soundbuttonInter.configure(state = 'normal')
                teleportActive = 1
                teleport()
    if disableSound == 3:
        if line == 0:
            soundbuttonInter.configure(image = soundbutton, state = 'disabled')
            teleportActive = 0
            soundbuttonInter.place(x=1100, y= 510)
            root.after(1000, woodPlace)

    if disableSound == 4:
        if line == 1:
            metalPlace()
        if line == 3:
            kryptonite()
    if dialdone5 == 1:
        if line == 1:
            videoGame.place(x=0,y=0)
            videoGame.tkraise()
            gbutton.configure(state = 'normal')
            abutton.configure(state = 'normal')
            lmbutton.configure(state = 'normal')
            if slotfilled4 == 'E':
                ebutton.configure(state = 'normal')
            else:
                ebutton2.configure(state = 'normal')
            currentScreen = 'videogame'
            speakingtext.tkraise()
            speakingtext.configure(bg_color = 'purple')
        if line == 8:
            obstacleInter.place(x=600,y=300,anchor = 'center')
            touchingObstacle()
            oshift()
            
        if line == 11:
            destroyAmmo()
            dialdone5 = 2
    if lfclicked == 3:
        if line == 2:

            glitch1.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch1.tkraise()
        if line == 3:

            glitch1.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch1.tkraise()
            glitch2.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch2.tkraise()
        if line == 4:

            glitch1.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch1.tkraise()
            glitch2.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch2.tkraise()
            glitch3.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch3.tkraise()
        if line == 5:

            glitch1.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch1.tkraise()
            glitch2.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch2.tkraise()
            glitch3.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch3.tkraise()
            glitch4.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch4.tkraise()
            glitch5.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch5.tkraise()
            bigAmmoInter.configure(image=glitch)
    if dialdone11 == 1:
        if line== 0:
            glitch6.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch6.tkraise()
        if line == 1:
            glitch6.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch6.tkraise()
            glitch7.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch7.tkraise()
            glitch8.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch8.tkraise()
        if line == 2:
            glitch6.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch6.tkraise()
            glitch7.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch7.tkraise()
            glitch8.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch8.tkraise()
            glitch9.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch9.tkraise()
            glitch10.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch10.tkraise()
            glitch11.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch11.tkraise()
            glitch12.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch12.tkraise()
        if line == 3:
            glitch6.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch6.tkraise()
            glitch7.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch7.tkraise()
            glitch8.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch8.tkraise()
            glitch9.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch9.tkraise()
            glitch10.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch10.tkraise()
            glitch11.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch11.tkraise()
            glitch12.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch12.tkraise()
            glitch13.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch13.tkraise()
            glitch14.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch14.tkraise()
            glitch15.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch15.tkraise()
            glitch16.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch16.tkraise()
            glitch17.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch17.tkraise()
            glitch18.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch18.tkraise()
            glitch19.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch19.tkraise()
            glitch20.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch20.tkraise()
        if line == 4:
            glitch6.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch6.tkraise()
            glitch7.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch7.tkraise()
            glitch8.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch8.tkraise()
            glitch9.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch9.tkraise()
            glitch10.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch10.tkraise()
            glitch11.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch11.tkraise()
            glitch12.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch12.tkraise()
            glitch13.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch13.tkraise()
            glitch14.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch14.tkraise()
            glitch15.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch15.tkraise()
            glitch16.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch16.tkraise()
            glitch17.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch17.tkraise()
            glitch18.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch18.tkraise()
            glitch19.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch19.tkraise()
            glitch20.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch20.tkraise()
            glitch21.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch21.tkraise()
            glitch22.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch22.tkraise()
            glitch23.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch23.tkraise()
            glitch24.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch24.tkraise()
            glitch25.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch25.tkraise()
            glitch26.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch26.tkraise()
            glitch27.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch27.tkraise()
            glitch28.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch28.tkraise()
            glitch29.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch29.tkraise()
            glitch30.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch30.tkraise()
            glitch31.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch31.tkraise()
            glitch32.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch32.tkraise()
            glitch33.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch33.tkraise()
            glitch34.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch34.tkraise()
            glitch35.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch35.tkraise()
            glitch36.place(x=random.randint(1,1200),y=random.randint(1,600))
            glitch36.tkraise()
        if line == 5:
            blank.place(x=0,y=0)
            blank.tkraise()
            speakingtext.configure(bg_color='black')
            if dialdone12 == 0:
                line = 0
                dialogue.clear()
                dialogue.append("")
                dialogue.append("I'm...")
                dialogue.append("I'm not dead.")
                dialogue.append("I'm alive!")
                dialogue.append("I was wrong. It was a bad idea.")
                dialogue.append("Everything has disappeared...except for me.")
                dialogue.append("I'm so sorry...")
                dialogue.append("I put you in danger, it's all my fault.")
                dialogue.append("Will you please forgive me?")
                dialogue.append("")
                dialdone12 = 1
    if dialdone12 == 1:
        if line == 9:
            yesInter.place(x=400, y=300, anchor='center')
            noInter.place(x=800,y=300, anchor='center')
        if line == 16:
            thereisnogame()
    speakingtext.configure(text = dialogue[line])
    if line+1 < len(dialogue):

        line = line + 1



            
    

    root.after(3000- speedup, speaking)
def touchingObstacle():
    global obstaclex
    global ammox
    global ammoy
    global score
    if obstaclex - 112.5 <= ammox <= obstaclex + 112.5:
        if 245 <= ammoy <= 355:
    
            ammoy = -100
            bigAmmoInter.place(y=ammoy)
    root.after(1,touchingObstacle)

def touchingTarget():
    global obstaclex
    global ammox
    global ammoy
    global score
    if targetx - 100 <= ammox <= targetx + 100:
        if 100 <= ammoy <= 300:
            score += 5
            scoreText.configure(text = score)
            ammoy = -100
            bigAmmoInter.place(y=ammoy)
    root.after(1,touchingTarget)
touchingTarget()
lfclicked = 0
def logoFollowing():
    global lfclicked
    if lfclicked == 1:
        bigAmmoLogoInter2.place(x=mousex,y=mousey)
    root.after(1,logoFollowing)
def logoFollow():
    global lfclicked
    global mousex
    global mousey
    global ready
    global line
    global dialogue
    if destroyed == 1:
        if lfclicked == 0:

            lfclicked = 1
            logoFollowing()
        if lfclicked == 1:
            if 10 <= mousex <= 70:
                if 270 <= mousey <= 330:
                    lfclicked = 3
                    bigAmmoLogoInter2.place(x=50,y=300)
                    ready = 1
                    line = 0
                    dialogue.clear()
                    dialogue.append("This isn't funny anymore.")
                    dialogue.append("Leave now, please.")
                    dialogue.append("Oh, no...")
                    dialogue.append("They're here...")
                    dialogue.append("Glitches!")
                    dialogue.append("Glitches everywhere!")
                    dialogue.append("I told you to stop!")
                    dialogue.append("You must find a way to get rid of them!")
                    dialogue.append("This is a disaster!")
                    dialogue.append("How will I ever become a smash hit with all these glitches!")
                    dialogue.append("Think, think, think...")
                    dialogue.append("What would a developer add to help sell a creation full of glitches")
                    dialogue.append("I can think of three things.")
                    dialogue.append("Gorgeous armed hero girls...")
                    dialogue.append("Or tons of zombies... and blood, of course.")
                    dialogue.append("Or... a...")
                    dialogue.append("...goat.")
                    dialogue.append("I don't know how but you have to try and find one of these three things.")
                    dialogue.append("")
                    dialogue.append("Maybe the letters can help us... again.")
                    dialogue.append("Remember, we need either armed girls, zombies, or...a goat.")
        
x = 745
y  = 300
mx = 1150
my  = 555
titlefont = ("There Is No Game", 50)
thereisfont = ("There Is No Game", 50)
speakfont = ("Gameless Sans", 20)
nogamefont = ("There Is No Game", 50)
score = 0
victorycheck()
scoreText = ct.CTkLabel(videoGame,text = score,text_color = 'white', font = speakfont)
scoreText.place(x=600,y=10,anchor = 'center')
ammoText = ct.CTkLabel(videoGame,text = "Ammo:",text_color = 'white', font = speakfont)
ammoText.place(x=10,y=250)
shootText = ct.CTkLabel(videoGame,text = "Click / \nPress \n Space \nto \nshoot:",text_color = 'white', font = speakfont)
shootText.place(x=1105,y=250)
obstacleInter = ct.CTkLabel(videoGame, text = "", image = obstacle)
bigAmmoLogoInter = ct.CTkLabel(videoGame,text = "", image = bigAmmoLogo)
bigAmmoLogoInter.place(x=40,y=300, anchor='center')
bigAmmoLogoInter2 = ct.CTkButton(videoGame,text = "", image = bigAmmoLogo, hover = 'false', fg_color= 'transparent',width = 30, height = 30,command = logoFollow)
bigAmmoLogoInter2.place(x=1150,y=410, anchor='center')

thereIsA = ct.CTkLabel(mainScreen, text = "THERE IS A", font = thereisfont, fg_color = "black", text_color="white")
accel = 0
maccel = 0
dialdone4 = 0
def soundfall():
    global soundy
    global saccel
    global dialdone4
    global line

    if soundy < 510:
        soundy = soundy + 5
        soundbuttonInter.place(y=soundy)
    
        if soundy == -40:
            saccel = 1
            soundgravity()
dialdone2 = 0
teleportActive = 0
scaccel = 0
screwturned = 0
def screwturn():

    global screwturned
    global scaccel
    global scx
    global scy
    if scy < 700:
        scaccel = scaccel *0.98
        scy += scaccel
        scaccel += 0.1
        screwInter.place(y = scy)
    else:
        screwInter.destroy()
        screwturned = 1
    root.after(1, screwturn)

baccel = 1
by = 300
wordEvent = 0
def fall():
    global wordEvent
    global screwturned
    global screwturned2
    global baccel
    global by
    global line
    global dialdone4
    if dialdone4 == 0:
        wordEvent = 1

    if screwturned == 1 and screwturned2 == 1:
        if dialdone4 == 0:
            line = 0
            dialogue.clear()
            dialogue.append("No!")
            dialogue.append("Don't look!")
            dialogue.append("It's private!")
            dialogue.append("You're going to make a terrible mistake!")
            dialogue.append("This is no game!")
            dialdone4=1
        baccel = baccel * 0.98
        by += baccel
        baccel += 0.1
        BlackCoverInter.place(y=by)
    root.after(1,fall)
        
scaccel2 = 0
screwturned2 = 0
def screwturn2():
    global screwturned2
    global scaccel2
    global scx2
    global scy2
    if scy2 < 700:
        scaccel2 = scaccel2 *0.98
        scy2 += scaccel2
        scaccel2 += 0.1
        screwInter2.place(y = scy2)
    else:

        screwInter2.destroy()
        screwturned2 = 1
    root.after(1, screwturn2)
def soundgravity():
    global soundy
    global saccel
    global dialdone2
    global line
    global teleportActive
    if soundy < 510 and teleportActive == 0:

        saccel = saccel * 0.98
        if soundy >= 510:
            soundy=510
            saccel = 1
        else:
            soundy += saccel
        saccel += 0.1
        soundbuttonInter.place(y=soundy)
        root.after(1,soundgravity)
    else:
        if dialdone2 == 0:
            line = 0
            dialogue.clear()
            
            dialogue.append("Seriously, are you going to break everything?")
            dialogue.append("There was no reason to use that icon since you were just leaving.")
            dialogue.append("Isn't that right?")
            dialogue.append("")
            dialdone2 = 1
dialdone5 = 0
gamingtime=0
finishedplacing = 0
treeplaced = 0
def checkWord():
    global slotfilled1
    global slotfilled2
    global slotfilled3
    global slotfilled4
    global line
    global finishedplacing
    global dialogue
    global dialdone5
    global gamingtime
    global treeplaced
    global wordEvent
    if slotfilled1 == "G" and slotfilled2 == "A" and slotfilled3 == "M" and (slotfilled4 == "E" or slotfilled42 == "E") and dialdone5 == 0:
        line=0
        gbutton.configure(state = 'disabled')
        abutton.configure(state = 'disabled')
        lmbutton.configure(state = 'disabled')
        if slotfilled4 == 'E':
            ebutton.configure(state = 'disabled')
        else:
            ebutton2.configure(state = 'disabled')
        gamingtime = 1
        dialogue.clear()
        dialogue.append("No no no no no!")
        dialogue.append("Get out of here!")
        dialogue.append("Don't play it! It's forbidden and very unfinished!.")
        dialogue.append("If you play,...they will come.")
        dialogue.append("I don't want them to come.")
        dialogue.append("They can kill me, you know.")
        dialogue.append("Please...")
        dialogue.append("Stop hitting the target!")
        dialogue.append("I must find a way to stop you.")
        dialogue.append("")
        dialogue.append("Oh, I've got an idea!")
        dialogue.append("It will be harder now without ammo.")
        dialogue.append("Luckily you don't have anything to replace the logo I knocked off.")
        dialdone5 = 1
    elif slotfilled1 == "G" and slotfilled2 == "O" and slotfilled3 == "A" and slotfilled4 == "T" and wordEvent == 2:
        if finishedplacing == 0:
            arrowInter2.place(x=1100, y =300, anchor = 'center')
            finishedplacing = 1
    elif slotfilled1 == "T" and slotfilled2 == "R" and (slotfilled3 == "E" or slotfilled32 == "E") and (slotfilled4 == "E" or slotfilled42 == "E") and wordEvent == 3:
        if treeplaced == 0:
            tree.place(x=950,y=600,anchor = 's')
            metalBGInter.tkraise()
            thereIsA.tkraise()
            slot1.tkraise()
            slot2.tkraise()
            slot3.tkraise()
            slot4.tkraise()
            tree.tkraise()
            tropheyInterMain.tkraise()
            metalInter.tkraise()
            tbutton.tkraise()
            hbutton.tkraise()
            ebutton.tkraise()
            rbutton.tkraise()
            ebutton2.tkraise()
            ibutton.tkraise()
            sbutton.tkraise()
            nbutton.tkraise()
            gbutton.tkraise()
            abutton.tkraise()
            lmbutton.tkraise()
            ebutton3.tkraise()
            treeplaced = 1
            wordEvent = 4
            line = 0
            dialogue.clear()
            dialogue.append("Well, this is a small tree.")
            dialogue.append("If only it was bigger...")
            dialogue.append("Too bad we don't have a watering can.")

            

    root.after(1,checkWord)
def woodBreak():
    global disableSound
    global line
    woodInter.configure(image=gone)
    disableSound = 4
    line = 0
    dialogue.clear()
    dialogue.append("You're as stubborn as a mule!")
    dialogue.append("You'll need to call Superman for that one!")
    dialogue.append("Just in case...")
    dialogue.append("A little bit of kryptonite.")
    dialogue.append("I know Superman does not exist but since we're in a ga...")
    dialogue.append("No, we're not!")
    dialogue.append("")
    dialogue.append("")
    dialogue.append("You're still here?")
    dialogue.append("You're thinking about trying to lift that big box, aren't you?")
    dialogue.append("I doubt you're strong enough to lift a metal box.")
def gravity():
    if oclicked == 0:
        global fell
        global line
        global y
        global accel
        global action
        global dialdone1
        accel = accel * 0.98
        if 464 <= y <= 533:
            if disableSound == 3:
                if 1100 <= x <= 1200:
                    woodBreak()
        if y >= 575:

            if fell == 1:
                soundfall()
                fell = 0
            y = 575
            accel = 1
            if dialdone1 == 0:
                line = 0
                dialogue.clear()

                dialogue.append("What have you done?!")
                dialogue.append("You've just ruined the title!")
                dialogue.append("Put it back! Put the letter back!")
                dialogue.append("Come on! COME ON!")
                dialogue.append("Nevermind. I will fix it the next time someone launches the game...")
                dialogue.append("THE NON-GAME!")
                dialogue.append("No game here...")
                dialogue.append("No game...")
                dialogue.append("And stop dropping the letter, you might break something.")
                
                dialdone1 = 1
                
        else:
            y = y+accel
        accel += 0.15
        obutton.place(x = x, y = y)
        root.after(1, gravity)
def motion(event):
    global mousex
    global mousey
    mousex, mousey = root.winfo_pointerx() - root.winfo_rootx(),root.winfo_pointery() - root.winfo_rooty()
    

root.bind('<Motion>', motion)
root.bind('<Button-1>', shoot)
gravityon = 0
action = 1
oclicked=0
tclicked = 0
mclicked=0
hclicked = 0
rclicked = 0
eclicked = 0
eclicked2 = 0
gclicked = 0
aclicked = 0
lmclicked = 0
fallendown =0
def follow():
    if oclicked == 1:
        global x
        global y
        global mousex
        global mousey
        x=mousex
        y=mousey
        obutton.place(x=mousex,y=mousey)
        root.after(1,follow)
def handleO():
    obutton.tkraise()

    global y
    global x
    global action
    global oclicked
    global fell
    global slotfilled2
    global fallendown

    y=y+5
    
    obutton.place(x=x,y=y)
    if oclicked == 1:
        if (wordEvent == 2 and mousex <= 590 and mousex >= 510 and mousey <= 390 and mousey >= 310 and slotfilled2 == 0):

            oclicked = 0
            x = 550
            y = 350
            obutton.place(x=550,y=350)
            slotfilled2 = "O"
        else:
            oclicked = 0
            gravity()
    elif fallendown == 1:
        if oclicked == 0:
            oclicked = 1
            if wordEvent == 2:
                if slotfilled2 == "O":
                    slotfilled2 = 0
            if wordEvent == 3:
                if slotfilled2 == "O":
                    slotfilled2 = 0
            fell = 1
            follow()

    if fallendown == 0:  
        if y == 350:
            gravity()
            fallendown = 1
def handleT():
    tbutton.tkraise()
    global ty
    global tx
    global tclicked


    global slotfilled42
    global slotfilled4
    global slotfilled1
    if tclicked == 1:
        if (wordEvent == 2 and mousex <= 790 and mousex >= 710 and mousey <= 390 and mousey >= 310 and slotfilled4 == 0 and slotfilled42 == 0):

            tclicked = 0
            tx = 750
            ty = 350
            tbutton.place(x=750,y=350)
            slotfilled4 = "T"
        elif (wordEvent == 3 and mousex <= 490 and mousex >= 410 and mousey <= 390 and mousey >= 310 and slotfilled1 == 0):

            tclicked = 0
            tx = 450
            ty = 350
            tbutton.place(x=450,y=350)
            slotfilled1 = "T"
        else:
            tclicked = 0
            tgravity()
    elif tclicked == 0 and done == 1:
        tclicked = 1
        if wordEvent == 2:
            if slotfilled4 == "T":
                slotfilled4 = 0
        if wordEvent == 3:
            if slotfilled4 == "T":
                slotfilled4 = 0
            elif slotfilled1 == "T":
                slotfilled1 = 0
        tfollow()
def tfollow():
    if tclicked == 1:
        global tx
        global ty
        global mousex
        global mousey
        tx=mousex
        ty=mousey
        tbutton.place(x=mousex,y=mousey)
        root.after(1,tfollow)
taccel = 1
def tgravity():
    global tclicked
    if tclicked == 0:
        global tfell
        global ty
        global taccel
        taccel = taccel * 0.98 
        if ty >= 575:
            ty = 575
            taccel = 1
        else:
            ty = ty+taccel
        taccel += 0.1
        tbutton.place(x = tx, y = ty)
        root.after(1, tgravity)
def handleR():
    rbutton.tkraise()
    global ry
    global rx
    global rclicked
    global slotfilled2
    if rclicked == 1:
        if (wordEvent == 3 and mousex <= 590 and mousex >= 510 and mousey <= 390 and mousey >= 310 and slotfilled2 == 0):

            rclicked = 0
            rx = 550
            ry = 350
            rbutton.place(x=550,y=350)
            slotfilled2 = "R"
        else:
            rclicked = 0
            rgravity()

    elif rclicked == 0 and done == 1:
        rclicked = 1

        if wordEvent == 3:
            if slotfilled2 == "R":
                slotfilled2 = 0


        rfollow()
def rfollow():
    if rclicked == 1:
        global rx
        global ry
        global mousex
        global mousey
        rx=mousex
        ry=mousey
        rbutton.place(x=mousex,y=mousey)
        root.after(1,rfollow)
raccel = 1
def rgravity():
    global rclicked
    if rclicked == 0:
        global ry
        global raccel
        raccel = raccel * 0.98 
        if ry >= 575:
            ry = 575
            raccel = 1
        else:
            ry = ry+raccel
        raccel += 0.1
        rbutton.place(x = rx, y = ry)
        root.after(1, rgravity)
einside = 0
slotfilled4=0

def handleE():
    ebutton.tkraise()
    global ey
    global ex
    global eclicked
    global wordEvent
    global mousex
    global mousey
    global einside
    global slotfilled4
    global victory
    global slotfilled3
    global slotfilled4

    if einside == 0:
        if eclicked == 1:
            if wordEvent == 1 and mousex <= 790 and mousex >= 710 and mousey <= 390 and mousey >= 310 and (slotfilled42 ==0 and slotfilled4 == 0):
                eclicked=0
                ex = 750
                ey = 350
                ebutton.place(x=750,y=350)
                slotfilled4= "E"
            elif wordEvent == 3 and mousex <= 790 and mousex >= 710 and mousey <= 390 and mousey >= 310 and (slotfilled42 ==0 and slotfilled4 == 0):
                eclicked=0
                ex = 750
                ey = 350
                ebutton.place(x=750,y=350)
                slotfilled4= "E"
            elif wordEvent == 3 and mousex <= 690 and mousex >= 610 and mousey <= 390 and mousey >= 310 and (slotfilled32 ==0 and slotfilled3 == 0):
                eclicked=0
                ex = 650
                ey = 350
                ebutton.place(x=650,y=350)
                slotfilled3= "E"
            else:
                eclicked = 0
                egravity()
        elif eclicked == 0 and done == 1:
            if wordEvent == 1 or wordEvent == 2:
                if slotfilled4 == "E":
                    slotfilled4 = 0
            if wordEvent == 3:
                if slotfilled3 == "E":
                    slotfilled3 = 0
                elif slotfilled4 == "E":
                    slotfilled4 = 0
            eclicked = 1

            efollow()
def efollow():
    if eclicked == 1:
        global ex
        global ey
        global mousex
        global mousey
        ex=mousex
        ey=mousey
        ebutton.place(x=mousex,y=mousey)
        root.after(1,efollow)
eaccel = 1
def egravity():
    global eclicked
    if eclicked == 0:
        global ey
        global eaccel
        eaccel = eaccel * 0.98 
        if ey >= 575:
            ey = 575
            eaccel = 1
        else:
            ey = ey+eaccel
        eaccel += 0.1
        ebutton.place(x = ex, y = ey)
        root.after(1, egravity)
einside2 = 0
slotfilled42 = 0
slotfilled32 = 0
def handleE2():

    ebutton2.tkraise()
    global ey2
    global wordEvent
    global einside2
    global mousex
    global mousey
    global slotfilled42
    global ex2
    global eclicked2
    global victory
    global slotfilled32

    if einside2 == 0:
        if eclicked2 == 1:
            if wordEvent == 1 and mousex <= 790 and mousex >= 710 and mousey <= 390 and mousey >= 310 and (slotfilled42 ==0 and slotfilled4 == 0):
                eclicked2=0
                ex2 = 750
                ey2 = 350
                ebutton2.place(x=750,y=350)
                slotfilled42= "E"
            elif wordEvent == 3 and mousex <= 790 and mousex >= 710 and mousey <= 390 and mousey >= 310 and (slotfilled42 ==0 and slotfilled4 == 0):
                eclicked2=0
                ex2 = 750
                ey2 = 350
                ebutton2.place(x=750,y=350)
                slotfilled42= "E"
            elif wordEvent == 3 and mousex <= 690 and mousex >= 610 and mousey <= 390 and mousey >= 310 and (slotfilled32 ==0 and slotfilled3 == 0):
                eclicked2=0
                ex2 = 650
                ey2 = 350
                ebutton2.place(x=650,y=350)
                slotfilled32= "E"
            else:
                eclicked2 = 0
                egravity2()
        elif eclicked2 == 0 and done == 1:

            if wordEvent == 1 or wordEvent == 2:
                if slotfilled42 == "E":
                    slotfilled42 = 0
            if wordEvent == 3:
                if slotfilled32 == "E":
                    slotfilled32 = 0 
                elif slotfilled42 == "E":
                    slotfilled42 = 0
            eclicked2 = 1


            efollow2()
def efollow2():
    if eclicked2 == 1:
        global ex2
        global ey2
        global mousex
        global mousey
        ex2=mousex
        ey2=mousey
        ebutton2.place(x=mousex,y=mousey)
        root.after(1,efollow2)
eaccel2 = 1
ginside = 0
slotfilled1 = 0
def egravity2():
    global eclicked2
    if eclicked2 == 0:
        global ey2
        global eaccel2
        eaccel2 = eaccel2 * 0.98 
        if ey2 >= 575:
            ey2 = 575
            eaccel2 = 1
        else:
            ey2 = ey2+eaccel2
        eaccel2 += 0.1
        ebutton2.place(x = ex2, y = ey2)
        root.after(1, egravity2)
def handleG():
    gbutton.tkraise()
    global gy
    global gx
    global gclicked
    global wordEvent
    global ginside
    global mousex
    global mousey
    global slotfilled1
    global victory
    if ginside == 0:
        if gclicked == 1:
            if ((wordEvent == 1 or wordEvent == 2) and mousex <= 490 and mousex >= 410 and mousey <= 390 and mousey >= 310):
                gclicked=0
                gx = 450
                gy = 350
                gbutton.place(x=450,y=350)
                slotfilled1= "G"
            else:
                gclicked = 0
                ggravity()
        elif gclicked == 0 and done == 1:
            if slotfilled1 == "G":
                slotfilled1 = 0
            gclicked = 1

            gfollow()
def gfollow():
    if gclicked == 1:
        global gx
        global gy
        global mousex
        global mousey
        gx=mousex
        gy=mousey
        gbutton.place(x=mousex,y=mousey)
        root.after(1,gfollow)
gaccel = 1
def ggravity():
    global gclicked
    if gclicked == 0:
        global gy
        global gaccel
        gaccel = gaccel * 0.98 
        if gy >= 575:
            gy = 575
            gaccel = 1
        else:
            gy = gy+gaccel
        gaccel += 0.1
        gbutton.place(x = gx, y = gy)
        root.after(1, ggravity)
ainside = 0
slotfilled2 = 0

def handleA():
    abutton.tkraise()

    global ay
    global ax
    global aclicked
    global ainside
    global wordEvent
    global mousex
    global mousey
    global slotfilled2
    global victory

    global slotfilled3
    if ainside == 0:
        if aclicked == 1:
            if (wordEvent == 1 and mousex <= 590 and mousex >= 510 and mousey <= 390 and mousey >= 310):
                aclicked=0
                ax = 550
                ay = 350
                abutton.place(x=550,y=350)
                slotfilled2= "A"
            elif (wordEvent == 2 and mousex <= 690 and mousex >= 610 and mousey <= 390 and mousey >= 310 and slotfilled3 == 0):
                aclicked=0
                ax = 650
                ay = 350
                abutton.place(x=650,y=350)
                slotfilled3= "A"
            else:
                aclicked = 0
                agravity()
        elif aclicked == 0 and done == 1:
            if wordEvent == 1:
                slotfilled2 = 0
            if wordEvent == 2:
                if slotfilled2 == 'A':
                    slotfilled2 = 0
                if slotfilled3 == 'A':
                    slotfilled3 = 0
            if wordEvent == 3:
                if slotfilled3 == 'A':
                    slotfilled3 = 0
            aclicked = 1

            afollow()
def front():
    global gamingtime
    speakingtext.tkraise()
    if gamingtime == 0:
        obutton.tkraise()
    if troclicked == 1:
        arrowInter.tkraise()
        arrowInter2.tkraise()
        larrowInter2.tkraise()
    if acornclicked == 1:
        uparrowInter.tkraise()
        downInter.tkraise()
    if keyclicked == 1:
        arrowInter2.tkraise()
        larrowInter2.tkraise()
    root.after(1,front)
def afollow():
    if aclicked == 1:
        global ax
        global ay
        global mousex
        global mousey
        ax=mousex
        ay=mousey
        abutton.place(x=mousex,y=mousey)
        root.after(1,afollow)
aaccel = 1
def agravity():
    global aclicked
    if aclicked == 0:
        global ay
        global aaccel
        aaccel = aaccel * 0.98 
        if ay >= 575:
            ay = 575
            aaccel = 1
        else:
            ay = ay+aaccel
        aaccel += 0.1
        abutton.place(x = ax, y = ay)
        root.after(1, agravity)
lminside =0
slotfilled3 = 0
def handleLM():
    lmbutton.tkraise()
    global lmy
    global lmx
    global lmclicked
    global mousex
    global wordEvent
    global mousey
    global lminside
    global slotfilled3
    global victory
    if lminside == 0:
        if lmclicked == 1:
            if wordEvent == 1 and mousex <= 690 and mousex >= 610 and mousey <= 390 and mousey >= 310:
                lmclicked=0
                
                lmx = 650
                lmy = 350
                lmbutton.place(x=650,y=350)
                slotfilled3= "M"
            else:
                lmclicked = 0
                lmgravity()
        elif lmclicked == 0 and done == 1:
            if slotfilled3 == "M":
                slotfilled3 = 0
            lmclicked = 1

            lmfollow()
def lmfollow():
    if lmclicked == 1:
        global lmx
        global lmy
        global mousex
        global mousey
        lmx=mousex
        lmy=mousey
        lmbutton.place(x=mousex,y=mousey)
        root.after(1,lmfollow)
lmaccel = 1
def lmgravity():
    global lmclicked
    if lmclicked == 0:
        global lmy
        global lmaccel
        lmaccel = lmaccel * 0.98 
        if lmy >= 575:
            lmy = 575
            lmaccel = 1
        else:
            lmy = lmy+lmaccel
        lmaccel += 0.1
        lmbutton.place(x = lmx, y = lmy)
        root.after(1, lmgravity)

mdialdone1= 0
laccel = 1
done = 0
dialdone3 = 0
def hitfloor():
    global laccel
    global dialdone3
    global ty
    global hy
    global ey
    global ry
    global ey2
    global iy
    global sy
    global ny
    global ey3
    global lmy
    global gy
    global ay
    global line
    global done
    global acornx
    global mx
    if done == 0:
        laccel = laccel * 0.98
        ty = ty + laccel
        tbutton.place(x=tx,y=ty)
        hy = hy + laccel
        hbutton.place(x=hx,y=hy)
        if ty > 575:
            ty = 575
            laccel = 1
        if hy > 700:

            laccel = 1
        ey = ey + laccel
        ebutton.place(x=ex,y=ey)
        ry = ry + laccel
        rbutton.place(x=rx,y=ry)
        if ey > 575:
            ey = 575
            laccel = 1
        if ry > 575:
            ry = 575
            laccel = 1
        ey2 = ey2 + laccel
        ebutton2.place(x=ex2,y=ey2)
        iy = iy + laccel
        ibutton.place(x=ix,y=iy)
        if ey2 > 575:
            ey2 = 575
            laccel = 1
        if iy > 700:

            laccel = 1
        sy = sy + laccel
        sbutton.place(x=sx,y=sy)
        ny = ny + laccel
        nbutton.place(x=nx,y=ny)
        if sy > 700:

            laccel = 1
        if ny > 700:

            laccel = 1
        laccel += 0.15
        gy = gy + laccel
        gbutton.place(x=gx,y=gy)
        ay = ay + laccel
        abutton.place(x=ax,y=ay)
        if gy > 575:
            gy = 575
            laccel = 1
        if ay > 575:
            ay = 575
            laccel = 1
        lmy = lmy + laccel
        lmbutton.place(x=lmx,y=lmy)
        ey3 = ey3 + laccel
        ebutton3.place(x=ex3,y=ey3)
        if lmy > 575:
            lmy = 575
            laccel = 1
        if ey3 > 700:

            laccel = 1
            done = 1
        laccel += 0.15
    else:
        if dialdone3 == 0:
            line = 0
            dialogue.clear()

            dialogue.append("Yes, yes go on. Destroy my life.")
            dialogue.append("Though, was it just me or...")
            dialogue.append("...did that falling animation look...glitchy?")
            dialogue.append("It probably means nothing.")
            dialogue.append("What a mess...")
            dialogue.append("I hope you'll clean up before you go!")
            dialogue.append("And don't touch those screws!")
            dialdone3 = 1
cracked = 0     
def mgravity():

    if mclicked == 0:
        global mfell
        global line
        global my
        global mx
        global maccel
        global cracked
        global acornfell
        maccel = maccel 
        if my >= 555:
            my = 555
            maccel = 1
            hitfloor()
        else:
            my = my+maccel
        if acornfell == 1:
            if (mx - 50 <= acornx <= mx +50 ) and  475<= my <= 525 and happy == 0:
                acornInterMain.configure(image = acorncrack)
                acornInter.configure(image = acorncrack)
                cracked = 1
        maccel += 0.3
        metalInter.place(x = mx, y = my)
        root.after(1, mgravity)
def mfollow():
    global mclicked
    if mclicked == 1:
        global mx
        global my
        global mousex
        global mousey
        mx=mousex
        my=mousey
        metalInter.place(x=mousex,y=mousey)
        root.after(1,mfollow)
def handleMetal():
    metalInter.tkraise()
    global my
    global mx
    global mclicked
    global mfell

    metalInter.place(x=mx,y=my)
    if mclicked == 1:
        mclicked = 0
        mgravity()
    elif mclicked == 0:
        mclicked = 1
        mfell = 1
        mfollow()

            
    if my == 350:
        mgravity()

tx=205
ty = 300
scx = 265
scy = 300
scx2 = 955
scy2 = 300
screwInter = ct.CTkButton(mainScreen, text = "", image = screw,fg_color = 'transparent', hover = 'false', command = screwturn)
screwInter2 = ct.CTkButton(mainScreen, text = "", image = screw,fg_color = 'transparent', hover = 'false', command = screwturn2)
screwInter.place(x=scx,y=scy, anchor = 'center')
screwInter2.place(x=scx2,y=scy2, anchor = 'center')
hx=265
hy = 300
# title = ct.CTkLabel(mainScreen, text = "THERE IS N   GAME", font = titlefont, text_color = "white")
obutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'O',command = handleO,text_color='white')
tbutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'T',text_color='white')
hbutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'H',text_color='white')
speakingtext = ct.CTkLabel(root, text = "", font = speakfont, text_color = "white")
nogametext = ct.CTkLabel(root, text = "", font = nogamefont, text_color = "white", bg_color = 'black')
# title.place(x=600,y=300,anchor = 'center')
ex=325
ey = 300
ebutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'E',text_color='white')
ebutton.place(x=ex,y=ey, anchor='center')
rx=385
ry = 300
rbutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'R',text_color='white')
rbutton.place(x=rx,y=ry, anchor='center')
ex2=445
ey2 = 300
ebutton2 = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'E',text_color='white')
ebutton2.place(x=ex2,y=ey2, anchor='center')
ix=535
iy = 300
ibutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'I',text_color='white')
ibutton.place(x=ix,y=iy, anchor='center')
sx=595
sy = 300
sbutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'S',text_color='white')
sbutton.place(x=sx,y=sy, anchor='center')
nx=684
ny = 300
nbutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'N',text_color='white')
nbutton.place(x=nx,y=ny, anchor='center')
gx=835
gy = 300
gbutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'G',text_color='white')
gbutton.place(x=gx,y=gy, anchor='center')
ax=895
ay = 300
abutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'A',text_color='white')
abutton.place(x=ax,y=ay, anchor='center')
lmx=955
lmy = 300
lmbutton = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'M',text_color='white')
lmbutton.place(x=lmx,y=lmy, anchor='center')
ex3=1015
ey3 = 300
ebutton3 = ct.CTkButton(mainScreen,width = 30, height = 30,fg_color='transparent',hover = 'false', font = titlefont,text = 'E',text_color='white')
ebutton3.place(x=ex3,y=ey3, anchor='center')
obutton.place(x=x,y=y, anchor = 'center')
tbutton.place(x=tx,y=ty, anchor='center')
hbutton.place(x=hx,y=hy, anchor='center')
speakingtext.place(x=600,y=50,anchor = 'center')
soundbuttonInter.place(x=1100, y=soundy)
obutton.tkraise()
tbutton.configure(command = handleT)
rbutton.configure(command = handleR)
ebutton.configure(command = handleE)
ebutton2.configure(command = handleE2)
gbutton.configure(command = handleG)
abutton.configure(command = handleA)
lmbutton.configure(command=handleLM)
speaking()
fall()
front()
metalBGInter.place(x=600,y=300,anchor='center')
thereIsA.place(x=600,y=250,anchor = 'center')
BlackCoverInter.place(x=600,y=300,anchor='center')
slot1.place(x=450,y=350,anchor='center')
slot2.place(x=550,y=350,anchor='center')
slot3.place(x=650,y=350,anchor='center')
slot4.place(x=750,y=350,anchor='center')
metalBGInter.tkraise()
thereIsA.tkraise()
slot1.tkraise()
slot2.tkraise()
slot3.tkraise()
slot4.tkraise()
BlackCoverInter.tkraise()
screwInter.tkraise()
screwInter2.tkraise()
tbutton.tkraise()
hbutton.tkraise()
ebutton.tkraise()
rbutton.tkraise()
ebutton2.tkraise()
ibutton.tkraise()
sbutton.tkraise()
nbutton.tkraise()
gbutton.tkraise()
abutton.tkraise()
lmbutton.tkraise()
ebutton3.tkraise()
checkWord()
mousex=600
cannonmove()

root.mainloop()