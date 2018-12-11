# code desired only for my input, only to get the answer fast, part 2 done
# by just manually testing values and using print's with points that has
# velocity of 1 to speed up that manual testing

from tkinter import *


class Simulation:

    def __init__(self):
        with open("data.txt", 'r') as file:
            data = [x.replace("\n", "") for x in file.readlines()]
            self.points = [[int(x[10:16]), int(x[18:24]),
                            int(x[-7:-5]),
                            int(x[-3:-1])] for x in data]

        self.counter = 0
        for p in self.points:
            p[0] += (p[2] * 10235)
            p[1] += (p[3] * 10235)


        self.master = Tk()
        self.canvas = Canvas(self.master, width=600, height=500)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.master.after(10, self.paint)
        self.master.mainloop()
        self.paint()

    def paint(self):
        self.canvas.delete("all")
        for p in self.points:
            x1, y1 = (p[0] - 33), (p[1] - 53)
            x2, y2 = (p[0] - 31), (p[1] - 51)
            self.canvas.create_oval(2*x1, 2*y1, 2*x2, 2*y2, width=0, \
                                                               fill="#000000")
            if self.counter % 16 < 8:
                p[0] += p[2]
                p[1] += p[3]
            else:
                p[0] -= p[2]
                p[1] -= p[3]

        self.counter += 1
        print(self.points[0])
        self.master.after(300, self.paint)


simulation = Simulation()
