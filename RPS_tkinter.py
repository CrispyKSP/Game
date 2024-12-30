import ttkbootstrap as ttk
from tkinter import Canvas, PhotoImage
import random
import os

comp_data = user_data = 0

def end(window, canvas):
    window.destroy()

def canva_delete(bist,canvas):

    for i in bist:
        canvas.delete(i)

def label_delete(cist):

    for i in cist:
        i.destroy()

def new_user_actions(window, canvas, cist, bist, style, name_entry, password_entry):

    global name,password_entered

    name_1 = name_entry.get()
    password_entered = str(password_entry.get())

    name = 'USER/'+name_1+'.txt'

    RPS(window, canvas, cist, bist, style)

def file_data_accessing(window, canvas, name_entry, cist, bist, password_entry, style):

    global comp_data,user_data,password_entered,name

    name_s = name_entry.get()
    password_entered = password_entry.get()

    name = 'USER/'+name_s+".txt"
    try:
        with open(name,"r") as file:
            lines = file.readlines()
            if len(lines) == 3:
                password_file, comp, user = map(str.strip, lines)
                comp_data = int(comp)
                user_data = int(user)
            else:
                print("Error with the file as it has less or more than 3")

            if password_entered == password_file:

                canva_delete(bist, canvas)
                label_delete(cist)

                display_1 = canvas.create_text(350,100,
                                               text="From our last game",
                                               fill="black",
                                               font=('Montserrat',15,'bold'))

                display_2 = canvas.create_text(350,150,
                                               text="Your points : %s" %(user_data),
                                               fill="black",
                                               font=('Montserrat',13))

                display_3 = canvas.create_text(339,200,
                                               text="Machine points :  %s" %(comp_data),
                                               fill="black",
                                               font=('Montserrat',13))

                Continue = ttk.Button(canvas, 
                                    text='Continue',
                                    command=lambda: RPS(window, 
                                                        canvas, 
                                                        cist, 
                                                        bist, 
                                                        style), 
                                    style='Buttons.TButton',
                                    width=8)
                canvas.create_window(400, 250, 
                                     anchor="center", 
                                     window=Continue)

                if user_data > comp_data:
                    age = PhotoImage(file="image/CHOSE/PAPER_S.png")
                    useless = canvas.create_image(200, 
                                                  200, 
                                                  anchor="nw", 
                                                  image=age)
                    canvas.image = age

                elif comp_data > user_data:
                    age = PhotoImage(file="image/CHOSE/SCISSOR_B.png")
                    useless = canvas.create_image(200, 
                                                  200, 
                                                  anchor="nw", 
                                                  image=age)
                    canvas.image = age

                cist.clear()
                bist.clear()
                cist.append(Continue)
                bist.extend([display_1, display_2, display_3, useless])

            else:

                wrong = canvas.create_text(480,250,
                                           text = "Incorrect password",
                                           fill = "Red",
                                           font = ("Montserrat", 10))

                bist.append(wrong)

    except FileNotFoundError:

        display = canvas.create_text(480,200,
                                     text = 'Incorrect Username',
                                     fill= "Red",
                                     font = ("Montserrat", 10))

        bist.append(display)

    except Exception as e:
        print("error with the file that has stored data : ", e)
        print("Between lines 41 to 139")

