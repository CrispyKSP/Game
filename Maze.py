import tkinter as tk
import ttkbootstrap as ttk

def end(window):
    window.destroy()

def new_user(window, bist, name):
    name_s = name + '.txt'

    for i in bist:
        i.destroy()

    Bist = []

    maze(window, name_s, Bist)

def retry(window, display, button):
    display.destroy()
    button.destroy()

    old_user(window)

def old_user(window):

    style = ttk.Style()
    style.configure('Body.TLabel',   
                    foreground = 'white', 
                    background = '#2a2438',
                    font = ('Times New Roman', 13))
    
    style.configure('Header.TLabel',
                    foreground = 'white', 
                    background = '#2a2438', 
                    font = ('Times New Roman', 15, 'bold'))
    
    style.configure('Buttons.TButton',
                    foreground = 'white',
                    background = '#3f3752',
                    borderwidth = 2,
                    relief = 'raised',
                    highlightcolor = '#dbd8e3',
                    bordercolor = '#dbd8e3',
                    font = ('Times New Roman', 13))
    
    style.configure('Entry.TEntry',
                    foreground = 'black',
                    background = '#79c2d0',
                    font = ('Times New Roman', 13))

    welcome = ttk.Label(master=window,
                       text='Good to have you back',
                       style='Header.TLabel',
                       anchor='center')
    welcome.grid(row=0,
                 column=11,
                 pady=10,
                 sticky='nsew')

    ask_name = ttk.Label(window,
                        text='Please enter your username',
                        style='Body.TLabel',
                        anchor='center') 
    ask_name.grid(row=1, 
                  column=11,
                  pady=10,
                  sticky='nsew')

    name = ttk.Entry(window,
                     style='Entry.TEntry')
    name.grid(row=2,
              column=11,
              pady=10,
              sticky='nsew')

    enter_button = ttk.Button(window,
                             text='Done', 
                             command=lambda: file_data_accessing(window, name_s, stuff),
                             style='Buttons.TButton')
    enter_button.grid(row=3, 
                      column=15, 
                      pady=10, 
                      sticky='nsew')

    name_s = name.get()
    stuff = [welcome,ask_name,name,enter_button]

def file_data_accessing(window, name, stuff):

    global me_data, user_data

    for i in stuff:
        i.destroy()

    style = ttk.Style()
    style.configure('Body.TLabel',   
                    foreground = 'white', 
                    background = '#2a2438',
                    font = ('Times New Roman', 13))
    
    style.configure('Header.TLabel',
                    foreground = 'white', 
                    background = '#2a2438', 
                    font = ('Times New Roman', 15, 'bold'))
    
    style.configure('Buttons.TButton',
                    foreground = 'white',
                    background = '#3f3752',
                    borderwidth = 2,
                    relief = 'raised',
                    highlightcolor = '#dbd8e3',
                    bordercolor = '#dbd8e3',
                    font = ('Times New Roman', 13))
    
    style.configure('Entry.TEntry',
                    foreground = 'black',
                    background = '#79c2d0',
                    font = ('Times New Roman', 13))

    name = name + '.txt' 
    try:
        with open(name, "r") as file:
            lines = file.readlines()
            if len(lines) == 2:
                me = lines[0].strip()
                user = lines[1].strip()
                me_data = int(me)
                user_data = int(user)

            display_1 = ttk.Label(window,
                                 text='From our last game',
                                 style='Header.TLabel',
                                 anchor='center')
            display_1.grid(row=0, 
                           column=11, 
                           pady=10, 
                           sticky='nsew')

            display_2 = ttk.Label(window,
                                 text='Your points %s ' % (user_data),
                                 style='Body.TLabel',
                                 anchor='center')
            display_2.grid(row=1, 
                           column=11, 
                           pady=10, 
                           sticky='nsew')

            display_3 = ttk.Label(window, 
                                 text='My points %s ' % (me_data),
                                 style='Body.TLabel',
                                 anchor='center')
            display_3.grid(row=2, 
                           column=11, 
                           pady=10, 
                           sticky='nsew')

            button = ttk.Button(window, 
                               text='continue', 
                               command=lambda: RPS(window, name, bist),
                               style='Buttons.TButton')
            button.grid(row=3, 
                        column=14, 
                        pady=10, 
                        sticky='nsew')

            bist = [ display_1, display_2, display_3, button]            

    except FileNotFoundError:
        display = ttk.Label(window, 
                           text='File Not found',
                           style='Header.TLabel',
                           anchor='center')
        display.grid(row=0, 
                     column=7, 
                     pady=10, 
                     sticky='nsew')

        button = ttk.Button(window, 
                           text = 'Retry', 
                           command=lambda: retry(window, display, button),
                           style='Buttons.TButton')
        button.grid(row=1,
                    column=7, 
                    pady=10, 
                    sticky='nsew')
            
    except Exception as e:
        print("error with the file stored data: ", e)

