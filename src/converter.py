from tkinter import *
import pathlib
from tkinter import filedialog

window = Tk()

icon_path = pathlib.Path("assets", "logo.png")
icon = PhotoImage(file=icon_path)

def file_browser():
    filename = filedialog.askopenfilename(initialdir="/", 
                                          title="Select a file",
                                          filetypes=(("Word files",
                                          "*.docx*"),
                                          ("Pdf files",
                                          "*.pdf*")))
    

window.title("Docx - PDF Converter")
window.geometry("1000x400")
window.iconphoto(True, icon)
window.config(background="#2b2a2a")
label = Label(window, text="input file", font=("Arial",12,"bold"),fg="#029bfa", bg="#2b2a2a")
label.place(x=500, y=40)
button_explore = Button(window, 
                        text = "Browse Files",
                        command = file_browser) 
button_explore.place(x=750, y=60)
input_file = Entry(width=50)
input_file.place(x=400, y=60)



window.mainloop()

