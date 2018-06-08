# Regex email search from txt files
# With tkinter GUI

from os import path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import re


class regexsearch:

    def __init__(self, parent):

        self.Frame = ttk.Frame(parent)
        self.Frame.grid(padx=5, pady=5)
        ttk.Label(self.Frame, text="Select a file to extract the e-mails from.") \
            .grid(row=0, columnspan=2, sticky='sw')
        self.entry = ttk.Entry(self.Frame, width=40)
        self.entry.grid(row=1, column=1)
        ttk.Button(self.Frame, text='Browse', command=self.browse) \
            .grid(row=1, column=2, sticky="nsew")
        ttk.Button(self.Frame, text='Scan', command=self.scan) \
            .grid(row=1, column=3, sticky="nsew")

    def browse(self):
        file_path = filedialog.askopenfilename()
        self.entry.delete(0, 'end')
        self.entry.insert(0, file_path)

    def scan(self):
        file_open = open(self.entry.get())
        file_read = file_open.read()
        emailregex = re.compile(r'''([a-zA-Z0-9.+-]+@+[a-zA-Z0-9.-]+[.\[a-zA-Z]{2,6})''', re.VERBOSE)
        matches = []
        for groups in emailregex.findall(file_read):
            matches.append(groups)
        file2_open = open('HRemails_regex.txt', 'w')
        print(len(matches))
        for i in range(len(matches)):
            file2_open.write(matches[i] + '\n')

        item_path = str(path.realpath("HRemails_regex.txt"))
        messagebox.showinfo(title='Success', message='Your file is saved in {}'.format(item_path))


def main():
    root = Tk()
    regexsearch(root)
    root.mainloop()


if __name__ == "__main__": main()
