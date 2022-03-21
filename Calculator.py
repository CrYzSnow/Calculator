import tkinter
from tkinter import ttk
import tkinter.font as tkfont
from functools import partial
import lib

init = False

colors = {'dark' : ['#404040','#363636','white'],
          'light': ['#f0f0f0','#d8d8d8','black']}

def Actualiser(txt):
    try:
        if lib.textCalc == '0' and str(txt) in '0123456789':
            lib.textCalc = str(txt)
            calcTxt.config(text=lib.textCalc)
            return
        if txt == 'SUPPR' :
            if lib.textCalc == 'Error' :
                lib.textCalc = ''
                calcTxt.config(text=lib.textCalc)
                return
            if lib.textCalc == "Error, result too long" :
                lib.textCalc = ''
                calcTxt.config(text=lib.textCalc)
                return
            if lib.textCalc == '' :
                return
            lib.textCalc = list(lib.textCalc)
            lib.textCalc.pop()
            lib.textCalc = ''.join(lib.textCalc)
            calcTxt.config(text=lib.textCalc)
            return
        if lib.textCalc == "Error, result too long" and str(txt) != '=' :
            lib.textCalc = str(txt)
            calcTxt.config(text=lib.textCalc)
            return
        if lib.textCalc == 'Error' and str(txt) != '=' :
            lib.textCalc = str(txt)
            calcTxt.config(text=lib.textCalc)
            return
        if txt == '=' :
            lib.textCalc = str(round(eval(lib.textCalc),3))
            if len(lib.textCalc) >= 21 :
                lib.textCalc = "Error, result too long"
            calcTxt.config(text=lib.textCalc)
            return
        if len(lib.textCalc) >= 21 :
            return
        lib.textCalc += str(txt)
        calcTxt.config(text=lib.textCalc)
    except:
        lib.textCalc = "Error"
        calcTxt.config(text=lib.textCalc)

def ChangeTheme(*args):
    lib.buttonColor = colors[option.get()][0]
    lib.fenetreColor = colors[option.get()][1]
    lib.textColor = colors[option.get()][2]
    fenetre.configure(bg=lib.fenetreColor)
    calcTxt.config(bg=lib.fenetreColor,fg=lib.textColor)
    for key in h.keys():
        h[key].config(highlightbackground=lib.buttonColor,
                   bg=lib.buttonColor,
                   fg=lib.textColor)

fenetre = tkinter.Tk()
fenetre.configure(bg=lib.fenetreColor)
fenetre.title("Calculatrice")

fontCalc = tkfont.Font(size=12,weight="bold")
calcTxt = tkinter.Label(fenetre, text=lib.textCalc,height=3,font=fontCalc,bg=lib.fenetreColor,fg=lib.textColor)
calcTxt.grid(column=0,row=0,columnspan=4,pady=5)

haut = 2; larg = 4
h = { 'b0':[0,1,5], 'b1':[1,0,4], 'b2':[2,1,4], 'b3':[3,2,4], 'b4':[4,0,3], 'b5':[5,1,3]
     ,'b6':[6,2,3], 'b7':[7,0,2], 'b8':[8,1,2], 'b9':[9,2,2],'bVirg':['.',0,5]
     ,'bEgal':['=',3,5], 'bPlus':['+',3,4],'bMoins':['-',3,3],'bFoix':['*',3,2]
     ,'bDiv':['/',3,1], 'bSUPPR':['SUPPR',2,1], 'bPatG':['(',0,1], 'bParD':[')',1,1]}

for key,value in h.items():
    h[key] = tkinter.Button(fenetre,text=str(value[0]),
                            command=partial(Actualiser,value[0]),
                            height = haut,
                            width = larg*3 if value[0] == 0 else larg,
                            relief="groove",
                            highlightbackground=lib.buttonColor,
                            bg=lib.buttonColor,
                            fg=lib.textColor)
    h[key].grid(column=value[1],
                row=value[2],
                columnspan=2 if value[0] == 0 else 1)

option = tkinter.StringVar()
listTheme = ('light','dark')
theme = ttk.OptionMenu(fenetre,option,listTheme[0],*listTheme,command=ChangeTheme)
theme.grid(column=0,
           row=6,
           columnspan=4)

init = True

fenetre.mainloop()