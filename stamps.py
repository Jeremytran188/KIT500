"""
3.4CR Stamp Function

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window.
"""

__author__ = "Ngoc Kien Tran"

from turtle import Turtle


def place_stamp(stamper: Turtle, x: float, y: float, ink: str) -> None:
    """
    Draw the author's initials in the given colour, with the bottom-left
    corner of the drawing placed at (x, y).
    """
    old_ink: str = stamper.pencolor()
    old_direction: float = stamper.heading()
    old_x: float = stamper.xcor()
    old_y: float = stamper.ycor()

    stamper.pencolor(ink)

    stamper.penup()
    stamper.goto(x, y)
    stamper.pendown()

    # Draw N
    stamper.left(90)
    stamper.forward(100)
    stamper.right(150)
    stamper.forward(115)
    stamper.left(150)
    stamper.forward(100)

    # Move to start position for K
    stamper.penup()
    stamper.right(90)
    stamper.forward(50)
    stamper.right(90)
    stamper.forward(100)
    stamper.pendown()

    # Draw K
    stamper.left(180)
    stamper.forward(100)
    stamper.backward(50)
    stamper.right(45)
    stamper.forward(70)
    stamper.backward(70)
    stamper.right(90)
    stamper.forward(70)

    stamper.penup()
    stamper.goto(old_x, old_y)
    stamper.pencolor(old_ink)
    stamper.setheading(old_direction)


def main() -> None:
    t = Turtle()

    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    t.speed(5)

    place_stamp(t, -200, 0, "blue")
    place_stamp(t, 0, 0, "red")
    place_stamp(t, 150, 100, "green")

    # Avoid closing the window automatically
    t.screen.mainloop()


if __name__ == "__main__":
    main()