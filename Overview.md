# Exploring Python's Turtle graphics library

## **_Question 1_: Which package/library did you select?**
- I chose to use the **Turtle Graphics Library** in python for the exploration activity.

## **_Question 2:_ What is the package/library?**
- _What purpose does it serve?_ : The Turtle graphics library in Python serves multiple valuable purposes. Primarily, it acts as an **educational tool**, providing an interactive and visually engaging way to teach programming concepts, especially to beginners. It is also a practical choice for **creating graphics, art, and simple animations**, making it accessible to programmers of all skill levels. Finally, it encourages **creative exploration and experimentation**, allowing programmers to invent their own drawing algorithms and artistic creations.

- _How do you use it?_ : You need to import the turtle module, create a turtle object, then give it commands to draw. This is demonstrated here:
 ### 1.Basic Setup 
To actually use Turtle graphics, you'll need to import the `turtle` module like so:
```python
import turtle
```

### 2.Creating a turtle
Now, to create a turtle object, you must use the 'Turtle' class:
```python
my_turtle = turtle.Turtle()
```
You can now customize the turtle's shape and/or speed using methods from the turtle class:
```python
my_turtle.shape('turtle')  # Set the turtle's shape to a turtle icon
my_turtle.speed(3)         # Set the turtle's drawing speed (1 is slowest, 10 is fastest)
```

### 3. Making the turtle draw using commands
To see the shapes you want to draw, you have to give the turtle commands to move and draw while the pen is down. Here are some examples of basic drawing commands:
```python
my_turtle.forward(100)  # Move the turtle 100 units
my_turtle.left(90)      # 90 in degrees
my_turtle.circle(50)    # Radius of circle is 50
```

### 4. Using conditionals & Loops to control the actions of the turtle.
An example of drawing a square using a for loop:
```python
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)
```

### 5. Pen Control
You can use the functions penup() and pendown() to lift the pen  so it doesn't draw while the turtle is moving or lower the pen to start drawing again:
```python
my_turtle.penup()  # Lift the pen
# Get the turtle to the position you need to start drawing again here
my_turtle.pendown()  # Lower the pen
```

### 6. Advanced Features in the turtle library
The Turtle graphics library offers advanced features, as shown in the documentation [^1^].
 Some of these features include:
- Filling Shapes: You can fill shapes with colors using methods like begin_fill() and end_fill().
- Multiple Turtles: You can work with multiple turtles on the same canvas.
[^1^]: Python Turtle Graphics Documentation, https://docs.python.org/3/library/turtle.html



## **_Question 3:_ What are the functionalities of the package/library?**
The library has multiple functionalities and features such as:
- Drawing using commands Example:
```python
import turtle

my_turtle = turtle.Turtle()

# Drawing a star
for _ in range(5):
    my_turtle.forward(100)
    my_turtle.right(144)

turtle.done()
```

- Pen Control:
```python
import turtle

my_turtle = turtle.Turtle()

# Lift the pen
my_turtle.penup()
my_turtle.goto(-50, -50)
my_turtle.pendown()

# Drawing a spiral
for i in range(36):
    my_turtle.forward(i * 10)
    my_turtle.right(90)

turtle.done()
```
- Setting the color of the drawing:
```python
import turtle

my_turtle = turtle.Turtle()

# Set drawing color
my_turtle.color('blue')

# Drawing a circle in blue
my_turtle.circle(50)

turtle.done()
```
- Turning the turtle at certain angles:
```python
import turtle

my_turtle = turtle.Turtle()

# Turning the turtle at 45 degrees
my_turtle.forward(100)
my_turtle.left(45)
my_turtle.forward(100)

turtle.done()
```


## **_Question 4:_ When was it created?**
- It was created in 1967 as an implementation of the popular geometric drawing tools introduced in Logo.

## **_Question 5:_ Why did you select this package/library**
- I chose to use turtle because I wanted to find a way to use graphics in Python instead of the standard input / output of the terminal. I wanted a practical way to view the output of my code line-by-line through the use of visual graphics, and I decided to do that by creating the classing Pong game to test out its functionalities.

## **_Question 6:_ How did learning the package/library influence your learning of the language**
- Learning turtle helped me understand Python better in the following ways: 
- I had to use and practice **Control Flow** through the usage of conditionals and loops.
-I learned **Event Handling** in Python by listening in to certain key presses
-I practiced and reviewed the implementations of **Coordinates & Geometry ** by moving the turtle to specific positions on the screen.
-I was able to see immediate **Visual Feedback** from the code I was writing, and I could see how my code was affecting the output with the smallest changes.

## **_Question 7:_ How was your overall experience with the package/library?**
- _When would you recommend this package/library to someone?_: Turtle is a graphics library, which makes it the most useful when a programmer wants to implement animations or graphics into their code. So I would be recommended it whenever someone wants to draw or animate and see the results on the screen.
- _Would you continue using this package/library? Why or why not?_: Yes I would, Turtle was very easy to work with and grasp the concepts of and I would probably immediately think about it if I has a programming problem where I had to utilize a library or package that required drawing shapes and colors etc...
