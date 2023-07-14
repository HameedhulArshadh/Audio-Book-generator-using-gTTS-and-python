# imports
from gtts import gTTS
import PyPDF2


def readTextFile(filename):
    with open(filename, "r") as file:
        return file.read()

def readPDFFile(filename):
    text = ""
    pdfreader = PyPDF2.PdfReader(filename)
    for page in range(len(pdfreader.pages)):
        content = pdfreader.pages[page]
        text = text + content.extract_text()
    return text

if __name__ == '__main__':
    filename = "TwoFriendsAndTheBear.txt"
    tld = 'co.in'
    text = readTextFile(filename)
    audioBook = gTTS(text, tld=tld, slow=False)
    audioBook.save(str(filename.split(".")[0]) + ".mp3")

    # filename = "10 Vertebrates F.pdf"
    # text = readPDFFile(filename)
    # audioBook = gTTS(text, tld=tld, slow=False)
    # audioBook.save(str(filename.split(".")[0]) + ".mp3")
