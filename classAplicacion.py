from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
class Aplicacion():
    __ventana=None
    __valorDolar=None
    __dolares=None
    __pesos=None
    def __init__(self,dolar):
        self.__valorDolar=dolar
        '''VENTANA'''
        self.__ventana=Tk()
        ancho_ventana = 290
        alto_ventana = 115
        x_ventana = self.__ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.__ventana.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.__ventana.geometry(posicion)
        self.__ventana.resizable(0,0)
        self.__ventana.title('Conversor de moneda')
        
        '''MAINFRAME'''
        mainframe=ttk.Frame(self.__ventana)
        mainframe.place(x=0,y=0,height=88,width=244)
        mainframe['relief'] = 'sunken'
        mainframe['borderwidth'] = 2
        
        '''ENTRY DOLARES'''
        self.__dolares=StringVar()
        self.dolaresEntry=ttk.Entry(mainframe,width=7,textvariable=self.__dolares)
        self.dolaresEntry.place(relx=0.5,y=20,anchor=tk.CENTER)
        self.__dolares.trace('w', self.calcular)
        self.dolaresEntry.focus()
        '''TEXT PESOS'''
        ttk.Label(mainframe,text='pesos',padding=(5,5)).place(x=150,rely=0.55,anchor=tk.W)
        
        '''RESULTADO PESOS'''
        self.__pesos=StringVar()    
        ttk.Label(mainframe,textvariable=self.__pesos).place(x=92,rely=0.55,anchor=tk.W)
        
        '''TEXT DOLARES'''
        ttk.Label(mainframe,text='dólares').place(x=150,y=20,anchor=tk.W)
        
        '''TEXT EQUIVALENTE'''
        ttk.Label(mainframe,text='es equivalente a').place(x=3,rely=0.55,anchor=tk.W)
        
        '''BOTON SALIR'''
        ttk.Button(mainframe,text='Salir',command=self.__ventana.destroy).place(relx=0.94,rely=0.96,anchor=tk.S + tk.E)
        
        self.__ventana.mainloop()

    def calcular(self,*args):
        if self.dolaresEntry.get()!='':
            try:
                valor=float(self.dolaresEntry.get())
                self.__pesos.set('{:.2f}'.format(self.__valorDolar*valor))
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                message='Debe ingresar un valor numérico')
                self.__pesos.set('')
                self.__dolares.set('')
                self.dolaresEntry.focus()
        else:
            self.__pesos.set('')


