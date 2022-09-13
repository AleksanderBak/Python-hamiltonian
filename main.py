import turtle
import random
import math
import time
import tkinter

"""
def write_slogan():
    frame = canvas
    frame.pack()

    button = tkinter.Button(frame,
                       text="QUIT",
                       fg="red",
                       command=quit)
    button.pack(side=tkinter.LEFT)
    slogan = tkinter.Button(frame,
                       text="Hello",
                       command=write_slogan)
    slogan.pack(side=tkinter.LEFT)

    canvas.mainloop()
"""

global n, cnt, t, t2, cykle, header, last_deleted, g1, screen, window, button, var

class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.V = vertices

    def is_safe(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamilton_util(self, path, pos):

        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.V):
            if self.is_safe(v, pos, path) is True:
                path[pos] = v
                if self.hamilton_util(path, pos + 1) is True:
                    return True
                path[pos] = -1

        return False

    def hamilton(self):
        path = [-1] * self.V
        path[0] = 0

        if self.hamilton_util(path, 1) is False:
            return False
        path.append(0)
        if path not in cykle:
            t2.pendown()
            cykle.append(path)
            t2.write("->"+str(path))
            t2.penup()
            t2.goto(t2.pos()[0], t2.pos()[1]-20)
        return path

    def check_hamilton(self, cycle):
        for i in range(len(cycle)-1):
            if self.graph[cycle[i]][cycle[i+1]] != 1:
                return False
        return True

    def losuj_krawedz(self):
        row = random.choice(range(len(self.graph)))
        while 1 not in self.graph[row]:
            row = random.choice(range(len(self.graph)))

        column = random.choice(range(len(self.graph[row])))
        while self.graph[row][column] == 0:
            column = random.choice(range(len(self.graph[row])))

        self.graph[row][column] = 0
        self.graph[column][row] = 0
        new = [row, column]
        return new

    def dodaj_krawedz(self, deleted):
        if deleted is not None:
            self.graph[deleted[0]][deleted[1]] = 1
            self.graph[deleted[1]][deleted[0]] = 1


def gnp(n, p):
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if random.random() <= p:
                a[i][j] = a[j][i] = 1
    return a


def rysujgraf(n, a):
    t.pencolor("black")
    t.penup()
    t.goto(300, 250)
    t.write("Liczba iteracji: "+str(cnt), font=header)
    r = 8
    s = 150
    p = 2 * 3.1415 / n
    x = [s * math.sin(p * (i + 1)) for i in range(n)]
    y = [s * math.cos(p * (i + 1)) for i in range(n)]
    t.pencolor("#f8f8f2")
    for i in range(n):
        if condition is False:
            exit()
        for j in range(i):
            if a[i][j] == 1:
                t.penup()
                t.goto(x[i], y[i])
                t.pendown()
                t.goto(x[j], y[j])
    t.pencolor("black")
    t.fillcolor('#50fa7b')
    for i in range(n):
        if condition is False:
            exit()
        t.pencolor("#50fa7b")
        t.penup()
        t.goto(x[i] + r / 2 - 3, y[i] - r / 2 - 3)
        t.pendown()
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.goto(x[i] + r / 2 - 3 + 5, y[i] - r / 2 - 3)
        t.pencolor("#50fa7b")
        if x[i] > 0 and y[i] > 0:
            t.penup()
            t.goto(x[i]+10, y[i]+10)
            t.pendown()
            t.write(i, font=("Arial", 15, "normal"))
        elif x[i] > 0 and y[i] < 0:
            t.penup()
            t.goto(x[i]+15, y[i]-20)
            t.pendown()
            t.write(i, font=("Arial", 15, "normal"))
        elif x[i] < 0 and y[i] < 0:
            t.penup()
            t.goto(x[i] - 25, y[i] - 25)
            t.pendown()
            t.write(i, font=("Arial", 15, "normal"))
        else:
            t.penup()
            t.goto(x[i] - 10, y[i] + 15)
            t.pendown()
            t.write(i, font=("Arial", 15, "normal"))


