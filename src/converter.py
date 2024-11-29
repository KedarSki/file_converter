from tkinter import *
from tkinter import filedialog, ttk
from docx2pdf import convert
from pdf2docx import Converter
import threading
import pathlib


class FileConverterApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("File Format Converter")
        self.window.geometry("800x600")
        self.window.config(background="#2b2a2a")

        icon_path = pathlib.Path("assets", "logo.png")
        try:
            self.icon = PhotoImage(file=icon_path)
            self.window.iconphoto(True, self.icon)
        except Exception:
            print("Icon file not found. Skipping icon setup.")

        self.filename = None
        self.processing_label = None
        self.setup_ui()

    def setup_ui(self):
        label_header = Label(
            self.window,
            text="File Format Converter",
            font=("Arial", 14, "bold"),
            fg="#00d4ff",
            bg="#2b2a2a",
        )
        label_header.place(x=200, y=10)

        label_input = Label(
            self.window,
            text="Select a file to convert:",
            font=("Arial", 10),
            fg="white",
            bg="#2b2a2a",
        )
        label_input.place(x=30, y=60)

        self.input_file = Entry(self.window, width=40)
        self.input_file.place(x=180, y=60, height=25)

        browse_button = Button(
            self.window,
            text="Browse Files",
            command=self.file_browser,
            font=("Arial", 10),
            bg="#00d4ff",
            fg="white",
            width=12,
        )
        browse_button.place(x=450, y=60, height=25)

        self.from_format = StringVar(value="DOCX")
        from_label = Label(
            self.window, text="From:", font=("Arial", 10), fg="white", bg="#2b2a2a"
        )
        from_label.place(x=80, y=110)
        from_dropdown = ttk.Combobox(
            self.window, textvariable=self.from_format, state="readonly", width=10
        )
        from_dropdown["values"] = ["DOCX", "PDF", "TXT"]
        from_dropdown.place(x=140, y=110)

        self.to_format = StringVar(value="PDF")
        to_label = Label(
            self.window, text="To:", font=("Arial", 10), fg="white", bg="#2b2a2a"
        )
        to_label.place(x=280, y=110)
        to_dropdown = ttk.Combobox(
            self.window, textvariable=self.to_format, state="readonly", width=10
        )
        to_dropdown["values"] = ["PDF", "DOCX", "TXT"]
        to_dropdown.place(x=330, y=110)

        convert_button = Button(
            self.window,
            text="Convert",
            command=self.start_conversion,
            font=("Arial", 10, "bold"),
            bg="#00d4ff",
            fg="white",
            width=12,
        )
        convert_button.place(x=250, y=160, height=30)

        self.processing_label = Label(
            self.window, text="", font=("Arial", 10), fg="#00d4ff", bg="#2b2a2a"
        )
        self.processing_label.place(x=250, y=200)

    def file_browser(self):
        self.filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select a file",
            filetypes=(
                ("All files", "*.*"),
                ("Word files", "*.docx*"),
                ("Pdf files", "*.pdf*"),
                ("Text files", "*.txt*"),
            ),
        )
        if self.filename:
            self.input_file.delete(0, END)
            self.input_file.insert(0, self.filename)

    def start_conversion(self):
        if not self.filename:
            self.processing_label.config(text="Please select a file first!")
            return

        self.processing_label.config(text="Processing...")

        threading.Thread(target=self.file_convert, daemon=True).start()

    def file_convert(self):
        try:
            from_format = self.from_format.get().lower()
            to_format = self.to_format.get().lower()

            output_file = filedialog.asksaveasfilename(
                defaultextension=f".{to_format}",
                filetypes=((f"{to_format.upper()} files", f"*.{to_format}"), ("All files", "*.*")),
            )

            if not output_file:
                self.processing_label.config(text="Conversion canceled.")
                return

            if from_format == "docx" and to_format == "pdf":
                convert(self.filename, output_file)
            elif from_format == "pdf" and to_format == "docx":
                cv = Converter(self.filename)
                cv.convert(output_file)
                cv.close()
            else:
                self.processing_label.config(
                    text="Conversion for selected formats is not supported yet."
                )
                return

            self.processing_label.config(text=f"File saved to {output_file}")
        except Exception as e:
            self.processing_label.config(text=f"Error: {str(e)}")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = FileConverterApp()
    app.run()
