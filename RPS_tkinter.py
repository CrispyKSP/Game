import  tkinter as tk
import ttkbootstrap as ttk
import random

me_data = 0
user_data = 0

def end(window):
    window.destroy()

def new_user(window, bist, name,password):

        
    name_1 = name.get()
    password_1 = str(password.get())

    name_s = name_1+'.txt'

    RPS(window, name_s, bist,password_1)

def retry(window, display, button):
    display.destroy()
    button.destroy()

    Bist = []

    old_user(window,Bist)

def old_user(window,Bist):

    for i in Bist:
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
    
    password = ttk.Entry(window,
                         style = 'Entry.TEntry')
    password.grid(row = 3,
                  column = 11,
                  pady = 10,
                  sticky = 'nsew')

    enter_button = ttk.Button(window,
                             text='Done', 
                             command=lambda: file_data_accessing(window, name, stuff,password),
                             style='Buttons.TButton')
    enter_button.grid(row=4, 
                      column=15, 
                      pady=10, 
                      sticky='nsew')
    
    stuff = [welcome,ask_name,name,enter_button,password]

def file_data_accessing(window, name, stuff, password):

    name_s = name.get()
    password_1 = str(password.get())

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
    
    style.configure('Red.TLabel',
                    foreground = 'red', 
                    background = '#2a2438', 
                    font = ('Times New Roman', 15, 'bold'))

    name = name_s + '.txt' 
    try:
        with open(name, "r") as file:
            lines = file.readlines()
            if len(lines) == 3:
                password_real, me, user = map(str.strip, lines)
                me_data = int(me)
                user_data = int(user)
            else:
                print('Error with the file having more than 3 lines in it')

            if password_1 == password_real: 

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
                                command=lambda: RPS(window, name, bist, password),
                                style='Buttons.TButton')
                button.grid(row=3, 
                            column=14, 
                            pady=10, 
                            sticky='nsew')

                bist = [ display_1, display_2, display_3, button]   


            else:

                Display_1 = ttk.Label(window,
                                      text = 'Incorrect password',
                                      style = 'Red.TLabel',
                                      anchor = 'center')
                Display_1.grid(row = 1,
                               column = 11,
                               pady = 10,
                               sticky = 'nsew')
                
                retry = ttk.Button(window,
                                   text = 'Retry',
                                   command = lambda: old_user(window,Bist), 
                                   style = 'Buttons.TButton')
                retry.grid(row = 2,
                           column = 15,
                            sticky = 'nsew')

                Quit = ttk.Button(window,
                                   text = 'Quit',
                                   command = lambda: end(window),
                                   style = 'Buttons.TButton')
                Quit.grid(row = 2,
                           column = 7,
                            sticky = 'nsew')
                
                Bist = [Display_1,retry,Quit]
                 

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

