from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

def submit():
    global pattern, string, player1_turn, player2_turn, guess_window
    pattern = pattern_entry.get()
    string = string_entry.get()

    pattern_entry.config(state='disabled')
    string_entry.config(state='disabled')

    player1_turn = False
    player2_turn = True

    guess_window = tk.Toplevel(root)
    guess_window.title("Guess")
    guess_window.configure(bg='pink')

    # hide the main window
    root.withdraw()

    pattern_label = tk.Label(guess_window, text=f"Pattern: {pattern}", bg='pink', fg='black', font=('TimesNewRoman', 16))
    pattern_label.pack(pady=10)

    guess_label = tk.Label(guess_window, text="Guess:", bg='pink', fg='black', font=('TimesNewRoman', 16))
    guess_label.pack(pady=10)

    global guess_entry, check_button

    guess_entry = tk.Entry(guess_window, width=30, font=('TimesNewRoman', 16))
    guess_entry.pack(pady=10)

    check_button = tk.Button(guess_window, text="Check", command=check_guess, bg='blue', fg='white', font=('TimesNewRoman', 16))
    check_button.pack(pady=10)

def check_guess():
    global guesses, max_guesses, player2_turn
    guess = guess_entry.get()

    if guess == string:
        if player2_turn:
            messagebox.showinfo("Congratulations", "Player 2 wins!")
        else:
            messagebox.showinfo("Congratulations", "Player 1 wins!")
        reset_game()
    else:
        guesses += 1
        max_guesses = 3

        if guesses == max_guesses:
            messagebox.showinfo("Game Over", "No more guesses left. Starting new game.")
            reset_game()
        else:
            messagebox.showerror("Incorrect", "Incorrect guess. Please try again.")

def reset_game():
    global pattern, string, guesses, player1_turn, player2_turn
    pattern = ""
    string = ""
    guesses = 0

    pattern_entry.delete(0, 'end')
    string_entry.delete(0, 'end')
    guess_entry.delete(0, 'end')

    pattern_entry.config(state='normal')
    string_entry.config(state='normal')

    player1_turn = True
    player2_turn = False

    # destroy the guess window
    guess_window.destroy()

    # show the main window
    root.deiconify()

def welcome_window():
    global root, image, image_label
    root = tk.Tk()
    root.title("Welcome")
    root.geometry('300x200+500+200')
    root.configure(bg='pink')

    # Ensure the image path is correct
    try:
        image = ImageTk.PhotoImage(Image.open("C:\\Users\\91837\\Downloads\\pp1.jpeg"))
        image_label = tk.Label(root, image=image)
        image_label.image = image  # Keep a reference to the image
        image_label.pack(padx=30, pady=20)
    except Exception as e:
        print(f"Error loading image: {e}")
        image_label = tk.Label(root, text="Image not found", bg='pink', fg='black', font=('TimesNewRoman', 16))
        image_label.pack(padx=30, pady=20)

    welcome_label = tk.Label(root, text="Welcome to the Pattern and String Game!", bg='pink', fg='black', font=('TimesNewRoman', 16))
    welcome_label.pack(pady=20)

    start_button = tk.Button(root, text="Start", command=create_main_window, bg='blue', fg='white', font=('TimesNewRoman', 16))
    start_button.pack(pady=10)

    root.mainloop()

def create_main_window():
    global root, pattern, string, player1_turn, player2_turn, guesses, max_guesses, pattern_entry, string_entry, submit_button

    root.destroy()

    root = tk.Tk()
    root.title("Pattern and String")
    root.geometry('400x300+500+200')
    root.configure(bg='pink')
    pattern = ""
    string = ""
    player1_turn = True
    player2_turn = False

    guesses = 0
    max_guesses = 3

    pattern_label = tk.Label(root, text="Pattern:", bg='pink', font=('TimesNewRoman', 16))
    pattern_label.pack(pady=10)

    pattern_entry = tk.Entry(root, width=30, font=('TimesNewRoman', 16))
    pattern_entry.pack(pady=10)

    string_label = tk.Label(root, text="String:", bg='pink', font=('TimesNewRoman', 16))
    string_label.pack(pady=10)

    string_entry = tk.Entry(root, width=30, font=('TimesNewRoman', 16))
    string_entry.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", command=submit, bg='blue', fg='white', font=('TimesNewRoman', 16))
    submit_button.pack(pady=10)

welcome_window()
