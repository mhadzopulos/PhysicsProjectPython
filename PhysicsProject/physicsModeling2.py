from __future__ import print_function, division
from visual import *
from visual.graph import *	 
from visual.controls import*


scene.width=1200
scene.height=768
scene.background = color.white
scene.range = (7.5,15,15)
scene.center = (7,0,0)
c = controls(title='Start/Reset',
         x=1230, y=450, width=100, height=300, range=50)
b = button(pos=(0,30),width =35,height=15,text='Start/Reset',action=lambda: change())
b1 = button(pos=(0,0),width =35,height=15,text='EFIELD',action=lambda: ModEField())
b2 = button(pos=(0,-30),width =35,height=15,text='MFIELD',action=lambda: ModMField())
Efield = 0
Mfield = 0
def ModMField():
     global Mfield
     Mfield = float(input('Enter the Mfield: '))
def ModEField():
     global Efield
     Efield = float(input('Enter the Efield: '))
def change():
    global Efield
    global Mfield
    charge = 1.6* pow(10,-19)
    mass =  9.11* pow(10,-31)
    
    pointer1 = arrow(pos=(7,1.25,1), axis=(2,-25,0), shaftwidth=.1,length=2,color=color.green)
    pointer2 = arrow(pos=(2,1.25,1), axis=(2,-25,0), shaftwidth=.1,length=2,color=color.green)
    pointer3 = arrow(pos=(4,-.5,1), axis=(5,0,-95), shaftwidth=.2,length=2,color=color.red)
    ball = sphere(pos=(0,0,0), radius=.1, color=color.cyan)
    TopPlate = box(pos=(5,1.5,0), size=(10,.1,2), color=color.blue)
    BotPlate = box(pos=(5,-1.5,0), size=(10,.1,2), color=color.blue)

    
    #this how i get the force with magnetic field on the bottom and electric on top
    temp =   (charge *Mfield) - (charge * Efield)
    acceleration =  temp /mass
     
    
    deltat = .00000000005
    time = 0
    Vi = 20000000
    Vy = 0
    ball.trail = curve(color=ball.color)
    ball.velocity = vector(Vi,Vy,0)

    graph1 = gdisplay(x=0, y=0, width=scene.width/2, height=scene.height*.27777,
              title='Distance vs. Time', xtitle='t', ytitle='D',
              xmax=pow(deltat,.5)/(50), xmin=0, ymax=BotPlate.size.x, ymin=0,
              foreground=color.black, background=color.white)
    funct1 = gcurve(color=color.red)
    graph2 = gdisplay(x=scene.width/2, y=0, width=scene.width/2, height=scene.height*.27777,
              title='Velocity vs. Time', xtitle='t', ytitle='V',
              xmax=pow(deltat,.5)/(50), xmin=0, ymax=ball.velocity.x+deltat*abs(acceleration)*900, ymin=0,
              foreground=color.black, background=color.white)
    funct2 = gcurve(color=color.green)

    while ball.pos.y-ball.radius >= BotPlate.pos.y+BotPlate.size.y/2 and ball.pos.y+ball.radius <= TopPlate.pos.y - TopPlate.size.y/2 and ball.pos.x < 10:
        rate(1000)
        speed = pow((pow(ball.velocity.x,2)+pow(ball.velocity.y,2)),.5)
        funct1.plot(pos=(time,ball.pos.x))	# curve
        funct2.plot(pos=(time,speed))
        ball.velocity.y += acceleration*deltat
        ball.pos += ball.velocity*deltat
        ball.trail.append(pos=ball.pos)
        time = time + deltat
    print("Final postion: ",ball.pos.x," at time ",time,"\n")
    print("Final vector: (",ball.velocity.x,"i,",ball.velocity.y,"j)\n")
    print("Resultant velocity: ", pow(pow(ball.velocity.x,2)+pow(ball.velocity.y,2),.5))


    
