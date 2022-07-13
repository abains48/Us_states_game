import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")



name=turtle.Turtle()

name.ht()
name.penup()

us_data_file = pandas.read_csv("50_states.csv")
us_state_name=us_data_file["state"]

game_on = True

states_revealed=0
guessed_states=[]
unguessed=[]

while game_on:
    guessed_answer = screen.textinput(title=f"{states_revealed}/50 Correct",prompt="What state do you guess?")
    guessed_answer = guessed_answer.title()
    if guessed_answer=="Exit":
        break
    for x in us_state_name:
        if x == guessed_answer:
            states_revealed+=1
            guessed_states.append(guessed_answer)
            guessed_state = us_data_file[us_data_file.state == x]
            x_cor = int(guessed_state.x)
            y_cor = int(guessed_state.y)
            name.goto(x_cor,y_cor)
            name.write(arg=f"{guessed_answer}",align="center",font=('Arial', 8, 'normal'))
        if states_revealed == 50:
            game_on = False

if states_revealed < 50:
    for x in us_state_name:
        if x not in guessed_states:
            new_state = us_data_file[us_data_file.state == x]
            new_x=int(new_state.x)
            new_y=int(new_state.y)
            name.goto(new_x,new_y)
            name.write(arg=f"{x}", align="center", font=('Arial', 8, 'normal'))



screen.exitonclick()