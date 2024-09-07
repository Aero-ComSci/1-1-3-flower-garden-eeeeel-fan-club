import turtle
import random
import re




# Turtle Setup
def setup_turtle(background_color="white"):
    turtle.reset()
    turtle.speed(0)
    turtle.bgcolor(background_color)
    turtle.hideturtle()




# Flower drawing functions
def draw_flower_petal(size, color):
    turtle.begin_fill()
    turtle.color(color)
    for _ in range(2):
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.circle(size, 60)
        turtle.left(120)
    turtle.end_fill()




def draw_sunflower():
    turtle.color("brown")  # Draw the center
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.color("yellow")
    for _ in range(12):
        draw_flower_petal(40, "yellow")
        turtle.right(30)
    turtle.color("green")
    turtle.right(90)
    turtle.width(5)
    turtle.forward(100)  # Draw stem




def draw_rose():
    turtle.color("green")
    turtle.right(90)
    turtle.width(5)
    turtle.forward(100)  # Draw stem
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.end_fill()
    for _ in range(10):
        turtle.circle(30,33)
        turtle.right(100)


def draw_daisy():
    turtle.color("yellow")  # Draw the center
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.color("white")
    for _ in range(10):
        draw_flower_petal(30, "white")
        turtle.right(36)
    turtle.color("green")
    turtle.right(90)
    turtle.width(5)
    turtle.forward(100)  # Draw stem




def draw_tulip():
    turtle.color("pink")
    turtle.begin_fill()
    turtle.circle(40, 180)
    turtle.left(90)
    turtle.forward(80)
    turtle.end_fill()
    turtle.color("green")
    turtle.right(90)
    turtle.width(5)
    turtle.forward(100)  # Draw stem




def draw_lily():
    turtle.color("white")
    for _ in range(5):
        draw_flower_petal(40, "white")
        turtle.right(72)
    turtle.color("green")
    turtle.right(90)
    turtle.width(5)
    turtle.forward(100)  # Draw stem




# Flower types and their drawing functions
flower_draw_functions = {
    "sunflower": draw_sunflower,
    "rose": draw_rose,
    "daisy": draw_daisy,
    "tulip": draw_tulip,
    "lily": draw_lily
}




# randomly position the flowers on the screen
def place_flower(flower_type, amount):
    for _ in range(amount):
        turtle.penup()
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        turtle.goto(x+30, y+30)
        turtle.pendown()
        flower_draw_functions[flower_type]()




# input parsing function
def parse_user_input(user_input):
    # convert the input to lowercase
    user_input = user_input.lower()




    # identify the background color
    background_colors = ["blue", "green", "yellow", "white", "black"]
    background_color = "white"
    for color in background_colors:
        if color in user_input:
            background_color = color
            break




    # identify the flower type
    flower_type = None
    for flower in flower_draw_functions.keys():
        if flower in user_input:
            flower_type = flower
            break




    # Identify the number of flowers
    match = re.search(r'\d+', user_input)
    amount = int(match.group()) if match else 1




    return flower_type, amount, background_color




# Main program loop
def main():
    user_input = input("Describe the flowers you'd like")




    flower_type, amount, background_color = parse_user_input(user_input)




    if flower_type:
        setup_turtle(background_color)
        place_flower(flower_type, amount)
        turtle.done()  
    else:
        print("Sorry, I don't recognize that flower type.")




if __name__ == "__main__":
    main()
