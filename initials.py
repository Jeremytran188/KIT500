"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.
Some of the code below has been _over_ commented to help
you understand what is happening.
"""

__author__ = "Ngoc Kien Tran"

import turtle as painter


def main():
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    painter.speed(3)

    # Draw your initials below, remembering to use painter.penup() to
    # move without drawing a line...
    
    # Draw N
    painter.left(90)
    painter.forward(100)
    painter.right(150)
    painter.forward(115)
    painter.left(150)
    painter.forward(100)

    # Move to start position for K
    painter.penup()
    painter.right(90)
    painter.forward(50)
    painter.right(90)
    painter.forward(100)
    painter.pendown()

    # Draw K
    painter.left(180)
    painter.forward(100)
    painter.backward(50)
    painter.right(45)
    painter.forward(70)
    painter.backward(70)
    painter.right(90)
    painter.forward(70)
    # Hide the turtle cursor 
    painter.hideturtle()


    # Avoid closing the window automatically
    painter.mainloop()


if __name__ == "__main__":
    main()
