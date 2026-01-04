'''
Use of OOP to get drink price, unique drink order and costumer each time
Use setActiveScreen to change game screen
Lots of animations to make smooth user interface
Unlimited rounds, keeps track of number of orders and total Profit
'''


from cmu_graphics import *
import random

def onAppStart(app):
    app.totalProfit=0
    app.orderNumber=0
    app.stepsPerSecond=60
    makeNewOrder(app)
    
def makeNewOrder(app):
    app.width=800
    app.height=533
    app.frontDesk=True
    app.costumers=[Costumer('Mike','cmu://1073283/43424346/image-removebg-preview+(3).png' ),Costumer('David','cmu://1073283/43424351/image-removebg-preview+(4).png' ), Costumer('Farnam', 'cmu://1073283/43424372/image-removebg-preview+(6).png'), Costumer('Emmy','cmu://1073283/43451102/IMG_3476__1_-removebg-preview.png'), Costumer('Camila','cmu://1073283/43451116/IMG_3479-removebg-preview.png'), Costumer('Avantika', 'cmu://1073283/43451119/IMG_3477-removebg-preview.png'), Costumer('Maria','cmu://1073283/43451124/IMG_3480-removebg-preview.png'), Costumer('Akshita','cmu://1073283/43451146/IMG_3478__1_-removebg-preview+(1).png'), Costumer('Isla','cmu://1073283/43470417/IMG_3496-removebg-preview.png'),Costumer('Nani','cmu://1073283/43534120/8434-removebg-preview.png'), Costumer('Julia','cmu://1073283/43534187/IMG_3535-removebg-preview.png'),
                    Costumer('Megha','cmu://1073283/43534199/IMG_3537-removebg-preview.png'),Costumer('Camille','cmu://1073283/43534206/IMG_3536-removebg-preview.png'), Costumer('Elizabeth','cmu://1073283/43534210/IMG_3538-removebg-preview.png'), Costumer('Yates','cmu://1073283/43992834/IMG_3717-removebg-preview.png')]
    print(len(app.costumers))
    app.costumerIndex=-1#random.randint(0,len(app.costumers)-1)
    app.baristaGreeting=False
    app.baristaimage='cmu://1073283/43425847/IMG_3420-removebg-preview.png'
    app.currentOrder=makeRandomOrder()
    app.iceInCupSpots=[]
    app.r=0
    app.g=0
    app.b=0
    app.chosenSize=None
    app.chosenBev=None
    app.chosenMilk=None
    app.chosenTopping=None
    app.chosenSize=None
    app.orderNumber+=1
    
def makeRandomOrder():
    drinks=['Chai Latte', 'Americano', 'Matcha', 'Pink Drink', 'Latte']
    milk=['Oat Milk', 'Soy Milk', 'Almond Milk', 'Whole Milk', '2% Milk']
    size=['Small','Medium','Large']
    ice=['No','Light','Normal','Extra','Light','Normal','Extra']
    bonus=['Whipped Cream', 'Cold Foam', 'Sprinkles', 'Cinnamon', None,'Whipped Cream', 'Cold Foam', 'Sprinkles', 'Cinnamon']
    return drinks[random.randint(0,len(drinks)-1)],milk[random.randint(0,len(milk)-1)],ice[random.randint(0,len(ice)-1)],size[random.randint(0,len(size)-1)],bonus[random.randint(0,len(bonus)-1)]

class Costumer:
    def __init__(self,name,imageurl):
        self.name=name
        self.imageurl=imageurl
    def __hash__(self):
        return hash(str(self))
    def __eq__(self,other):
        return type(self)==type(other) and (self.name==other.name and self.imageurl==other.imageurl)
    
class Beverage:
    def __init__(self, version, milk,ice,size,bonus):
        self.version=version
        self.milk=milk
        self.ice=ice
        self.size=size
        self.bonus=bonus
    def __repr__(self):
        return f'{self.version}, {self.milk}, {self.size}, {self.ice}, {self.bonus}'
        #return f'Can I get a {self.version}\nin a {self.size}\nwith {self.milk}.' if extra=='' else f'Can I get a {self.version}\nin a {self.size}\nwith {self.milk}\nand {extra}.'
    def __hash__(self):
        return hash(str(self))
    def __eq__(self,other):
        if type(self)==type(other):
            if (self.version==other.version and self.milk==other.milk) and (self.bonus==other.bonus and self.size==other.size):
                return self.ice==other.ice
        return False
    def getPrice(self):
        price=4
        if self.version=='Chai Latte' or self.version=='Matcha': price=5.5
        if self.version=='Latte': price=5
        if self.bonus!=None:
            price+=0.8
        if self.size=='Small':
            price-=0.5
        if self.size=='Large':
            price+=1
        return price
            
class Food:
    def __init__(self,version,price):
        self.version=version
        self.price=price
    def __eq__(self,other):
        return self.version==other.version and self.price==other.price
    def __hash__(self):
        return hash(str(self))
    def __repr__(self):
        return f'I want a {self.version}.'

############################################################
        #instructions
############################################################

def instructions_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill=rgb(171,111,85))
    drawLabel('''Rosalind's Coffee Corner''',app.width/2,app.height/10,size=40,fill='white',font='cinzel')
    drawLabel('Instructions',app.width/2,app.height/10+50,fill='white',size=24,font='monospace',bold=True)
    drawInstructions(app)
    drawLabel('Click anywhere to continue', app.width/2,app.height*0.9,size=20,fill='white',font='monospace',bold=True)
    
def drawInstructions(app):
    drawLabel('Congratulations! You decided to pursue your dream of',app.width/2,app.height/10+100,fill='white',size=20,font='monospace')
    drawLabel('fueling your caffeine addiction and opening a coffee shop.',app.width/2,app.height/10+130,fill='white',size=20,font='monospace')
    drawLabel('''Today is the opening day and you've invited all your friends.''',app.width/2,app.height/10+160,fill='white',size=20,font='monospace')
    drawLabel('Take and create their order, but remember- if you mess up',app.width/2,app.height/10+210,fill='white',size=20,font='monospace')
    drawLabel('they get their money back!',app.width/2,app.height/10+240,fill='white',size=20,font='monospace')

def instructions_onMousePress(app,mouseX,mouseY):
    setActiveScreen('takingOrder')

############################################################
        #takingOrder
############################################################

def takingOrder_onAppStart(app):
    takingOrder_resetForNewOrder(app)
    
def takingOrder_resetForNewOrder(app):
    app.baristaGreeting=False
    app.costumerOrdering=False
    app.baristaConfirming=False
    app.frontDeskurl='cmu://1073283/43424026/images+(1).jpg'
    app.moneyurl='cmu://1073283/43425941/image-removebg-preview+(8).png'
    app.moneyExchange=False
    app.moneycx,app.moneycy=500,500
    app.costumercx=app.width+130
    app.costumerComingIn=True
    takingOrder_onStep(app)

def takingOrder_redrawAll(app):
    if app.frontDesk:
        drawBackground(app,app.frontDeskurl)
        
def takingOrder_onKeyHold(app,key):
    if 'space' not in key:
        takingOrder_takeStep(app)
        
