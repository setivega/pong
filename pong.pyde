ballY = 350
ballX = 500

ySpeed = 5
xSpeed = 5

paddle1 = 400
paddle2 = 400

score1 = 0
score2 = 0

def createGame():

    #Pong Paddles
    rect(20, paddle1, 30, 150)
    rect(950, paddle2, 30, 150)
    
    y=20
    while y<height:
        strokeWeight(1)
        fill(255,255,255)
        rect((width/2 - 8), y, 16, 16)
        y += 50

    stroke(255, 255, 255)
    
    strokeWeight(20)
    
    fill(0,0,0)
        
    # rect(262, 30, 80, 100)
        
    # rect(382, 30, 80, 100)
    
    # rect(562, 30, 80, 100)
    
    # rect(682, 30, 80, 100)
    
    fill(255,255,255)
    textSize(22)
    text("Score: "+ str(score1), 10,30 )
    text("Score: "+ str(score2), 900,30)
    
    noStroke()
    fill(255,255,255)


def setup():
    
    size(1000,800)
    background(0,0,0)
    createGame()
    

def draw():
    global ballY
    global ballX
    global ySpeed
    global xSpeed
    global paddle1
    global paddle2
    global score1
    global score2
    

    background(0,0,0)
    createGame()
    rect(ballX, ballY, 30, 30)
    # print("ballX: " + str(ballX))
    # print("ballY: " + str(ballY))
    
    #Top and Bottom border
    if ballY > 770:
        ySpeed = -5
    elif ballY < 0:
        ySpeed = 5
    
    #THIS WHERE THE BALL HITS THE PADDLE
    if ballX > 920 and ballX < 950 and ballY > paddle2-30 and ballY < paddle2 + 150:
        xSpeed = -5
    elif ballX < 50 and ballX > 20 and ballY > paddle1-30 and ballY < paddle1 + 150:
        xSpeed = 5
    
    #Score Counter
    if ballX > 2000 or ballX < -1000:
        if ballX>2000:
            score1 += 1
            print(score1)
        elif ballX<-1000:
            score2 += 1
            print(score2)
        ballY = 350
        ballX = 500
        rect(ballX, ballY, 30, 30)
    
    ballY += ySpeed
    ballX += xSpeed
    
    if keyPressed:
        if key == CODED:
            if keyCode == UP:
                if paddle2 > 0:
                    paddle2 -= 8
                else:
                    paddle2 -= 0
                # print(paddle2)
            elif keyCode == DOWN:
                if paddle2 < 650:
                    paddle2 += 8
                else:
                    paddle2 += 0
                # print(paddle2)
                
    if keyPressed:
        if key == 'w' or key == 'W':
            if paddle1 > 0:
                paddle1 -= 8
            else:
                paddle1 -= 0
            # print(paddle1)
        elif key == 's' or key == 'S':
            if paddle1 < 650:
                paddle1 += 8
            else:
                paddle1 += 0
            # print(paddle1)

# def keyPressed():
#     global paddle1
#     global paddle2
#     if key == CODED:
#         if keyCode == UP:
#             paddle2 -= 5
#             print(paddle2)
#         elif keyCode == DOWN:
#             paddle2 += 5
#             print(paddle2)
#     elif key == 'w' or key == 'W':
#         paddle1 -= 5
#         print(paddle1)
#     elif key == 's' or key == 'S':
#         paddle1 += 5
#         print(paddle1)
    



#Numbers/Score Board



#Seperator of sides
