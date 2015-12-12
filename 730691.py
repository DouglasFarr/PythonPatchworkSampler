#-------------------------------------------------------------------------------
# Python Coursework: A Patchwork Sampler 
# 730691
#-------------------------------------------------------------------------------
from graphics import *

def main():
    size, colourOrder = getInputs()
    win = drawPatchWork(size, colourOrder)
    changePatchColour(win, size, colourOrder)
     
     
def getInputs():
    size = 999
    while size != "5" and size != "7" and size != "9":
        size = (input("Please enter a size (5,7 or 9):"))
    size = int(size)
    
    validColour = ["red", "green", "blue", "magenta", "yellow", "cyan"]
    colourOrder = []
    for i in range(4):
        print("Valid colours: {0} Remaining:[{1}]".format(validColour, (4-i)))
        colour = "Not Vaild"
        while not colour in validColour:
            colour = (input("Please enter a valid colour :"))
        colourOrder.append(colour)
    return size, colourOrder
 
 
def drawPatchWork(size, colourOrder):
    lstColour = colourOrder*21
    rowOrder = createList("F", size, "P")
    lstArrangement = createList(["F"]*size, size, rowOrder)
    size = size*100
    win = GraphWin("Python Coursework: A Patchwork Sampler ", size,size)
    win.setBackground("white")
    j=0
    colour = 0
    for y in range(0, size,100):
        i=0
        lstRow = lstArrangement[j]
        for x in range(0, size,100):
            if lstRow[i] == "F":
                drawPatchHi(win, x, y, lstColour[colour]) 
            else:
                drawPatchChevron(win, x, y, lstColour[colour])
            i = i+1
            colour = colour+1
        j=j+1
    return win


def createList(edges, size, appendValue):
    list = [edges]
    for i in range(size-2):
        list.append(appendValue) 
    list.append(edges)
    return list


def drawPatchHi(win, posX, posY, colour):
    for x in range(0+posX,100+posX,20):
        verticalLine = Line(Point(x,posY), Point(x,posY+100))
        drawShape(win, verticalLine, colour)
        for y in range(0+posY,100+posY,20): 
            horizontalLine =  Line(Point(posX,y),Point(posX+100,y))
            drawShape(win, horizontalLine, colour)
            textHi = Text(Point(x+10,y+10), "hi!")
            drawShape(win, textHi, colour)  
        

def drawPatchChevron(win, posX, posY, colour):
    for x in range(0+posX,100+posX,20): 
        for y in range(0+posY,100+posY,20): 
            chevron = Polygon(Point(0+x,20+y),Point(0+x,10+y),Point(10+x,0+y),\
                      Point(20+x,10+y),Point(20+x,20+y), Point(10+x,10+y))
            drawShape(win, chevron, colour)

def drawShape(win, shape, colour):
    shape.setFill(colour)
    shape.setOutline(colour)
    shape.draw(win)

def changePatchColour(win, size, colourOrder):
    maxHi = (size * 100)-100
    lstColourIndex = [0,1,2,3]*21
    while True:
        p1 = win.getMouse()
        rows = (p1.getX()//100)
        colum = (p1.getY()//100) 
        x = rows * 100           
        y = colum * 100
        resetPatch =  Rectangle(Point(x, y), Point(x + 99, y + 99))
        drawShape(win, resetPatch, "white")
        
        position = int((rows * size) + colum)
        newColourIndex = lstColourIndex[position] + 1
        if newColourIndex == 4:
            newColourIndex = 0
        newColour = colourOrder[newColourIndex]
       
        if x ==0 or y ==0 or x==maxHi or y==maxHi :
            drawPatchHi(win, x, y, newColour)
        else:
            drawPatchChevron(win, x, y, newColour)
    
        lstColourIndex[position] = newColourIndex
main()