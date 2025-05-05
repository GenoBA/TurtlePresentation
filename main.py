import turtle
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")
t=turtle.Turtle()

#first slide
t.penup()
t.goto(0, 200)
t.pendown()
t.write("Turtle Presentation", font=("Arial", 45, "bold"), align="center")
t.penup()
t.goto(0, -250)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30,"bold"), align="center")

#turtlelogo
t.penup()
t.goto(0, 0)
t.pendown()
screen.addshape("turtle.gif")
t.shape("turtle.gif")
t.stamp()
t.shape("classic")



#shape1
t.begin_fill()
t.penup()
t.goto(-15,-150)
t.pendown()
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.end_fill()

t.hideturtle()


round = input("Press Enter to Continue: ")
screen.bgcolor("purple")
t.clear()
t.showturtle()

#intro slide
t.penup()
t.goto(0, 300)
t.pendown()
t.write("THE", font=("Arial", 30, "bold"), align="center")

#picture of me
t.penup()
t.goto(-150, 50)
t.pendown()
screen.addshape("me.gif")
t.shape("me.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(-150, -140)
t.pendown()
t.write("This Is Me", font=("Arial", 20,"bold italic"), align="center")

t.penup()
t.goto(0, 250)
t.pendown()
t.write("INTRO", font=("Arial", 30, "bold"), align="center")
#my dogs
t.penup()
t.goto(150, 50)
t.pendown()
screen.addshape("dogsleep.gif")
t.shape("dogsleep.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(150, -140)
t.pendown()
t.write("Teddy and Kola", font=("Arial", 20,"bold italic"), align="center")



#shape2
t.penup()
t.goto(-50,-200)
t.begin_fill()
t.pendown()
t.goto(50,-200)
t.goto(0,-100)
t.goto(-50,-200)
t.end_fill()


t.penup()
t.goto(0, -250)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30,"bold"), align="center")
t.hideturtle()

round = input("Press Enter to Continue: ")
screen.bgcolor("blue")
t.clear()
t.showturtle()

#favorite foods slides
t.penup()
t.goto(0, 300)
t.pendown()
t.pencolor("white")
t.write("Favorite Foods", font=("Arial", 30, "bold"), align="center")

