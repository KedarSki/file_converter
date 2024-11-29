from tkinter import *
from tkinter import filedialog
from docx2pdf import convert
from pdf2docx import parse
import pathlib


class FileConverterApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Docx - PDF Converter")
        self.window.geometry("600x200")
        self.window.config(background="#2b2a2a")

        icon_path = pathlib.Path("assets", "logo.png")
        try:
            self.icon = PhotoImage(file=icon_path)
            self.window.iconphoto(True, self.icon)
        except Exception:
            print("Icon file not found. Skipping icon setup.")

        self.input_file = None
        self.filename = None

        self.setup_ui()

    def setup_ui(self):

        label = Label(
            self.window,
            text="Input file",
            font=("Arial", 12, "bold"),
            fg="#029bfa",
            bg="#2b2a2a",
        )
        label.place(x=230, y=20)

        self.input_file = Entry(self.window, width=40)
        self.input_file.place(x=80, y=60, height=30)

        browse_button = Button(
            self.window,
            text="Browse Files",
            command=self.file_browser,
            font=("Arial", 10, "bold"),
            bg="#029bfa",
            fg="white",
            width=12,
        )
        browse_button.place(x=400, y=60, height=30)

        convert_button = Button(
            self.window,
            text="Convert",
            command=self.file_convert,
            font=("Arial", 10, "bold"),
            bg="#029bfa",
            fg="white",
            width=12,
        )
        convert_button.place(x=240, y=110, height=30)

    def file_browser(self):
        self.filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select a file",
            filetypes=(("All files", "*.*"), ("Word files", "*.docx*"), ("Pdf files", "*.pdf*"), ("Text files", "*.txt*")))
        if self.filename:
            self.input_file.delete(0, END)
            self.input_file.insert(0, self.filename)

    def file_convert(self):
        if not self.filename:
            self.input_file.delete(0, END)
            self.input_file.insert(0, "PLEASE SELECT THE FILE!")
            return
        if self.filename.endswith(".docx"):
            convert(
                self.filename, self.filename.endswith(".pdf"))
        elif self.filename.endswith(".pdf"):
            parse(self.filename, self.filename.endswith(".docx"))
        elif self.filename.endswith(".txt"):
            convert(
                self.filename, self.filename.endswith(".pdf"))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = FileConverterApp()
    app.run()