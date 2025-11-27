import pandas as pd
import tkinter as tk
from tkinter import messagebox
import sys

# --- Dark Theme Color Palette ---
BG_DARK = '#1E1E1E'          # Very dark gray for main background
FG_LIGHT = 'white'           # White text (for main elements like Title, Question, Score)
FG_LIGHT_GRAY = '#CCCCCC'    # Light gray text (for the Subtitle)
BG_SECONDARY = '#3C3C3C'     # Slightly lighter gray for buttons/frames
FG_ACTIVE = '#555555'        # Color when a button is pressed
# --------------------------------

class PMPQuizApp:
    def __init__(self, master, filename):
        self.master = master
        master.title("PMP Agile Quiz (GUI)")

        # Set master background color
        master.config(bg=BG_DARK)

        # Quiz State Variables
        self.questions = self._load_questions(filename)
        self.current_q_index = 0
        self.score = 0
        self.total_questions = len(self.questions)

        # Set initial window size
        self.master.geometry("600x650")
        
        # --- UI Elements ---
        
        # 0. Header Frame (Top Left)
        header_frame = tk.Frame(master, bg=BG_DARK)
        header_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.NW, padx=15, pady=5)
        
        # Title: "📝200 PMP Questions (Agile)" 
        tk.Label(header_frame, 
                 text="📝200 PMP Questions (Agile)", 
                 font=('Calibri Light', 18, 'bold'),
                 bg=BG_DARK, fg=FG_LIGHT, 
                 anchor='w', justify=tk.LEFT).pack(fill=tk.X)

        # Subtitle: "✨ Created by: Sally Law 🌟" 
        tk.Label(header_frame, 
                 text="✨ Created by: Sally Law 🌟", 
                 font=('Calibri Light', 11),
                 bg=BG_DARK, fg=FG_LIGHT_GRAY, 
                 anchor='w', justify=tk.LEFT).pack(fill=tk.X)

        # --- SPACER LINE ---
        tk.Label(master, text="", bg=BG_DARK, height=1).pack(pady=5)
        # -------------------

        # 1. Score/Status Bar
        self.status_label = tk.Label(master, text="", font=('Helvetica', 12),
                                     bg=BG_DARK, fg=FG_LIGHT)
        self.status_label.pack(pady=5)

        # 2. Question Area
        self.question_label = tk.Label(master, text="Loading...", 
                                        justify=tk.LEFT,
                                        anchor='w', 
                                        font=('Calibri Light', 14, 'bold'),
                                        bg=BG_DARK, fg=FG_LIGHT,
                                        wraplength=550)
        self.question_label.pack(pady=10, padx=15, fill=tk.X)
        
        # 3. Answer Buttons Frame (MODIFIED TO FILL WIDTH)
        self.buttons_frame = tk.Frame(master, bg=BG_DARK)
        self.buttons_frame.pack(pady=10, fill=tk.X)
        self.buttons_frame.grid_columnconfigure(0, weight=1)

        # Create four buttons (A, B, C, D)
        self.answer_buttons = {}
        choices = ['A', 'B', 'C', 'D']
        for i, choice in enumerate(choices):
            btn = tk.Button(self.buttons_frame, text=f"{choice}) Option Text", 
                            # width removed to allow stretching
                            height=2, justify=tk.LEFT, anchor='w',
                            font=('Calibri Light', 13), 
                            wraplength=550, # Added wraplength for text wrapping
                            bg=BG_SECONDARY, fg=FG_LIGHT,
                            activebackground=FG_ACTIVE, activeforeground=FG_LIGHT,
                            command=lambda c=choice: self.check_answer(c))
            # sticky='ew' added to make button stretch horizontally
            btn.grid(row=i, column=0, pady=5, padx=10, sticky='ew') 
            self.answer_buttons[choice] = btn

        # 4. Footer Frame (Bottom Left)
        footer_frame = tk.Frame(master, bg=BG_DARK)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor=tk.SW, padx=15, pady=5)
        
        # Copyright
        tk.Label(footer_frame, 
                 text="Copyright © 2025 - 2026 by Sally Law ", 
                 font=('Helvetica', 10), 
                 bg=BG_DARK, fg=FG_LIGHT,
                 anchor='w', justify=tk.LEFT).pack(fill=tk.X)

        # All rights reserved. (Font size 7)
        tk.Label(footer_frame, 
                 text="All rights reserved. ", 
                 font=('Helvetica', 7),
                 bg=BG_DARK, fg=FG_LIGHT,
                 anchor='w', justify=tk.LEFT).pack(fill=tk.X)
        
        # Start the quiz
        self.display_question()


    def _load_questions(self, filename):
        """Loads and processes questions from the CSV file."""
        try:
            df = pd.read_csv(filename)
            df.columns = df.columns.str.strip()
            df = df.rename(columns={'Question': 'question', 'Selections (Options)': 'options', 'Answer': 'correct_answer', 'Explanation': 'explanation'})
            
            def parse_options(options_str):
                options = [opt.strip() for opt in options_str.split('.') if opt.strip()]
                if options and options[0].isdigit():
                    options = options[1:]
                
                labeled_options = {}
                labels = ['A', 'B', 'C', 'D']
                for i, text in enumerate(options[:4]):
                    labeled_options[labels[i]] = text.replace(f"{labels[i]})", "").strip() 
                return labeled_options

            df['parsed_options'] = df['options'].apply(parse_options)
            df['correct_answer'] = df['correct_answer'].str.strip().str.upper().str[0]
            
            return df.to_dict('records')

        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{filename}' was not found.")
            sys.exit(1)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the data: {e}")
            sys.exit(1)

    def display_question(self):
        """Updates the GUI with the current question and options."""
        if self.current_q_index >= self.total_questions:
            self.show_final_score()
            return

        q = self.questions[self.current_q_index]
        self.status_label.config(text=f"Question {self.current_q_index + 1} of {self.total_questions} | Score: {self.score}")
        self.question_label.config(text=q['question'])

        for choice, btn in self.answer_buttons.items():
            option_text = q['parsed_options'].get(choice, f"[Option {choice} Missing]")
            btn.config(text=f"{choice}) {option_text}", state=tk.NORMAL) 

    def check_answer(self, user_choice):
        """Checks the user's selected answer against the correct answer."""
        current_q = self.questions[self.current_q_index]
        correct_answer = current_q['correct_answer']
        is_correct = (user_choice == correct_answer)

        for btn in self.answer_buttons.values():
            btn.config(state=tk.DISABLED)

        if is_correct:
            self.score += 1
            self.status_label.config(text=f"Question {self.current_q_index + 1} of {self.total_questions} | Score: {self.score}")

        self.show_feedback_popup(is_correct, correct_answer, current_q['explanation'])

    def show_feedback_popup(self, is_correct, correct_answer, explanation):
        """Creates a Toplevel pop-up window to display feedback and explanation."""
        popup = tk.Toplevel(self.master, bg=BG_DARK)
        popup.title("Feedback & Explanation")
        popup.geometry("600x350")
        
        feedback_message = "🎉 CORRECT!" if is_correct else "❌ INCORRECT!"
        color = 'green' if is_correct else 'red'
        
        tk.Label(popup, text=feedback_message, fg=color, bg=BG_DARK, font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        tk.Label(popup, text=f"The correct answer was: {correct_answer}", 
                 font=('Helvetica', 12, 'italic'), bg=BG_DARK, fg=FG_LIGHT).pack(pady=5)

        tk.Label(popup, text="--- Explanation ---", font=('Helvetica', 12), bg=BG_DARK, fg=FG_LIGHT).pack()
        
        text_frame = tk.Frame(popup, bg=BG_DARK)
        text_frame.pack(pady=5, padx=10, fill='both', expand=True)

        text_widget = tk.Text(text_frame, wrap='word', height=8, font=('Helvetica', 10),
                              bg=BG_SECONDARY, fg=FG_LIGHT, insertbackground=FG_LIGHT)
        text_widget.insert('1.0', explanation)
        text_widget.config(state='disabled')
        text_widget.pack(side='left', fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
        scrollbar.pack(side='right', fill='y')
        text_widget.config(yscrollcommand=scrollbar.set)

        next_btn_text = "Finish Quiz" if self.current_q_index == self.total_questions - 1 else "Next Question >>"
        next_button = tk.Button(popup, text=next_btn_text, command=lambda: self._next_question(popup), 
                                bg=BG_SECONDARY, fg=FG_LIGHT,
                                activebackground=FG_ACTIVE, activeforeground=FG_LIGHT,
                                font=('Helvetica', 12, 'bold'))
        next_button.pack(pady=10)

        popup.transient(self.master)
        popup.grab_set()
        self.master.wait_window(popup)

    def _next_question(self, popup):
        """Closes the popup and advances to the next question."""
        popup.destroy()
        self.current_q_index += 1
        self.display_question()

    def show_final_score(self):
        """Shows the final results when the quiz is complete."""
        final_score = (self.score / self.total_questions) * 100
        messagebox.showinfo("Quiz Complete", 
                            f"Quiz Finished!\n"
                            f"You scored {self.score} out of {self.total_questions} questions correctly.\n"
                            f"Final Percentage: {final_score:.2f}%")
        self.master.destroy()

# --- Main Execution Block ---
if __name__ == "__main__":
    csv_file = '26_PMP_Questions.csv'

    root = tk.Tk()
    app = PMPQuizApp(root, csv_file)
    root.mainloop()