import csv
from tkinter import *


def text_to_word_set(text):
    text = text.lower()
    result = set()
    s = ''
    for c in text:
        if c.isalnum():
            s += c
        else:
            if s:
                result.add(s)
                s = ''
    return result


with open('train_full.csv') as file:
    lines = tuple(csv.reader(file))
    key_words = set()
    for line in lines:
        key_words |= set(line[0].split('%20'))

    words0 = set()
    words1 = set()

    for line in lines:
        if line[3] == '0':
            words0 |= text_to_word_set(line[2])
        else:
            words1 |= text_to_word_set(line[2])

    words_emergency = words0 - words1
    undefined = words0 & words1
    words_not_emergency = words1 - words0


def show_message():
    words = text_to_word_set(entry.get())
    if key_words & words:
        is_emergency = words_not_emergency & words
        is_not_emergency = words_emergency & words
        if is_emergency == is_not_emergency:
            label["text"] = 'Не определено'
        elif is_emergency:
            label["text"] = 'ЧП'
        else:
            label["text"] = 'Не ЧП'
    else:
        label["text"] = 'Не ЧП'


root = Tk()
root.resizable(width=False, height=False)
root.title("ПРОГРАММА")
root.geometry("250x200")
entry = Entry()
entry.pack(anchor=NW, padx=6, pady=6)
button = Button(text="Проверить сообщение", command=show_message)
button.pack(anchor=NW, padx=6, pady=6)
label = Label()
label.pack(anchor=NW, padx=6, pady=6)
root.mainloop()
