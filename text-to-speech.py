import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import docx
from gtts import gTTS
import os
import shutil

def convert_to_audio():
    #open file dialoge to select a pdf,word doc,or text file
    file_path= filedialog.askopenfilename()

    if file_path.endswith('.pdf'):
        pdf_file=open(file_path,'rb')
        pdf_reader =PyPDF2.PdfReader(pdf_file)
        mytext=''
        for page in pdf_reader.pages:
            mytext+=page.extract_text()
        pdf_file.close()
    elif file_path.endswith('.docx'):
        doc =docx.Document(file_path)
        paragraphs=[p.mytext for p in doc.paragraphs]
        mytext='\n'.join(paragraphs)
    elif file_path.endswith('.txt'):
        with open(file_path,'r') as file:
            mytext=file.read()
    else:
        return messagebox.showerror('error','unsupport file formate!')
    
    #convert text to audio
    myobj = gTTS()
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")
    # engin=pyttsx3.init()
    # output_file ='output.mp3'
    # engin.save_to_file(text,output_file)
    # engin.runAndWait()

    #update status lable
    output_label.config(text='conversion compleated')

    #enable the downloade button and exit button
    download_button.config(state='normal')
    exit_button.config(state='normal')

def download_audio(file_path):
    # open file dialog to setect the download location
    download_path = filedialog.asksaveasfilename(defaultextension='.mp3')

    if download_path:
        # move the output file to the download location
        shutil.move(file_path,download_path)

def exit_app():
    if messagebox.askyesno('exit','do you want to exit'):
        window.destroy()

# create the main windo
window=tk.Tk()
window.title('text to audio converter')

# creat a button for file selection
select_button=tk.Button(window,text='select file', command=convert_to_audio)
select_button.pack(pady=15)

# create a lable to display status
output_label=tk.Label(window,text='')
output_label.pack()

# create a button for donloading the audio
download_button=tk.Button(window,text='Download Audio', state='disabled',command=lambda: download_audio('output.mp3') )
download_button.pack(pady=15)

#creat an exit button
exit_button=tk.Button(window,text='Exit',state='disabled',command=exit_app,fg='white',bg='red')
exit_button.pack(pady=15)

#run the main loop
window.mainloop()



# https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes