import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog
import sys
import random 

# --- Dark Theme Color Palette ---
BG_DARK = '#1E1E1E'          # Very dark gray for main background
FG_LIGHT = 'white'           # White text (for main elements like Title, Question, Score)
FG_LIGHT_GRAY = '#CCCCCC'    # Light gray text (for the Subtitle)
BG_SECONDARY = '#3C3C3C'     # Slightly lighter gray for buttons/frames
FG_ACTIVE = '#555555'        # Color when a button is pressed
# --------------------------------

class PMPQuizApp:
    def __init__(self, master, filename, randomize_questions=0):
        self.master = master
        master.title("PMP Agile Quiz (GUI)")

        # Set master background color
        master.config(bg=BG_DARK)

        # Quiz State Variables
        self.questions = self._load_questions(filename)
        self.current_q_index = 0
        self.score = 0
        self.total_questions = len(self.questions)

        # NEW: Randomization Logic
        if randomize_questions == 1:
            random.shuffle(self.questions)

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
        
        # 3. Answer Buttons Frame
        self.buttons_frame = tk.Frame(master, bg=BG_DARK)
        self.buttons_frame.pack(pady=10, fill=tk.X)
        self.buttons_frame.grid_columnconfigure(0, weight=1)

        # Create four buttons (A, B, C, D)
        self.answer_buttons = {}
        choices = ['A', 'B', 'C', 'D']
        for i, choice in enumerate(choices):
            btn = tk.Button(self.buttons_frame, text=f"{choice}) Option Text", 
                            height=2, justify=tk.LEFT, anchor='w',
                            font=('Calibri Light', 13), 
                            wraplength=550, 
                            bg=BG_SECONDARY, fg=FG_LIGHT,
                            activebackground=FG_ACTIVE, activeforeground=FG_LIGHT,
                            command=lambda c=choice: self.check_answer(c))
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
            # Check for default filename placeholder
            if ' - see attached for the original v.csv' in filename:
                filename = '26 PMP Questions.xlsx - see attached for the original v.csv'
                
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
            messagebox.showerror("Error", f"The file '{filename}' was not found. Please select a valid file.")
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


# =========================================================================
# START SCREEN IMPLEMENTATION (FIXED)
# =========================================================================

class QuizStartScreen:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Setup")
        master.geometry("400x280")
        master.config(bg=BG_DARK)
        
        # 1. Title
        tk.Label(master, text="Select PMP Question Set", 
                 font=('Calibri Light', 16, 'bold'), 
                 bg=BG_DARK, fg=FG_LIGHT).pack(pady=10)
        
        # 2. File Path Frame
        file_frame = tk.Frame(master, bg=BG_DARK)
        file_frame.pack(padx=10, fill=tk.X)
        
        self.file_entry = tk.Entry(file_frame, width=30, bg=BG_SECONDARY, fg=FG_LIGHT, insertbackground=FG_LIGHT)
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # 3. Browse Button
        browse_btn = tk.Button(file_frame, text="Browse...", command=self.open_file_dialog,
                               bg=BG_SECONDARY, fg=FG_LIGHT, activebackground=FG_ACTIVE)
        browse_btn.pack(side=tk.RIGHT)
        
        # Pre-populate with the last used file name
        self.file_entry.insert(0, '26 PMP Questions.xlsx - see attached for the original v.csv')

        # 4. Randomization Selection (Radio Buttons)
        tk.Label(master, text="Question Order:", 
                 font=('Calibri Light', 12), bg=BG_DARK, fg=FG_LIGHT).pack(pady=(15, 5))
        
        self.random_var = tk.IntVar(value=0) # 0: In Order (Default), 1: Randomize
        
        radio_frame = tk.Frame(master, bg=BG_DARK)
        radio_frame.pack()
        
        # Radio Button 1: Display in Order
        tk.Radiobutton(radio_frame, text="Display in Order", variable=self.random_var, value=0,
                       font=('Calibri Light', 11), bg=BG_DARK, fg=FG_LIGHT, 
                       activebackground=BG_DARK, activeforeground=FG_LIGHT,
                       indicatoron=0, padx=10, pady=5, width=15, 
                       selectcolor=BG_SECONDARY).pack(side=tk.LEFT, padx=5) # Corrected: Removed duplicate selectcolor
        
        # Radio Button 2: Randomize Questions
        tk.Radiobutton(radio_frame, text="Randomize Questions", variable=self.random_var, value=1,
                       font=('Calibri Light', 11), bg=BG_DARK, fg=FG_LIGHT, 
                       activebackground=BG_DARK, activeforeground=FG_LIGHT,
                       indicatoron=0, padx=10, pady=5, width=18,
                       selectcolor=BG_SECONDARY).pack(side=tk.LEFT, padx=5) # Corrected: Removed duplicate selectcolor

        # 5. Start Button
        start_btn = tk.Button(master, text="Start Quiz", command=self.start_quiz,
                              font=('Calibri Light', 12, 'bold'),
                              bg='green', fg=FG_LIGHT, activebackground='dark green')
        start_btn.pack(pady=20)

    def open_file_dialog(self):
        """Opens the file dialog to select a CSV file."""
        filename = filedialog.askopenfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")]
        )
        if filename:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)

    def start_quiz(self):
        """Validates the file path and launches the main quiz application."""
        filepath = self.file_entry.get().strip()
        random_pref = self.random_var.get()

        if not filepath:
            messagebox.showerror("Error", "Please select a file to begin.")
            return
        
        # Destroy the start screen
        self.master.destroy()
        
        # Launch the main quiz app, passing the file path and randomization preference
        root = tk.Tk()
        app = PMPQuizApp(root, filepath, random_pref)
        root.mainloop()

# --- Main Execution Block ---
if __name__ == "__main__":
    # Start the application with the setup screen
    start_root = tk.Tk()
    app = QuizStartScreen(start_root)
    start_root.mainloop()