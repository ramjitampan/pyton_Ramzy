import turtle

def move (x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw (heading, lenght):
        turtle.setheading(heading)
        turtle.forward(lenght)

def drwa_outline():
      turtle.fillcolor("gray")
      turtle.begin_fill()
      move(-200, -200)

      draw(90, 150)
      draw(0, 50)
      draw(90, 50)
      draw(0, 50)
      draw(90, 100)
      draw(0, 70)
      draw(270, 120)
      draw(0, 50)
      draw(90, 70)
      draw(0,50)
      draw(270, 50)
      draw(0, 20)
      draw(270, 50)
      draw(0, 50)
      draw(270, 150)
      draw(180, 340)

      turtle.end_fill()

def draw_sky():
      move(-200, -50)
      turtle.fillcolor("black")
      turtle.begin_fill()

      draw(90, 250)
      draw(0, 340)
      draw(270, 250)
      draw(180, 350)

      turtle.end_fill()

def draw_square (size):
      turtle.fillcolor("white")
      turtle.begin_fill()

      draw(0, size)
      draw(270, size)
      draw(180, size)
      draw(90, size)

      turtle.end_fill()

def draw_windows():
     move (-140, -10)
     draw_square(10)

     move (-90, 70)
     draw_square(10)

     move (-90, 85)
     draw_square(10)

     move (-50, 40)
     draw_square(10)

     move (30, 30)
     draw_square(10)

     move (-60, -50)
     draw_square(10)

def draw_stars():
      move (-170, 40)
      draw_square(2)

      move (-120, 30)
      draw_square (2)

      move (-150, 100)
      draw_square (2)

      move (-70, 120)
      draw_square (2)

      move (0, 80)
      draw_square (2)

      move (120, 110)
      draw_square (2)

      move (90, 30)
      draw_square (2)

def draw_stars():
      move (-170, 40)
      draw_square(2)

      move(-120, 30)
      draw_square(2)

      move (-150, 100)
      draw_square(2)

      move (-70, 120)
      draw_square (2)

      move (0, 80)
      draw_square (2)
      
      move (120, 110)
      draw_square (2)

      move (90, 30)
      draw_square (2)

def end():
      move (400, 400)

turtle.setup (400, 400)
turtle.screensize(100, 100)

draw_sky()
drwa_outline()
draw_windows()
draw_stars()
end()

turtle.done