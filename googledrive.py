import gdown
import tkinter as tk
from tkinter import filedialog

def dowloadfile(url, output):
    gdown.download(url, output, quiet=False)

def inputfile():
    url = input('Enter URL: ')
    id = url.split('/')[-2]
    outurl = 'https://drive.google.com/uc?export=download&id=' + id
    namefile = input('Enter Name file Output (ex: tools.exe ): ')
    print('Pls choose folder output')
    output = choosefolderoutput()+ '/' +namefile
    dowloadfile(outurl, output)
    return output


def choosefolderoutput():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def main():
    inputfile()

if __name__ == '__main__':
    main()