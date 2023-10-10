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
- [^1^]: Python Turtle Graphics Documentation, https://docs.python.org/3/library/turtle.html



## **_Question 3:_**
- Answer 1
- Answer 2
- Answer 3

## **_Question 4:_**
- Answer 1
- Answer 2
- Answer 3

## **_Question 5:_**
- Answer 1
- Answer 2
- Answer 3

## **_Question 6:_**
- Answer 1
- Answer 2
- Answer 3

## **_Question 7:_**
- Answer 1
- Answer 2
- Answer 3
