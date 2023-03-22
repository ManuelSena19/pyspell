from tkinter import *
from textblob import Word

root = Tk()
root.title("PySpell")
root.geometry("900x500")
root.config(background="#000080")


def check_spelling():
    word = enter_text.get()
    suggestions = Word(word).spellcheck()
    correct_words = [suggestion[0] for suggestion in suggestions][:4]
    if correct_words:
        right = ", ".join(correct_words)
    else:
        right = "No corrections could be found"

    cs = Label(root, text="Possible spellings: ", font=("Times New Roman", 20), bg="#000080", fg="#ff960b")
    cs.place(x=130, y=300)
    spell.config(text=right)


heading = Label(root, text="PySpell Spelling Checker", font=("Times New Roman", 30, "bold"), bg="#000080", fg="#ff960b")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("arial", 25), bg="white", border=2)
enter_text.pack(pady=(50, 20))
enter_text.focus()

button = Button(root, text="Check", font=("Times New Roman", 20, "bold"), fg="white", bg="#ff960b",
                command=check_spelling)
button.pack()

spell = Label(root, font=("Times New Roman", 20), bg="#000080", fg="#ff960b")
spell.place(x=350, y=300)

root.mainloop()