def drawBackground(app,imageurl):
    imageWidth,imageHeight=getImageSize(app.baristaimage)
    drawImage(imageurl,0,0,width=app.width,height=app.height)
    drawImage(app.baristaimage,app.width/5,app.height*2.5/4,width=imageWidth/2,height=imageHeight/2,align='center')
    imageWidth,imageHeight=getImageSize(app.costumers[app.costumerIndex].imageurl)
    drawImage(app.costumers[app.costumerIndex].imageurl,app.costumercx,app.height*3/4+10,width=imageWidth*0.7,height=imageHeight*0.7,align='center')
    if app.costumerOrdering:
        version,milk,ice,size,bonus=app.currentOrder
        drawOrder(app,Beverage(version,milk,ice,size,bonus),imageurl)
    elif app.baristaGreeting: drawBaristaGreeting(app)
    elif app.baristaConfirming: drawBaristaConfirming(app)
    elif app.moneyExchange: drawMoneyExchange(app)
    drawRect(app.width-100,0,100,70,fill='white')
    drawLabel('Profit:',app.width-50,20,size=16,font='monospace',bold=True)
    drawLabel('$'+str(app.totalProfit),app.width-50,50,size=16,font='monospace',bold=True)
    
def drawBaristaGreeting(app):
    drawOval(app.width/3,app.height/5,200,100,fill='white')
    drawRect(app.width/3-85,app.height/5+20,20,20,fill='white',borderWidth=2,rotateAngle=0,align='center')
    drawLabel('Hi, what can I get',app.width/3,app.height/5-10,size=16,font='monospace',bold=True)
    drawLabel('for you today?',app.width/3,app.height/5+10,size=16,font='monospace',bold=True)
    
def drawBaristaConfirming(app):
    drawOval(app.width/3,app.height/5,200,100,fill='white')
    drawRect(app.width/3-85,app.height/5+20,20,20,fill='white',borderWidth=2,rotateAngle=0,align='center')
    drawLabel('Ok, that will',app.width/3,app.height/5-10,size=16,font='monospace',bold=True)
    version,milk,ice,size,bonus=app.currentOrder
    new=Beverage(version,milk,ice,size,bonus)
    drawLabel(f'be ${Beverage.getPrice(new)}!',app.width/3,app.height/5+10,size=16,font='monospace',bold=True)
    
def drawOrder(app,index,imageurl):
    drawRect(app.width*0.75,app.height*0.25+75,20,20,fill='white',borderWidth=2,rotateAngle=45,align='center')
    drawOval(app.width*0.75,app.height*0.25,200,150,fill='white',borderWidth=2)
    drawLabel(index.version,app.width*0.75,app.height*0.25-40,size=20,font='monospace',bold=True)
    drawLabel(index.milk,app.width*0.75,app.height*0.25-20,size=20,font='monospace',bold=True)
    drawLabel(index.size,app.width*0.75,app.height*0.25,size=20,font='monospace',bold=True)
    drawLabel(index.ice+' ice',app.width*0.75,app.height*0.25+20,size=20,font='monospace',bold=True)
    if index.bonus!=None:
        drawLabel(index.bonus,app.width*0.75,app.height*0.25+40,size=20,font='monospace',bold=True)
        
def drawMoneyExchange(app):
    drawImage(app.moneyurl,app.moneycx,app.moneycy)
    pass
        
def takingOrder_onMousePress(app,mouseX,mouseY):
    if app.baristaGreeting:
        app.costumerOrdering=True
        app.baristaGreeting=False
    elif app.costumerOrdering:
        app.baristaGreeting=False
        app.baristaConfirming=True
        app.costumerOrdering=False
    elif app.baristaConfirming:
        version,milk,ice,size,bonus=app.currentOrder
        new=Beverage(version,milk,ice,size,bonus)
        app.totalProfit+=Beverage.getPrice(new)
        app.moneyExchange=True
        app.baristaConfirming=False
        
def takingOrder_onStep(app):
    if app.moneyExchange:
        app.moneycx-=7
        app.moneycy-=7
        if app.moneycx<=-455:
            app.moneyExchange=False
            pickingSize_resetForNewOrder(app)
            setActiveScreen('pickingSize')
    if app.costumerComingIn:
        if app.costumercx>app.width*3/4:
            app.costumercx-=5
        if app.costumercx<=app.width*3/4:
            app.baristaGreeting=True
            app.costumerComingIn=False

############################################################
        #Picking Size
############################################################

def pickingSize_onAppStart(app):
    pickingSize_resetForNewOrder(app)
    
def pickingSize_resetForNewOrder(app):
    app.borderColor1='black'
    app.borderColor2='black'
    app.borderColor3='black'
    app.cx11=100
    app.cx21=275
    app.cx31=450
    app.cupsMoving=False
    app.cupsExist=True
    app.cx=app.width/2

