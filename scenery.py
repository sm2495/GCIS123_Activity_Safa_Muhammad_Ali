"""
This program was designed to fulfill the requirements of Activity 1 of the GCIS 123 class. As instructed the program will prompt the
user for information on how he/she wants to design his/her cake. With the information that the user gave the program will then draw
a table, a cake, a candle and some decorations.
"""
"""
Here our github repositories:
Julian Pascher: https://github.com/jp8697/GCIS123_Scenery.py
Mutete Kimweli: https://github.com/mutete-k/lab1-gcis123
Safa Muhammad Ali : https://github.com/sm2495/GCIS123_Activity_Safa_Muhammad_Ali
"""
import turtle


"""
The first 4 functions in our program ask for the users input. These functions are very important to the program as the rest of the 
program would not work without the users input. They return the users input to the main function when they are called upon, where 
the input is then tranfered to the parameters of the diffrent function that require the users input
"""
def get_table_specifications():
    t_color=input("Enter color of table: ")
    t_length=int(input("Enter length of table: "))
    t_height=int(input("Enter height of table: "))
    tabletop_thickness=int(input("Enter thickness of table top: "))
    t_width=int(input("Enter width of table top: "))
    leg_thickness=int(input("Enter thickness of legs: "))
    return t_color, t_length, t_height, tabletop_thickness, t_width, leg_thickness

def get_cake_specifications():
    width = int(input("Enter the fixed width for all layers: "))
    h1 = int(input("Enter the height for layer 1: "))
    c1 = input("Enter the color for layer 1: ")
    h2 = int(input("Enter the height for layer 2: "))
    c2 = input("Enter the color for layer 2: ")
    h3 = int(input("Enter the height for layer 3: "))
    c3 = input("Enter the color for layer 3: ")
    h4 = int(input("Enter the height for layer 4: "))
    c4 = input("Enter the color for layer 4: ")
    h5 = int(input("Enter the height for layer 5: "))
    c5 = input("Enter the color for layer 5: ")
    return width, h1, c1, h2, c2, h3, c3, h4, c4, h5, c5



def get_candle_spec():
    c_width = int(input("width of candle: "))
    c_height = int(input("height of candle: "))
    c_color = input("color of the candle: ")
    f_color = input("color of the flame: ")
    f_length = int(input("enter size of flame [max 7]: "))
    return c_height, c_color, c_width, f_color, f_length

def get_ball_specs():
    ball_1_color = input("ball color 1: ")
    ball_1_size = int(input("ball 1 size: "))
    ball_2_color = input("ball color 2")
    ball_2_size = int(input("ball 2 size: "))
    return ball_1_color, ball_1_size, ball_2_color, ball_2_size


"""
This function is defined to draw the legs of the table. With the help of the user information the proportions of the table legs are
determined. When called upon in the main function it will draw 4 legs in 4 diffrent positions. These positons depend on the user input
regarding the proportions of the rest of the table
"""
def legs(color,height,thickness,startpos):
    turtle.penup()
    turtle.goto(startpos,0)
    turtle.right(90)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(thickness)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()
    turtle.right(90)
"""
This function defines the proportions of the tabletop and is therefore dependant on some user input. 
"""
def tabletop(color,length,thickness,width):
    turtle.penup()
    turtle.goto(0,0)
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(thickness)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(thickness)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.end_fill()
    turtle.penup()
    turtle.left(180)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(thickness)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(width)
    turtle.right(45)
    # The value "0.7071067812" = cos (45) and it is necessary to obtain the lenght of the back edge of the table
    turtle.forward(length-(width*0.7071067812*2))
    turtle.right(45)
    turtle.forward(width) 
    turtle.end_fill()
    turtle.penup()
    turtle.right(45)
    turtle.forward(thickness)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.right(180)

"""
This function defines the shape and size of the candle.
"""
def draw_candle(c_height, c_color, c_width, top_y):
    turtle.penup()
    turtle.goto(-c_width / 2, top_y)  
    turtle.pendown()
    turtle.color(c_color)
    turtle.pencolor(c_color)
    turtle.begin_fill()
    turtle.forward(c_width)
    turtle.left(90) 
    turtle.forward(c_height)
    turtle.left(90)
    turtle.forward(c_width)
    turtle.left(90) 
    turtle.forward(c_height)
    turtle.left(90)
    turtle.end_fill()

