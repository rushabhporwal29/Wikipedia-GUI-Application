# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:38:00 2020

@author: HP
"""

import wikipedia
import tkinter as tk


def save():
    key=keyword.get()
    window.destroy()
    results=wikipedia.search(key)
    i=0
    print(results)
    win=tk.Tk()
    v = tk.IntVar()
    v.set(0)
    def sel():
        search=results[v.get()]
        win.destroy()
        w1=tk.Tk()
        w1.title(search)
        page=wikipedia.page(search)
        print(page.title)
        tk.Button(w1,text="close",command=w1.destroy).pack()
        tk.Label(w1,text=page.title,font="Times 20 bold").pack()
        #tk.Label(w1,text=page.content).pack()
        Sx = tk.Scrollbar(w1)
        Sy = tk.Scrollbar(w1)
        T = tk.Text(w1, height=80, width=200)
        Sx.pack(side=tk.RIGHT, fill=tk.Y)
        Sx.pack(side=tk.BOTTOM, fill=tk.X)
        T.pack(side=tk.LEFT, fill=tk.Y)
        Sx.config(command=T.yview)
        Sy.config(command=T.xview)
        T.config(yscrollcommand=Sx.set,xscrollcommand=Sy.set)
        T.insert(tk.END, page.content)
        tk.Button(w1,text="close",command=w1.destroy).pack()
        w1.mainloop()
        
    for result in results:
        tk.Radiobutton(win, 
                  text=result,
                  padx = 20, 
                  variable=v, 
                  command=sel,
                  value=i).pack(anchor=tk.W)
        i=i+1
    win.title("Result")
    win.mainloop()
    return


window=tk.Tk()
window.title("Wikipedia ")
label=tk.Label(window,text="Enter Keyword :")
label.grid(row=0,column=0,padx=8,pady=8)
keyword=tk.Entry(window)
keyword.grid(row=0,column=1,padx=8,pady=8)
submit=tk.Button(window,text="Submit",command=save)
submit.grid(row=1,column=1,padx=8,pady=8)
window.mainloop()



















