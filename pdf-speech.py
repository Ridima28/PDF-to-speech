import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
numpages = len(pdfreader.pages)

engine = pyttsx3.init()

for i in range(numpages):
    page = pdfreader.pages[i]
    text = page.extract_text()
    if text:
        engine.say(text)

engine.runAndWait()
    
    