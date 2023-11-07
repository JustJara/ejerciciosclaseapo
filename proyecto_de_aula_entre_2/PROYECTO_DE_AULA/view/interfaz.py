
import tkinter as tk
from tkinter import messagebox
from model.estacionamiento import Estacionamiento
class InterfazGrafica:

    def __init__(self, root):
        self.estacionamiento = Estacionamiento()
        self.root = root
        self.root.title("Sistema de Parqueaderos P&J")
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)
        self.parqueadero_labels = []
        self.mostrar_menu_inicial()

    def mostrar_parqueadero_usuario(self):
        self.limpiar_frame()

        if self.estacionamiento.usuario_actual.parqueadero_asociado:
            parqueadero = self.estacionamiento.usuario_actual.parqueadero_asociado.parqueadero

            self.parqueadero_labels = []
            for i, fila in enumerate(parqueadero):
                fila_labels = []
                for j, celda in enumerate(fila):
                    label = tk.Label(self.frame, text=str(celda), borderwidth=1, relief="solid", width=5, height=2)
                    label.grid(row=i, column=j, padx=2, pady=2)
                    fila_labels.append(label)
                self.parqueadero_labels.append(fila_labels)

            volver_btn = tk.Button(self.frame, text="Volver al Menú", command=self.mostrar_menu_dentro_app)
            volver_btn.grid(row=len(parqueadero), column=0, columnspan=len(parqueadero[0]), pady=10)
        else:
            tk.Label(self.frame, text="Este usuario no tiene un parqueadero asociado.").pack()

    def mostrar_menu_inicial(self):
        self.limpiar_frame()

        tk.Label(self.frame, text="Escoje la opción según lo que deseas hacer").pack()

        tk.Button(self.frame, text="Registrarse", command=self.registrar_usuario).pack()
        tk.Button(self.frame, text="Logearse", command=self.iniciar_sesion).pack()
        tk.Button(self.frame, text="Salir", command=self.root.destroy).pack()

    def registrar_usuario(self):
        self.limpiar_frame()

        tk.Label(self.frame, text="Bienvenido al sistema de parqueaderos P&J").pack()
        tk.Label(self.frame, text="Para registrarte debes seguir las instrucciones").pack()

        tk.Label(self.frame, text="Ingresa el nombre de usuario:").pack()
        self.nombre_usuario_entry = tk.Entry(self.frame)
        self.nombre_usuario_entry.pack()

        tk.Label(self.frame, text="Ingrese la contraseña:").pack()
        self.contrasena_entry = tk.Entry(self.frame, show="*")
        self.contrasena_entry.pack()

        tk.Label(self.frame, text="Ingrese el tamaño del parqueadero").pack()

        tk.Label(self.frame, text="Ingrese la cantidad de filas del parqueadero:").pack()
        self.filas_entry = tk.Entry(self.frame)
        self.filas_entry.pack()

        tk.Label(self.frame, text="Ingrese la cantidad de columnas del parqueadero:").pack()
        self.columnas_entry = tk.Entry(self.frame)
        self.columnas_entry.pack()

        tk.Button(self.frame, text="Registrar", command=self.registrar_usuario_accion).pack()
        volver_btn = tk.Button(self.frame, text="Volver al Menú", command=self.mostrar_menu_inicial)
        volver_btn.pack()

    def registrar_usuario_accion(self):
        nombre_usuario = self.nombre_usuario_entry.get()
        contrasena = self.contrasena_entry.get()
        filas = int(self.filas_entry.get())
        columnas = int(self.columnas_entry.get())

        try:
            usuario = self.estacionamiento.registrar_usuario(nombre_usuario, contrasena, filas, columnas)
            messagebox.showinfo("Registro Exitoso", f"Usuario {usuario.nombre_usuario} registrado exitosamente")
            self.mostrar_menu_inicial()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def iniciar_sesion(self):
        self.limpiar_frame()

        tk.Label(self.frame, text="Para iniciar sesión debes seguir las instrucciones.").pack()
        tk.Label(self.frame, text="Ingresa el nombre de usuario").pack()
        self.nombre_usuario_entry = tk.Entry(self.frame)
        self.nombre_usuario_entry.pack()

        tk.Label(self.frame, text="Ingrese la contraseña").pack()
        self.contrasena_entry = tk.Entry(self.frame, show="*")
        self.contrasena_entry.pack()

        tk.Button(self.frame, text="Iniciar Sesión", command=self.iniciar_sesion_accion).pack()
        volver_btn = tk.Button(self.frame, text="Volver al Menú", command=self.mostrar_menu_inicial)
        volver_btn.pack()

    def iniciar_sesion_accion(self):
        nombre_usuario = self.nombre_usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        try:
            if self.estacionamiento.iniciar_sesion_usuario(nombre_usuario, contrasena):
                messagebox.showinfo("Inicio de Sesión", f"Inicio de sesión exitoso para usuario: {nombre_usuario}")
                self.mostrar_menu_dentro_app()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_menu_dentro_app(self):
        self.limpiar_frame()

        tk.Button(self.frame, text="Mostrar parqueadero", command=self.mostrar_parqueadero_usuario).pack()
        tk.Button(self.frame, text="Ingresar vehiculo", command=self.ingresar_vehiculo).pack()
        tk.Button(self.frame, text="Retirar vehiculo", command=self.retirar_vehiculo).pack()
        tk.Button(self.frame, text="Reservar celda para un vehículo", command=self.reservar_celda_parqueadero).pack()
        tk.Button(self.frame, text="Cerrar sesión", command=self.cerrar_sesion).pack()

    def ingresar_vehiculo(self):
        self.limpiar_frame()

        tk.Label(self.frame, text="Ingresar vehículo").pack()
        tk.Label(self.frame, text="Ingrese la placa del vehículo:").pack()
        self.placa_vehiculo_entry = tk.Entry(self.frame)
        self.placa_vehiculo_entry.pack()

        tk.Label(self.frame, text="Ingrese la hora de ingreso (formato 00:00):").pack()
        self.hora_ingreso_entry = tk.Entry(self.frame)
        self.hora_ingreso_entry.pack()

        tk.Label(self.frame, text="Ingrese el índice de la fila:").pack()
        self.indice_fila_entry = tk.Entry(self.frame)
        self.indice_fila_entry.pack()

        tk.Label(self.frame, text="Ingrese el índice de la columna:").pack()
        self.indice_columna_entry = tk.Entry(self.frame)
        self.indice_columna_entry.pack()

        tk.Button(self.frame, text="Ingresar Vehículo", command=self.ingresar_vehiculo_accion).pack()

        volver_btn = tk.Button(self.frame, text="Volver al Menú", command=self.mostrar_menu_dentro_app)
        volver_btn.pack()

    def ingresar_vehiculo_accion(self):
        placa_vehiculo = self.placa_vehiculo_entry.get()
        hora_ingreso = self.hora_ingreso_entry.get()
        indice_fila = int(self.indice_fila_entry.get())
        indice_columna = int(self.indice_columna_entry.get())

        try:
            ingreso = self.estacionamiento.ingresar_vehiculo_parqueadero(placa_vehiculo, hora_ingreso, indice_fila, indice_columna)
            if ingreso == "reservado":
                messagebox.showinfo("Ingreso Exitoso", "El vehículo se ingresó con éxito y tiene su estadía paga por haber reservado.")
                self.mostrar_menu_dentro_app()
            if ingreso == True:
                messagebox.showinfo("Ingreso Exitoso", "El vehículo se ingresó con éxito")
                self.mostrar_menu_dentro_app()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def retirar_vehiculo(self):
        self.limpiar_frame()

        tk.Label(self.frame, text="Retirar vehículo").pack()
        tk.Label(self.frame, text="Ingrese la placa del vehículo:").pack()
        self.placa_vehiculo_entry = tk.Entry(self.frame)
        self.placa_vehiculo_entry.pack()

        tk.Label(self.frame, text="Ingrese la hora de salida (formato 00:00):").pack()
        self.hora_salida_entry = tk.Entry(self.frame)
        self.hora_salida_entry.pack()

        tk.Label(self.frame, text="¿Desea generar una factura? (si - no)").pack()
        self.decision_factura_entry = tk.Entry(self.frame)
        self.decision_factura_entry.pack()


        tk.Button(self.frame, text="Retirar Vehículo", command=self.retirar_vehiculo_accion).pack()

        volver_btn = tk.Button(self.frame, text="Volver al Menú", command=self.mostrar_menu_dentro_app)
        volver_btn.pack()

    def retirar_vehiculo_accion(self):
        placa_vehiculo = self.placa_vehiculo_entry.get()
        hora_salida = self.hora_salida_entry.get()
        decision_factura = self.decision_factura_entry.get()
        try:
            vehiculo = self.estacionamiento.retirar_vehiculo_parqueadero(placa_vehiculo,hora_salida,decision_factura)
            valor_a_cobrar = self.estacionamiento.calcular_valor_a_pagar(vehiculo,hora_salida)
            mensaje = self.estacionamiento.generar_factura(vehiculo,hora_salida,valor_a_cobrar)
            if decision_factura == "si":
                messagebox.showinfo("Detalles del estacionamiento",mensaje)
            if decision_factura == "no":
                messagebox.showinfo("Retiro Exitoso", f"El vehículo se retiró con éxito. Costo: {valor_a_cobrar}")
            self.mostrar_menu_dentro_app()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reservar_celda_parqueadero(self):
        self.limpiar_frame()

        tk.Label(self.frame, text="Reservar celda para un vehículo").pack()
        tk.Label(self.frame, text="Ingrese la placa del vehículo:").pack()
        self.placa_vehiculo_entry = tk.Entry(self.frame)
        self.placa_vehiculo_entry.pack()

        tk.Label(self.frame, text="Ingrese la hora inicio de la reserva: ").pack()
        self.hora_ingreso_reserva_entry = tk.Entry(self.frame)
        self.hora_ingreso_reserva_entry.pack()

        tk.Label(self.frame, text="Ingrese la hora final de la reserva: ").pack()
        self.hora_final_entry = tk.Entry(self.frame)
        self.hora_final_entry.pack()

        tk.Label(self.frame, text="Ingrese la fila para la reserva:").pack()
        self.indice_fila_entry = tk.Entry(self.frame)
        self.indice_fila_entry.pack()

        tk.Label(self.frame, text="Ingrese la columna para la reserva:").pack()
        self.indice_columna_entry = tk.Entry(self.frame)
        self.indice_columna_entry.pack()

        tk.Button(self.frame, text="Reservar Celda", command=self.reservar_celda_accion).pack()

        volver_btn = tk.Button(self.frame, text="Volver al Menú", command=self.mostrar_menu_dentro_app)
        volver_btn.pack()

    def reservar_celda_accion(self):
        placa_vehiculo = str(self.placa_vehiculo_entry.get())
        hora_inicio_reserva = str(self.hora_ingreso_reserva_entry.get())
        hora_final_reserva = str(self.hora_final_entry.get())
        indice_fila = int(self.indice_fila_entry.get())
        indice_columna = int(self.indice_columna_entry.get())

        cobro = self.estacionamiento.reservar_vehiculo_parqueadero(hora_inicio_reserva,hora_final_reserva,placa_vehiculo,indice_fila,indice_columna)
        if cobro == False:
            messagebox.showinfo("Reserva Fallida", f"La celda se encuentra ocupada, revise nuevamente el estado del parqueadero")
            self.mostrar_menu_dentro_app()
        else:
            messagebox.showinfo("Reserva Exitosa", f"La celda se reservó con éxito. El cliente debe pagar {cobro}$")
            self.mostrar_menu_dentro_app()

    def cerrar_sesion(self):
        self.limpiar_frame()
        self.estacionamiento.cerrar_sesion()
        messagebox.showinfo("Cierre de Sesión", "Sesión cerrada con éxito")
        self.mostrar_menu_inicial()

    def limpiar_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
