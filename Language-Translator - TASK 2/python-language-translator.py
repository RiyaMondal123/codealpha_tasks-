from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# ================= ROOT WINDOW =================
root = Tk()
root.geometry("1100x500")
root.title("Modern Language Translator")
root.resizable(False, False)
root.configure(bg="#1e1e2f")   # Dark background

# ================= STYLE =================
style = ttk.Style()
style.theme_use("clam")

style.configure("TCombobox",
                fieldbackground="#2c2c3e",
                background="#2c2c3e",
                foreground="white")

# ================= HEADING =================
heading = Label(root,
                text="🌍 LANGUAGE TRANSLATOR",
                font=("Segoe UI", 24, "bold"),
                bg="#1e1e2f",
                fg="#00f5ff")
heading.pack(pady=15)

sub_heading = Label(root,
                    text="Python 3.13 Compatible Version",
                    font=("Segoe UI", 11),
                    bg="#1e1e2f",
                    fg="#bbbbbb")
sub_heading.pack(side=BOTTOM, pady=10)

# ================= INPUT LABEL =================
Label(root,
      text="Enter Text",
      font=("Segoe UI", 12, "bold"),
      bg="#1e1e2f",
      fg="#ffffff").place(x=200, y=80)

# ================= INPUT TEXT =================
Input_text = Text(root,
                  font=("Segoe UI", 11),
                  bg="#2c2c3e",
                  fg="white",
                  insertbackground="white",
                  relief=FLAT,
                  height=12,
                  width=55,
                  padx=10,
                  pady=10)
Input_text.place(x=40, y=120)

# ================= OUTPUT LABEL =================
Label(root,
      text="Translated Text",
      font=("Segoe UI", 12, "bold"),
      bg="#1e1e2f",
      fg="#ffffff").place(x=750, y=80)

# ================= OUTPUT TEXT =================
Output_text = Text(root,
                   font=("Segoe UI", 11),
                   bg="#2c2c3e",
                   fg="#00ffcc",
                   insertbackground="white",
                   relief=FLAT,
                   height=12,
                   width=55,
                   padx=10,
                   pady=10)
Output_text.place(x=600, y=120)

# ================= LANGUAGES =================
languages = [
    "english", "hindi", "bengali", "french",
    "german", "spanish", "urdu", "japanese",
    "chinese", "arabic"
]

src_lang = ttk.Combobox(root,
                        values=languages,
                        width=20,
                        font=("Segoe UI", 10))
src_lang.place(x=40, y=80)
src_lang.set("english")

dest_lang = ttk.Combobox(root,
                         values=languages,
                         width=20,
                         font=("Segoe UI", 10))
dest_lang.place(x=880, y=80)
dest_lang.set("hindi")

# ================= TRANSLATE FUNCTION =================
def Translate():
    try:
        text = Input_text.get(1.0, END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        translated = GoogleTranslator(
            source=src_lang.get(),
            target=dest_lang.get()
        ).translate(text)

        Output_text.delete(1.0, END)
        Output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed:\n{e}")

# ================= BUTTON =================
translate_btn = Button(root,
                       text="Translate",
                       font=("Segoe UI", 13, "bold"),
                       bg="#00f5ff",
                       fg="black",
                       activebackground="#00c8d7",
                       relief=FLAT,
                       padx=20,
                       pady=8,
                       command=Translate)
translate_btn.place(x=500, y=230)

root.mainloop()
