from tkinter import *
import pathlib
from tkinter import filedialog

window = Tk()

icon_path = pathlib.Path("assets", "logo.png")
icon = PhotoImage(file=icon_path)


def file_browser():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a file",
        filetypes=(("Word files", "*.docx*"), ("Pdf files", "*.pdf*")),
    )
    input_file.delete(0, END)
    input_file.insert(0, filename)


window.title("Docx - PDF Converter")
window.geometry("600x400")
window.iconphoto(True, icon)
window.config(background="#2b2a2a")

# Label
label = Label(
    window, text="Input file", font=("Arial", 12, "bold"), fg="#029bfa", bg="#2b2a2a"
)
label.place(x=190, y=40)

# Pole tekstowe
input_file = Entry(window, width=40)
input_file.place(x=80, y=70, height=30)

# Przycisk "Browse Files"
button_explore = Button(
    window,
    text="Browse Files",
    command=file_browser,
    font=("Arial", 10, "bold"),
    bg="#029bfa",
    fg="white",
    width=12,
)
button_explore.place(x=350, y=70, height=30)

# Przycisk "Convert"
button_convert = Button(
    window,
    text="Convert",
    font=("Arial", 10, "bold"),
    bg="#029bfa",
    fg="white",
    width=12,
)
button_convert.place(x=180, y=120, height=30)

window.mainloop()
