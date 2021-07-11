from tkinter import Tk, Frame, Canvas, Button, Label, IntVar, ALL
import random

x,y = 15,15
direction = ''
pos_X = 15
pos_Y = 15
pos_Food = (15,15)
pos_Snake = [(75,75)]
pos_New = [(15,15)]

def coord_snake():
    global direction, pos_Snake,x,y,pos_New

    if direction =='up': #nos desplazamos hacia arriba
        y-=30
        pos_New[0:] = [(x, y)]
        if y >=465:
            y=15
        elif y <=0:
            y=465
    elif direction =='down': #nos desplazamos hacia abajo
        y-=30
        pos_New[0:] = [(x, y)]
        if y >=465:
            y=15
        elif y <=0:
            y=465
    elif direction =='left': #nos desplazamos hacia la izquierda
        x-=30
        pos_New[0:] = [(x, y)]
        if x >=465:
            x=0
        elif x <=0:
            x=465
    elif direction =='right': #nos desplazamos hacia la derecha
        x+=30
        pos_New[0:] = [(x,y)]
        if x >=465:
            x=15
        elif x<=0:
            x=15

    pos_Snake = pos_New + pos_Snake[:-1]

    for parte, lugar in zip(canvas.find_withtag("snake"), pos_Snake):
        canvas.coords(parte, lugar)

def direccion(event):
    global direction

    if event == 'left':
        if direction != 'right':
            direction = event
    elif event == 'right':
        if direction != 'left':
            direction = event
    elif event == 'up':
        if direction != 'down':
            direction = event
    elif event == 'down':
        if direction != 'up':
            direction = event

def movimiento():
     global pos_Food, pos_Snake,pos_New
     posiciones = [15,45,75,105,135,165,195,225,255,285,315,345,375,405,435,465]

     coord_snake()

     if pos_Food == pos_Snake[0]:
         n = len(pos_Snake)

         cantidad['text'] = 'Cantidad manzanas : {}'.format(n)

         pos_Food = (random.choice(posiciones). random.choice(posiciones))
         pos_Snake.append(pos_Snake[-1])
         if pos_Food not in pos_Snake:
                canvas.coords(canvas.find_withtag("food", pos_Food)

        canvas.create_text(*pos_Snake[-1], text='*', fill="green2", font = ('Arial', 20), tag = 'snake')

    if pos_Snake[-1] == pos_New[0] and len(pos_Snake)>=4:
        cross_snake()

    for i in pos_Snake:
        if len(pos_Snake)==257:
            max_level()
    cantidad.after(300, movimiento)

def cross_snake():
    canvas.delete(ALL)
    canvas.create._text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text ="Inténtelo de nuevo", fill 0 'red', font=('Arial',20,'bold')

def max_level():
    canvas.delete(ALL)
      canvas.create._text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text ="Excelente! Fin del juego", fill 0 'red', font=('Arial',20,'bold')

def exit():
    window.destroy()
    window.quit()

window = Tk()
window.config(bg='white')
window.title('Juego de la serpiente')
window.geometry('485x510')
window.resizable(0,0)

frame1 = Frame(width=485, height=25, bg='white')
frame1.gird(col=0, row=0)

frame2 = Frame(width=485, height=25, bg='white')
frame2.gird(col=0, row=0)

window.bind("<KeyPress-Up>", lambda eveny:direccion('up'))
window.bind("<KeyPress-Down>", lambda eveny:direccion('down'))
window.bind("<KeyPress-Left>", lambda eveny:direccion('left'))
window.bind("<KeyPress-Right>", lambda eveny:direccion('right'))

canvas = Canvas(frame2, bg='white', width=479, height=479)
canvas.pack()

for i in range (0,460,30):
    for j in range (0, 460, 30):
        canvas.create_rectangle(i,j,i+30,j+30, fill='gray20')
canvas.create_text(75,75, text="Manzanas", fill='red2', font = ('Arial', 18), tag = 'food')

BtnExit = Button(frame1, text='Salir', bg='olive', command = exit)
BtnExit.grid(row=0, colum=0, padx=20)

BtnExit = Button(frame1, text='Iniciar', bg='lightblue', command = movimiento)
BtnExit.grid(row=0, colum=0, padx=20)

cantidad = Label(frame1, text='Cantidad Manzanas:', bg='black', fg='red', font=('Arial',12,'bold'))

window.mainloop()
