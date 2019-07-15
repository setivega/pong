size(1024,1024)

background(0,0,0)

#Pong Paddles
rect(20, 400, 30, 150)
rect(974, 256, 30, 150)

#Ball
rect(400, 600, 30, 30);

#Numbers/Score Board

stroke(255, 255, 255)
strokeWeight(20)

fill(0,0,0)
     
rect(262, 30, 80, 100)
     
rect(382, 30, 80, 100)

rect(562, 30, 80, 100)

rect(682, 30, 80, 100)

#Seperator of sides

strokeWeight(1)
fill(255,255,255)

x=20
while x<height:
    rect(504, x, 16, 16)
    x += 50
    

textSize(30)
text("Seti Vega", 950, 40)