def RPS(window, name, bist,password):
    
    for i in bist:
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

    quit_button = ttk.Button(window,
                            text='quit',
                            command=lambda: file_data_saving(window, name, disable, password),
                            style='Buttons.TButton')
    quit_button.grid(row=10,
                     column=17, 
                     pady=10, 
                     sticky='nsew')

    option = ttk.Label(window, 
                       text='Choose',
                       style='Header.TLabel', 
                       anchor='center')
    option.grid(row=3, 
                column=7, 
                pady=10, 
                sticky='nsew')

    rock_button = ttk.Button(window, 
                            text='rock', 
                            command=lambda: Rock(window, me_1, you_1, word2, word3, result_label, result_label1),
                            style='Buttons.TButton')
    rock_button.grid(row=4, 
                     column=3, 
                     pady=10, 
                     sticky='nsew')

    paper_button = ttk.Button(window, 
                             text='paper', 
                             command=lambda: Paper(window, me_1, you_1, word2, word3, result_label, result_label1),
                             style='Buttons.TButton')
    paper_button.grid(row=4,
                      column=7, 
                      pady=10, 
                      sticky='nsew')

    scissors_button = ttk.Button(window, 
                                text='scissors', 
                                command=lambda: Scissors(window, me_1, you_1, word2, word3, result_label, result_label1),
                                style='Buttons.TButton')
    scissors_button.grid(row=4, 
                         column=11, 
                         pady=10, 
                         sticky='nsew')

    me_label = ttk.Label(window, 
                        text='My point : ',
                        style='Body.TLabel',
                        anchor='center')
    me_label.grid(row=0, 
                  column=16, 
                  pady=10, 
                  sticky='nsew')

    me_1 = ttk.Label(window, 
                    text=me_data,
                    style='Body.TLabel', 
                    anchor='center')
    me_1.grid(row=0, 
              column=17,
              pady=10, 
              sticky='nsew')

    you_label = ttk.Label(window, 
                         text='Your point : ', 
                         style='Body.TLabel',
                         anchor='center')
    you_label.grid(row=1, 
                   column=16, 
                   pady=10, 
                   sticky='nsew')

    result_label = ttk.Label(window, 
                            text='',
                            style='Body.TLabel',
                            anchor='center')
    result_label.grid(row=9, 
                      column=7, 
                      pady=10, 
                      sticky='nsew')

    result_label1 = ttk.Label(window, 
                             text='',
                             style='Body.TLabel', 
                             anchor='center')
    result_label1.grid(row=10, 
                       column=7, 
                       pady=10, 
                       sticky='nsew')

    you_1 = ttk.Label(window, 
                     text=user_data,
                     style='Body.TLabel',
                     anchor='center')
    you_1.grid(row=1, 
               column=17, 
               pady=10, 
               sticky='nsew')

    word = ttk.Label(window, 
                    text='you chose : ',
                    style='Body.TLabel',
                    anchor='center')
    word.grid(row=6, 
              column=3, 
              pady=10, 
              sticky='nsew')

    word2 = ttk.Label(window, 
                     text='',
                     style='Body.TLabel',
                     anchor='center')
    word2.grid(row=8, 
               column=3, 
               pady=10, 
               sticky='nsew')

    word1 = ttk.Label(window, 
                     text='I chose : ',
                     style='Body.TLabel',
                     anchor='center')
    word1.grid(row=6, 
               column=11, 
               pady=10, 
               sticky='nsew')

    word3 = ttk.Label(window, 
                     text='',
                     style='Body.TLabel',
                     anchor='center')
    word3.grid(row=8, 
               column=11, 
               pady=10, 
               sticky='nsew')

    disable = [quit_button,option,rock_button,paper_button,scissors_button,me_label,me_1,you_label,you_1,word,word2,word1,word3,result_label,result_label1]

def Rock(window, me_1, you_1, word2, word3, result_label ,result_label1):

    global me_data, user_data

    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)
    word2.config(text='Rock')

    if choice == 3:
        user_data += 1
        text = 'Scissors'
        user_win(text, window, me_1, you_1, word3, result_label, result_label1) 

    elif choice == 2:
        me_data += 1
        text='Paper'
        user_lose(text, window, me_1, you_1, word3, result_label, result_label1)

    else:
        text = 'Rock'
        user_draw(text, window, me_1, you_1, word3, result_label, result_label1)

    print('rock')

def Paper(window, me_1, you_1, word2, word3, result_label, result_label1):
    
    global me_data, user_data

    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)
    word2.config(text='Paper')

    if choice == 1:
        user_data += 1
        text = 'Rock'
        user_win(text, window, me_1, you_1, word3, result_label, result_label1) 

    elif choice == 3:
        me_data += 1
        text='Scissors'
        user_lose(text, window, me_1, you_1, word3, result_label, result_label1)

    else:
        text = 'Paper'
        user_draw(text, window, me_1, you_1, word3, result_label, result_label1)

    print("paper")

def Scissors(window, me_1, you_1, word2, word3, result_label, result_label1):

    global me_data, user_data

    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)
    word2.config(text='Scissors')

    if choice == 2:
        user_data += 1
        text = 'Paper'
        user_win(text, window, me_1, you_1, word3, result_label, result_label1)       

    elif choice == 1:
        me_data += 1
        text = 'Rock'
        user_lose(text, window, me_1, you_1, word3, result_label, result_label1)

    else:
        text = 'Scissors'
        user_draw(text, window, me_1, you_1, word3, result_label, result_label1)

    print("scissors")

