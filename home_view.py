import tkinter as tk

from utils import center_window
from conexion import obtener_interfaces

class Home:
    def __init__(self, panel, nodo_user):
        self.nodo_user = nodo_user
        self.panel = panel
        self.init_ventana()
        self.mostrarInterfaces()
        
    def init_ventana(self):
        self.panel.geometry("980x600")
        self.panel.configure(bg="gray10")
        center_window(self.panel, 980, 600)
        
    def mostrarInterfaces(self):
        interfaces = obtener_interfaces(self.nodo_user)
        
        self.label_datos = tk.Label(self.panel, text=f"{self.nodo_user[0]['e']['nombre']}", width=30,font=("Arial", 20)) 
        self.label_datos.pack()
       
        for interfaz in interfaces:
            if interfaz == 'dar tarea':
                self.btn_login = tk.Button(self.panel, text=interfaz, width=30,font=("Arial", 25), bd=2, relief=tk.GROOVE)
                self.btn_login.pack(pady=15, padx=20)
                continue
               
            if interfaz == 'ver entregas':
               self.btn_login = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25))
               self.btn_login.pack(pady=15, padx=20)
               continue
               
            if interfaz == 'ver planilla':
               self.btn_login = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25), bd=2, relief=tk.GROOVE, state=tk.DISABLED)
               self.btn_login.pack(pady=15, padx=20)
               continue
               
            if interfaz == 'subir tarea':
                self.btn_login = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25), bd=2, relief=tk.GROOVE)
                self.btn_login.pack(pady=15, padx=20)
                continue
            
            if interfaz == 'ver notas':
                self.btn_login = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25), bd=2, relief=tk.GROOVE, state=tk.DISABLED)
                self.btn_login.pack(pady=15, padx=20)
                continue
            
            if interfaz == 'ver materias inscritas':
                self.btn_login = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25), bd=2, relief=tk.GROOVE, state=tk.DISABLED)
                self.btn_login.pack(pady=15, padx=20)
                continue
        
def show_home(main_panel, nodo_user):
    Home(main_panel, nodo_user)