def RPS(window, canvas, cist, bist, style):

    global rist

    rist = []

    global comp_data, user_data

    canva_delete(bist, canvas)
    label_delete(cist)

    style.configure('Option_Buttons.TButton',
                    foreground = 'white',
                    background = '#3f3752',
                    borderwidth = 2,
                    relief = 'raised',
                    highlightcolor = '#dbd8e3',
                    bordercolor = '#dbd8e3',
                    font = ('Montserrat', 10))

    Quit_button = ttk.Button(canvas,
                             text = 'Quit',
                             command = lambda : Data_Showing(window, canvas, cist, bist, style),
                             style = 'Option_Buttons.TButton',
                             width = 7)
    canvas.create_window(600,400,
                         anchor="center",
                         window=Quit_button)

    Option = canvas.create_text(260,100,
                                text = "Choose",
                                fill = "black",
                                font = ('Montserrat',18,'bold'))

    Rock_button = ttk.Button(canvas,
                             text = 'Rock',
                             command = lambda : Rock(window, canvas, Comp_Point, User_Point),
                             style = 'Buttons.TButton',
                             width = 7)
    canvas.create_window(160,160,
                         anchor = 'center',
                         window = Rock_button)

    Paper_button = ttk.Button(canvas,
                              text = "Paper",
                              command = lambda : Paper(window, canvas, Comp_Point, User_Point),
                              style = "Buttons.TButton",
                              width = 7)
    canvas.create_window(260,160,
                         anchor = 'center',
                         window = Paper_button)

    Scissor_button = ttk.Button(canvas,
                                text = "Scissor",
                                command = lambda : Scissor(window, canvas, Comp_Point, User_Point),
                                style = "Buttons.TButton",
                                width = 7)
    canvas.create_window(360,160,
                         anchor = 'center',
                         window = Scissor_button)

    Comp_Point = canvas.create_text(600,50,
                                   text="Computer : %s" %(comp_data),
                                   fill="#403a2b",
                                   font=('Montserrat',13,'bold'))

    User_Point = canvas.create_text(624,70,
                                   text="You : %s" %(user_data),
                                   fill="#403a2b",
                                   font=('Montserrat',13,'bold'))

    You = canvas.create_text(80,230,
                             text="You Chose:",
                             fill="black",
                             font=('Montserrat',12,'bold'))

    Comp = canvas.create_text(400,230,
                             text="Computer Chose:",
                             fill="black",
                             font=('Montserrat',12,'bold'))

    cist = [Quit_button, Rock_button, Paper_button, Scissor_button]
    bist = [Option, Comp_Point, User_Point, You, Comp]

