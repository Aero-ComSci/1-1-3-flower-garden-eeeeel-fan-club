Flower Drawing Turtle Program
Overview
This Python program uses the turtle graphics module to draw various types of flowers based on user input. The user can specify the type of flower, the number of flowers, and the background color. The program will interpret the user's input and draw the flowers accordingly.

Features
Flower Types: The program supports drawing five types of flowers:
Sunflower
Rose
Daisy
Tulip
Lily
Background Colors: The user can choose from the following background colors:
Blue
Green
Yellow
White
Black
Random Flower Placement: Each flower is placed at a random location on the canvas.
How It Works
User Input: The user describes the flowers they want by mentioning the flower type, the number of flowers, and the background color.
Input Parsing: The program analyzes the input to determine the flower type, the number of flowers, and the background color.
Flower Drawing: Based on the parsed input, the program randomly positions and draws the specified number of flowers on the turtle canvas with the chosen background color.
Turtle Graphics: The program uses the turtle graphics module to draw the flowers, which stay on the screen until the user closes the window.
Example Input
The program expects input in natural language, for example:

css
Copy code
Draw 3 sunflowers with a blue background.
Requirements
Python 3.x
Turtle graphics module (comes pre-installed with Python)
How to Run
Install Python on your system if not already installed.

Copy the code to a Python file (e.g., flower_drawing.py).

Run the program by executing the following command in the terminal:

Copy code
python flower_drawing.py
When prompted, enter a description of the flowers you'd like to see. The program will draw them on the canvas.

Customization
You can modify the flowers or background colors by adding or editing entries in the flower_draw_functions dictionary or the background_colors list.
The program uses simple turtle drawing techniques, so adding more flower types or styles is straightforward.
Notes
The turtle.done() function ensures the window remains open until you manually close it.
The program will only draw recognized flower types; if the input is not valid, it will return an error message.
Enjoy creating beautiful flowers!
