

#By Fabian Beck @INFHO
#22.04.2023


import turtle
import time
from tkinter import *



class Ampel():
    """Hier wird eine Ampel mit vielen Funktionen enstehen"""
    
    def __init__(self,xpos,ypos,can=None):
        # hier passiert was tolles.
        print("Hier ist ihre Ampel entstanden")
        self.farben = ["Red","Yellow","Green"]
        self.turtyR = turtle.RawTurtle(can)
        self.turtyR.penup()
        self.turtyR.shape("circle")
        self.turtyR.color("Black")
        self.turtyR.goto(xpos,ypos+100)
        self.turtyG = turtle.RawTurtle(can)
        self.turtyG.penup()
        self.turtyG.shape("circle")
        self.turtyG.goto(xpos,ypos-100)
        self.turtyG.color("Green")
        self.turtyY = turtle.RawTurtle(can)
        self.turtyY.penup()
        self.turtyY.shape("circle")
        self.turtyY.color("Black")
        self.turtyY.goto(xpos,ypos+0)
        self.status = "Green"
        
    def __str__(self):
        return self.status
    
    def rot(self):
        self.turtyR.color("Red")
        self.status = "Red"
        self.turtyG.color("Black")
        self.turtyY.color("Black")
        
    def gruen(self):
        self.turtyG.color("Green")
        self.status = "Green"
        self.turtyR.color("Black")
        self.turtyY.color("Black")
        
    def gelb(self):
        self.turtyY.color("Yellow")
        self.turtyG.color("Black")
        self.turtyR.color("Black")
    def GelbRot(self):
        self.turtyG.color("Black")
        self.turtyY.color("Yellow")
        self.turtyR.color("Red")
         
   
class controller:
    """Der Ampelcontroller"""
    def __init__(A1,A2):
        pass
        









fenster = Tk()
fenster.title("Ampel")
canvas = Canvas(master = fenster, width = 600, height = 600)

canvas.pack()
		

try:
    
    fussgaengerampel = Ampel(100,0,canvas)
    autoampel = Ampel(-100,0,canvas)
    button = None
    def Auto():
        button.config(state="disabled")
        fussgaengerampel.gelb()
        fenster.after(2000,fussgaengerampel.rot)
        fenster.after(4000,autoampel.GelbRot)
        fenster.after(6000,autoampel.gruen)
        fenster.after(16000,autoampel.gelb)
        fenster.after(18000,autoampel.rot)
        fenster.after(20000,fussgaengerampel.GelbRot)
        fenster.after(22000,fussgaengerampel.gruen)
        fenster.after(22001,lambda:button.config(state="normal"))
    button = Button(fenster, text="Drücken", command=Auto)
    button.pack(side = LEFT)
    
    
    """"while True:
        autoampel.rot()
        fussgaengerampel.gruen()
        time.sleep(1)
        autoampel.GelbRot()
        time.sleep(1)
        autoampel.gruen()
        fussgaengerampel.rot()
        time.sleep(1)
        autoampel.gelb()
        time.sleep(1)
        fussgaengerampel.gruen()"""

except Exception as fehler:
    print("Irgentwas war komisch, error 404. Fehler:",
          fehler)
fenster.mainloop()


   