def pickingSize_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill=rgb(245,222,179))
    drawRect(0,app.height/2,app.width,app.height,fill=rgb(184,150,115))
    drawRect(-10,app.height*3/8,app.width+20,200,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawRect(-10,app.height*3/8+195,app.width+20,20,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawPolygon(130,250,250,250,270,350,100,350,fill=rgb(129,99,67),border=rgb(99,77,53),borderWidth=5)
    drawOrderNote(app)
    drawStep1(app)
    pass

def drawCupSelection(app):
    if app.cupsExist:
        drawPolygon(app.cx11,322,app.cx11+40,322,app.cx11+50,245,app.cx11-10,245,fill='white',opacity=80,border=app.borderColor1,borderWidth=3)
        drawPolygon(app.cx21,322,app.cx21+60,322,app.cx21+75,200,app.cx21-15,200,fill='white',opacity=80,border=app.borderColor2,borderWidth=3)
        drawPolygon(app.cx31,322,app.cx31+80,322,app.cx31+100,160,app.cx31-20,160,fill='white',opacity=80,border=app.borderColor3,borderWidth=3)
    pass

def pickingSize_onMouseMove(app,mouseX,mouseY):
    app.borderColor1='black'
    app.borderColor2='black'
    app.borderColor3='black'
    if True:
        if (mouseX>90 and mouseX<150) and (mouseY>245 and mouseY<322):
            app.borderColor1='gold'
        if (mouseX>85+175 and mouseX<350) and (mouseY>200 and mouseY<322):
            app.borderColor2='gold'
        if (mouseX>80+350 and mouseX<200+350) and (mouseY>160 and mouseY<322):
            app.borderColor3='gold'
            
def pickingSize_onMousePress(app,mouseX,mouseY):
    if True:
        if (mouseX>90 and mouseX<150) and (mouseY>245 and mouseY<322):
            app.chosenSize='Small'
            app.cupsMoving=True
        if (mouseX>85+175 and mouseX<350) and (mouseY>200 and mouseY<322):
            app.chosenSize='Medium'
            app.cupsMoving=True
        if (mouseX>80+350 and mouseX<200+350) and (mouseY>160 and mouseY<322):
            app.chosenSize='Large'
            app.cupsMoving=True
                
def pickingSize_onStep(app):
    if app.cupsMoving:
        app.cx+=10 if app.cx<3/2*app.width+50 else 0
        if app.chosenSize=='Small':
            app.cx11+=5 if app.cx11<400-20 else 0
            app.cx21+=5
            app.cx31+=5
        elif app.chosenSize=='Medium':
            app.cx11+=5 
            app.cx21+=5 if app.cx21<400-30 else 0
            app.cx31+=5
        elif app.chosenSize=='Large':
            app.cx11+=5
            app.cx21+=5
            app.cx31-=1 if app.cx31>400-40 else 0
        if app.cx11>app.width or (app.chosenSize=='Small' and app.cx21>app.width):
            app.cupsExist=False
            ice_resetForNewOrder(app)
            setActiveScreen('ice')
        
def drawStep1(app):
    drawLabel('Step #1: Get correct cup size', app.cx,app.height-50,size=30,font='monospace')
    drawLabel('Step #2: Drag ice into cup',-50-app.width+app.cx,app.height-50,size=30,font='monospace')
    drawCupSelection(app)

def drawOrderNote(app):
    drawRect(app.width-100,120,160,200,fill='white',align='center',borderWidth=3,border='black')
    drawLabel(f'Order #{app.orderNumber}',app.width-100,50,font='monospace',size=24,bold=True)
    cy=60
    for i in range(len(app.currentOrder)):
        cy+=25
        if i==2:
            drawLabel(app.currentOrder[i]+' ice',app.width-100,cy,size=20,font='monospace')
            continue
        elif i==4 and app.currentOrder[i]==None:
            continue
        drawLabel(app.currentOrder[i],app.width-100,cy,size=20,font='monospace')

############################################################
        #ice
############################################################

def ice_onAppStart(app):
    ice_resetForNewOrder(app)

def ice_resetForNewOrder(app):
    if app.currentOrder[2]=='No': app.numberOfIceCubes=0
    elif app.currentOrder[2]=='Light': app.numberOfIceCubes=2
    elif app.currentOrder[2]=='Normal': app.numberOfIceCubes=4
    elif app.currentOrder[2]=='Extra': app.numberOfIceCubes=6
    app.iceCubesInCup=0
    app.draggingIceCube=False
    i=0
    app.iceCubePositions=[]
    while i<20:
        i+=1
        app.iceCubePositions+=[[random.randint(140,240),random.randint(265,335)]]
    pass

def ice_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill=rgb(245,222,179))
    drawRect(0,app.height/2,app.width,app.height,fill=rgb(184,150,115))
    drawRect(-10,app.height*3/8,app.width+20,200,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawRect(-10,app.height*3/8+195,app.width+20,20,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawOrderNote(app)
    drawStep2(app)
    if app.draggingIceCube:
        drawCircle(app.icecx,app.icecy,10,fill=rgb(181,216,255),borderWidth=3,border=rgb(116,170,232))
    pass

def drawStep2(app):
    drawLabel('Step #2: Drag ice into cup', app.width/2,app.height-50,size=30,font='monospace')
    drawIceMachine(app)
    drawSingleCup(app,app.chosenSize)
    
def drawSingleCup(app,size):
    if size=='Small':
        drawPolygon(app.width/2-20,322,app.width/2+20,322,app.width/2+30,245,app.width/2-30,245,fill='white',opacity=80,border='black',borderWidth=3)
    elif size=='Medium':
        drawPolygon(app.width/2-30,322,app.width/2+30,322,app.width/2+45,200,app.width/2-45,200,fill='white',opacity=80,border='black',borderWidth=3)
    elif size=='Large':
        drawPolygon(app.width/2-40,322,app.width/2+40,322,app.width/2+60,160,app.width/2-60,160,fill='white',opacity=80,border='black',borderWidth=3)
    drawIceInCup(app,0)

def drawIceMachine(app):
    drawPolygon(130,250,250,250,270,350,100,350,fill=rgb(222,237,255),border=rgb(99,77,53),borderWidth=5)
    drawPolygon(130,250,250,250,270,150,100,150,fill=rgb(129,99,67),border=rgb(99,77,53),borderWidth=5)
    i=0
    for [cx,cy] in app.iceCubePositions:
        drawCircle(cx,cy,10,fill=rgb(181,216,255),borderWidth=3,border=rgb(116,170,232))
    pass

def ice_onMouseDrag(app,mouseX,mouseY):
    if app.draggingIceCube:
        app.icecx=mouseX
        app.icecy=mouseY

def ice_onMousePress(app,mouseX,mouseY):
    if (mouseX>130 and mouseX<270) and (mouseY>250 and mouseY<350):
        app.draggingIceCube=True
        app.icecx,app.icecy=mouseX,mouseY
    if len(app.iceInCupSpots)>app.numberOfIceCubes and ((mouseX>app.width/2-30 and mouseX<app.width/2+30) and (mouseY>170 and mouseY<315)):
        app.iceInCupSpots.pop()

def ice_onMouseRelease(app,mouseX,mouseY):
    if app.draggingIceCube and ((mouseX>app.width/2-30 and mouseX<app.width/2+30) and (mouseY>170 and mouseY<315)):
        app.iceInCupSpots+=[[mouseX,mouseY]]
        app.iceCubesInCup+=1
    app.draggingIceCube=False
    
def drawIceInCup(app,icecx):
    for i in range(len(app.iceInCupSpots)):
        [cx,cy]=app.iceInCupSpots[i]
        drawCircle(cx,cy+icecx,10,fill=rgb(181,216,255),borderWidth=3,border=rgb(116,170,232))
    if len(app.iceInCupSpots)>app.numberOfIceCubes:
        drawLabel('Too many ice cubes!',app.width/2,20,font='monospace',size=24,fill='red',bold=True)
        drawLabel('Press the cup to',app.width/2,45,font='monospace',size=24,fill='red',bold=True)
        drawLabel('remove an ice cube',app.width/2,70,font='monospace',size=24,fill='red',bold=True)
    else:
        drawLabel('Press space bar',app.width/2,20,font='monospace',size=24,bold=True)
        drawLabel('bar when done',app.width/2,45,font='monospace',size=24,bold=True)
        if len(app.iceInCupSpots)<app.numberOfIceCubes:
            drawLabel('Add more ice!',app.width/2,90,font='monospace',size=30,bold=True)
        
def ice_onKeyPress(app,key):
    if key=='space':# and len(app.iceInCupSpots)==app.numberOfIceCubes:
        addCaf_resetForNewOrder(app)
        setActiveScreen(screen='addCaf')
    pass
        
############################################################
        #addCaf
############################################################    

def addCaf_onAppStart(app):
    addCaf_resetForNewOrder(app)
    
def addCaf_resetForNewOrder(app):
    app.machinecy=-50
    app.ordercy=20
    app.movingDown=True
    app.cupcx=app.width/2
    app.highlightedMachineIndex=None
    app.drawDrink=False
    app.drinkColor=None
    app.moveMachinesUp=False

def addCaf_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill=rgb(245,222,179))
    drawRect(0,app.height/2,app.width,app.height,fill=rgb(184,150,115))
    drawRect(-10,app.height*3/8,app.width+20,200,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawRect(-10,app.height*3/8+195,app.width+20,20,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawPolygon(130,250,250,250,270,350,100,350,fill=rgb(129,99,67),border=rgb(99,77,53),borderWidth=5)
    drawMachines(app)
    drawStep3(app)
    drawMovingOrderNote(app)
    pass

def drawStep3(app):
    drawLabel('Step #3: Add caffeine', app.width/2,app.height-50,size=30,font='monospace')
    drawSingleCupWithLiquid(app,app.chosenSize)
    drawIceInCup1(app)
    
def drawIceInCup1(app):
    for i in range(len(app.iceInCupSpots)):
        [cx,cy]=app.iceInCupSpots[i]
        drawCircle(cx+app.cupcx-app.width/2,cy,10,fill=rgb(181,216,255),borderWidth=3,border=rgb(116,170,232))

def drawSingleCupWithLiquid(app,size):
    opacityLevel=80
    if size=='Small':
        drawPolygon(app.cupcx-20,322,app.cupcx+20,322,app.cupcx+30,245,app.cupcx-30,245,fill='white',opacity=opacityLevel,border='black',borderWidth=3)
        if app.drawDrink:
            opacityLevel=80
            drawPolygon(app.cupcx-20,322,app.cupcx+20,322,app.cupcx+25,270,app.cupcx-25,270,fill=app.drinkColor)
            drawPolygon(app.cupcx-20,322,app.cupcx+20,322,app.cupcx+30,245,app.cupcx-30,245,fill=None,opacity=opacityLevel,border='black',borderWidth=3)
    elif size=='Medium':
        drawPolygon(app.cupcx-30,322,app.cupcx+30,322,app.cupcx+45,200,app.cupcx-45,200,fill='white',opacity=opacityLevel,border='black',borderWidth=3)
        if app.drawDrink:
            opacityLevel=80
            drawPolygon(app.cupcx-30,322,app.cupcx+30,322,app.cupcx+40,240,app.cupcx-40,240,fill=app.drinkColor)
            drawPolygon(app.cupcx-30,322,app.cupcx+30,322,app.cupcx+45,200,app.cupcx-45,200,fill=None,opacity=opacityLevel,border='black',borderWidth=3)
    elif size=='Large':
        drawPolygon(app.cupcx-40,322,app.cupcx+40,322,app.cupcx+60,160,app.cupcx-60,160,fill='white',opacity=opacityLevel,border='black',borderWidth=3)
        if app.drawDrink:
            opacityLevel=80
            drawPolygon(app.cupcx-40,322,app.cupcx+40,322,app.cupcx+55,200,app.cupcx-55,200,fill=app.drinkColor)
            drawPolygon(app.cupcx-40,322,app.cupcx+40,322,app.cupcx+60,160,app.cupcx-60,160,fill=None,opacity=opacityLevel,border='black',borderWidth=3)
    drawIceInCup(app,app.cupcx-app.width)

def drawMachines(app):
    for i in range(5):
        borderColor='black'
        cx=app.width/10+app.width/5*i
        if i==0: 
            fillcolor=rgb(138,94,40)
            label='Chai'
        elif i==1: 
            fillcolor=rgb(102,119,68)
            label='Matcha'
        elif i==2: 
            fillcolor=rgb(102,57,2)
            label='Latte'
        elif i==3: 
            fillcolor=rgb(101,67,33)
            label='Americano'
        elif i==4: 
            fillcolor=rgb(255,105,180)
            label='Pink Mix'
        if app.highlightedMachineIndex==i:
            borderColor='gold'
        drawRect(cx,app.machinecy,100,150,border=borderColor,fill=fillcolor,align='center')
        drawRect(cx,app.machinecy+30,90,20,border='black',borderWidth=2,fill=rgb(225,204,177),align='center')
        drawLabel(label,cx,app.machinecy+30,font='monospace',bold=True,size=16)
        
def addCaf_onStep(app):
    if not app.moveMachinesUp:
        if app.machinecy<60:
            app.machinecy+=5
        if app.ordercy<=app.height-220:
            app.ordercy+=5
    else:
        if app.machinecy>-150:
            app.machinecy-=5
        else:
            milk_resetForNewOrder(app)
            setActiveScreen(screen='milk')
        
def addCaf_onMouseMove(app,mouseX,mouseY):
    if mouseY<140:
        if (mouseY<140) and (mouseX>app.width/10+app.width/5*0-50 and mouseX<app.width/10+app.width/5*0+50):
            app.highlightedMachineIndex=0
        elif (mouseY<app.machinecy+60) and (mouseX>app.width/10+app.width/5*1-50 and mouseX<app.width/10+app.width/5*1+50):
            app.highlightedMachineIndex=1
        elif (mouseY<app.machinecy+60) and (mouseX>app.width/10+app.width/5*2-50 and mouseX<app.width/10+app.width/5*2+50):
            app.highlightedMachineIndex=2
        elif (mouseY<app.machinecy+60) and (mouseX>app.width/10+app.width/5*3-50 and mouseX<app.width/10+app.width/5*3+50):
            app.highlightedMachineIndex=3
        elif (mouseY<app.machinecy+60) and (mouseX>app.width/10+app.width/5*4-50 and mouseX<app.width/10+app.width/5*4+50):
            app.highlightedMachineIndex=4
    else:
        app.highlightedMachineIndex=None
            
def addCaf_onMousePress(app,mouseX,mouseY):
    if cupUnderneathCorrectMachine(app,mouseX,mouseY):
        app.moveMachinesUp=True
        pass
        
def cupUnderneathCorrectMachine(app,mouseX,mouseY):
    app.drinkType=app.currentOrder[0]
    print(mouseX,mouseY,app.cupcx)
    if mouseY<140 and abs(mouseX-app.cupcx)<=50:
        if (mouseY<130) and (mouseX>app.width/10+app.width/5*0-50 and mouseX<app.width/10+app.width/5*0+50):
            if True:#app.drinkType=='Chai Latte':
                app.drawDrink=True
                app.drinkColor=rgb(138,94,40)
                app.r=138
                app.g=94
                app.b=40
                app.chosenBev='Chai Latte'
                return True
        elif (mouseY<app.machinecy+60) and (mouseX>app.width/10+app.width/5*1-50 and mouseX<app.width/10+app.width/5*1+50):
            if True:# app.drinkType=='Matcha':
                app.drawDrink=True
                app.drinkColor=rgb(102,119,68)
                app.r=102
                app.g=119
                app.b=68
                app.chosenBev='Matcha'
                return True
        elif (mouseY<app.machinecy+60) and (mouseX>app.width/10+app.width/5*2-50 and mouseX<app.width/10+app.width/5*2+50):
            if True:#app.drinkType=='Latte':
                app.drawDrink=True
                app.drinkColor=rgb(102,57,2)
                app.r=102
                app.g=57
                app.b=2
                app.chosenBev='Latte'
                return True
        elif (mouseY<app.machinecy+60) and (mouseX>app.width/10+app.width/5*3-50 and mouseX<app.width/10+app.width/5*3+50):
            if True:#app.drinkType=='Americano':
                app.drawDrink=True
                app.drinkColor=rgb(101,67,33)
                app.r=101
                app.g=67
                app.b=33
                app.chosenBev='Americano'
                return True
        elif (mouseY<app.machinecy+60) and (mouseX>app.width/10+app.width/5*4-50 and mouseX<app.width/10+app.width/5*4+50):
            if True:#app.drinkType=='Pink Drink':
                app.drawDrink=True
                app.drinkColor=rgb(255,105,180)
                app.r=255
                app.g=105
                app.b=180
                app.chosenBev='Pink Drink'
                return True
    return False
        
def addCaf_onMouseDrag(app,mouseX,mouseY):
    app.cupcx=mouseX
    pass
        
def drawMovingOrderNote(app):
    drawRect(app.width-100,app.ordercy+100,160,200,fill='white',align='center',borderWidth=3,border='black')
    drawLabel(f'Order #{app.orderNumber}',app.width-100,app.ordercy+30,font='monospace',size=24,bold=True)
    cy=app.ordercy+30
    for i in range(len(app.currentOrder)):
        cy+=25
        if i==2:
            drawLabel(app.currentOrder[i]+' ice',app.width-100,cy,size=20,font='monospace')
            continue
        elif i==4 and app.currentOrder[i]==None:
            continue
        drawLabel(app.currentOrder[i],app.width-100,cy,size=20,font='monospace')

############################################################
        #milk
############################################################

def milk_resetForNewOrder(app):
    app.milkMachinecy=-50
   # app.ordercy=20
    #app.cupcx=app.width/2
    app.drawDrink=True
    app.drawMilk=False
    app.moveMilkMachinesUp=False
    app.highlightedMilkMachineIndex=None
    
def milk_onAppStart(app):
    milk_resetForNewOrder(app)

def milk_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill=rgb(245,222,179))
    drawRect(0,app.height/2,app.width,app.height,fill=rgb(184,150,115))
    drawRect(-10,app.height*3/8,app.width+20,200,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawRect(-10,app.height*3/8+195,app.width+20,20,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawPolygon(130,250,250,250,270,350,100,350,fill=rgb(129,99,67),border=rgb(99,77,53),borderWidth=5)
    drawStep4(app)
    drawMovingOrderNote(app)
    drawMilkMachines(app)
    pass

def drawStep4(app):
    drawLabel('Step #4: Add milk', app.width/2,app.height-50,size=30,font='monospace')
    drawSingleCupWithLiquid(app,app.chosenSize)
    drawIceInCup1(app)

def drawSingleCupWithLiquid(app,size):
    opacityLevel=80
    if size=='Small':
        drawPolygon(app.cupcx-20,322,app.cupcx+20,322,app.cupcx+30,245,app.cupcx-30,245,fill='white',opacity=opacityLevel,border='black',borderWidth=3)
        if app.drawDrink:
            opacityLevel=80
            drawPolygon(app.cupcx-20,322,app.cupcx+20,322,app.cupcx+25,270,app.cupcx-25,270,fill=app.drinkColor)
            if app.drawMilk:
                drawPolygon(app.cupcx+25,270,app.cupcx-25,270,app.cupcx-30,245,app.cupcx+30,245,fill='white')
            drawPolygon(app.cupcx-20,322,app.cupcx+20,322,app.cupcx+30,245,app.cupcx-30,245,fill=None,opacity=opacityLevel,border='black',borderWidth=3)
    elif size=='Medium':
        drawPolygon(app.cupcx-30,322,app.cupcx+30,322,app.cupcx+45,200,app.cupcx-45,200,fill='white',opacity=opacityLevel,border='black',borderWidth=3)
        if app.drawDrink:
            opacityLevel=80
            drawPolygon(app.cupcx-30,322,app.cupcx+30,322,app.cupcx+40,240,app.cupcx-40,240,fill=app.drinkColor)
            if app.drawMilk:
                drawPolygon(app.cupcx+40,240,app.cupcx-40,240,app.cupcx-45,200,app.cupcx+45,200,fill='white')
            drawPolygon(app.cupcx-30,322,app.cupcx+30,322,app.cupcx+45,200,app.cupcx-45,200,fill=None,opacity=opacityLevel,border='black',borderWidth=3)
    elif size=='Large':
        drawPolygon(app.cupcx-40,322,app.cupcx+40,322,app.cupcx+60,160,app.cupcx-60,160,fill='white',opacity=opacityLevel,border='black',borderWidth=3)
        if app.drawDrink:
            opacityLevel=80
            drawPolygon(app.cupcx-40,322,app.cupcx+40,322,app.cupcx+55,200,app.cupcx-55,200,fill=app.drinkColor)
            if app.drawMilk:
                drawPolygon(app.cupcx+55,200,app.cupcx-55,200,app.cupcx-60,160,app.cupcx+60,160,fill='white')
            drawPolygon(app.cupcx-40,322,app.cupcx+40,322,app.cupcx+60,160,app.cupcx-60,160,fill=None,opacity=opacityLevel,border='black',borderWidth=3)

def drawMilkMachines(app):
    for i in range(5):
        borderColor='black'
        cx=app.width/10+app.width/5*i
        fillcolor=rgb(255,253,245)
        if i==0: 
            label='Oat'
        elif i==1: 
            label='Soy'
        elif i==2: 
            label='Almond'
        elif i==3: 
            label='Whole'
        elif i==4: 
            label='2% Milk'
        if app.highlightedMilkMachineIndex==i:
            borderColor='gold'
        drawRect(cx,app.milkMachinecy,100,150,border=borderColor,fill=fillcolor,align='center')
        drawRect(cx,app.milkMachinecy+30,90,20,border='black',borderWidth=2,fill=rgb(212,243,255),align='center')
        drawLabel(label,cx,app.milkMachinecy+30,font='monospace',bold=True,size=16)
        
def milk_onStep(app):
    if not app.moveMilkMachinesUp:
        if app.milkMachinecy<60:
            app.milkMachinecy+=5
    else:
        if app.milkMachinecy>-150:
            app.milkMachinecy-=5
        if app.cupcx//5<app.width//10:
            app.cupcx+=5
        elif app.cupcx//5>app.width//10:
            app.cupcx-=5
        else:
            if app.milkMachinecy<-50:
                shake_resetForNewOrder(app)
                setActiveScreen(screen='shake')
        
def milk_onMouseMove(app,mouseX,mouseY):
    if mouseY<140:
        if (mouseX>app.width/10+app.width/5*0-50 and mouseX<app.width/10+app.width/5*0+50):
            app.highlightedMilkMachineIndex=0
        elif (mouseX>app.width/10+app.width/5*1-50 and mouseX<app.width/10+app.width/5*1+50):
            app.highlightedMilkMachineIndex=1
        elif (mouseX>app.width/10+app.width/5*2-50 and mouseX<app.width/10+app.width/5*2+50):
            app.highlightedMilkMachineIndex=2
        elif (mouseX>app.width/10+app.width/5*3-50 and mouseX<app.width/10+app.width/5*3+50):
            app.highlightedMilkMachineIndex=3
        elif (mouseX>app.width/10+app.width/5*4-50 and mouseX<app.width/10+app.width/5*4+50):
            app.highlightedMilkMachineIndex=4
        else:
            app.highlightedMilkMachineIndex=None
    else:
        app.highlightedMilkMachineIndex=None
            
def milk_onMousePress(app,mouseX,mouseY):
    if cupUnderneathCorrectMilkMachine(app,mouseX,mouseY):
        app.moveMilkMachinesUp=True
        pass
        
def cupUnderneathCorrectMilkMachine(app,mouseX,mouseY):
    app.milkType=app.currentOrder[1]
    if mouseY<140 and abs(mouseX-app.cupcx)<=50:
        if (mouseX>app.width/10+app.width/5*0-50 and mouseX<app.width/10+app.width/5*0+50):
            if True:#app.milkType=='Oat Milk':
                app.drawMilk=True
                app.chosenMilk='Oat Milk'
                return True
        elif (mouseX>app.width/10+app.width/5*1-50 and mouseX<app.width/10+app.width/5*1+50):
            if True:# app.milkType=='Soy Milk':
                app.drawMilk=True
                app.chosenMilk='Soy Milk'
                return True
        elif (mouseX>app.width/10+app.width/5*2-50 and mouseX<app.width/10+app.width/5*2+50):
            if True:# app.milkType=='Almond Milk':
                app.drawMilk=True
                app.chosenMilk='Almond Milk'
                return True
        elif (mouseX>app.width/10+app.width/5*3-50 and mouseX<app.width/10+app.width/5*3+50):
            if True:# app.milkType=='Whole Milk':
                app.drawMilk=True
                app.chosenMilk='Whole Milk'
                return True
        elif (mouseX>app.width/10+app.width/5*4-50 and mouseX<app.width/10+app.width/5*4+50):
            if True:# app.milkType=='2% Milk':
                app.drawMilk=True
                app.chosenMilk='2% Milk'
                return True
    return False
        
def milk_onMouseDrag(app,mouseX,mouseY):
    app.cupcx=mouseX
    pass

############################################################
        #shake
############################################################

def shake_onAppStart(app):
    shake_resetForNewOrder(app)
    
def shake_resetForNewOrder(app):
    app.shakeAngle=0
    app.shakedy=0
    app.shakeIt=False
    app.counter=0
    app.drinkIsMixed=False
    app.startTransitionTo6=False
    app.titleside=0

def shake_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill=rgb(245,222,179))
    drawRect(0,app.height/2,app.width,app.height,fill=rgb(184,150,115))
    drawRect(-10,app.height*3/8,app.width+20,200,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawRect(-10,app.height*3/8+195,app.width+20,20,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawPolygon(130,250,250,250,270,350,100,350,fill=rgb(129,99,67),border=rgb(99,77,53),borderWidth=5)
    drawStep5(app)
    drawMovingOrderNote(app)
    pass

def drawStep5(app):
    drawLabel('Step #5: Hold the space bar to shake', app.width/2+app.titleside,50,size=30,font='monospace')
    drawShakingSingleCupWithLiquid(app,app.chosenSize) if not app.drinkIsMixed else drawMixedDrink(app,app.chosenSize)
    drawIceInCup2(app)
    if app.drinkIsMixed:
        drawLabel('All Done! Press',app.width/2,app.height-60+app.titleside,font='monospace',size=24,bold=True)
        drawLabel('anywhere to continue',app.width/2,app.height-30+app.titleside,font='monospace',size=24,bold=True)
    
def drawIceInCup2(app):
    for i in range(len(app.iceInCupSpots)):
        [cx,cy]=app.iceInCupSpots[i]
        drawCircle(cx+app.cupcx-app.width/2,cy+app.shakedy,10,fill=rgb(181,216,255),borderWidth=3,border=rgb(116,170,232))
    
def drawShakingSingleCupWithLiquid(app,size):
    opacityLevel=80
    fillColor=app.drinkColor
    if size=='Small':
        drawPolygon(app.cupcx-20,322+app.shakedy,app.cupcx+20,322+app.shakedy,app.cupcx+30,245+app.shakedy,app.cupcx-30,245+app.shakedy,fill='white',border='black',borderWidth=3)
        drawPolygon(app.cupcx-20,322+app.shakedy,app.cupcx+20,322+app.shakedy,app.cupcx+25,270+app.shakedy,app.cupcx-25,270+app.shakedy,fill=fillColor)
        drawPolygon(app.cupcx+25,270+app.shakedy,app.cupcx-25,270+app.shakedy,app.cupcx-30,245+app.shakedy,app.cupcx+30,245+app.shakedy,fill='white')
        drawPolygon(app.cupcx-20,322+app.shakedy,app.cupcx+20,322+app.shakedy,app.cupcx+30,245+app.shakedy,app.cupcx-30,245+app.shakedy,fill=None,border='black',borderWidth=3)
    elif size=='Medium':
        drawPolygon(app.cupcx-30,322+app.shakedy,app.cupcx+30,322+app.shakedy,app.cupcx+45,200+app.shakedy,app.cupcx-45,200+app.shakedy,fill='white',border='black',borderWidth=3)
        drawPolygon(app.cupcx-30,322+app.shakedy,app.cupcx+30,322+app.shakedy,app.cupcx+40,240+app.shakedy,app.cupcx-40,240+app.shakedy,fill=fillColor)
        drawPolygon(app.cupcx+40,240+app.shakedy,app.cupcx-40,240+app.shakedy,app.cupcx-45,200+app.shakedy,app.cupcx+45,200+app.shakedy,fill='white')
        drawPolygon(app.cupcx-30,322+app.shakedy,app.cupcx+30,322+app.shakedy,app.cupcx+45,200+app.shakedy,app.cupcx-45,200+app.shakedy,fill=None,border='black',borderWidth=3)
    elif size=='Large':
        drawPolygon(app.cupcx-40,322+app.shakedy,app.cupcx+40,322+app.shakedy,app.cupcx+60,160+app.shakedy,app.cupcx-60,160+app.shakedy,fill='white',border='black',borderWidth=3)
        drawPolygon(app.cupcx-40,322+app.shakedy,app.cupcx+40,322+app.shakedy,app.cupcx+55,200+app.shakedy,app.cupcx-55,200+app.shakedy,fill=fillColor)
        drawPolygon(app.cupcx+55,200+app.shakedy,app.cupcx-55,200+app.shakedy,app.cupcx-60,160+app.shakedy,app.cupcx+60,160+app.shakedy,fill='white')
        drawPolygon(app.cupcx-40,322+app.shakedy,app.cupcx+40,322+app.shakedy,app.cupcx+60,160+app.shakedy,app.cupcx-60,160+app.shakedy,fill=None,border='black',borderWidth=3)
        
def shake_onKeyHold(app,key):
    if 'space' in key:
        if not app.drinkIsMixed:
            app.shakeIt=True
        
def shake_onKeyRelease(app,key):
    if 'space' in key:
        app.shakeIt=False
        
def shake_onStep(app):
    if app.shakeIt:
        app.counter+=1
        if app.shakedy!=10 and app.shakedy!=0.01:
            app.shakedy=10
        else:
            app.shakedy=-10
    if app.counter>=150:
        app.cupcx=app.width/2
        app.drinkIsMixed=True
        app.shakedy=0.01
    if app.startTransitionTo6:
        if app.titleside<app.width:
            app.titleside+=10
        else:
            toppings_resetForNewOrder(app)
            setActiveScreen(screen='toppings')
        
def shake_onMousePress(app,mouseX,mouseY):
    if app.drinkIsMixed:
        app.startTransitionTo6=True
        
def drawMixedDrink(app,size):
    fillcolor=rgb((app.r+255/2)//1.5,(app.g+255/2)//1.5,(app.b+255/2)//1.5)
    if size=='Small':
        drawPolygon(app.cupcx-20,322,app.cupcx+20,322,app.cupcx+30,245,app.cupcx-30,245,fill=fillcolor,border='black',borderWidth=3)
    elif size=='Medium':
        drawPolygon(app.cupcx-30,322,app.cupcx+30,322,app.cupcx+45,200,app.cupcx-45,200,fill=fillcolor,border='black',borderWidth=3)
    elif size=='Large':
        drawPolygon(app.cupcx-40,322,app.cupcx+40,322,app.cupcx+60,160,app.cupcx-60,160,fill=fillcolor,border='black',borderWidth=3)
    
############################################################
        #toppings
############################################################

def toppings_onAppStart(app):
    toppings_resetForNewOrder(app)
    
def toppings_resetForNewOrder(app):
    app.titledx=-50
    toppings_reset(app)
    app.isDragging=False
    app.draggedIndex=None
    app.movingToppings=True
    app.pourCounter=0
    app.isPouring=False
    app.cy1=app.height+50
    app.cy2=app.height+50
    app.cy3=app.height+50
    app.cy4=app.height+50
    
def toppings_reset(app):
    app.cy1=193
    app.cy2=193
    app.cy3=193
    app.cy4=193
    app.cx1=app.width/6
    app.cx2=app.width/3
    app.cx3=app.width*2/3
    app.cx4=app.width*5/6
    app.rotate1=0
    app.rotate2=0
    app.rotate3=0
    app.rotate4=0

def toppings_redrawAll(app):
    drawRect(0,0,app.width,app.height,fill=rgb(245,222,179))
    drawRect(0,app.height/2,app.width,app.height,fill=rgb(184,150,115))
    drawRect(-10,app.height*3/8,app.width+20,200,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawRect(-10,app.height*3/8+195,app.width+20,20,border=rgb(99,77,53),fill=rgb(129,99,67),borderWidth=5)
    drawPolygon(130,250,250,250,270,350,100,350,fill=rgb(129,99,67),border=rgb(99,77,53),borderWidth=5)
    drawStep6(app)
    drawMovingOrderNote(app)
    
def drawStep6(app):
    drawLabel('Step #6: Add-ons', app.width/2,app.titledx,size=30,font='monospace')
    drawLabel('Press space to remove topping', app.width/2,app.titledx+30,size=24,font='monospace')
    drawLabel('Press d when done', app.width/2,app.height-app.titledx,size=24,font='monospace')
    if app.isPouring==False and app.pourCounter>0:
        drawToppingsOnDrink(app,app.chosenSize)
    drawMixedDrink(app,app.chosenSize)
    drawIceInCup2(app)
    drawToppings(app)
    
def toppings_onStep(app):
    if app.movingToppings:
        if app.titledx<50:
            app.titledx+=5
        if app.cy1>200:
            app.cy1-=10
        elif app.cy2>200:
            app.cy2-=10
        elif app.cy3>200:
            app.cy3-=10
        elif app.cy4>200:
            app.cy4-=10
        else:
            app.movingToppings=False
    if app.isPouring:
        if app.pourCounter<50:
            app.pourCounter+=1
        else:
            app.isPouring=False
            toppings_reset(app)
        
def drawToppings(app):
    drawRect(app.cx1,app.cy1,50,100,align='center',fill='red',border='black',rotateAngle=app.rotate1)
    drawLabel('Sprinkles',app.cx1,app.cy1,font='monospace',bold=True,rotateAngle=-90+app.rotate1,size=16)
    drawRect(app.cx2,app.cy2,50,100,align='center',fill='lightBlue',border='black',rotateAngle=app.rotate2)
    drawLabel('Whipped',app.cx2,app.cy2,font='monospace',bold=True,rotateAngle=-90+app.rotate2,size=16)
    drawRect(app.cx3,app.cy3,50,100,align='center',fill=rgb(107,65,57),border='black',rotateAngle=app.rotate3)
    drawLabel('Cinnamon',app.cx3,app.cy3,font='monospace',bold=True,rotateAngle=90+app.rotate3,fill='white',size=16)
    drawRect(app.cx4,app.cy4,50,100,align='center',fill=rgb(245,245,245),border='black',rotateAngle=app.rotate4)
    drawLabel('Cold Foam',app.cx4,app.cy4,font='monospace',bold=True,rotateAngle=90+app.rotate4,size=16)
    
def toppings_onMouseDrag(app,mouseX,mouseY):
    if app.pourCounter==0:
        if ((mouseX>app.cx1-25 and mouseX<app.cx1+25) and (mouseY>app.cy1-50 and mouseY<app.cy1+50)) and (app.draggedIndex==None or app.draggedIndex==1):
            app.isDragging=True
            app.cx1,app.cy1=mouseX,mouseY
            app.rotate1=45
            app.draggedIndex=1
        elif ((mouseX>app.cx2-25 and mouseX<app.cx2+25) and (mouseY>app.cy2-50 and mouseY<app.cy2+50)) and (app.draggedIndex==None or app.draggedIndex==2):
            app.isDragging=True
            app.cx2,app.cy2=mouseX,mouseY
            app.rotate2=45
            app.draggedIndex=2
        elif ((mouseX>app.cx3-25 and mouseX<app.cx3+25) and (mouseY>app.cy3-50 and mouseY<app.cy3+50)) and (app.draggedIndex==None or app.draggedIndex==3):
            app.isDragging=True
            app.cx3,app.cy3=mouseX,mouseY
            app.rotate3=-45
            app.draggedIndex=3
        elif ((mouseX>app.cx4-25 and mouseX<app.cx4+25) and (mouseY>app.cy4-50 and mouseY<app.cy4+50)) and (app.draggedIndex==None or app.draggedIndex==4):
            app.isDragging=True
            app.cx4,app.cy4=mouseX,mouseY
            app.rotate4=-45
            app.draggedIndex=4
            
def toppings_onMouseRelease(app,mouseX,mouseY):
    if app.pourCounter!=50:
        if (mouseX>300 and mouseX<470) and mouseY<200:
            app.isPouring=True
            if app.draggedIndex==1: app.rotate1,app.chosenTopping=110,'Sprinkles'
            elif app.draggedIndex==2: app.rotate2,app.chosenTopping=110,'Whipped Cream'
            elif app.draggedIndex==3: app.rotate3,app.chosenTopping=-110,'Cinnamon'
            elif app.draggedIndex==4: app.rotate4,app.chosenTopping=-110, 'Cold Foam'
        else:
            toppings_reset(app)
            app.draggedIndex=None
            
def toppings_onKeyPress(app,key):
    if 'space' in key:
        toppings_reset(app)
        app.draggedIndex=None
        app.pourCounter=0
    elif 'd' in key:
        givingBackOrder_resetForNewOrder(app)
        setActiveScreen(screen='givingBackOrder')
        
def toppings_reset(app):
    app.cy1=193
    app.cy2=193
    app.cy3=193
    app.cy4=193
    app.cx1=app.width/6
    app.cx2=app.width/3
    app.cx3=app.width*2/3
    app.cx4=app.width*5/6
    app.rotate1=0
    app.rotate2=0
    app.rotate3=0
    app.rotate4=0
    
def drawToppingsOnDrink(app,size):
    if size=='Small': y,w=245,50
    if size=='Medium': y,w=200,80
    if size=='Large': y,w=160,110
    if app.draggedIndex==1:
        drawRect(app.width/2,y-2,w,4,fill='red',align='center')
    elif app.draggedIndex==2:
        drawCircle(app.width/2,y,(w)/2,fill='white')
    elif app.draggedIndex==3:
        drawRect(app.width/2,y-2,w,4,fill=rgb(107,65,57),align='center')
    elif app.draggedIndex==4:
        drawRect(app.width/2,y-2,w,6,fill='white',align='center')
    
############################################################
        #Giving Back Order
############################################################

def givingBackOrder_onAppStart(app):
    givingBackOrder_resetForNewOrder(app)
    
def givingBackOrder_resetForNewOrder(app):
    app.finalDrinkSize=app.chosenSize
    app.finalDrinkcx=245
    app.finalDrinkcy=500
    app.personThanking=False
    app.handingOver=True
    app.costumerLeaving=False
    app.pressToContinuecy=-50

def givingBackOrder_redrawAll(app):
    if app.frontDesk:
        drawBackground(app,app.frontDeskurl)
        drawFinalDrink(app,app.chosenSize)
    if app.personThanking:
        drawRect(app.width*0.75,app.height*0.25+75,20,20,fill='white',borderWidth=2,rotateAngle=45,align='center')
        drawOval(app.width*0.75,app.height*0.25,200,150,fill='white',borderWidth=2)
        drawLabel('Press anywhere to continue',app.width/2,app.pressToContinuecy,size=24,bold=True,font='monospace',fill='white')
        if sameAsOrder(app):
            drawLabel('This is',app.width*0.75,app.height*0.25-40,size=20,font='monospace',bold=True)
            drawLabel('delicious!',app.width*0.75,app.height*0.25-20,size=20,font='monospace',bold=True)
            drawLabel('Thank you',app.width*0.75,app.height*0.25,size=20,font='monospace',bold=True)
            drawLabel('for this',app.width*0.75,app.height*0.25+20,size=20,font='monospace',bold=True)
            drawLabel('yummy drink.',app.width*0.75,app.height*0.25+40,size=20,font='monospace',bold=True)
        else:
            drawLabel('Umm, I',app.width*0.75,app.height*0.25-40,size=20,font='monospace',bold=True)
            drawLabel('''don't think''',app.width*0.75,app.height*0.25-20,size=20,font='monospace',bold=True)
            drawLabel('that this',app.width*0.75,app.height*0.25,size=20,font='monospace',bold=True)
            drawLabel('is correct.',app.width*0.75,app.height*0.25+20,size=20,font='monospace',bold=True)
            drawLabel('0 stars.',app.width*0.75,app.height*0.25+40,size=20,font='monospace',bold=True)

def drawFinalDrink(app,size):
    fillcolor=rgb((app.r+255/2)//1.5,(app.g+255/2)//1.5,(app.b+255/2)//1.5)
    if size=='Small':
        y,w=245-322+app.finalDrinkcy,50
        drawFinalToppings(app,y,w)
        drawPolygon(app.finalDrinkcx-20,app.finalDrinkcy,app.finalDrinkcx+20,app.finalDrinkcy,app.finalDrinkcx+30,245-322+app.finalDrinkcy,app.finalDrinkcx-30,245-322+app.finalDrinkcy,fill=fillcolor,border='black',borderWidth=3)
        drawIceInCup3(app,322-245)
    elif size=='Medium':
        y,w=200-322+app.finalDrinkcy,80
        drawFinalToppings(app,y,w)
        drawPolygon(app.finalDrinkcx-30,app.finalDrinkcy,app.finalDrinkcx+30,app.finalDrinkcy,app.finalDrinkcx+45,200-322+app.finalDrinkcy,app.finalDrinkcx-45,200-322+app.finalDrinkcy,fill=fillcolor,border='black',borderWidth=3)
        drawIceInCup3(app,322-200)
    elif size=='Large':
        y,w=160-322+app.finalDrinkcy,110
        drawFinalToppings(app,y,w)
        drawPolygon(app.finalDrinkcx-40,app.finalDrinkcy,app.finalDrinkcx+40,app.finalDrinkcy,app.finalDrinkcx+60,160-322+app.finalDrinkcy,app.finalDrinkcx-60,160-322+app.finalDrinkcy,fill=fillcolor,border='black',borderWidth=3)
        drawIceInCup3(app,322-160)
        
def drawFinalToppings(app,y,w):
    if app.draggedIndex==1:
        drawRect(app.finalDrinkcx,y-2,w,4,fill='red',align='center')
    elif app.draggedIndex==2:
        drawCircle(app.finalDrinkcx,y,w/2,fill='white')
    elif app.draggedIndex==3:
        drawRect(app.finalDrinkcx,y-2,w,4,fill=rgb(107,65,57),align='center')
    elif app.draggedIndex==4:
        drawRect(app.finalDrinkcx,y-2,w,6,fill='white',align='center')
        
def givingBackOrder_onMouseDrag(app,mouseX,mouseY):
    if app.handingOver:
        app.finalDrinkcx=mouseX
        app.finalDrinkcy=mouseY+50
        
def givingBackOrder_onMouseRelease(app,mouseX,mouseY):
    if (mouseX>420 and mouseX<700) and mouseY>200:
        app.finalDrinkcx=500
        app.finalDrinkcy=500
        app.personThanking=True
        app.handingOver=False
    else:
        app.finalDrinkcx=245
        app.finalDrinkcy=500
        
def givingBackOrder_onMousePress(app,mouseX,mouseY):
    if app.personThanking:
        app.costumerLeaving=True
        if not sameAsOrder(app):
            version,milk,ice,size,bonus=app.currentOrder
            new=Beverage(version,milk,ice,size,bonus)
            app.totalProfit-=Beverage.getPrice(new)
        '''
        makeNewOrder(app)
        takingOrder_resetForNewOrder(app)
        setActiveScreen(screen='takingOrder')
        '''
        
def givingBackOrder_onStep(app):
    if app.personThanking:
        if app.pressToContinuecy<app.height/12:
            app.pressToContinuecy+=5
    if app.costumerLeaving:
        app.costumercx+=2
        if app.costumercx<=app.width+130:
            makeNewOrder(app)
            takingOrder_resetForNewOrder(app)
            setActiveScreen(screen='takingOrder')
            
def drawIceInCup3(app,height):
    for i in range(len(app.iceInCupSpots)):
        [cx,cy]=app.iceInCupSpots[i]
        drawCircle(cx+app.finalDrinkcx-app.width/2,cy+app.finalDrinkcy-322,10,fill=rgb(181,216,255),borderWidth=3,border=rgb(116,170,232))
        
def sameAsOrder(app):
    if len(app.iceInCupSpots)==0: iceAmound='No'
    elif len(app.iceInCupSpots)==2: iceAmound='Light'
    elif len(app.iceInCupSpots)==4: iceAmound='Normal'
    elif len(app.iceInCupSpots)==6: iceAmound='Extra'
    else:
        return False
    return Beverage(app.currentOrder[0],app.currentOrder[1],app.currentOrder[2],app.currentOrder[3],app.currentOrder[4])==Beverage(app.chosenBev,app.chosenMilk,iceAmound,app.chosenSize,app.chosenTopping)

def main():
    runAppWithScreens(initialScreen='instructions')
    
main()