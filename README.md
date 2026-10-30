# Oliver the Cat Art with Python Turtle

## Project Description

For my COMP 115 project, I decided to draw my cat, Oliver, using Python's Turtle graphics library.

I wanted to create something personal while applying the programming concepts we've learned throughout the semester. My goal was to draw Oliver using simple geometric shapes and then add a colorful background.

I used circles, triangles, and straight lines to create his head, ears, eyes, nose, and whiskers. I also added a rainbow behind him using the rainbow drawing exercise from Lab 2.

## Example Output

![Oliver the Cat](oliver.png)

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

The rainbow starts with a radius of 120, and each time the loop runs, the radius increases by 15. This makes each new semicircle larger than the previous one, creating the rainbow effect.

I also adjusted the starting position to `(-radius, -100)` so the rainbow would appear behind Oliver.

### 3. Creating Functions

I created two functions to make my code easier to write and organize.

**`move(x, y)`**

This function moves the turtle to a specific coordinate without drawing a line. It uses `penup()` before moving and `pendown()` afterward.

I used this function throughout the project because I needed to move the turtle between different parts of Oliver's face without connecting them with unwanted lines.

**`circle(x, y, r, color)`**

This function draws a filled circle using a center position, radius, and color.

Instead of writing the same instructions every time I needed a circle, I could simply call this function with different values.

For example, I used a radius of 80 for Oliver's head and a radius of 7 for his eyes.

### 4. Drawing Oliver

To draw Oliver, I combined several simple shapes using Turtle commands.

**Shoulders:** I used a semicircle with a radius of 100 to create a rounded shape below his head.

**Ears:** I drew two triangles using `goto()` to connect three different coordinates for each ear. The left and right ears are positioned on opposite sides of his head.

**Head:** I used my `circle()` function to draw a large white circle centered at `(0, 0)`.

**Eyes:** I drew two small black circles at `(-30, 10)` and `(30, 10)` to make them symmetrical.

**Nose:** I used three coordinates to create a small pink triangle in the middle of his face.

**Whiskers:** Instead of writing separate instructions for every whisker, I used a `for` loop with the Y-coordinates `[-30, -40, -50]`. This allowed me to draw three whiskers on each side of Oliver's face.

Finally, I used `t.write()` to add his name below the drawing.

## Python Concepts Used

This project helped me practice several concepts from COMP 115:

- **Functions:** Creating reusable instructions with parameters.
- **Lists:** Storing the rainbow colors and whisker positions.
- **For loops:** Repeating drawing instructions without writing the same code multiple times.
- **Variables:** Storing values such as the rainbow radius and radius increase.
- **Accumulator pattern:** Updating the rainbow radius after each iteration.
- **Coordinates:** Using X and Y values to control where shapes appear.
- **Turtle graphics:** Using commands such as `goto()`, `circle()`, `forward()`, `left()`, `penup()`, and `pendown()`.

## Challenges and What I Learned

The most challenging part of this project was figuring out how to position Oliver's features using coordinates.

At first, I found it difficult to understand exactly where the turtle would move when I used `goto(x, y)`. Drawing the ears was particularly challenging because I wanted them to look like they were attached to his head rather than floating above it.

I experimented with different coordinates and eventually changed the bottom Y-coordinates of his ears from 60 to 50. This made the triangles overlap more with the head, creating a more natural appearance.

Another thing I learned was how important the order of drawing is. For example, I drew the ears before the head so the large white circle would cover the lower parts of the triangles. Similarly, I drew the rainbow before Oliver so it would appear in the background.

I also enjoyed seeing how concepts from previous labs could be reused in a different project. The rainbow was originally a separate exercise, but I was able to adapt it to become part of my drawing.

Overall, this project helped me become more comfortable with Turtle graphics, especially working with coordinates, functions, and loops.

## AI Assistance

I used ChatGPT as a learning tool while working on this project.

It helped me understand how Turtle coordinates work and visualize where different points should be placed to create Oliver's features. This was especially useful when I was trying to position his ears.

I also received help combining my Oliver drawing with the rainbow code from Lab 2 and explaining the structure of my program.

I experimented with different coordinates, adjusted parts of the drawing, and used the explanations to better understand how the code worked.

ChatGPT also assisted me with writing and organizing this README.

## How to Run

1. Download the Python file from this repository.
2. Open the file in a Python IDE that supports Turtle graphics, such as IDLE or Thonny.
3. Run the program using Python 3.
4. A Turtle graphics window will open and display Oliver with the rainbow behind him.
5. Click anywhere in the window to close the program.

## Acknowledgments

- COMP 115 — Capilano University
- COMP 115 Lab 2 — Rainbow Drawing Exercise
- ChatGPT (OpenAI) — Assistance with understanding coordinates, combining code, and documenting the project

## Author

Ana Sofía Ochoa Quintero  
COMP 115 — Capilano University  
Fall 2026