def maze(window,name,Bist):
    C = tk.Canvas(window, bg="#2a2438", height=600, width=600)

    
    C.pack()


def level_one():
    walls = "#dbd8e3"
    shadow = 'black'
                        # x0,y0   x1,y1
    line_1 = C.create_line(135,135,465,135, fill = walls , width = 4)
    line_2 = C.create_line(135,133,135,165, fill = walls , width = 4)
    line_3 = C.create_line(133,165,225,165, fill = walls , width = 4)
    line_4 = C.create_line(255,165,255,195, fill = walls , width = 4)
    line_5 = C.create_line(253,195,345,195, fill = walls , width = 4)
    line_6 = C.create_line(285,135,285,165, fill = walls , width = 4)
    line_7 = C.create_line(315,165,407,165, fill = walls , width = 4)
    line_8 = C.create_line(405,135,405,165, fill = walls , width = 4)
    line_9 = C.create_line(435,135,435,225, fill = walls , width = 4)
    line_10 = C.create_line(315,163,315,225, fill = walls , width = 4)
    line_11 = C.create_line(135,195,135,465, fill = walls , width = 4)
    line_12 = C.create_line(135,465,465,465, fill = walls , width = 4)
    line_13 = C.create_line(465,135,465,405, fill = walls , width = 4)
    line_14 = C.create_line(465,435,465,465, fill = walls , width = 4)
    line_15 = C.create_line(135,195,195,195, fill = walls , width = 4)
    line_16 = C.create_line(165,255,165,315, fill = walls , width = 4)
    line_17 = C.create_line(135,315,165,315, fill = walls , width = 4)
    line_18 = C.create_line(165,225,195,225, fill = walls , width = 4)
    line_19 = C.create_line(165,255,195,255, fill = walls , width = 4)
    line_20 = C.create_line(195,225,195,255, fill = walls , width = 4)
    line_21 = C.create_line(165,345,165,465, fill = walls , width = 4)
    line_22 = C.create_line(225,195,225,255, fill = walls , width = 4)
    line_23 = C.create_line(195,285,195,375, fill = walls , width = 4)
    line_24 = C.create_line(195,405,195,435, fill = walls , width = 4)
    line_25 = C.create_line(195,285,255,285, fill = walls , width = 4)
    line_26 = C.create_line(195,405,255,405, fill = walls , width = 4)
    line_27 = C.create_line(225,435,225,465, fill = walls , width = 4)
    line_28 = C.create_line(225,345,255,345, fill = walls , width = 4)
    line_29 = C.create_line(225,315,225,345, fill = walls , width = 4)
    line_30 = C.create_line(255,195,285,195, fill = walls , width = 4)
    line_31 = C.create_line(195,375,225,375, fill = walls , width = 4)
    line_32 = C.create_line(375,195,405,195, fill = walls , width = 4)
    line_33 = C.create_line(225,225,315,225, fill = walls , width = 4)
    line_34 = C.create_line(255,225,255,285, fill = walls , width = 4)
    line_35 = C.create_line(225,315,285,315, fill = walls , width = 4)
    line_36 = C.create_line(345,225,375,225, fill = walls , width = 4)
    line_37 = C.create_line(405,225,435,225, fill = walls , width = 4)
    line_38 = C.create_line(225,435,285,435, fill = walls , width = 4)
    line_39 = C.create_line(315,435,345,435, fill = walls , width = 4)
    line_40 = C.create_line(405,435,465,435, fill = walls , width = 4)
    line_41 = C.create_line(255,345,255,435, fill = walls , width = 4)
    line_42 = C.create_line(285,315,285,405, fill = walls , width = 4)
    line_43 = C.create_line(405,195,405,255, fill = walls , width = 4)
    line_44 = C.create_line(375,225,375,255, fill = walls , width = 4)
    line_45 = C.create_line(345,225,345,255, fill = walls , width = 4)
    line_46 = C.create_line(285,255,345,255, fill = walls , width = 4)
    line_47 = C.create_line(285,255,285,285, fill = walls , width = 4)
    line_48 = C.create_line(315,255,315,345, fill = walls , width = 4)
    line_49 = C.create_line(285,345,315,345, fill = walls , width = 4)
    line_50 = C.create_line(315,375,315,435, fill = walls , width = 4)
    line_51 = C.create_line(435,255,465,255, fill = walls , width = 4)
    line_52 = C.create_line(435,255,435,315, fill = walls , width = 4)
    line_53 = C.create_line(405,315,435,315, fill = walls , width = 4)
    line_54 = C.create_line(405,285,405,315, fill = walls , width = 4)
    line_55 = C.create_line(375,285,405,285, fill = walls , width = 4)
    line_56 = C.create_line(375,315,375,375, fill = walls , width = 4)
    line_57 = C.create_line(375,435,375,465, fill = walls , width = 4)
    line_58 = C.create_line(345,285,345,345, fill = walls , width = 4)
    line_59 = C.create_line(345,315,375,315, fill = walls , width = 4) 
    line_60 = C.create_line(315,375,375,375, fill = walls , width = 4)
    line_61 = C.create_line(345,375,345,405, fill = walls , width = 4)
    line_62 = C.create_line(375,345,465,345, fill = walls , width = 4)
    line_63 = C.create_line(405,375,435,375, fill = walls , width = 4)
    line_64 = C.create_line(405,375,405,405, fill = walls , width = 4)
    line_65 = C.create_line(375,405,465,405, fill = walls , width = 4)


