THEME_COLOR = "#375362"
from tkinter import *
text_font=('Arial',20,'italic')
from quiz_brain import QuizBrain



class Quizeinterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_Label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_Label.grid(row=0,column=2)

        self.canvas=Canvas(bg="white",height=250,width=300)
        self.question_text=self.canvas.create_text(150,125,text="Question text",width=260, fill="black",font=text_font)
        self.canvas.grid(row=0,column=0,columnspan=2,pady=50)

        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_answer)
        self.true_button.grid(row=2,column=0)

        false_image=PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_image,highlightthickness=0,command=self.false_answer)
        self.false_button.grid(row=2,column=1)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_Label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"QUESTIN ARE FINISHED. YOUR FINAL SCORE IS {self.quiz.score}")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))


        # self.score_Label.config(text=s)

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self,isright):
        self.canvas.config(bg="white")
        if isright:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)





