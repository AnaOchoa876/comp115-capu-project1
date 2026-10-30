# Oliver the Cat Art with Python Turtle

## Project Description

For my COMP 115 project, I decided to draw my cat, Oliver, using Python's Turtle graphics library. My goal was to draw Oliver using simple geometric shapes and then add a colorful background.

<img width="490" height="317" alt="image" src="https://github.com/user-attachments/assets/02fecd58-7e96-4711-9f52-50551aef90c9" />

*My beautiful cat.*



I used circles, triangles, and straight lines to create his head, ears, eyes, nose, and whiskers. I also added a rainbow behind him using the rainbow drawing exercise from Lab 2.


<img width="1357" height="687" alt="image" src="https://github.com/user-attachments/assets/3e71deec-083f-4adc-9295-09da799a2788" />


*My final drawing of Oliver with a rainbow in the background.*

## How the Program Works

### 1. Setting Up the Drawing

I started by creating a Turtle graphics window with a light blue background and a size of 900 × 700 pixels.

I then created two separate turtles:

- **`t`** is responsible for drawing Oliver.
- **`alex`** is responsible for drawing the rainbow.

Using two turtles allowed me to draw the rainbow separately without interfering with the turtle I was using for Oliver.

### 2. Drawing the Rainbow

For the rainbow, I adapted the code from our COMP 115 Lab 2 exercise.

I created a list containing seven rainbow colors:

`["violet", "indigo", "blue", "green", "yellow", "orange", "red"]`

Instead of drawing each color individually, I used a `for` loop to go through the list.

The rainbow starts with a radius of 120, and each time the loop runs, the radius increases by 15. This makes each new semicircle larger than the previous one.

I also adjusted the starting position to `(-radius, -100)` so the rainbow would appear behind Oliver.

### 3. Creating Functions

I created two functions to make my code easier to write and organize.

**`move(x, y)`**

This function moves the turtle to a specific coordinate without drawing a line. It uses `penup()` before moving and `pendown()` afterward.I used this function throughout the project because I needed to move the turtle between different parts of Oliver's face without connecting them with unwanted lines.

**`circle(x, y, r, color)`**

This function draws a filled circle using a center position, radius, and color.

Instead of writing the same instructions every time I needed a circle, I could simply call this function with different values. For example, I used a radius of 80 for Oliver's head and a radius of 7 for his eyes.

### 4. Drawing Oliver

To draw Oliver, I combined several simple shapes using Turtle commands.

**Shoulders:** I used a semicircle with a radius of 100 to create a rounded shape below his head.

**Ears:** I drew two triangles using `goto()` to connect three different coordinates for each ear. The left and right ears are positioned on opposite sides of his head.

**Head:** I used my `circle()` function to draw a large white circle centered at `(0, 0)`.

**Eyes:** I drew two small black circles at `(-30, 10)` and `(30, 10)` to make them symmetrical.

**Nose:** I used three coordinates to create a small pink triangle in the middle of his face.

**Whiskers:** Instead of writing separate instructions for every whisker, I used a `for` loop with the Y-coordinates `[-30, -40, -50]`. This allowed me to draw three whiskers on each side of Oliver's face.

Finally, I used `t.write()` to add his name below the drawing.

## AI Assistance

I used ChatGPT as a learning tool while working on this project. It helped me understand how Turtle coordinates work and visualize where different points should be placed to create Oliver's features, especially his ears. However, I still had to experiment with different coordinates and make several adjustments myself to achieve the precise positioning I wanted.


## How to Run

1. Download the Python file from this repository.
2. Open the file in a Python IDE that supports Turtle graphics.
3. Run the program: project_1.py
4. A Turtle graphics window will open and display Oliver with the rainbow behind him.
5. Click anywhere in the window to close the program.

## Author

Ana Sofía Ochoa Quintero  
COMP 115 — Capilano University  
Fall 2026
