from graphics import *

windowWidth = 512
windowLength = 512

# Draw control points
def drawPoints(ptSet, color, window):
    for i in range(len(ptSet)):
        ptSet[i].setOutline(color)
        ptSet[i].draw(window)

## Draw lines from the points set
def drawLines(ptSet, color, window, width):
    for i in range(len(ptSet)):
        if i < len(ptSet) - 1:
            pt1 = ptSet[i]
            pt2 = ptSet[i + 1]
            ln = Line(pt1, pt2)
            ln.setOutline(color)
            ln.setWidth(width)
            ln.draw(window)

# Draw closed lines from the points set
def drawClosedLines(ptSet, color, window, width):
    # Draw lines from the first to the last control points
    drawLines(ptSet, color, window, width)
    
    # Close the line
    firstPt = ptSet[0]
    lastPt = ptSet[len(ptSet) - 1]
    lastLn = Line(lastPt, firstPt)
    lastLn.setOutline(color)
    lastLn.setWidth(width)
    lastLn.draw(window)

# Draw a white rectangle to clear the previous result
def clearWindow(window):
    windowClearer = Rectangle(Point(0, 0), Point(512, 512))
    windowClearer.setOutline(color_rgb(255, 255, 255))
    windowClearer.setFill(color_rgb(255, 255, 255))
    windowClearer.draw(window)

# Subdivision of four point scheme
def subdivideFourPointScheme(ptList):
    newPtList = [Point(0, 0) for i in range(len(ptList) * 2)]

    # Calculate new control points
    for j in range(len(ptList)):
        newPtList[2 * j].x = ptList[j].x
        newPtList[2 * j].y = ptList[j].y

        if j == 0:
            newPtList[2 * j + 1].x = -0.0625 * ptList[len(ptList) - 1].x + 0.5625 * ptList[j].x + 0.5625 * ptList[j + 1].x - 0.0625 * ptList[j + 2].x
            newPtList[2 * j + 1].y = -0.0625 * ptList[len(ptList) - 1].y + 0.5625 * ptList[j].y + 0.5625 * ptList[j + 1].y - 0.0625 * ptList[j + 2].y
        elif j == len(ptList) - 2:
            newPtList[2 * j + 1].x = -0.0625 * ptList[j - 1].x + 0.5625 * ptList[j].x + 0.5625 * ptList[j + 1].x - 0.0625 * ptList[0].x
            newPtList[2 * j + 1].y = -0.0625 * ptList[j - 1].y + 0.5625 * ptList[j].y + 0.5625 * ptList[j + 1].y - 0.0625 * ptList[0].y
        elif j == len(ptList) - 1:
            newPtList[2 * j + 1].x = -0.0625 * ptList[j - 1].x + 0.5625 * ptList[j].x + 0.5625 * ptList[0].x - 0.0625 * ptList[1].x
            newPtList[2 * j + 1].y = -0.0625 * ptList[j - 1].y + 0.5625 * ptList[j].y + 0.5625 * ptList[0].y - 0.0625 * ptList[1].y
        else:
            newPtList[2 * j + 1].x = -0.0625 * ptList[j - 1].x + 0.5625 * ptList[j].x + 0.5625 * ptList[j + 1].x - 0.0625 * ptList[j + 2].x
            newPtList[2 * j + 1].y = -0.0625 * ptList[j - 1].y + 0.5625 * ptList[j].y + 0.5625 * ptList[j + 1].y - 0.0625 * ptList[j + 2].y

    return newPtList

def main():
    win = GraphWin('Interactive Test', windowWidth, windowLength)
    win.setBackground(color_rgb(255, 255, 255))

    controlPtList = []
    
    keyIsPressed = False

    while True:
        # Mouse detection
        if keyIsPressed == False:
            mouseCoord = win.getMouse()
            controlPt = Point(mouseCoord.x, mouseCoord.y)
            controlPt.setOutline(color_rgb(0, 0, 0))
            controlPt.draw(win)
            controlPtList.append(controlPt)
        
        # Pressed key detection
        keyPressed = win.checkKey()
        if keyPressed:
            keyIsPressed = True

            # Clear the window
            clearWindow(win)

            if keyPressed == 'return' or keyPressed == 'space':
                newControlPtList = controlPtList
                
                # Draw close lines
                drawClosedLines(controlPtList, color_rgb(200, 200, 200), win, 1)

            # If UP is pressed, subdivide the curve
            if keyPressed == 'Up':
                newControlPtList = subdivideFourPointScheme(newControlPtList)
                
                drawPoints(newControlPtList, color_rgb(0, 0, 0), win)
                drawClosedLines(newControlPtList, color_rgb(200, 200, 200), win, 1)


main()
