#RayonBalle
r=5
#DimensionsRaquette
lar=90
haut=10
#dt
lastTimeFrame=0
dt=0


SpeedY=0

def setup():
    global RackX, RackY, lastTimeFrame,Lancer
    size(400,400)
    frameRate(240)
    RackX=mouseX
    RackY=height-(height*5/100)
    lastTimeFrame=millis()
    Lancer=False
    
def draw():
    global dt, lastTimeFrame
    clear()
    dt=millis()-lastTimeFrame
    lastTimeFrame=millis()
    
    drawRaquette()
    drawBall()
    brick()
    
def drawRaquette():
    global RackX, RackY,lar,haut
    #TEST DE POSITION
    if 0+lar/2>mouseX:
        RackX=0
    if mouseX>width-lar/2:
        RackX=width-lar
    if 0+lar/2<mouseX<width-lar/2:
        RackX=mouseX-lar/2
    
    #DESSIN
    fill(255)
    rect(RackX, RackY,lar,haut)
        
def drawBall():
    ##AVANT LANCER
    global x, y, r, Speed, Lancer, dt,ballAngle, angleMax
    if Lancer==False:
        y=height-haut*2-r
        fill(255,0,0)
        circle(RackX+lar/2,RackY-r,r*2)    
        if mousePressed and (mouseButton == LEFT):
            Lancer=True
            x=mouseX 
            Speed=0.3
            ballAngle=PI/5
            angleMax=PI/1.9
    ##APRES LANCER
    if Lancer==True:
         move()
         fill(255,0,0)
         circle(x,y,r*2) 
    
         
def move():
    global x, y, Speed, ballAngle, angleMax, SpeedY,SpeedX
    
    #REBOND MUR
    if x+(r)>= width:
        Speed*=-1
        x=width-r
        ballAngle=-ballAngle
    elif x-(r)<=0:
        Speed*=-1
        ballAngle=-ballAngle
        x=r
    if y-(r)<=0:
        y=r
        ballAngle*=-1
        
    #REBOND RAQUETTE
    #de dessus:
    if RackY<y+r<RackY+haut and SpeedY<0:
        if RackX<x<RackX+lar:
            y=RackY-r
            Speed*=-1
            ratio=(x-RackX-lar/2)/(lar/2)
            ballAngle=PI/2-ratio*angleMax
            

    #des côtés:
    if RackY<y:
        if RackX-r<=x<=RackX or RackX+lar<=x<=RackX+lar+r :
            Speed*=-1
            Speed*=-1
    if y>=height:
        print("ded")
        clear()
        setup()
        firstbump=False
    SpeedX=Speed*dt*cos(ballAngle)
    SpeedY=Speed*dt*sin(ballAngle)
    x+=SpeedX
    y-=SpeedY
    
def brick():
    global x,y,r,Speed,ballAngle,SpeedX,SpeedY
    fill(0,255,0)
    bHaut=20
    bLar=100
    bX=width/2-bLar/2
    bY=height/5
    rect (bX,bY,bLar,bHaut)
    
    #bas
    if bY+bHaut-r<y-r<bY+bHaut:
        if bX<x<bX+bLar:
            if SpeedY>0:
                y=bY+bHaut+r
                Speed*=-1
                ratioB=(x-bX-bLar/2)/(bLar/2)
                ballAngle=PI/2+ratioB*angleMax
    #haut
    elif bY<y+r<bY+r:
        if bX<x<bX+bLar:
            if SpeedY<0:
                y=bY-r
                Speed*=-1
                ratioH=(x-bX-bLar/2)/(bLar/2)
                ballAngle=PI/2-ratioH*angleMax       
    #gauche
    if bY<y<bY+bHaut:
        if bX<x+r<bX+r:
            if SpeedX>0:
                print(SpeedX)
                x=bX-r
                Speed*=-1
                ratioG=(y-bY-bHaut/2)/(bHaut/2)
                ballAngle=PI/2-ratioG*angleMax
    #droite
        elif bX+bLar<x<bX+bLar+r:
            if SpeedX<0:
                ratioD=(y-bY-bHaut/2)/(bHaut/2)
                ballAngle=PI/2+ratioD*angleMax
                x=bX+bLar+r
                Speed*=-1


            
    
    
