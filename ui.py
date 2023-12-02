THEME_COLOR = "#375362"
from tkinter import *
text_font=('Arial',20,'italic')
class Quizeinterface:
    def __init__(self):
        self.window=Tk()
        self.window.title("quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_Label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_Label.grid(row=0,column=2)

        self.canvas=Canvas(bg="white",height=250,width=300)
        self.question_text=self.canvas.create_text(150,125,text="Question text", fill="black",font=text_font)
        self.canvas.grid(row=0,column=0,columnspan=2,pady=50)

        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0)
        self.true_button.grid(row=2,column=0)

        false_image=PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_image,highlightthickness=0)
        self.false_button.grid(row=2,column=1)


        self.window.mainloop()

