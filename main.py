import RPS_tkinter 
import tkinter as tk
import Maze
import ttkbootstrap as ttk

def ROCK(window,bist):

    for i in bist:
        i.destroy()

    cist = []
    RPS_tkinter.func(window,cist)

def maze(window,bist):

    for i in bist:
        i.destroy()

    cist = []
    Maze.Welcome(window,cist)

def main():

    window = ttk.Window()
    window.geometry("700x500")
    window.configure(background="#2a2438")
    window.title("Welcome")

    for i in range(21):
        window.grid_columnconfigure(i,weight = 1)
        window.grid_rowconfigure(i,weight = 1)

    style = ttk.Style()
    style.configure('Header.TLabel',
                    foreground = 'white', 
                    background = '#2a2438', 
                    font = ('Times New Roman', 15, 'bold'))
    
    style.configure('Body.TLabel',
                    foreground = 'white', 
                    background = '#2a2438', 
                    font = ('Times New Roman', 13))
    
    style.configure('Button.TButton',
                    foregound = 'white',
                    backgound = '#2a2438',
                    borderwidth = 2,
                    relief = 'raised',
                    highlightcolor = '#3f3752',
                    bordercolor = '#dbd8e3',
                    font = ('Times New Roman', 11))

    text = ttk.Label(window,
                     text = "Welcome",
                     style = 'Header.TLabel',
                     anchor = 'center')
    text.grid(row = 1,
              column = 11,
              sticky = 'nsew')

    option = ttk.Label(window,
                       text = 'Choose one of the following',
                       style = 'Body.TLabel',
                       anchor = 'center')
    option.grid(row = 2,
                column = 11,
                sticky = 'nsew')

    RPS = ttk.Button(window,
                     text = 'Rock, Papers & Scissors',
                     style = 'Button.TButton',
                     command = lambda : ROCK(window,bist))
    RPS.grid(row = 4,
             column = 11,
             sticky = 'nsew')

    maze = ttk.Button(window,
                      text = 'Maze',
                      style = 'Button.TButton',
                      command = lambda : maze(window,bist,style))
    
    bist = [text,option,RPS]

    window.mainloop()
    
main()