"""
This function, when called in the main function will draw the flame of the candle on top of the rest of the candle.
"""
def flame(c_height, f_color, f_length, top_y):
    turtle.penup()
    #this line defines the position in the middle of the top of the candle
    turtle.goto(0, top_y + c_height)
    turtle.pendown()
    turtle.color(f_color)
    turtle.begin_fill()
    turtle.circle(f_length)
    turtle.end_fill()

"""
This function will draw the diffrent layers of the cake each layer's color and width depending on the user input 
"""
def draw_layer(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()


"""
This function will draw the table according to the user input
"""
def table(t_color, t_length, t_height, tabletop_thickness, t_width, leg_thickness):
    tabletop(t_color,t_length,tabletop_thickness,t_width)
    leg_offset = t_length / 2 - leg_thickness / 2 
    legs(t_color, t_height, leg_thickness, -leg_offset+leg_thickness/2)  
    legs(t_color, t_height, leg_thickness, leg_offset+leg_thickness/2) 
    legs(t_color, t_height * 0.75, leg_thickness, -leg_offset + t_width) 
    legs(t_color, t_height*0.75, leg_thickness, leg_offset - t_width+leg_thickness)


"""
This function defines the size and color of our decoration 
"""
def draw_balls(ball_1_color, ball_1_size, ball_2_color, ball_2_size, top_y, width):
    x_b1 = (width)//4 
    y_b1 = top_y
    x_b2 = (-width)//4
    y_b2 = top_y
    turtle.penup()
    turtle.goto(x_b1, y_b1)
    turtle.pendown()
    turtle.color(ball_1_color)
    turtle.pencolor(ball_1_color)
    turtle.begin_fill()
    turtle.circle(ball_1_size)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x_b2, y_b2)
    turtle.pendown()
    turtle.color(ball_2_color)
    turtle.pencolor(ball_2_color)
    turtle.begin_fill()
    turtle.circle(ball_2_size)
    turtle.end_fill()


def main():
    #These next 4 lines get the user input into the main function so that we can assign them to the parameters of the other functions
    t_color,t_length, t_height, tabletop_thickness, t_width, leg_thickness = get_table_specifications()
    width, h1, c1, h2, c2, h3, c3, h4, c4, h5, c5 = get_cake_specifications()
    c_height, c_color, c_width, f_color, f_length = get_candle_spec()
    ball_1_color, ball_1_size, ball_2_color, ball_2_size = get_ball_specs()

    #These lines of code define the scene on which the cake is drawn
    turtle.bgcolor("lightblue")
    turtle.title("Customizable Cake")
    turtle.speed(2)

    #First we call the table function to draw the table according to the users input
    table(t_color, t_length, t_height, tabletop_thickness, t_width, leg_thickness)
    
    #Then position the t in the middle of the table so that we can start drawing the layers
    x, y = 0 - width/2, 0 + tabletop_thickness
    
    turtle.speed(2)

    # Draw each cake layer individually
    x, y = 0 - width / 2, 0 + tabletop_thickness
    draw_layer(x, y, width, h1, c1)
    y += h1
    draw_layer(x, y, width, h2, c2)
    y += h2
    draw_layer(x, y, width, h3, c3)
    y += h3
    draw_layer(x, y, width, h4, c4)
    y += h4
    draw_layer(x, y, width, h5, c5)
    y += h5
    
    #Next we adjust the position of the turtle again so that it is on top of the cake, situated in the middle so that we can start drawing the candle
    turtle.penup()
    top_y = y 
    turtle.goto(0, top_y)  
    turtle.setheading(0)
    turtle.pendown()

    #We then proceed by drawing the candle and the flame according to the user input
    draw_candle(c_height, c_color, c_width, top_y)
    flame(c_height, f_color, f_length, top_y)

    #Finally we finish by drawing the ball decoration
    draw_balls(ball_1_color, ball_1_size, ball_2_color, ball_2_size, top_y, width)

    #And then we return to the starting point
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    print("Exit by clicking on the icon ")
    turtle.exitonclick()

main()



