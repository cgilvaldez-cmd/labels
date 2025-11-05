# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:09:12 2025

@author: Carlos Gil
"""

import tkinter

datos= '''1
2
3
4
5
6
7
8
9  '''

datos = datos.split('\n')
print(len(datos))

window = tkinter.Tk()
window.geometry("400x400+100+100")
window.title("GUI")

color = ['green', 'yellow']

for k, ss in enumerate(datos):
  i = k % 2
  label = tkinter.Label(window, text=ss,font=("Helvetica", 20), bg=color[i], fg="red")
  label.grid(row=0, column=k, padx=10)

window.mainloop()