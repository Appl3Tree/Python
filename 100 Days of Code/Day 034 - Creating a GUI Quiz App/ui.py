from tkinter import *
from sys import argv
from quiz_brain import QuizBrain
from data import question_data

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title(f'Quizzler - {question_data[0]["category"]}')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f'Score: 0/10', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightbackground=THEME_COLOR)
        self.question_text = self.canvas.create_text(150, 125, text='Some Question Text', fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'), width=290)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file=f'{argv[0][:-7]}images/true.png')
        self.true = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row=2)

        false_image = PhotoImage(file=f'{argv[0][:-7]}images/false.png')
        self.false = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        # Keep at the end
        self.window.mainloop()

    def get_next_question(self):
        if self.canvas['bg'] != 'white':
            self.canvas['bg'] = 'white'
        self.score_label['text'] = f'Score: {self.quiz.score}/10'
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))
        # if self.quiz.still_has_questions():
        #     self.get_next_question()
        # else:
        #     self.canvas.itemconfig(self.question_text, text='No more questions!')

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('false'))
        # if self.quiz.still_has_questions():
        #     self.get_next_question()
        # else:
        #     self.canvas.itemconfig(self.question_text, text='No more questions!')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas['bg'] = 'green'
            if self.quiz.still_has_questions():
                self.window.after(1000, self.get_next_question)
            else:
                self.window.after(1000, self.reset_canvas_color)
        else:
            self.canvas['bg'] = 'red'
            if self.quiz.still_has_questions():
                self.window.after(1000, self.get_next_question)
            else:
                self.window.after(1000, self.reset_canvas_color)

    def reset_canvas_color(self):
        self.canvas['bg'] = 'white'
        self.canvas.itemconfig(self.question_text, text='No more questions!')
