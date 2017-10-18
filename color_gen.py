def getAllSteps(positions):
    stepAmount = 255/(positions-1)
    return(stepAmount)

def createSlots(number,color):
    if len(color)== 0:
        for i in range(number):
           color.append(i)
    else:
        clearUnused()
        print('Please Run Again. I"m a shit programmer')

def populateSlots(number,color,width):
    for i in range(number):
      color[i] = round(i*width)

def clearUnused():
    global red
    global green
    global blue
    red=[]
    green=[]
    blue=[]

    
## Empty Arrays - Cause I'm a shit programmer        

red=[]
green=[]
blue=[]

createSlots(4,red)

  