def Welcome(window,style,cist):

    for i in cist:
        i.destroy()

    style.configure('Body.TLabel',   
                    foreground = 'white', 
                    background = '#2a2438',
                    font = ('Times New Roman', 13))
    
    style.configure('Header.TLabel',
                    foreground = 'white', 
                    background = '#2a2438', 
                    font = ('Times New Roman', 15, 'bold'))
    
    style.configure('Buttons.TButton',
                    foreground = 'white',
                    background = '#3f3752',
                    borderwidth = 2,
                    relief = 'raised',
                    highlightcolor = '#dbd8e3',
                    bordercolor = '#dbd8e3',
                    font = ('Times New Roman', 13))
    
    intro = ttk.Label(window, 
                      text='Welcome to Rock, Paper and Scissors', 
                      style = 'Header.TLabel',
                      anchor='center')
    intro.grid(row=0, 
               column=11, 
               pady=2, 
               sticky='nsew')

    about = ttk.Label(window, 
                      text='Are you an old user?',
                      style = 'Body.TLabel',
                      anchor='center')
    about.grid(row=1, 
               column=11, 
               pady=2, 
               sticky='nsew')
    
    yes_button = ttk.Button(window, 
                            text='Yes', 
                            command=lambda: yes(window, cist), 
                            style = 'Buttons.TButton',
                            width=3)
    yes_button.grid(row=2, 
                    column=7, 
                    pady=2, 
                    sticky='nsew')
    
    no_button = ttk.Button(window, 
                           text='No', 
                           command=lambda: no(window, cist),
                           style = 'Buttons.TButton',
                           width=3)
    no_button.grid(row=2, 
                   column=15, 
                   pady=2, 
                   sticky='nsew')
    
    cist = [intro, about, yes_button, no_button] 

def main():
    window = tk.Tk()

    

    window.mainloop()