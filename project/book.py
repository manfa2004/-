import random
import tkinter as tk
from tkinter import *
import tkinter.filedialog as tkf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import time

import pandas as pd
import json

select = 0

def childWindow():
    window = tk.Toplevel(root)
    window.title("장르")
    
    def re0():
        label2.configure(text=0)
        select = 0
        window.destroy()

    def re1():
        label2.configure(text=100)
        select = 100
        window.destroy()

    def re2():
        label2.configure(text=200)
        select = 200
        window.destroy()

    def re3():
        label2.configure(text=300)
        select = 300
        window.destroy()

    def re4():
        label2.configure(text=400)
        select = 400
        window.destroy()

    def re5():
        label2.configure(text=500)
        select = 500
        window.destroy()

    def re6():
        label2.configure(text=600)
        select = 600
        window.destroy()

    def re7():
        label2.configure(text=700)
        select = 700
        window.destroy()

    def re8():
        label2.configure(text=800)
        select = 800
        window.destroy()

    def re9():
        label2.configure(text=900)
        select = 900
        window.destroy()

    img0 = PhotoImage(file='사진/총류.png')
    img1 = PhotoImage(file='사진/철학.png')
    img2 = PhotoImage(file='사진/종교.png')
    img3 = PhotoImage(file='사진/사회과학.png')
    img4 = PhotoImage(file='사진/자연과학.png')
    img5 = PhotoImage(file='사진/기술과학.png')
    img6 = PhotoImage(file='사진/예술.png')
    img7 = PhotoImage(file='사진/언어.png')
    img8 = PhotoImage(file='사진/문학.png')
    img9 = PhotoImage(file='사진/역사.png')

    button0 = tk.Button(window, image=img0, command=re0)
    button0.grid(row=0, column=0)

    button1 = tk.Button(window, image=img1, command=re1)
    button1.grid(row=0, column=1)

    button2 = tk.Button(window, image=img2, command=re2)
    button2.grid(row=0, column=2)

    button3 = tk.Button(window, image=img3, command=re3)
    button3.grid(row=0, column=3)

    button4 = tk.Button(window, image=img4, command=re4)
    button4.grid(row=0, column=4)

    button5 = tk.Button(window, image=img5, command=re5)
    button5.grid(row=1, column=0)

    button6 = tk.Button(window, image=img6, command=re6)
    button6.grid(row=1, column=1)

    button7 = tk.Button(window, image=img7, command=re7)
    button7.grid(row=1, column=2)

    button8 = tk.Button(window, image=img8, command=re8)
    button8.grid(row=1, column=3)

    button9 = tk.Button(window, image=img9, command=re9)
    button9.grid(row=1, column=4)

    window.mainloop()
    return True

def childWindow2():

    select = label2.cget("text")
    select = int(select)
    general = [0,1]
    philosophy = [0,1]
    religion = [0,1]
    social_science = [0,1]
    natural_science = [0,1]
    technology_science = [0,1]
    language = [0,1]
    art = [0,1]
    literature = [0,1]
    history = [0,1]




    if select == 0:
        test = pd.read_csv('책목록/book000.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('총류')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)

        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()



    elif select == 100:
        test = pd.read_csv('책목록/book100.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('철학')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)

        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()


    elif select == 200:
        test = pd.read_csv('책목록/book200.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('종교')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)
        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()


    elif select == 300:
        test = pd.read_csv('책목록/book300.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('사회과학')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)
        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()


    elif select == 400:
        test = pd.read_csv('책목록/book400.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('자연과학')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)
        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()


    elif select == 500:
        test = pd.read_csv('책목록/book500.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('기술과학')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)
        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()

    elif select == 600:
        test = pd.read_csv('책목록/book600.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('언어')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)
        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()


    elif select == 700:
        test = pd.read_csv('책목록/book700.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('예술')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)
        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()


    elif select == 800:
        test = pd.read_csv('책목록/book800.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('문학')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)
        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()


    elif select == 900:
        test = pd.read_csv('책목록/book900.csv',encoding='UTF-8')
        df = pd.DataFrame(test, columns = ['제목'])

        window2 = tk.Toplevel(root)
        window2.title('역사')

        label_text0 = df.sample(n=1)

        label_text0 = str(label_text0)
        label0 = tk.Label(window2, text=label_text0, font=('맑은 고딕', 30),)
        label0.grid(column=0, row=0)

        window2.mainloop()

    return True

root = tk.Tk()
root.title('광주과학고등학교 도서관 책 추천 시스템')

b = tk.Button(root, text="책 종류 선택", width=20, font=('맑은 고딕', 14), command=childWindow)
b.grid(column=0, row=0)
c = tk.Button(root, text="책 추천", width=20, font=('맑은 고딕',14), command=childWindow2)
c.grid(column=1, row=0)
label2 = Label(root, text="책의 종류 : ", font=("돋음", 10))
label2.grid(column=0, row=1)
label3 = Label(root, text="책을 추천합니다!", font=("돋움",10))
label3.grid(column=1,row=1)

root.mainloop()