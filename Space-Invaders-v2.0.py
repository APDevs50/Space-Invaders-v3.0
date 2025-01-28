try:
    import os
    import tkinter as tk
    import threading
    import time
    import random
    import sys
    import subprocess
    import ast
    import traceback
    import pygame
    import importlib
except Exception as e:
    with open(os.path.join(os.getcwd(),"ERROR_IN_SPACEINVADERS.txt"),'w') as f:
            f.write(f"""
SPACE INVADERS HAS CRASHED!!!
_____________________________
-----------------------------
ERROR: PYTHON TKINTER UNKNOWN ERROR OCCURED!!!
ERROR IS AS FOLLOWS:
{traceback.format_exc()}""")
    os.system(f"notepad {os.path.join(os.getcwd(),"ERROR_IN_SPACEINVADERS.txt")}")

try:
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the sound file
    click_sound = pygame.mixer.Sound(os.path.join(os.getcwd(),"ClickEffectSFX.wav"))  # Replace with your sound file
    buying_sound = pygame.mixer.Sound(os.path.join(os.getcwd(),"EazyBUY.wav"))
    error = pygame.mixer.Sound(os.path.join(os.getcwd(),"Error.wav"))
    mouse_hover_effect = pygame.mixer.Sound(os.path.join(os.getcwd(),"Hover.wav"))
    background_music = pygame.mixer.Sound(os.path.join(os.getcwd(),"BG_MUSIC.wav"))
    shooting_sound_effect = pygame.mixer.Sound(os.path.join(os.getcwd(),"GUNSHOT.wav"))
    explosion = pygame.mixer.Sound(os.path.join(os.getcwd(),"EXPLOSION.wav"))
    footstep = pygame.mixer.Sound(os.path.join(os.getcwd(),"STEPS.wav"))
    game_over = False
    root = tk.Tk()
    root.geometry("500x300")
    root.resizable(False,False)
    root.title("SPACE INVADERS")
    logo = tk.PhotoImage(file=os.path.join(os.getcwd(),"logo.png"))
    scores = []
    score = 10
    # Set the window's icon
    root.iconphoto(True, logo)
    canvas = tk.Canvas(root,bg="#000000",width=500,height=300)
    canvas.pack()
    class Skin:
        def __init__(self):
            if os.path.isfile(os.path.join(os.getcwd(),"EQUIPPED.spaceinvaders")):
                with open(os.path.join(os.getcwd(),"EQUIPPED.spaceinvaders"),"r") as f:
                    self.skin = f.readline()
            else:
                self.skin = "Player.png"
            #print(self.skin)
            self.others = [
                "Player.png",
                "Deathly_Hallows_Skin.png",
                "Rainbow_Skin.png",
                "Pizza_Skin.png",
                "Ice_Cream_Skin.png",
                "Cupcake_Skin.png",
                "Magic_Wand_Skin.png",
                "Sorting_Hat_Skin.png"
            ]

            self.others.remove(self.skin)
            #print(self.others)
            self.todispothers = {
                "Player.png" : 0,
                "Deathly_Hallows_Skin.png" : 10000,
                "Rainbow_Skin.png": 1000,
                "Pizza_Skin.png": 2000,
                "Ice_Cream_Skin.png": 5000,
                "Cupcake_Skin.png": 7500,
                "Magic_Wand_Skin.png" : 4500,
                "Sorting_Hat_Skin.png" : 9999
            }
            self.displaynames = {
                "Default" : "Player.png",
                "Deathly Hallows" : "Deathly_Hallows_Skin.png",
                "Rainbow Rush" : "Rainbow_Skin.png",
                "Pizza Party" : "Pizza_Skin.png",
                "I Scream for Ice Cream" : "Ice_Cream_Skin.png",
                "Cupcake n' Coffee" : "Cupcake_Skin.png",
                "Magician Work" : "Magic_Wand_Skin.png",
                "Slytherin" : "Sorting_Hat_Skin.png"
            }
            if os.path.isfile(os.path.join(os.getcwd(),"SKINS.spaceinvaders")):
                with open(os.path.join(os.getcwd(),"SKINS.spaceinvaders"),"r") as f:
                    self.llygddwswdF = f.readline()
                    self.bought = ast.literal_eval(self.llygddwswdF)
            else:
                self.bought = ["Player.png"]
            self.curr = 0

        def pickle_bought(self):
            with open(os.path.join(os.getcwd(),"SKINS.spaceinvaders"),"w") as f:
                f.write(str(self.bought))
        
        def pickle_equipped(self):
            with open(os.path.join(os.getcwd(),"EQUIPPED.spaceinvaders"),"w") as f:
                f.write(self.skin)
        def changeskin(self, skinxx):
            if x.issfx == True:
                click_sound.play()
            #print("Called")
            try:
                self.skinx = self.others[self.others.index(skinxx)]
                self.othersx = self.others.index(skinxx)
            except ValueError as e:
                #print(f"ERROR: {traceback.format_exc()}")
                return "Already Equipped"
        
            # Swap the current skin
            self.intermediate = self.skin
            self.skin = self.skinx
            self.others.append(self.intermediate)
            self.others.remove(self.skin)

            # Assuming "ClickEffectSFX.mp3" is in the same directory

            
            # Persist the equipped skin
            self.pickle_equipped()

        
            # Refresh the shop UI to reflect the change
            x.skinchooser()

            
        def getskin(self):
            return self.skin, self.todispothers[self.skin]
        def isequipped(self,skin):
            if self.skin == skin:
                return "EQUIPPED"
            else:
                return " EQ-UIP "
        def isbought(self,skin):
            if self.displaynames[skin] in self.bought:
                return "BOUGHT"
            else:
                return " TAKE " 
        def is_affordable(self, skin, xp):
            if self.todispothers[self.displaynames[skin]] <=  xp:
                return True
            else:
                return False

    xxychooser = Skin()

    class MainMenu:
        def __init__(self,wasicalledbyanotherfunction=False,didthisfunctionkillsfx=False):
            try:
                background_music.stop()
            except:
                pass
            background_music.play(loops=-1)
            if didthisfunctionkillsfx == True:
                self.issfx = False
            else:
                self.issfx = True
            if wasicalledbyanotherfunction == True:
                if self.issfx == True:
                    click_sound.play()
            self.ifflag = False
            for i in root.winfo_children():
                i.destroy()
            
            
            
            # Check if sound effects (SFX) are enabled and background music is not already playing
            # If sound effects (SFX) are enabled and background music is not already playing



            self.f = tk.Frame(root, bg="#000000", width=500, height=300)
            self.f.pack()
            self.topic = tk.Label(self.f, bg="#000000", fg="#00ff00", text="Space Invaders", font=('F77 Minecraft Regular',25,'bold'))
            self.topic.place(x=0,y=0)
            self.msg = tk.Text(width=62, height=10,font=('Consolas',11,'normal'), background="#000000")
            self.msg.insert(tk.END, "In the distant reaches of space, from the star system 40 Eridani, a formidable alien fleet has set its sights on Earth. Their arrival is sudden and their intentions clear—an invasion is imminent. However, due to a malfunction in their spacecraft and the exhaustion of their crew, humanity has a fleeting chance to repel the onslaught. As the world’s last line of defense, you are the chosen hero. With the weight of the entire human race resting on your shoulders, you must act swiftly and strategically. The alien invaders are relentless and highly skilled in reinforcements, sending waves of their best warriors to break our defenses. Equipped with your trusty spaceship, you navigate using the arrow keys, dodging and weaving through the enemy barrage. With the spacebar as your weapon, you unleash bullets of hope and defiance, fending off wave after wave of alien attackers. Your mission is not just to survive, but to protect the Earth for as long as you can. Each alien destroyed earns you points and experience, allowing you to unlock new skins and power-ups. These rewards not only bolster your strength but also serve as symbols of your valor. Compete with other heroes across the globe in epic high score battles, proving your mettle and determination. But remember, the aliens are cunning and will always be hot on your trail. Stay vigilant, stay fast, and never let your guard down. The fate of humanity is in your hands. Choose wisely, fight bravely, and become the legend Earth needs.")
            self.msg.place(x=0,y=50)
            self.msg.tag_add('story','0.0',tk.END)
            self.msg.tag_config('story',foreground="#00ff00",background="#000000")
            self.scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.msg.yview)
            self.msg.configure(yscrollcommand=self.scrollbar.set)
            self.msg.config(state="disabled")
            self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
            self.playbtn = tk.Button(pady=10,padx=50,text="Play",font=('F77 Minecraft Regular',-11,'bold'),bg="#000000",fg="#00ff00",command= lambda : startgame() ,borderwidth=0,highlightthickness=0,activebackground="#000000")
            self.playbtn.place(x=0,y=250)
            self.playbtnx = tk.Button(pady=10,padx=50,text="Shop",font=('F77 Minecraft Regular',-11,'bold'),bg="#000000",fg="#00ff00",command = lambda: self.skinchooser(),borderwidth=0,highlightthickness=0,activebackground="#000000")
            self.playbtny = tk.Button(pady=10,padx=50,text="Menu",font=('F77 Minecraft Regular',-11,'bold'),bg="#000000",fg="#00ff00",command=lambda : self.showsettingsmenu() ,borderwidth=0, highlightthickness=0,activebackground="#000000")
            self.playbtnx.place(x=150,y=250)
            self.playbtny.place(x=300,y=250)
            self.playbtn.bind("<Enter>", self.magic_hover)
            self.playbtnx.bind("<Enter>", self.magic_hover)
            self.playbtny.bind("<Enter>", self.magic_hover)
            self.playbtn.bind("<Leave>", self.stopthemagic)
            self.playbtnx.bind("<Leave>", self.stopthemagic)
            self.playbtny.bind("<Leave>", self.stopthemagic)
            self.ifflag = True
        
        def magic_hover(self,ev):
            width = ev.widget.cget("width")
            height = ev.widget.cget("height")
            #print(width,height)
            ev.widget.config(width=6, height=1,font=('F77 Minecraft Regular',-14,'bold'))
            if self.ifflag != False and self.issfx != False:
                mouse_hover_effect.play()
        
        def stopthemagic(self,ev):
            ev.widget.config(width=0, height=0,font=('F77 Minecraft Regular',-11,'bold'))

        def purchase(self, skin):
            if self.issfx == True:
                buying_sound.play()            
            xxychooser.bought.append(skin)
            self.xp -= xxychooser.todispothers[skin]
            xxychooser.pickle_bought()
            self.skinchooser()


        def skinchooser(self):
            # Clear existing widgets when transitioning to the shop screen
            for i in root.winfo_children():
                i.destroy()


            # Create canvas for shop menu
            self.cv = tk.Canvas(root, bg="#000000", width=500, height=90)
            self.cv.propagate(0)  # Disable resizing to maintain the given size
            self.cv.place(x=0,y=0)
            self.fla = False
            try:
                print(self.xp)
            except AttributeError:
                self.fla = True
            if self.fla:
                if os.path.isfile(os.path.join(os.getcwd(), "PROGRESS.spaceinvaders")):
                    with open(os.path.join(os.getcwd(), "PROGRESS.spaceinvaders"),"r") as f:
                        self.xp = int(f.readline())
                        #print(self.xp)
                else:
                    with open(os.path.join(os.getcwd(), "PROGRESS.spaceinvaders"),"w") as f:
                        self.xp = "10"
                        f.write(self.xp)
            else:
                with open(os.path.join(os.getcwd(), "PROGRESS.spaceinvaders"),"w") as f:
                    self.xpp = str(self.xp)
                    f.write(self.xpp)

            # Create Shop Heading (Centered)
            self.cv.create_text(60, 30, text="Shop", font=('F77 Minecraft Regular', 25, 'normal'), fill="#00ff00")
            self.cv.create_text(420,40,text=f"XP: {self.xp}",font=('F77 Minecraft Regular',-15, 'normal'),fill="#00ff00")
            self.cv.create_line(0,50,500,50,fill="#00ff00")
            self.cv.create_line(370,0,370,50,fill="#00ff00")
            self.cv.create_line(0,90,500,90,fill="#00ff00")
            self.back_button = tk.Button(self.cv, text="Back to Home", font=('F77 Minecraft Regular', 12, 'normal'), bg="#000000", fg="#00ff00", command=lambda: self.__init__(wasicalledbyanotherfunction=True,didthisfunctionkillsfx= not self.issfx),borderwidth=0,highlightthickness=0)
            self.back_button.place(x=5, y=60)  # Button for going back to the main menu
            self.cv2 = tk.Canvas(root, bg="#000000", width=500, height=210, scrollregion=(0, 0, 500, 500))  # Initial scrollregion
            self.cv2.place(x=0, y=90)

            # Scrollbar Configuration
            self.scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.cv2.yview)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.cv2.configure(yscrollcommand=self.scrollbar.set)

            # Bind Mouse Scroll
            self.cv2.bind_all("<MouseWheel>", lambda e: self.cv2.yview_scroll(-1 * (e.delta // 120), "units"))
            self.cv2.create_text(40,20,text="Skins: ",font=('F77 Minecraft Regular',11,'bold'),fill="#00ff00")
            self.defaultskin = tk.PhotoImage(file=os.path.join(os.getcwd(),"Player.png"))
            self.cv2.create_image(60,60,image=self.defaultskin,anchor=tk.NW)
            self.cv2.create_text(86,110,text="Default",font=('F77 Minecraft Regular',9,'normal'),fill="#00ff00")
            self.buyplayer = tk.Button(self.cv2,text="BOUGHT",borderwidth=0,font=('F77 Minecraft Regular',9,'normal'),fg="#00ff00",bg="#000000",highlightthickness=0)
            self.cv2.create_window(81, 130, window=self.buyplayer)
            self.buyplayer.config(state=tk.DISABLED)
            self.eqplayer = tk.Button(self.cv2, text=f"{xxychooser.isequipped("Player.png")}",bg="#000000",fg="#00ff00",font=('F77 Minecraft Regular',9,'normal'),borderwidth=0,highlightthickness=0,command=lambda: xxychooser.changeskin("Player.png"))
            self.eqplayert = self.eqplayer.cget("text")
            if self.eqplayert == "EQUIPPED":
                self.eqplayer.config(state=tk.DISABLED)
                #print("DISABLED!")
            self.cv2.create_window(80, 150, window=self.eqplayer)
            self.rainbowskinimg = tk.PhotoImage(file=os.path.join(os.getcwd(), "Rainbow_Skin.png"))
            self.cv2.create_image(160,60,image=self.rainbowskinimg,anchor=tk.NW)
            self.cv2.create_text(186,110,text="Rainbow",font=('F77 Minecraft Regular',9,'normal'),fill="#00ff00")
            self.buyrainbow = tk.Button(self.cv2, text=f"{xxychooser.isbought("Rainbow Rush")}",font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",borderwidth=0,highlightthickness=0,command=lambda: self.purchase("Rainbow_Skin.png"))
            self.buyrainbowtext = self.buyrainbow.cget("text")
            if self.buyrainbowtext == "BOUGHT":
                self.buyrainbow.config(state=tk.DISABLED)
            elif xxychooser.is_affordable("Rainbow Rush",int(self.xp)) == False:
                self.buyrainbow.config(state=tk.DISABLED)
            self.cv2.create_window(186, 130, window=self.buyrainbow)
            self.equiprainbow = tk.Button(self.cv2,text=f"{xxychooser.isequipped("Rainbow_Skin.png")}",font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",borderwidth=0,highlightthickness=0,command=lambda: xxychooser.changeskin("Rainbow_Skin.png"))
            if self.buyrainbowtext != "BOUGHT":
                self.equiprainbow.config(state=tk.DISABLED)
            elif self.equiprainbow.cget("text") == "EQUIPPED":
                self.equiprainbow.config(state=tk.DISABLED)
            self.cv2.create_window(181, 150, window=self.equiprainbow)
            self.pizzaskinimg = tk.PhotoImage(file=os.path.join(os.getcwd(),"Pizza_Skin.png"))
            self.cv2.create_image(256,60,image=self.pizzaskinimg,anchor=tk.NW)
            self.cv2.create_text(281,110,text="Pizza",font=('F77 Minecraft Regular',9,'normal'),fill="#00ff00")
            self.buypizza = tk.Button(self.cv2, text=f"{xxychooser.isbought("Pizza Party")}", bg="#000000", fg="#00ff00", borderwidth=0, highlightthickness=0, font=('F77 Minecraft Regular',9,'normal'), command = lambda: self.purchase("Pizza_Skin.png"))
            if self.buypizza.cget("text") == "BOUGHT":
                self.buypizza.config(state=tk.DISABLED)
            elif xxychooser.is_affordable("Pizza Party",int(self.xp)) == False:
                self.buypizza.config(state=tk.DISABLED)
            self.cv2.create_window(286, 130, window=self.buypizza)        
            self.eatthepizza = tk.Button(self.cv2,text=f"{xxychooser.isequipped("Pizza_Skin.png")}", font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",command=lambda: xxychooser.changeskin("Pizza_Skin.png"),borderwidth=0,highlightthickness=0)
            if self.eatthepizza.cget("text") == "EQUIPPED":
                self.eatthepizza.config(state=tk.DISABLED)
            elif self.buypizza.cget("text") != "BOUGHT":
                self.eatthepizza.config(state=tk.DISABLED)
            self.cv2.create_window(281, 150, window=self.eatthepizza)
            self.cupcakeimage = tk.PhotoImage(file=os.path.join(os.getcwd(),"Cupcake_Skin.png"))
            self.cv2.create_text(377,110,text="Cupcake",font=('F77 Minecraft Regular',9,'normal'),fill="#00ff00")
            self.cv2.create_image(352,60,image=self.cupcakeimage,anchor=tk.NW)
            self.buycupcake = tk.Button(self.cv2, text=f"{xxychooser.isbought("Cupcake n' Coffee")}", bg="#000000", fg="#00ff00", borderwidth=0, highlightthickness=0, font=('F77 Minecraft Regular',9,'normal'), command = lambda: self.purchase("Cupcake_Skin.png"))

            if self.buycupcake.cget("text") == "BOUGHT":
                self.buycupcake.config(state=tk.DISABLED)
            elif xxychooser.is_affordable("Cupcake n' Coffee",int(self.xp)) == False:
                self.buycupcake.config(state=tk.DISABLED)
            self.cv2.create_window(377, 130, window=self.buycupcake)    
            self.eatthecupcake = tk.Button(self.cv2,text=f"{xxychooser.isequipped("Cupcake_Skin.png")}", font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",command=lambda: xxychooser.changeskin("Cupcake_Skin.png"),borderwidth=0,highlightthickness=0)
            if self.eatthecupcake.cget("text") == "EQUIPPED":
                self.eatthecupcake.config(state=tk.DISABLED)
            elif self.buycupcake.cget("text") != "BOUGHT":
                self.eatthecupcake.config(state=tk.DISABLED)
            self.cv2.create_window(377, 150, window=self.eatthecupcake)
            self.iceimage = tk.PhotoImage(file=os.path.join(os.getcwd(),"Ice_Cream_Skin.png"))
            self.cv2.create_text(80,210,text="Ice Cream",font=('F77 Minecraft Regular',9,'normal'),fill="#00ff00")
            self.cv2.create_image(60,170,image=self.iceimage,anchor=tk.NW)
            self.buyice = tk.Button(self.cv2, text=f"{xxychooser.isbought("I Scream for Ice Cream")}", bg="#000000", fg="#00ff00", borderwidth=0, highlightthickness=0, font=('F77 Minecraft Regular',9,'normal'), command = lambda: self.purchase("Ice_Cream_Skin.png"))

            if self.buyice.cget("text") == "BOUGHT":
                self.buyice.config(state=tk.DISABLED)
            elif xxychooser.is_affordable("I Scream for Ice Cream",int(self.xp)) == False:
                self.buyice.config(state=tk.DISABLED)
            self.cv2.create_window(80, 230, window=self.buyice)        
            self.eattheice = tk.Button(self.cv2,text=f"{xxychooser.isequipped("Ice_Cream_Skin.png")}", font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",command=lambda: xxychooser.changeskin("Ice_Cream_Skin.png"),borderwidth=0,highlightthickness=0)
            if self.eattheice.cget("text") == "EQUIPPED":
                self.eattheice.config(state=tk.DISABLED)
            elif self.buyice.cget("text") != "BOUGHT":
                self.eattheice.config(state=tk.DISABLED)
            self.cv2.create_window(80, 250, window=self.eattheice)
            # Deathly Hallows skin
            self.lookslikeyouaretheownerofdeathasyouhaveallthedeathlyhallows = tk.PhotoImage(file=os.path.join(os.getcwd(),"Deathly_Hallows_Skin.png"))
            self.cv2.create_image(160,170,image=self.lookslikeyouaretheownerofdeathasyouhaveallthedeathlyhallows,anchor=tk.NW)
            self.buydeath = tk.Button(self.cv2, text=f"{xxychooser.isbought('Deathly Hallows')}", bg="#000000", fg="#00ff00", borderwidth=0, highlightthickness=0, font=('F77 Minecraft Regular',9,'normal'), command=lambda: self.purchase("Deathly_Hallows_Skin.png"))
            self.cv2.create_text(180,210,text="D'ly Hallows",font=('F77 Minecraft Regular',9,'normal'),fill="#00ff00")

            # Update the purchase button state based on the purchase status and affordability
            if self.buydeath.cget("text") == "BOUGHT":
                self.buydeath.config(state=tk.DISABLED)
            elif not xxychooser.is_affordable('Deathly Hallows', int(self.xp)):
                self.buydeath.config(state=tk.DISABLED)

            self.cv2.create_window(180, 230, window=self.buydeath)

            # Equip button for Deathly Hallows skin
            self.makedeathkillyou = tk.Button(self.cv2, text=f"{xxychooser.isequipped('Deathly_Hallows_Skin.png')}", font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",command=lambda: xxychooser.changeskin('Deathly_Hallows_Skin.png'),borderwidth=0,highlightthickness=0)

            # If the skin is equipped, disable the button
            if self.makedeathkillyou.cget("text") == "EQUIPPED":
                self.makedeathkillyou.config(state=tk.DISABLED)
            elif self.buydeath.cget("text") != "BOUGHT":
                self.makedeathkillyou.config(state=tk.DISABLED)

            self.cv2.create_window(180, 250, window=self.makedeathkillyou)

            # Magic Wand skin
            self.harryswand = tk.PhotoImage(file=os.path.join(os.getcwd(),"Magic_Wand_Skin.png"))
            self.cv2.create_image(260,170,image=self.harryswand,anchor=tk.NW)
            self.ollivander = tk.Button(self.cv2, text=f"{xxychooser.isbought('Magician Work')}", bg="#000000", fg="#00ff00", borderwidth=0, highlightthickness=0, font=('F77 Minecraft Regular',9,'normal'), command=lambda: self.purchase('Magic_Wand_Skin.png'))
            self.cv2.create_text(280,210,text="HP Wand",font=('F77 Minecraft Regular',9,'normal'),fill="#00ff00")

            # Update purchase button for Magic Wand skin
            if self.ollivander.cget("text") == "BOUGHT":
                self.ollivander.config(state=tk.DISABLED)
            elif not xxychooser.is_affordable('Magician Work', int(self.xp)):
                self.ollivander.config(state=tk.DISABLED)

            self.cv2.create_window(280, 230, window=self.ollivander)

            # Equip button for Magic Wand skin
            self.expectopatronum = tk.Button(self.cv2, text=f"{xxychooser.isequipped('Magic_Wand_Skin.png')}", font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",command=lambda: xxychooser.changeskin('Magic_Wand_Skin.png'),borderwidth=0,highlightthickness=0)

            # If the skin is equipped, disable the button
            if self.expectopatronum.cget("text") == "EQUIPPED":
                self.expectopatronum.config(state=tk.DISABLED)
            elif self.ollivander.cget("text") != "BOUGHT":
                self.expectopatronum.config(state=tk.DISABLED)

            self.cv2.create_window(280, 250, window=self.expectopatronum)

            # Sorting Hat skin
            self.rab = tk.PhotoImage(file=os.path.join(os.getcwd(),"Sorting_Hat_Skin.png"))
            self.cv2.create_image(360,170,image=self.rab,anchor=tk.NW)
            self.hocrux = tk.Button(self.cv2, text=f"{xxychooser.isbought('Slytherin')}", bg="#000000", fg="#00ff00", borderwidth=0, highlightthickness=0, font=('F77 Minecraft Regular',9,'normal'), command=lambda: self.purchase('Sorting_Hat_Skin.png'))
            self.cv2.create_text(380,210,text="Sorting Hat",font=('F77 Minecraft Regular',9,'normal'),fill="#00ff00")

            # Update purchase button for Sorting Hat skin
            if self.hocrux.cget("text") == "BOUGHT":
                self.hocrux.config(state=tk.DISABLED)
            elif not xxychooser.is_affordable('Slytherin', int(self.xp)):
                self.hocrux.config(state=tk.DISABLED)

            self.cv2.create_window(380, 230, window=self.hocrux)

            # Equip button for Sorting Hat skin
            self.gryffindor = tk.Button(self.cv2, text=f"{xxychooser.isequipped('Sorting_Hat_Skin.png')}", font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",command=lambda: xxychooser.changeskin('Sorting_Hat_Skin.png'),borderwidth=0,highlightthickness=0)

            # If the skin is equipped, disable the button
            if self.gryffindor.cget("text") == "EQUIPPED":
                self.gryffindor.config(state=tk.DISABLED)
            elif self.hocrux.cget("text") != "BOUGHT":
                self.gryffindor.config(state=tk.DISABLED)


            self.cv2.create_window(380, 250, window=self.gryffindor)
            self.bannerimage = tk.PhotoImage(file=os.path.join(os.getcwd(),"BANNER.png"))
            self.cv2.create_image(80,350,image=self.bannerimage)
            self.cv2.create_text(100,300,text="Ad-based Rewards:",font=('F77 Minecraft Regular',11,'bold'),fill="#00ff00")
            self.pushbtn = tk.Button(self.cv2,text="AD +30XP",font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",highlightthickness=0,borderwidth=0,command=self.triggeradvertismentoverlay)
            self.cv2.create_window(85,400,window=self.pushbtn)
        def triggeradvertismentoverlay(self):
            if self.issfx == True:
                error.play()
            self.advert = tk.Canvas(root,width=500,height=300,bg="#000000")
            self.advert.pack()
            self.advert.create_polygon(150, 100, 350, 100, 350, 200, 150, 200, outline="#00ff00", fill="")
            self.advert.create_text(250,150,text="No Ads Found!",font=('F77 Minecraft Regular',9,'bold'),fill="#00ff00")
            self.quitbtn = tk.Button(self.advert,text="QUIT",font=('F77 Minecraft Regular',9,'normal'),bg="#000000",fg="#00ff00",command=self.adverterrorquit,borderwidth=0,highlightthickness=0)
            self.quitbtn.place(x=230,y=175)
        def adverterrorquit(self):
            if self.issfx == True:
                click_sound.play()
            self.advert.destroy()
        def showsettingsmenu(self):
            for i in root.winfo_children():
                i.destroy()
            self.cvsettings = tk.Canvas(root,width=500,height=300,bg="#000000")
            self.cvsettings.pack()
            self.cvsettings.create_text(130,150,text="Settings",font=('F77 Minecraft Regular',15,'bold'),fill="#00ff00")
            self.btn_back_to_home = tk.Button(self.cvsettings,text="Back To Home",font=('F77 Minecraft Regular',-15,'normal'),bg="#000000",fg="#00ff00",command=lambda: self.__init__(wasicalledbyanotherfunction=True,didthisfunctionkillsfx= not self.issfx),borderwidth=0,highlightthickness=0)
            self.btn_back_to_home.place(x=300,y=110)
            self.sfxbtn = tk.Button(
                root,
                text=f"SFX: {'On' if self.issfx else 'Off'}",
                font=('F77 Minecraft Regular', -15, 'normal'),
                bg="#000000",
                fg="#00ff00",
                command=self.toggle_sfx,
                borderwidth=0,
                highlightthickness=0
            )
            self.sfxbtn.place(x=300,y=190)
            self.cvsettings.create_line(190,145,240,145,240,115,300,115,fill="#00ff00")
            self.cvsettings.create_line(190,155,240,155,240,195,300,195,fill="#00ff00")
        def toggle_sfx(self):
            click_sound.play()
            if self.issfx == True:
                self.issfx = False
            else:
                self.issfx = True
            self.showsettingsmenu()
    def startgame():
        for i in root.winfo_children():
            i.destroy()
        game_over = False


        scores = []
        score = 10
        # Set the window's icon
        canvas = tk.Canvas(root,bg="#000000",width=500,height=300)
        canvas.pack()
        class Scoreboard:
            def __init__(self):
                self.myself = canvas.create_text(60, 10, font=('F77 Minecraft Regular', -15, 'normal'), text=f"Score: {score}", fill="#00ff00")
                self.highscore_display = canvas.create_text(420, 10, font=('F77 Minecraft Regular', -15, 'normal'), text="", fill="#00ff00", justify='left')
                self.updateThread = threading.Thread(target=self.update)
                self.updateThread.daemon = True
                self.updateThread.start()

            def update(self,score=score):
                canvas.itemconfig(self.myself, text=f"Score: {score}")
                score = score
                self.update_highscore_display()


            def update_highscore_display(self):
                high = self.highscore()
                canvas.itemconfig(self.highscore_display, text=f"High Score: {high}")

            def highscore(self):
                high = 0
                if os.path.isfile(os.path.join(os.getcwd(), "SCORE.spaceinvaders")):
                    with open("SCORE.spaceinvaders", 'r') as f:
                        try:
                            scorets = f.readline().strip()
                            if scorets:
                                high = int(scorets)
                        except Exception as e:
                            print(f"Error reading highscore: {e}")
                return high

            def update_highscore(self):
                high = self.highscore()
                if score > high:
                    with open("SCORE.spaceinvaders", 'w') as f:
                        f.write(str(score))




        scorer = Scoreboard()
        scorer.highscore()
        class Player:
            def __init__(self):
                self.myself = tk.PhotoImage(file=os.path.join(os.getcwd(),xxychooser.getskin()[0]))
                self.img = canvas.create_image(100,268,anchor=tk.NW,image=self.myself)
            def move_right(self,ev):
                if x.issfx == True:
                    footstep.play()
                curr_coords = canvas.coords(self.img)
                if curr_coords[0] + 10 >= 450:
                    #print("ILLEGAL")
                    return
                canvas.move(self.img, 10, 0)
                #print(self.whereami())
            def move_left(self,ev):
                if x.issfx == True:
                    footstep.play()
                curr_coords = canvas.coords(self.img)
                if curr_coords[0] - 10 <= 0:
                    #print("ILLEGAL")
                    return
                canvas.move(self.img, -10, 0)
                #print(self.whereami())
            def whereami(self):
                return canvas.coords(self.img)
        player = Player()
        class Bullet:
            def __init__(self):
                self.myclones = []
                self.blaster = []
                self.origx = []
                self.daemonThread = threading.Thread(target=self.ascend)
                self.daemonThread.daemon = True
                self.daemonThread.start()
            def shoot(self,ev):
                if x.issfx == True:
                    shooting_sound_effect.play()
                self.blaster.append(tk.PhotoImage(file=os.path.join(os.getcwd(),"Bullet.png")))
                self.origx.append(int(player.whereami()[0]+25))
                self.meid = canvas.create_image(self.origx[-1],255,anchor=tk.NW,image=self.blaster[-1])
                self.myclones.append(self.meid)
            def ascend(self):
                self.l1 = threading.Lock()
                self.l1.acquire()
                while True:
                    if game_over == True:
                        return
                    for i in self.myclones:
                        try:
                            if canvas.coords(i)[1] == 0:
                                canvas.delete(i)
                                self.todel = self.myclones.index(i)
                                self.myclones.remove(i)
                                del self.origx[self.todel]
                                del self.blaster[self.todel]
                            else:
                                canvas.move(i,0,-10)
                        except:
                            print("Crash averted")
                    time.sleep(0.05)
                self.l1.release()
            def whereamim(self):
                bulletcoords = []
                for i in self.myclones:
                    bulletcoords.append(canvas.coords(i))
                return coords
            
        class Enemy_bullet:
            def __init__(self):
                self.myselveswhowannakill = []
                self.origcoords = []
                self.img = tk.PhotoImage(file=os.path.join(os.getcwd(),"Bullet.png"))
            def spawn(self,x,y,whoshot):
                if whoshot == "green":
                    self.keid = canvas.create_image(x+16,y+32,anchor=tk.NW,image=self.img)
                    self.myselveswhowannakill.append(self.keid)
                else:
                    self.keid = canvas.create_image(x+24,y+32,anchor=tk.NW,image=self.img)
                    self.myselveswhowannakill.append(self.keid)
            def descend(self):
                while True:
                    if game_over == True:
                        return
                    for i in self.myselveswhowannakill:
                        try:
                            if canvas.coords(i)[1] >= 300:
                                canvas.delete(i)
                                self.myselveswhowannakill.remove(i)
                                #print("DEL")
                            else:
                                canvas.move(i,0,10)
                                #print("GO!")
                            #print("Something")
                        except Exception as e:
                            #print(f"Crashpad: {e}")
                            continue
                    time.sleep(0.05)

        alien_revenge = Enemy_bullet()
        daethro = threading.Thread(target=alien_revenge.descend)
        daethro.daemon = True
        daethro.start()
                    
                    
                    
                
        class Alien:
            def __init__(self):
                self.myselves = []
                self.origcoords = []
                self.finales = []
                self.x = 100
                self.y = 100
                self.num = 0   # Alien movement speed
                self.currentimage = 1
                self.daemonThreade = threading.Thread(target=self.move_aliens_left)
                self.daemonThreade.daemon = True
                self.daemonThreade.start()

            def create(self):
                for i in range(18):
                    self.switch = tk.PhotoImage(file=os.path.join(os.getcwd(), "Green_Alien_Frame_2.png"))
                    self.qorig = tk.PhotoImage(file=os.path.join(os.getcwd(), "Green_Alien_Frame_1.png"))
                    self.myselves.append(tk.PhotoImage(file=os.path.join(os.getcwd(), "Green_Alien_Frame_1.png")))
                    self.origcoords.append([self.x, self.y])
                    self.ceid = canvas.create_image(self.origcoords[i][0], self.origcoords[i][1], anchor=tk.NW, image=self.myselves[-1])
                    self.finales.append(self.ceid)
                    if self.x > 400:  # Create aliens in rows
                        self.x = 100
                        self.y += 40
                        continue
                    self.x += 40
            def animate(self):
                for i in self.finales:
                    if self.currentimage == 1:
                        canvas.itemconfig(i, image=self.switch)
                    else:
                        canvas.itemconfig(i, image=self.qorig)
                        
                if self.currentimage == 1:
                    self.currentimage = 2
                else:
                    self.currentimage = 1
            def move_aliens_left(self):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,-10,0)
                self.animate()
                self.num += 1
                time.sleep(1)
                if self.num != 5:
                    self.move_aliens_left()
                else:
                    self.num = 0
                    self.move_aliens_down('left')
            def move_aliens_down(self,mode):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,0,10)
                self.animate()
                time.sleep(1)
                if mode == 'left':
                    self.move_aliens_right()
                else:
                    self.move_aliens_left()

            def move_aliens_right(self):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,10,0)
                self.animate()
                self.num += 1
                time.sleep(1)
                if self.num != 5:
                    self.move_aliens_right()
                else:
                    self.num = 0
                    self.move_aliens_down('right')
            def whereamij(self):
                aliencoords = []
                for i in self.finales:
                    aliencoords.append(canvas.coords(i))

            def powerblast(self):
                if game_over == True:
                    return
                #global alien_revenge
                while True:
                    try:
                        shooter = random.choice(self.finales)
                        coords = canvas.coords(shooter)
                        #print("Someone Shot...")
                        alien_revenge.spawn(coords[0],coords[1],"green")
                    except:
                        print("Error")
                    finally:
                        time.sleep(7)


        enemies = Alien()
        enemies.create()
        enemiesthread = threading.Thread(target = enemies.powerblast)
        enemiesthread.daemon = True
        enemiesthread.start()
        class Alien_Tenacity_1:
            def __init__(self):
                self.myselves = []
                self.origcoords = []
                self.finales = []
                self.x = 100
                self.y = 60
                self.num = 0   # Alien movement speed
                self.currentimage = 1
                self.daemonThreade = threading.Thread(target=self.move_aliens_left)
                self.daemonThreade.daemon = True
                self.daemonThreade.start()

            def create(self):
                for i in range(6):
                    self.switch = tk.PhotoImage(file=os.path.join(os.getcwd(), "Blue_Alien_Frame_2.png"))
                    self.qorig = tk.PhotoImage(file=os.path.join(os.getcwd(), "Blue_Alien_Frame_1.png"))
                    self.myselves.append(tk.PhotoImage(file=os.path.join(os.getcwd(), "Blue_Alien_Frame_1.png")))
                    self.origcoords.append([self.x, self.y])
                    self.ceid = canvas.create_image(self.origcoords[i][0], self.origcoords[i][1], anchor=tk.NW, image=self.myselves[-1])
                    self.finales.append(self.ceid)
                    if self.x > 400:  # Create aliens in rows
                        self.x = 100
                        self.y += 40
                        continue
                    self.x += 60
            def animate(self):
                for i in self.finales:
                    if self.currentimage == 1:
                        canvas.itemconfig(i, image=self.switch)
                    else:
                        canvas.itemconfig(i, image=self.qorig)
                        
                if self.currentimage == 1:
                    self.currentimage = 2
                else:
                    self.currentimage = 1
            def move_aliens_left(self):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,-10,0)
                self.animate()
                self.num += 1
                time.sleep(1)
                if self.num != 5:
                    self.move_aliens_left()
                else:
                    self.num = 0
                    self.move_aliens_down('left')
            def move_aliens_down(self,mode):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,0,10)
                self.animate()
                time.sleep(1)
                if mode == 'left':
                    self.move_aliens_right()
                else:
                    self.move_aliens_left()

            def move_aliens_right(self):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,10,0)
                self.animate()
                self.num += 1
                time.sleep(1)
                if self.num != 5:
                    self.move_aliens_right()
                else:
                    self.num = 0
                    self.move_aliens_down('right')
            def whereamij(self):
                aliencoords = []
                for i in self.finales:
                    aliencoords.append(canvas.coords(i))
                    
            def powerblast(self):
                if game_over == True:
                    return
                #global alien_revenge
                while True:
                    try:
                        shooter = random.choice(self.finales)
                        coords = canvas.coords(shooter)
                        #print("Someone Shot...")
                        alien_revenge.spawn(coords[0],coords[1],"blue")
                    except:
                        print("Error")
                    finally:
                        time.sleep(6)
                        
        bluey = Alien_Tenacity_1()
        bluey.create()
        dd = threading.Thread(target=bluey.powerblast)
        dd.daemon = True
        dd.start()
        class Alien_Tenacity_2:
            def __init__(self):
                self.myselves = []
                self.origcoords = []
                self.finales = []
                self.x = 100
                self.y = 20
                self.num = 0   # Alien movement speed
                self.currentimage = 1
                self.daemonThreade = threading.Thread(target=self.move_aliens_left)
                self.daemonThreade.daemon = True
                self.daemonThreade.start()

            def create(self):
                for i in range(6):
                    self.switch = tk.PhotoImage(file=os.path.join(os.getcwd(), "Red_Alien_Frame_2.png"))
                    self.qorig = tk.PhotoImage(file=os.path.join(os.getcwd(), "Red_Alien_Frame_1.png"))
                    self.myselves.append(tk.PhotoImage(file=os.path.join(os.getcwd(), "Red_Alien_Frame_1.png")))
                    self.origcoords.append([self.x, self.y])
                    self.ceid = canvas.create_image(self.origcoords[i][0], self.origcoords[i][1], anchor=tk.NW, image=self.myselves[-1])
                    self.finales.append(self.ceid)
                    if self.x > 400:  # Create aliens in rows
                        self.x = 100
                        self.y += 40
                        continue
                    self.x += 60
            def animate(self):
                for i in self.finales:
                    if self.currentimage == 1:
                        canvas.itemconfig(i, image=self.switch)
                    else:
                        canvas.itemconfig(i, image=self.qorig)
                        
                if self.currentimage == 1:
                    self.currentimage = 2
                else:
                    self.currentimage = 1
            def move_aliens_left(self):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,-10,0)
                self.animate()
                self.num += 1
                time.sleep(1)
                if self.num != 5:
                    self.move_aliens_left()
                else:
                    self.num = 0
                    self.move_aliens_down('left')
            def move_aliens_down(self,mode):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,0,10)
                self.animate()
                time.sleep(1)
                if mode == 'left':
                    self.move_aliens_right()
                else:
                    self.move_aliens_left()

            def move_aliens_right(self):
                if game_over == True:
                    return
                for i in self.finales:
                    canvas.move(i,10,0)
                self.animate()
                self.num += 1
                time.sleep(1)
                if self.num != 5:
                    self.move_aliens_right()
                else:
                    self.num = 0
                    self.move_aliens_down('right')
            def whereamij(self):
                aliencoords = []
                for i in self.finales:
                    aliencoords.append(canvas.coords(i))
                    
            def powerblast(self):
                if game_over == True:
                    return
                #global alien_revenge
                while True:
                    try:
                        shooter = random.choice(self.finales)
                        coords = canvas.coords(shooter)
                        #print("Someone Shot...")
                        alien_revenge.spawn(coords[0],coords[1],"red")
                    except:
                        print("Error")
                    finally:
                        time.sleep(5)
                        
        red_light = Alien_Tenacity_2()
        red_light.create()
        df = threading.Thread(target=red_light.powerblast)
        df.daemon = True
        df.start()
        killer = Bullet()
        class CollisionDetection:
            def detectbullet(self):
                try:
                    global score 
                    for bullet in killer.myclones:

                        #print(killer.myclones)
                        box = canvas.bbox(bullet)
                        if box is None:  # Check if the bullet exists
                            continue
                        to_kill = canvas.find_overlapping(*box)
                        for i in to_kill:
                            if i in enemies.finales:
                                canvas.delete(i)
                                canvas.delete(bullet)
                                killer.myclones.remove(bullet)
                                enemies.finales.remove(i)
                                score += 10
                                if x.issfx == True:
                                    explosion.play()
                                print(score)
                                scorer.update(score=score)
                                break
                            elif i in bluey.finales:
                                canvas.delete(i)
                                canvas.delete(bullet)
                                bluey.finales.remove(i)
                                killer.myclones.remove(bullet)
                                score += 20
                                if x.issfx == True:
                                    explosion.play()
                                scorer.update(score=score)
                                print(score)
                                break
                            elif i in red_light.finales:
                                canvas.delete(i)
                                canvas.delete(bullet)
                                killer.myclones.remove(bullet)
                                red_light.finales.remove(i)
                                score += 30
                                if x.issfx == True:
                                    explosion.play()
                                scorer.update(score=score)
                                print(score)
                                break
                except Exception as e:
                    print("Error: (detectbullet)", e)                
            def detectdeath(self):
                try:
                    global game_over
                    sbox = canvas.bbox(player.img)
                    l = canvas.find_overlapping(*sbox)
                    if len(l) > 1:
                        scorer.update_highscore()
                        overlay = tk.Canvas(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='black', highlightthickness=0)
                        overlay.place(x=0, y=0)
                        overlay.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2 - 30,
                                text="YOU LOST!", fill="#00ff00", font=("F77 Minecraft Regular", 36, 'bold'))
                        restart_button = tk.Button(overlay, text="Restart", font=("F77 Minecraft Regular", 16, 'bold'), command=reset_game, bg="#000000", borderwidth=0, highlightthickness=0, fg="#00ff00")
                        restart_button.place(x=200, y=150)

                        game_over = True
                        canvas.delete("all")
                except Exception as e:
                    print("Error: (detectdeath)",e)
        
            def detectvictory(self):
                scorer.update_highscore() 
                global game_over
                if len(red_light.finales) == 0 and len(bluey.finales) == 0 and len(enemies.finales) == 0 and game_over == False:
                    print(red_light.finales,bluey.finales,enemies.finales)
                    game_over = True
                    print("DETECT VICTORY: I RESTTED THE GAME!")
                    self.next_wave()
                
                
            def detect_alien_hit(self):
                
                try:
                    for i in enemies.finales:
                        try:
                            if canvas.coords(i)[1] + 32 >= 268:
                                scorer.update_highscore()
                                game_over = True
                                overlay = tk.Canvas(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='black', highlightthickness=0)
                                overlay.place(x=0, y=0)
                                overlay.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2 - 30,
                                    text="YOU LOST!", fill="#00ff00", font=("F77 Minecraft Regular", 36, "bold"))
                                restart_button = tk.Button(overlay, text="Restart", font=("F77 Minecraft Regular", 16, 'bold'), command=reset_game, bg="#000000", borderwidth=0, highlightthickness=0, fg="#00ff00")
                                restart_button.place(x=200,y=150)
                        except:
                            continue
                    for i in red_light.finales:
                        try:
                            if canvas.coords(i)[1] + 32 >= 268:
                                scorer.update_highscore()
                                game_over=True
                                overlay = tk.Canvas(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='black', highlightthickness=0)
                                overlay.place(x=0, y=0)
                                overlay.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2 - 30,
                                    text="YOU LOST!", fill="#00ff00", font=("F77 Minecraft Regular", 36, "bold"))
                                restart_button = tk.Button(overlay, text="Restart", font=("F77 Minecraft Regular", 16, 'bold'), command=reset_game, bg="#000000", borderwidth=0, highlightthickness=0, fg="#00ff00")
                                restart_button.place(x=200,y=150)
                        except:
                            continue
                    for i in bluey.finales:
                        try:
                            if canvas.coords(i)[1] + 32 >= 268:
                                scorer.update_highscore()
                                game_over = True
                                overlay = tk.Canvas(canvas, width=canvas.winfo_width(), height=canvas.winfo_height(), bg='black', highlightthickness=0)
                                overlay.place(x=0, y=0)
                                overlay.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2 - 30,
                                    text="YOU LOST!", fill="#00ff00", font=("F77 Minecraft Regular", 36, "bold"))
                                restart_button = tk.Button(overlay, text="Restart", font=("F77 Minecraft Regular", 16, 'bold'), command=reset_game, bg="#000000", borderwidth=0, highlightthickness=0, fg="#00ff00")
                                restart_button.place(x=200,y=150)
                        except:
                            continue
                except Exception as e:
                    print("Error: (detect_alien_hit)",e)
            def next_wave(self):
                canvas.unbind("<Left>")
                canvas.unbind("<Right>")
                canvas.unbind("<Space>")
                if x.issfx == True:
                    footstep.play(loops=10)
                canvas.delete("all")
                canvas.create_text(250, 100, font=('F77 Minecraft Regular', 25, 'bold'), text="YOU WIN!", fill="#00ff00")
                with open(os.path.join(os.getcwd(),"PROGRESS.spaceinvaders"),'r+') as f:
                    old_score = f.read()
                    new_score = int(old_score)+25
                with open(os.path.join(os.getcwd(),"PROGRESS.spaceinvaders"),'w') as f:
                    f.write(str(new_score))
                xpearned = canvas.create_text(240,150,text="+25 XP",font=('F77 Minecraft Regular',11,'normal'),fill="#00ff00")
                backtohomebtn = tk.Button(canvas,text="Home",font=('F77 Minecraft Regular',14,'bold'),bg="#000000",fg="#00ff00",borderwidth=0,highlightthickness=0,command=lambda: reset_game())
                backtohomebtn.place(x=210,y=170)

                root.update()
                #time.sleep(2)

                # Reset the canvas
                #startgame(score=score)





        collbot = CollisionDetection()
        def check_if_collide():
            global bluey, enemies
            while True:
                if game_over == True:
                    return
                collbot.detectbullet()
                collbot.detectdeath()
                collbot.detectvictory()
                collbot.detect_alien_hit()
                print("COLLIDE")
                time.sleep(0.05)
        bulldetect = threading.Thread(target=check_if_collide)
        bulldetect.daemon = True
        bulldetect.start()
        def reset_game():
                background_music.stop()
                root.destroy()
                python_executable = sys.executable
                script_path = __file__  # This is the path to your script

                # Run the script using subprocess
                subprocess.run([python_executable, script_path], shell=False)
            
        root.bind("<Right>", player.move_right)
        root.bind("<d>", player.move_right)
        root.bind("<Left>",player.move_left)
        root.bind("<a>",player.move_left)
        root.bind("<space>",killer.shoot)
        root.bind("<s>",killer.shoot)




            



            

                    



            


            

            

    x = MainMenu()
    root.mainloop()
except FileNotFoundError as e:
    with open(os.path.join(os.getcwd(),"ERROR_IN_SPACEINVADERS.txt"),'w') as f:
        f.write(f"""
SPACE INVADERS HAS CRASHED!!!
_____________________________
-----------------------------
ERROR: THE GAME FILES LIKE
SOUNDTRACKS AND IMAGES WEREN'T
FOUND! ERROR IS AS FOLLOWS:
{traceback.format_exc()}""")
    os.system(f"notepad {os.path.join(os.getcwd(),"ERROR_IN_SPACEINVADERS.txt")}")
    import ctypes

    ctypes.windll.user32.MessageBoxW(0, f"{traceback.format_exc()}", "Warning: Space Invaders Has Crashed", 0x10 | 0x1)

except Exception as e:
    with open(os.path.join(os.getcwd(),"ERROR_IN_SPACEINVADERS.txt"),'w') as f:
            f.write(f"""
SPACE INVADERS HAS CRASHED!!!
_____________________________
-----------------------------
ERROR: PYTHON TKINTER UNKNOWN ERROR OCCURED!!!
ERROR IS AS FOLLOWS:
{traceback.format_exc()}""")
    os.system(f"notepad {os.path.join(os.getcwd(),"ERROR_IN_SPACEINVADERS.txt")}")


