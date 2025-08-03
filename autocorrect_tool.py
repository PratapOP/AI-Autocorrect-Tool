from tkinter import *
from textblob import TextBlob
from tkinter import filedialog

def autocorrect():
    input_text = input_entry.get("1.0", END)
    corrected_text = str(TextBlob(input_text).correct())
    output_entry.delete("1.0", END)
    output_entry.insert(END, corrected_text)
    input_word_count.set(f"Word count: {len(input_text.split())}")
    output_word_count.set(f"Word count: {len(corrected_text.split())}")

def clear_text():
    input_entry.delete("1.0", END)
    output_entry.delete("1.0", END)
    input_word_count.set("Word count: 0")
    output_word_count.set("Word count: 0")

def save_text():
    corrected_text = output_entry.get("1.0", END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(corrected_text)

def toggle_case():
    global preserve_case
    preserve_case = not preserve_case
    autocorrect()

def autocorrect_with_case():
    input_text = input_entry.get("1.0", END)
    blob = TextBlob(input_text)
    corrected_text = str(blob.correct() if preserve_case else blob.correct().lower())
    output_entry.delete("1.0", END)
    output_entry.insert(END, corrected_text)
    input_word_count.set(f"Word count: {len(input_text.split())}")
    output_word_count.set(f"Word count: {len(corrected_text.split())}")

# Initial state
preserve_case = True

window = Tk()
window.title("AI-Driven Autocorrect Tool")
window.geometry("600x400")
window.config(bg="lightblue")

Label(window, text="Autocorrect Tool", font=("Helvetica", 20, "bold"), bg="lightblue").pack(pady=10)
Label(window, text="Enter text:", font=("Arial", 12), bg="lightblue").pack()
input_entry = Text(window, height=6, width=70, font=("Arial", 12))
input_entry.pack(pady=5)

Button(window, text="Autocorrect", font=("Arial", 12, "bold"), command=autocorrect_with_case).pack(pady=10)

Label(window, text="Corrected text:", font=("Arial", 12), bg="lightblue").pack()
output_entry = Text(window, height=6, width=70, font=("Arial", 12))
output_entry.pack(pady=5)

Button(window, text="Clear", font=("Arial", 12, "bold"), command=clear_text).pack(pady=10)
Button(window, text="Save", font=("Arial", 12, "bold"), command=save_text).pack(pady=10)

input_word_count = StringVar()
input_word_count.set("Word count: 0")
Label(window, textvariable=input_word_count, font=("Arial", 12), bg="lightblue").pack()
output_word_count = StringVar()
output_word_count.set("Word count: 0")
Label(window, textvariable=output_word_count, font=("Arial", 12), bg="lightblue").pack()

case_var = BooleanVar()
case_var.set(True)
Checkbutton(window, text="Preserve Case", variable=case_var, command=toggle_case, bg="lightblue").pack()

window.mainloop()