from tkinter import *


class App:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg="#D8D9DA", padx=100, pady=50)
        self.root.title("Text Disappearing App")

        self.title_label = Label(text="Start Writing Text", fg="#96C291", font=("Comic sans", 50, "bold"), bg="#D8D9DA")
        self.title_label.grid(column=1, row=0)
        self.title_label = Label(
            text="After you started writing, if you stopped the writing\n for few seconds, the text will disappear.",
            font=("Comic sans", 20, "normal"), bg="#D8D9DA")
        self.title_label.grid(column=1, row=1)

        self.delay = 5000
        self.after_id = None

        self.text = Text(self.root)
        self.text.insert(END, "Type here...")

        self.text.bind("<Key>", self.clear_text)
        self.text.grid(column=1, row=2, pady=30)

        self.root.mainloop()

    def clear_text(self, event=None):
        if not event:
            self.text.delete("1.0", "end")

        else:
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None

            self.after_id = self.root.after(self.delay, self.clear_text)


app = App()
