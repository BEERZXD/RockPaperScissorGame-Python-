'''
Thanathorn Thepsumrung M.4/1 No.8
Surawittayakarn school
Simple Rock Paper Scissors Game!
'''

import tkinter as tk
import random
from tkinter import *
from PIL import Image, ImageTk

def checkResult(player1,player2):
    #Rock - 1
    #Paper - 2
    #Scissors - 3
    if(mode == "Single"):
        player1_detail = "(Player)"
        player2_detail = "(BOT)"
        player2 = random.randint(1,3)
    if(mode == "Multi"):
        player1_detail = "(Player1)"
        player2_detail = "(Player2)"
    if(player1 == player2):
        print("It's a Draw")
        showResult("It's a Draw")
    elif player1 == 1 and player2 == 2:
        print("Enemy WIN!")
        showResult(f"Enemy WIN!{player2_detail}")
    elif player1 == 1 and player2 == 3:
        print("You WIN!")
        showResult(f"You WIN!{player1_detail}")
    elif player1 == 2 and player2 == 1:
        print("You WIN!")
        showResult(f"You WIN!{player1_detail}")
    elif player1 == 2 and player2 == 3:
        print("Enemy WIN!")
        showResult(f"Enemy WIN!{player2_detail}")
    elif player1 == 3 and player2 == 1:
        print("Enemy WIN!")
        showResult(f"Enemy WIN!{player2_detail}")
    elif player1 == 3 and player2 == 2:
        print("You WIN!")
        showResult(f"You WIN!{player1_detail}")
    else:
        print("Error!")
        showResult("Error!")

def showResult(result):
    global result_label,restart_button,result_text
    instructions.grid_forget()
    rock.grid_forget()
    paper.grid_forget()
    scissors.grid_forget()
    result_text = tk.Label(app, text="The result is ...")
    result_text.config(font=(50))
    result_text.grid(columnspan=3, column=1, row=1)
    result_label = tk.Label(app, text=result)
    result_label.config(font=(80))
    result_label.grid(columnspan=3, column=1, row=2)
    restart_button = tk.Button(text='RESTART', height=2, width=15, bg="#20bebe", command=lambda:restart())
    restart_button.grid(columnspan=3, column=3, row=2)

def restart():
    logo_label.grid_forget()
    result_text.grid_forget()
    result_label.grid_forget()
    instructions.grid_forget()
    restart_button.grid_forget()
    canvas.grid_forget()
    main()

def choosemode():
    start_button.grid_forget()
    global single_button,multi_button,mode_text
    mode_text = tk.Label(app, text="Choose mode")
    mode_text.config(font=(40))
    mode_text.grid(column=2, row=2)
    single_button = tk.Button(text='Singleplayer', height=2, width=15, bg="#20bebe", command=lambda:singlemode())
    single_button.grid(column=1, row=2)
    multi_button = tk.Button(text='Multiplayer', height=2, width=15, bg="#20bebe", command=lambda:multimode())
    multi_button.grid(column=3, row=2)

def singlemode():
    mode_text.grid_forget()
    global rock,paper,scissors,instructions
    global mode
    mode = "Single"
    single_button.grid_forget()
    multi_button.grid_forget()
    game_name.grid_forget()
    instructions = tk.Label(app, text="Your turn")
    instructions.config(font=(50))
    instructions.grid(columnspan=3, column=1, row=1)
    rock = tk.Button(text='Rock', height=2, width=15, bg="#20bebe", command=lambda:checkResult(1,"player2"))
    rock.grid(column=1, row=2)
    paper = tk.Button(text='Paper', height=2, width=15, bg="#20bebe", command=lambda:checkResult(2,"player2"))
    paper.grid(column=2, row=2)
    scissors = tk.Button(text='Scissors', height=2, width=15, bg="#20bebe", command=lambda:checkResult(3,"player2"))
    scissors.grid(column=3, row=2)

def multimode():
    global mode
    mode = "Multi"
    single_button.grid_forget()
    multi_button.grid_forget()
    mode_text.grid_forget()
    game_name.grid_forget()
    p1choose()

def p1choose():
    global rock_p1,paper_p1,scissors_p1,instructions_p1
    instructions_p1 = tk.Label(app, text="Player 1 Turn")
    instructions_p1.config(font=(50))
    instructions_p1.grid(columnspan=3, column=1, row=1)
    rock_p1 = tk.Button(text='Rock', height=2, width=15, bg="#20bebe", command=lambda:[player1Multi(1), p2choose()])
    rock_p1.grid(column=1, row=2)
    paper_p1 = tk.Button(text='Paper', height=2, width=15, bg="#20bebe", command=lambda:[player1Multi(2), p2choose()])
    paper_p1.grid(column=2, row=2)
    scissors_p1 = tk.Button(text='Scissors', height=2, width=15, bg="#20bebe", command=lambda:[player1Multi(3), p2choose()])
    scissors_p1.grid(column=3, row=2)

def p2choose():
    global instructions,rock,paper,scissors
    rock_p1.grid_forget()
    paper_p1.grid_forget()
    scissors_p1.grid_forget()
    instructions_p1.grid_forget()
    instructions = tk.Label(app, text="Player 2 Turn")
    instructions.config(font=(50))
    instructions.grid(columnspan=3, column=1, row=1)
    rock = tk.Button(text='Rock', height=2, width=15, bg="#20bebe", command=lambda:player2Multi(1))
    rock.grid(column=1, row=2)
    paper = tk.Button(text='Paper', height=2, width=15, bg="#20bebe", command=lambda:player2Multi(2))
    paper.grid(column=2, row=2)
    scissors = tk.Button(text='Scissors', height=2, width=15, bg="#20bebe", command=lambda:player2Multi(3))
    scissors.grid(column=3, row=2)

def player1Multi(p1_input):
    global player1_input
    player1_input = p1_input

def player2Multi(p2_input):
    player2_input = p2_input
    checkResult(player1_input,player2_input)

app = tk.Tk()
app.title('Rock Paper Scissors Game By BEERZ')

def main():
    global start_button,logo_label,app,canvas,game_name
    canvas = tk.Canvas(app, width=600, height=300)
    canvas.grid(columnspan=5, rowspan=3)

    logo = Image.open('logo_start.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=2, row=0)

    game_name = tk.Label(app, text="Rock Paper Scissors Game")
    game_name.config(font=(50))
    game_name.grid(columnspan=3, column=1, row=1)

    start_button = tk.Button(text='START', height=2, width=15, bg="#20bebe", command=lambda:choosemode())
    start_button.grid(column=2, row=2)
    app.mainloop()
main()