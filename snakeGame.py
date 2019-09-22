from tkinter import *
import random

y = 0
forward = -1
backward = -1
right = -1
left = -1

class GAME:

    def __init__(self):

        global y

        self.x1 = 145
        self.x2 = 160
        self.y1 = 150+y
        self.y2 = 180+y

        self.canvas = Canvas(mainWindow, height=300, width=300, bg='blue')
        self.canvas.pack()

        self.food = self.canvas.create_rectangle(20, 20, 30, 30, fill='white')
        self.snake = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='red')
        self.tempRectangle = self.canvas.create_rectangle(0,0,0,0,fill='red')

    def foodPosition(self, event):

        self.canvas.delete(self.food)

        x1 = random.randrange(20, 280)
        x2 = x1 + 10

        y1 = random.randrange(20, 280)
        y2 = y1 + 10

        self.food = self.canvas.create_rectangle(x1, y1, x2, y2, fill='white')

    def snakeForward(self, event):

        global forward, backward, left, right
        forward = 1
        backward = 0

        self.canvas.delete(self.snake)
        self.canvas.delete(self.tempRectangle)

        if left == -1 and right == -1:

            self.y1 -= 10
            self.y2 -= 10

            self.snake = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='red')


        # global forward, backward
        #
        # forward = 0
        # backward = 1
        #
        # self.canvas.delete(self.snake)
        # self.canvas.delete(self.tempRectangle)
        #
        # if abs(self.x2-self.x1) == 15:
        #
        #
        # if abs((self.y1 - self.y2)) > 15:
        #
        #     if forward == 1 or forward == -1:
        #         self.y2 -= 10
        #         self.tempRectangle = self.canvas.create_rectangle(self.x1 - 10, self.y1, self.x1, self.y1 + 15,
        #                                                           fill='red')
        #
        #     elif backward == 1 or backward == -1:
        #         self.y1 += 10
        #         self.tempRectangle = self.canvas.create_rectangle(self.x2-25, self.y2 - 15, self.x2-15, self.y2,
        #                                                           fill='red')
        #
        #     if abs((self.y1 - self.y2)) < 15:
        #         self.y2 = self.y1 + 15
        #         self.x2 = self.x1 + 30
        #
        # else:
        #     self.x1 -= 10
        #     self.x2 -= 10
        #     self.y2 = self.y1 + 15
        #
        # self.snake = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='red')


    def snakeBackward(self, event):

        global forward, backward


        self.canvas.delete(self.snake)

        self.y1 += 10
        self.y2 += 10

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





mainWindow = Tk()



o = GAME()

mainWindow.bind('<Double-Button-1>', o.foodPosition)

mainWindow.bind('<Up>', o.snakeForward)
mainWindow.bind('<Down>', o.snakeBackward)
mainWindow.bind('<Right>', o.snakeRight)
mainWindow.bind('<Left>', o.snakeLeft)

mainWindow.mainloop()