def rysujhamilton(a, n):
    t.speed(2)
    t.pencolor('#50fa7b')
    s = 150
    p = 2 * 3.1415 / n
    x = [s * math.sin(p * (i + 1)) for i in range(n)]
    y = [s * math.cos(p * (i + 1)) for i in range(n)]
    for i in range(0, len(a)-1):
        if condition is False:
            exit()
        t.penup()
        t.goto(x[a[i]], y[a[i]])
        t.st()
        t.pendown()
        t.goto(x[a[i+1]], y[a[i+1]])
    t.ht()
    t.speed(10)


def komunikat(typ, ham, pre):
    t.penup()
    t.goto(0, 300)
    t.pendown()
    t.pencolor('#8be9fd')
    if ham is False:
        t.write('Brak cyklu hamiltona', font=('Courier', 20, 'italic'), align='center')
        return
    if len(ham) <= 11:
        style = ('Courier', 20, 'italic')
    elif len(ham) <= 18:
        style = ('Courier', 17, 'italic')
    else:
        style = ('Courier', 12, 'italic')
    if typ is False:
        t.write('Brak cyklu hamiltona', font=style, align='center')
    else:
        t.write(pre+str(ham), font=style, align='center')


def usun_krawedz(a, n):
    t.speed(2)
    t.pencolor("#ff5555")
    s = 150
    p = 2 * 3.1415 / n
    x = [s * math.sin(p * (i + 1)) for i in range(n)]
    y = [s * math.cos(p * (i + 1)) for i in range(n)]
    t.penup()
    t.goto(x[a[0]], y[a[0]])
    t.st()
    t.pendown()
    t.goto(x[a[1]], y[a[1]])
    t.ht()
    t.speed(10)


condition = True


def loop():
    global n, last_deleted, cnt, button, var
    while condition:
        found = False
        cycle = None

        if last_deleted is not None:
            screen.tracer(0)
            rysujgraf(n, g1.graph)
            screen.update()
            screen.tracer(1)

        for i in cykle:
            if g1.check_hamilton(i) is True:
                komunikat(True, i, "Poprzedni cykl ->")
                rysujhamilton(i, n)
                found = True
                break

        if found is False:
            cycle = g1.hamilton()

        if cycle is False:
            komunikat(False, cycle, "")
        elif cycle is not None:
            komunikat(True, cycle, "Nowy cykl -> ")
            rysujhamilton(cycle, n)

        g1.dodaj_krawedz(last_deleted)
        last_deleted = g1.losuj_krawedz()
        time.sleep(1)
        usun_krawedz(last_deleted, n)
        time.sleep(1)
        button.wait_variable(var)
        t.clear()
        cnt += 1


def stop():
    global condition
    condition = False
    exit()


def main_code(vertices, p):
    global n, cnt, t, t2, cykle, header, last_deleted, g1, screen, window, var, button
    n = vertices

    cykle = []
    cnt = 1

    header = ('Courier', 12, 'italic')

    window = tkinter.Tk()
    window.resizable(False, False)
    window.title("Poszukiwanie cykli Hamiltona w grafie ze zmiennymi krawędziami")

    canvas = tkinter.Canvas(window, width=1100, height=800)
    canvas.pack()

    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("#44475a")


    var = tkinter.IntVar()
    button = tkinter.Button(window, bg="#282a36", fg="#f8f8f2", text="Kolejna iteracja", width=34, height=3, font="Arial, 20", command=lambda: var.set(1))
    button.pack(side=tkinter.LEFT)

    exit_button = tkinter.Button(window, bg="#282a36", fg="#f8f8f2", text="Zakończ program", width=34, height=3, font="Arial, 20", command=stop)
    exit_button.pack(side=tkinter.RIGHT)


    t2 = turtle.RawTurtle(screen)
    t2.ht()
    t2.penup()
    t2.goto(-500, 250)
    t2.write("Lista wykorzystanych cykli:", font=header)
    t2.goto(-500, 230)
    t2.st()

    a = gnp(n, p)
    g1 = Graph(n)
    g1.graph = a

    t = turtle.RawTurtle(screen)
    t.ht()
    t.width(2)
    t.speed(0.1)
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    rysujgraf(n, g1.graph)

    last_deleted = None
    loop()

main_code(10,0.5)