#carrot
t.penup()
t.goto(150, 50)
t.pendown()
screen.addshape("carrot.gif")
t.shape("carrot.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(150, -60)
t.pendown()
t.write("Carrot", font=("Arial", 20, "bold italic"), align="center")

#pizza
t.penup()
t.goto(-150, 50)
t.pendown()
screen.addshape("pizza.gif")
t.shape("pizza.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(-165, -115)
t.pendown()
t.write("Pizza", font=("Arial", 20, "bold italic"), align="center")

#steak
t.penup()
t.goto(0, -50)
t.pendown()
screen.addshape("steak.gif")
t.shape("steak.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0, -130)
t.pendown()
t.write("Steak", font=("Arial", 20, "bold italic"), align="center")


#shape3
t.penup()
t.goto(0,-200)
t.pendown()
t.begin_fill()
t.circle(35)
t.end_fill()


t.penup()
t.goto(0, -250)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30,"bold"), align="center")
t.hideturtle()
round = input("Press Enter to Continue: ")
screen.bgcolor("red")
t.clear()
t.showturtle()
#hobbies slide
t.penup()
t.goto(0, 300)
t.pendown()
t.pencolor("white")
t.write("Hobbies", font=("Arial", 30, "bold"), align="center")

#teddyangry
t.penup()
t.goto(-150, 50)
t.pendown()
screen.addshape("maddog.gif")
t.shape("maddog.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(-150, -115)
t.pendown()
t.write("Making My Dog Mad", font=("Arial", 20, "bold italic"), align="center")

#sleeping
t.penup()
t.goto(150, 50)
t.pendown()
screen.addshape("sleeping.gif")
t.shape("sleeping.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(150, -45)
t.pendown()
t.write("Sleeping", font=("Arial", 20, "bold italic"), align="center")

t.penup()
t.goto(150, 175)
t.pendown()
t.write("Drawing", font=("Arial", 20, "bold italic"), align="center")

t.penup()
t.goto(100, -90)
t.pendown()
t.write("Coding", font=("Arial", 20, "bold italic"), align="center")

#shape4
t.penup()
t.goto(-10,-200)
t.begin_fill()
t.pendown()
t.goto(10,-200)
t.goto(20,-180)
t.goto(10,-160)
t.goto(-10,-160)
t.goto(-20,-180)
t.goto(-10,-200)
t.end_fill()




t.penup()
t.goto(0, -250)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30,"bold"), align="center")
t.hideturtle()
round = input("Press Enter to Continue: ")
screen.bgcolor("green")
t.clear()
t.showturtle()


#favoritemovie
t.penup()
t.goto(0, 300)
t.pendown()
t.pencolor("white")
t.write("My Favorite Movie", font=("Arial", 30, "bold"), align="center")

#starwarsposter
t.penup()
t.goto(-150, 50)
t.pendown()
screen.addshape("poster1.gif")
t.shape("poster1.gif")
t.stamp()
t.shape("classic")


t.penup()
t.goto(-150, -115)
t.pendown()
t.write("Starwars", font=("Arial", 20, "bold italic"), align="center")

t.penup()
t.goto(-150, -145)
t.pendown()
t.write("The Empire Strikes Back", font=("Arial", 20, "bold italic"), align="center")

#starwars intro
t.penup()
t.goto(150, 50)
t.pendown()
screen.addshape("introstarwar.gif")
t.shape("introstarwar.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(150, -95)
t.pendown()
t.write("Movie Intro", font=("Arial", 20, "bold italic"), align="center")

t.penup()
t.goto(0,-275)
t.begin_fill()
t.pendown()
t.goto(25,-300)
t.goto(0,-325)
t.goto(-25,-300)
t.goto(0,-275)
t.end_fill()


t.penup()
t.goto(0, -250)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30,"bold"), align="center")
t.hideturtle()
round = input("Press Enter to Continue: ")
screen.bgcolor("yellow")
t.clear()
t.showturtle()


#favoritesport
t.penup()
t.goto(0, 300)
t.pendown()
t.pencolor("black")
t.write("My Favorite Sport", font=("Arial", 30, "bold"), align="center")

#puck
t.penup()
t.goto(-150, 50)
t.pendown()
screen.addshape("puck.gif")
t.shape("puck.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0, -115)
t.pendown()
t.write("Hockey", font=("Arial", 20, "bold italic"), align="center")

#hockeystick
t.penup()
t.goto(150, 50)
t.pendown()
screen.addshape("hockeystick.gif")
t.shape("hockeystick.gif")
t.stamp()
t.shape("classic")
#shape5
t.penup()
t.goto(-100,-200)
t.pendown()
t.begin_fill()
t.goto(100,-200)
t.goto(100,-150)
t.goto(-100,-150)
t.goto(-100,-200)
t.end_fill()

t.penup()
t.goto(0, -250)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30,"bold"), align="center")
t.hideturtle()
round = input("Press Enter to Continue: ")
screen.bgcolor("black")
t.clear()
t.showturtle()
t.pencolor("white")
t.penup()
t.goto(0, 200)
t.pendown()
t.write("THE END", font=("Arial", 45, "bold"), align="center")
t.penup()
t.goto(0, -250)
t.pendown()

#dog2
t.penup()
t.goto(0, 0)
t.pendown()
screen.addshape("dog2.gif")
t.shape("dog2.gif")
t.stamp()
t.shape("classic")
#shape7
t.penup()
t.goto(0,-250)
t.pendown()
t.pencolor("white")
t.begin_fill()
t.goto(100,-200)
t.goto(0,-150)
t.goto(-100,-200)
t.goto(0,-250)
t.end_fill()

turtle.done()