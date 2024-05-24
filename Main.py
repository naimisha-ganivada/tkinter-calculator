from tkinter import *
evaluated_expression = ""
def press(button):
     global evaluated_expression
     evaluated_expression+=str(button)
     expression.set(evaluated_expression)
def clear():
    global evaluated_expression
    evaluated_expression = "" 
    expression.set("")
def evaluate():
    global evaluated_expression
    try:
        result = str(eval(evaluated_expression))
        expression.set(result)
        evaluated_expression = ""
    except:
        expression.set("SYNTAX ERROR !!")
        evaluated_expression = ""
if __name__ == '__main__':
    frame = Tk()
    frame.geometry('500x500')
    frame.title("CALCULATOR")
    frame.configure(background='cadetblue1')
    expression = StringVar()
    text_entry = Entry(frame,textvariable=expression)
    text_entry.grid(columnspan=25,ipadx=500,ipady=40)
    one_button = Button(frame, text='1',fg='white',bg='black',command=lambda :press(1),height=3,width=12)
    one_button.grid(row=2,column=0)
    second_button = Button(frame , text='2',fg = 'white',bg='black',command=lambda : press(2),height=3,width = 12)
    second_button.grid(row = 2, column=1)
    third_button = Button(frame , text = '3', fg = 'white',bg = 'black',command=lambda : press(3),height = 3, width=12)
    third_button.grid(row = 2 , column= 2)
    fourth_button = Button(frame , text = '4',fg = 'white',bg = 'black',command=lambda : press(4),height = 3, width=12,)
    fourth_button.grid(row= 4 ,column=0)
    fifth_button = Button(frame ,text = '5',fg = 'white', bg = 'black',command = lambda : press(5),height = 3, width= 12)
    fifth_button.grid(row = 4 , column = 1)
    sixth_Button = Button(frame , text = '6' , fg = 'white',bg = 'black' , command = lambda : press(6), height = 3 , width = 12)
    sixth_Button.grid(row = 4 , column= 2)
    seventh_button = Button(frame,text='7',fg = 'white' , bg = 'black' , command=lambda : press(7) , height = 3 , width = 12 )
    seventh_button.grid(row = 5 , column= 0)
    eight_button = Button(frame, text = '8' ,fg = 'white' , bg = 'black' , command= lambda : press(8) , height = 3 , width = 12)
    eight_button.grid(row = 5, column = 1)
    nine_button = Button(frame , text= '9' , fg = 'white' , bg = 'black', command=lambda :press(9) , height = 3 , width= 12 )
    nine_button.grid(row =5 , column=2)
    zero_button = Button(frame , text = '0' , fg = 'white' , bg = 'black', command= lambda : press(0) , height = 3 , width= 12)
    zero_button.grid(row = 6 , column= 0)
    plus_button = Button(frame , text='+' , fg = 'white' , bg = 'black' , command= lambda :  press('+')  , height = 3 , width = 12)
    plus_button.grid(row = 6 , column = 1)
    minus_button = Button(frame , text= '-' , fg = 'white' , bg = 'black' , command= lambda : press('-') , height = 3 , width = 12)
    minus_button.grid(row = 6 ,column= 2 )
    division_button = Button(frame , text = '/' , fg = 'white' , bg = 'black' , command = lambda : press('/') , height= 3 , width = 12)
    division_button.grid(row = 2 , column= 3)
    multiply_button = Button(frame , text = '*' , fg = 'white' , bg = 'black' , command= lambda : press('*') , height = 3  , width = 12)
    multiply_button.grid(row = 4 , column= 3)
    decimal_button = Button(frame , text='( . )',command = lambda : press('.') , fg = 'white' , bg = 'black' , height= 3 , width=12)
    decimal_button.grid(row = 5 , column= 3)
    equal_button = Button(frame , text='=', command= lambda :evaluate() , fg = 'white' , bg = 'black' , height= 3 , width= 12)
    equal_button.grid(row = 6 , column= 3)
    clear_button = Button(frame , text='CLEAR' , command= lambda : clear() , fg = 'white' , bg = 'black' , height= 3, width= 12)
    clear_button.grid(row = 7 , column = 0)
    frame.mainloop()
