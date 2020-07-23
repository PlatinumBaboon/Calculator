try:
    import tkinter as tk
except:
    print('tkinter is preinstalled on the newest version of python on windows')
    print('For other Operating Systems without tKinter preinstalled use pip install tkinter with the terminal command:')
    print('pip install python-tk')
from BODMASCalculator import math

def spacer2(str1):
    str6 = str1.replace("-", " - ")
    str2 = str6.replace("+", " + ")
    str3 = str2.replace("*", " * ")
    str4 = str3.replace("/", " / ")
    str5 = str4.replace("0", " 0 ")
    str6 = str5.replace("1", " 1 ")
    str7 = str6.replace("2", " 2 ")
    str8 = str7.replace("3", " 3 ")
    str9 = str8.replace("4", " 4 ")
    str10 = str9.replace("5", " 5 ")
    str11 = str10.replace("6", " 6 ")
    str12 = str11.replace("7", " 7 ")
    str13 = str12.replace("8", " 8 ")
    str14 = str13.replace("9", " 9 ")
    return str14
    return str7
def increase():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '1'

def decrease():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '2'

def three():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '3'

def four():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '4'

def five():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '5'

def six():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '6'

def seven():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '7'

def eight():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '8'

def nine():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '9'

def plus():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '+'

def minus():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '-'

def multiply():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '*'

def division():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '/'

def power():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '^'

def equals():
    value = lbl_value["text"]

    try:
        if isinstance(int(math(lbl_value["text"])), int) == True:
            lbl_value["text"] = lbl_value["text"] + ' = ' + math(lbl_value["text"])
    except:
        try:
            if isinstance(float(math(lbl_value["text"])), float) == True:
                lbl_value["text"] = lbl_value["text"] + ' = ' + math(lbl_value["text"])
        except:
            if isinstance(math(lbl_value["text"]), int) == False:
                lbl_value['text'] = 'incorrect format try again'


def Del():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = spacer2(lbl_value["text"])
    text3 = spacer2(lbl_value["text"])
    text3 = text3.split()
    for e in text3:
        if e == '=':
            lbl_value["text"] = ''
    text2 = lbl_value["text"].split()
    text2.pop(-1)
    text2 = ''.join(text2)
    lbl_value["text"] = text2




def bracone():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + '('

def bractwo():
    if lbl_value['text'] == 'incorrect format try again':
        lbl_value['text'] = ''
    value = lbl_value["text"]
    lbl_value["text"] = lbl_value["text"] + ')'
window = tk.Tk()

window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_one = tk.Button(master=window, text="1", command=increase)
btn_one.grid(row=1, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="", width=25,
    height=5, borderwidth=5)
lbl_value.grid(row=0, column=1)

btn_two = tk.Button(master=window, text="2", command=decrease, width=25,
    height=5,)
btn_two.grid(row=1, column=1, sticky="nsew")

btn_three = tk.Button(master=window, text="3", command=three, width=25,
    height=5,)
btn_three.grid(row=1, column=2, sticky="nsew")

btn_four = tk.Button(master=window, text="4", command=four, width=25,
    height=5,)
btn_four.grid(row=2, column=0, sticky="nsew")

btn_four = tk.Button(master=window, text="5", command=five, width=25,
    height=5,)
btn_four.grid(row=2, column=1, sticky="nsew")

btn_four = tk.Button(master=window, text="6", command=six, width=25,
    height=5,)
btn_four.grid(row=2, column=2, sticky="nsew")

btn_four = tk.Button(master=window, text="7", command=seven, width=25,
    height=5,)
btn_four.grid(row=3, column=0, sticky="nsew")

btn_four = tk.Button(master=window, text="8", command=eight, width=25,
    height=5,)
btn_four.grid(row=3, column=1, sticky="nsew")

btn_four = tk.Button(master=window, text="9", command=nine, width=25,
    height=5,)
btn_four.grid(row=3, column=2, sticky="nsew")

btn_four = tk.Button(master=window, text="+", command=plus, width=25,
    height=5,)
btn_four.grid(row=1, column=3, sticky="nsew")

btn_four = tk.Button(master=window, text="-", command=minus, width=25,
    height=5,)
btn_four.grid(row=2, column=3, sticky="nsew")

btn_four = tk.Button(master=window, text="*", command=multiply, width=25,
    height=5,)
btn_four.grid(row=3, column=3, sticky="nsew")

btn_four = tk.Button(master=window, text="/", command=division, width=25,
    height=5,)
btn_four.grid(row=4, column=3, sticky="nsew")

btn_four = tk.Button(master=window, text="^", command=power, width=25,
    height=5,)
btn_four.grid(row=4, column=2, sticky="nsew")

btn_four = tk.Button(master=window, text=")", command=bractwo, width=25,
    height=5,)
btn_four.grid(row=4, column=1, sticky="nsew")

btn_four = tk.Button(master=window, text="(", command=bracone, width=25,
    height=5,)
btn_four.grid(row=4, column=0, sticky="nsew")

btn_four = tk.Button(master=window, text="=", command=equals, width=25,
    height=5,)
btn_four.grid(row=4, column=4, sticky="nsew")

btn_four = tk.Button(master=window, text="Del", command=Del, width=25,
    height=5,)
btn_four.grid(row=3, column=4, sticky="nsew")


window.mainloop()
