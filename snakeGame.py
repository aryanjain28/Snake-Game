from tkinter import *
import random
import time

points = 0
forward = -1
backward = -1
right = -1
left = -1
y=0
x=0

class GAME:

    def __init__(self):

        global points
        points = -1

        self.size = 30

        self.x1 = 145
        self.x2 = 160
        self.y1 = 150
        self.y2 = 180

        self.canvas = Canvas(mainWindow, height=500, width=500, bg='blue')
        self.canvas.pack()

        self.food = self.canvas.create_rectangle(20, 20, 30, 30, fill='white')
        self.snake = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='red')
        self.tempRectangle = self.canvas.create_rectangle(0,0,0,0,fill='red')

        self.point = Label(mainWindow, text=str(points))
        self.point.pack()

        self.encounter()

    def encounter(self):

        global forward, backward, right, left, x, y

        self.canvas.delete(self.food)

        self.foodX1 = random.randrange(20, 480)
        self.foodX2 = self.foodX1 + 25

        self.foodY1 = random.randrange(20, 480)
        self.foodY2 = self.foodY1 + 25

        self.food = self.canvas.create_rectangle(self.foodX1, self.foodY1, self.foodX2, self.foodY2, fill='white')


        global points
        points+=1
        self.point.destroy()
        self.point = Label(mainWindow, text=str(points))
        self.point.pack()


    def snakeForward(self, event):

        global forward, backward, right, left

        forward = 1
        backward = 0

        self.canvas.delete(self.snake)
        self.canvas.delete(self.tempRectangle)

        if (((self.x1 > self.foodX1 and self.x1 < self.foodX2) and (
                self.y1 > self.foodY1 and self.y1 < self.foodY2)) or
              ((self.x2 > self.foodX1 and self.x2 < self.foodX2) and (
                      self.y2 > self.foodY1 and self.y2 < self.foodY2))):
            self.size += 30
            self.encounter()

        if abs((self.x1 - self.x2))>15:

            if right == 1 or right == -1:
                self.x1 += 10
                self.tempRectangle = self.canvas.create_rectangle(self.x1 + 5, self.y1-10, self.x2, self.y1, fill='red')

            elif left == 1 or left == -1:
                self.x2 -= 10
                self.tempRectangle = self.canvas.create_rectangle(self.x1, self.y1-10, self.x2-15, self.y2-15, fill='red')

            if abs((self.x1 - self.x2)) < 15:
                self.y2 = self.y1 + self.size
                self.x2 = self.x1 + 15

        else:
            self.y1 -= 10
            self.y2 -= 10
            self.x2 = self.x1+15

        self.snake = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='red')


    def snakeBackward(self, event):

        global forward, backward, right, left

        forward = 0
        backward = 1

        self.canvas.delete(self.snake)
        self.canvas.delete(self.tempRectangle)

        if abs((self.x1 - self.x2))>15:

            if right == 1 or right == -1:
                self.tempRectangle = self.canvas.create_rectangle(self.x1 + 15, self.y2, self.x1 + 30, self.y2 +10,fill='red')
                self.x1 += 10

            elif left == 1 or left == -1:
                self.tempRectangle = self.canvas.create_rectangle(self.x1, self.y2, self.x2-15, self.y2+10, fill='red')
                self.x2 -= 10

            if abs((self.x1 - self.x2)) < 15:
                self.y2 = self.y1 + 30
                self.x2 = self.x1 + 15

        else:
            self.y1 += 10
            self.y2 += 10
            self.x2 = self.x1-15

        self.snake = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='red')

    def snakeLeft(self, event):

        global forward, backward, left, right

        left = 1
        right  = 0

        self.canvas.delete(self.snake)
        self.canvas.delete(self.tempRectangle)

        if abs((self.y1 - self.y2)) > 15:

            if forward == 1 or forward == -1:
                self.y2 -= 10
                self.tempRectangle = self.canvas.create_rectangle(self.x1 - 10, self.y1, self.x1, self.y1 + 15,
                                                                  fill='red')

            elif backward == 1 or backward == -1:
                self.y1 += 10
                self.tempRectangle = self.canvas.create_rectangle(self.x2-25, self.y2 - 15, self.x2-15, self.y2,
                                                                  fill='red')

            if abs((self.y1 - self.y2)) < 15:
                self.y2 = self.y1 + 15
                self.x2 = self.x1 + 30

        else:
            self.x1 -= 10
            self.x2 -= 10
            self.y2 = self.y1 + 15

        self.snake = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='red')

        if (((self.x1 > self.foodX1 and self.x1 < self.foodX2) and (self.y2 > self.foodY1 and self.y2 < self.foodY2)) or
        ((self.x1 > self.foodX1 and self.x1 < self.foodX2) and (self.y1 > self.foodY1 and self.y1 < self.foodY2))):
            self.encounter()

    def snakeRight(self, event):

        global forward, backward, right, left

        right = 1
        left = 0

        self.canvas.delete(self.snake)
        self.canvas.delete(self.tempRectangle)

        if abs((self.y1 - self.y2))>15:

            if forward == 1 or forward == -1:
                self.y2 -= 10
                self.tempRectangle = self.canvas.create_rectangle(self.x1 + 15, self.y1, self.x1 + 25, self.y1 + 15, fill='red')

            elif backward == 1 or backward == -1:
                self.y1 += 10
                self.tempRectangle = self.canvas.create_rectangle(self.x2, self.y2-15, self.x2 + 10, self.y2, fill='red')

            if abs((self.y1 - self.y2)) < 15:
                self.y2 = self.y1 + 15
                self.x2 = self.x1 + 30

        else:
            self.x1 += 10
            self.x2 += 10
            self.y2 = self.y1+15

        self.snake = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='red')

        if (((self.x2 > self.foodX1 and self.x2 < self.foodX2) and (self.y2 > self.foodY1 and self.y2 < self.foodY2)) or
                ((self.x2 > self.foodX1 and self.x2 < self.foodX2) and (
                        self.y1 > self.foodY1 and self.y1 < self.foodY2))):
            self.encounter()





mainWindow = Tk()



o = GAME()

mainWindow.bind('<Up>', o.snakeForward)
mainWindow.bind('<Down>', o.snakeBackward)
mainWindow.bind('<Right>', o.snakeRight)
mainWindow.bind('<Left>', o.snakeLeft)

mainWindow.mainloop()