def user_win(text, window, me_1, you_1, word3, result_label, result_label1):

    me_1.config(text=me_data)
    you_1.config(text=user_data)
    word3.config(text=text)
    result_label.config(text='U win')
    result_label1.config(text='ಠ_ಠ')

def user_lose(text, window, me_1, you_1, word3, result_label, result_label1):

    me_1.config(text=me_data)
    you_1.config(text=user_data)
    word3.config(text=text)
    result_label.config(text='I win')
    result_label1.config(text='(⌐■_■)')

def user_draw(text, window, me_1, you_1, word3, result_label, result_label1):

    me_1.config(text=me_data)
    you_1.config(text=user_data)
    word3.config(text=text)
    result_label.config(text='Draw')
    result_label1.config(text='(〃￣︶￣)人')

def file_data_saving(window, name, disable, password):

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

    for i in disable:
        i.destroy()

    try:
        with open(name,"w") as file:
            pass
        with open(name,"w") as file:
            me=str(me_data)
            user=str(user_data)
            file.write(password+'\n')
            file.write(me+"\n")
            file.write(user+"\n")
    except Exception as e:
        print("error while storing data : ",e)

    you = ttk.Label(window, 
                    text='Your points : %s' %(user_data),
                    style='Header.TLabel',
                    anchor='center')
    you.grid(row=1, 
             column=11, 
             pady=10, 
             sticky='nsew')

    me = ttk.Label(window, 
                   text='My points : %s' %(me_data),
                   style='Header.TLabel',
                   anchor='center')
    me.grid(row=2, 
            column=11, 
            pady=10, 
            sticky='nsew')

    done = ttk.Button(window, 
                      text='Done', 
                      command= lambda : end(window), 
                      style='Buttons.TButton' )
    done.grid(row=3, 
              column=15, 
              pady=10, 
              sticky='nsew')

    go_back = ttk.Button(window, 
                         text='Return', 
                         command= lambda : RPS(window,name,bist),
                         style='Buttons.TButton')
    go_back.grid(row=3, 
                 column=7, 
                 pady=10, 
                 sticky='nsew') 
 
    bist = [you, me, done, go_back]

def no(window, cist):
    for i in cist:
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

    welcome = ttk.Label(window,
                        text='Good to have you', 
                        style='Header.TLabel',
                        anchor='center')
    welcome.grid(row=0, 
                 column=11, 
                 pady=10, 
                 sticky='nsew')

    ask_name = ttk.Label(window, 
                         text='Please enter the username you would like to use',
                         style='Body.TLabel',
                         anchor='center')
    ask_name.grid(row=1, 
                  column=11, 
                  pady=10, 
                  sticky='nsew')

    name = ttk.Entry(window, 
                    style = 'Entry.TEntry')
    name.grid(row=2, 
              column=11, 
              pady=10, 
              sticky='nsew')
    
    password = ttk.Entry(window,
                         style = 'Entry.TEntry')
    password.grid(row = 3,
                  column = 11,
                  pady = 10,
                  sticky = 'nsew')

    enter_button = ttk.Button(window, 
                              text='Done', 
                              command=lambda: new_user(window,bist,name,password),
                              style='Buttons.TButton')
    enter_button.grid(row=4, 
                      column=12, 
                      pady=10, 
                      sticky='nsew')
    
    Back_button = ttk.Button(window,
                             text = 'Back',
                             command=lambda: func(window,bist),
                             style = 'Buttons.TButton')
    Back_button.grid(row=4,
                     column=10,
                     pady=10,
                     sticky='nsew')

    bist = [welcome,ask_name,name,enter_button,Back_button,password]
    
def func(window,bist):

    style = ttk.Style()

    for i in bist:
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
                            command=lambda: old_user(window, cist), 
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


def welcome():

    window = ttk.Window()
    window.configure(background = '#2a2438' )
    window.title("Rock Paper Scissors")
    window.geometry('700x500') 
    
    
    # Configure the grid to center widgets
    for i in range(21):
        window.grid_columnconfigure(i, weight=1)
        window.grid_rowconfigure(i, weight=1)

    bist=[]

    func(window,bist)
    
    
    window.mainloop()
