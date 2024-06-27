
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import docx
from gtts import gTTS
import os
import shutil

def convert_to_audio():
    file_path = filedialog.askopenfilename()
    if file_path.endswith('.pdf'):
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        pdf_file.close()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        paragraphs = [p.text for p in doc.paragraphs]
        text = '\n'.join(paragraphs)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            text = file.read()
    else:
        return messagebox.showerror('error', 'unsupport file format!')

    myobj = gTTS(text=text)
    myobj.save("output.mp3")
    os.system("start output.mp3")

    output_label.config(text='conversion completed')
    download_button.config(state='normal')
    exit_button.config(state='normal')

def download_audio():
    download_path = filedialog.asksaveasfilename(defaultextension='.mp3')
    if download_path:
        shutil.move('output.mp3', download_path)

def exit_app():
    if messagebox.askyesno('exit', 'do you want to exit'):
        window.destroy()

window = tk.Tk()
window.title('text to audio converter')

select_button = tk.Button(window, text='select file', command=convert_to_audio)
select_button.pack(pady=15)

output_label = tk.Label(window, text='')
output_label.pack()

download_button = tk.Button(window, text='Download Audio', state='disabled', command=download_audio)
download_button.pack(pady=15)

exit_button = tk.Button(window, text='Exit', state='disabled', command=exit_app, fg='white', bg='red')
exit_button.pack(pady=15)

window.mainloop()