def Rock(window, canvas, Comp_Point, User_Point):

    global rist
    global comp_data, user_data

    canva_delete(rist, canvas)
    
    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)    
 
    if choice == 3:
        user_data += 1
        subject = PhotoImage(file="image/CHOSE/ROCK_B.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/SCISSOR_S.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something


    elif choice == 2:
        comp_data += 1
        subject = PhotoImage(file="image/CHOSE/ROCK_S.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/PAPER_B.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something
        
    else:
        subject = PhotoImage(file="image/CHOSE/ROCK_B.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/ROCK_B.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something

    canvas.itemconfig(Comp_Point, text="Computer : %s" % comp_data)
    canvas.itemconfig(User_Point, text="You : %s" % user_data)

    rist = [useless_comp, useless_user] 



    print('rock')

def Paper(window, canvas, Comp_Point, User_Point):

    global rist
    global comp_data, user_data

    canva_delete(rist, canvas)
    
    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)    
 
    if choice == 1:
        user_data += 1
        subject = PhotoImage(file="image/CHOSE/PAPER_B.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/ROCK_S.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something

    elif choice == 3:
        comp_data += 1
        subject = PhotoImage(file="image/CHOSE/PAPER_S.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/SCISSOR_B.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something
        
    else:
        subject = PhotoImage(file="image/CHOSE/PAPER_B.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/PAPER_B.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something

    canvas.itemconfig(Comp_Point, text="Computer : %s" % comp_data)
    canvas.itemconfig(User_Point, text="You : %s" % user_data)

    rist = [useless_comp, useless_user]

    print('rock')

def Scissor(window, canvas, Comp_Point, User_Point):

    global rist
    global comp_data, user_data

    canva_delete(rist, canvas)
    
    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)    
 
    if choice == 2:
        user_data += 1
        subject = PhotoImage(file="image/CHOSE/SCISSOR_B.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/PAPER_S.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something

    elif choice == 1:
        comp_data += 1
        subject = PhotoImage(file="image/CHOSE/SCISSOR_S.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/ROCK_B.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something
        
    else:
        subject = PhotoImage(file="image/CHOSE/SCISSOR_B.png")
        useless_user = canvas.create_image(60, 
                                           310, 
                                           anchor="center", 
                                           image=subject)   
        canvas.image_subject = subject

        something = PhotoImage(file="image/CHOSE/SCISSOR_B.png")
        useless_comp = canvas.create_image(390, 
                                           310, 
                                           anchor="center", 
                                           image=something)
        canvas.image = something

    canvas.itemconfig(Comp_Point, text="Computer : %s" % comp_data)
    canvas.itemconfig(User_Point, text="You : %s" % user_data)

    rist = [useless_comp, useless_user] 

    print('Scissor')

def Data_Showing(window, canvas, cist, bist, style):

    canva_delete(bist,canvas)
    canva_delete(rist,canvas)
    label_delete(cist)

    bg_image = PhotoImage(file="image/end.png")
    balls = canvas.create_image(-3, 
                                -3, 
                                anchor="nw", 
                                image=bg_image)
    canvas.background = bg_image

    comp=str(comp_data)
    user=str(user_data)
    password = password_entered

    try:
        with open(name,"w") as file:
            pass
        with open(name,"w") as file:
            file.write(password+'\n')
            file.write(comp+"\n")
            file.write(user+"\n")
    except Exception as e:
        print("error while storing data : ",e)

    user_point = canvas.create_text(350,100,
                                    text ='Your points : %s' %(user_data),
                                    fill = "black",
                                    font = ('Montserrat',13,'bold'))
    
    comp_point = canvas.create_text(350,150,
                                    text='Computer points : %s' %(comp_data),
                                    fill = "black",
                                    font = ('Montserrat',13,'bold'))
    
    done = ttk.Button(canvas, 
                      text='Done', 
                      command= lambda : end(window,canvas), 
                      style='Buttons.TButton',
                      width = 6)
    canvas.create_window(450,200,
                         anchor = 'center',
                         window = done)

    go_back = ttk.Button(canvas, 
                         text='Return', 
                         command= lambda : RPS(window, canvas, cist, bist, style),
                         style='Buttons.TButton',
                         width = 6)
    canvas.create_window(200,200,
                         anchor = 'center',
                         window = go_back)

    bist = [user_point,comp_point,balls]
    cist = [go_back,done]

def Old_user(window,canvas,cist,style,bist):

    canva_delete(bist, canvas)
    label_delete(cist)

    big_image = PhotoImage(file="image/CHOSE/ROCK_B.png")
    useless = canvas.create_image(150, 
                        350, 
                        anchor="nw", 
                        image=big_image)

    canvas.image = big_image

    intro = canvas.create_text(350,100,
                       text="Good to have You back",
                       fill="black",
                       font=('Montserrat',15,'bold'))

    head = canvas.create_text(350,150,
                              text="Please enter the following data",
                              fill="black",
                              font=('Montserrat',13))

    name_entry = ttk.Entry(window, 
                           style='Entry.TEntry')
    canvas.create_window(350, 200, 
                         anchor="center", 
                         window=name_entry)

    password_entry = ttk.Entry(window, 
                               style='Entry.TEntry')
    canvas.create_window(350, 250, 
                         anchor="center", 
                         window=password_entry)

    name = canvas.create_text(235,200,
                              text="Username",
                              fill="black",
                              font=('Montserrat',13))

    password = canvas.create_text(235,250,
                              text="Password",
                              fill="black",
                              font=('Montserrat',13))

    submit = ttk.Button(canvas, 
                        text='Submit',
                        command=lambda: file_data_accessing(window, 
                                                            canvas, 
                                                            name_entry, 
                                                            cist, 
                                                            bist, 
                                                            password_entry, 
                                                            style), 
                        style='Buttons.TButton',
                        width=7)
    canvas.create_window(400, 300, 
                         anchor="center", 
                         window=submit)

    cist = [password_entry, name_entry, submit]
    bist = [intro, head,  name,  password, useless]

def new_user(window,canvas,cist,style,bist):
    canva_delete(bist, canvas)
    label_delete(cist)

    big_image = PhotoImage(file="image/CHOSE/ROCK_S.png")
    useless = canvas.create_image(150, 
                        350, 
                        anchor="nw", 
                        image=big_image)

    canvas.image = big_image

    intro = canvas.create_text(350,100,
                       text="Good to have You",
                       fill="black",
                       font=('Montserrat',15,'bold'))

    head = canvas.create_text(350,150,
                              text="Please enter the following data",
                              fill="black",
                              font=('Montserrat',13))

    name_entry = ttk.Entry(window, 
                           style='Entry.TEntry')
    canvas.create_window(350, 200, 
                         anchor="center", 
                         window=name_entry)

    password_entry = ttk.Entry(window, 
                               style='Entry.TEntry')
    canvas.create_window(350, 250, 
                         anchor="center", 
                         window=password_entry)

    name = canvas.create_text(235,200,
                              text="Username",
                              fill="black",
                              font=('Montserrat',13))

    password = canvas.create_text(235,250,
                              text="Password",
                              fill="black",
                              font=('Montserrat',13))

    submit = ttk.Button(canvas, 
                        text='Submit',
                        command=lambda: new_user_actions(window, canvas, cist, bist, style, name_entry, password_entry), 
                        style='Buttons.TButton',
                        width=7)
    canvas.create_window(400, 300, 
                         anchor="center", 
                         window=submit)

    cist = [password_entry, name_entry, submit]
    bist = [intro, head,  name,  password, useless]

def func(window,canvas):
    # Add text directly to the Canvas with a transparent background

    style = ttk.Style()

    style.configure('Buttons.TButton',
                     foreground='white',
                     background='#00eadc',
                     borderwidth=2,
                     relief='raised',
                     highlightcolor='#31572c',
                     bordercolor='#dbd8e3',
                     font=('Montserrat', 13))

    style.configure('Entry.TEntry',
                    foreground = 'White',
                    background = '#79c2d0',
                    font = ('Montserrat', 13))

    image = PhotoImage(file="image/CHOSE/PAPER_B.png")
    useless = canvas.create_image(189, 
                                  158, 
                                  anchor="nw", 
                                  image=image)

    canvas.image = image

    intro = canvas.create_text(350, 100, 
                               text="Welcome to Rock, Paper and Scissors", 
                               fill="black", 
                               font=('Montserrat', 15, 'bold'))
    
    ask = canvas.create_text(350, 200, 
                             text="Are you an old user?", 
                             fill="black", 
                             font=('Montserrat', 13))

    

    # You can place buttons directly on the canvas using 'window'
    yes_button = ttk.Button(canvas, 
                            text='Yes',
                            command=lambda: Old_user(window,canvas,cist,style,bist), 
                            style='Buttons.TButton',
                            width=10)
    canvas.create_window(250, 300, 
                         anchor="center", 
                         window=yes_button)

    no_button = ttk.Button(canvas, 
                           text='No',
                           command=lambda: new_user(window,canvas,cist,style,bist), 
                           style='Buttons.TButton',
                           width=10)
    canvas.create_window(450, 300, 
                         anchor="center", 
                         window=no_button)

    cist = [no_button ,yes_button]
    bist = [intro ,ask ,useless]

def welcome():

    window = ttk.Window(themename="darkly")
    window.title("Rock Paper Scissors")
    window.geometry('700x500') 
    window.resizable(False,False)

    canvas = Canvas(window,
                    width=700, 
                    height=500)
    canvas.place(x=0, 
                 y=0, 
                 relwidth=1.5, 
                 relheight=1.5)

    bg_image = PhotoImage(file="image/START.png")
    canvas.create_image(-3, 
                        -3, 
                        anchor="nw", 
                        image=bg_image)

    func(window,canvas)
    
    window.mainloop()

welcome()
