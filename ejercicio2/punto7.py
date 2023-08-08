""""Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance."
Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria."""

class CuentaBancaria:

    def __init__(self,numero_cuenta,propietarios,balance):

        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self,deposito):
        if deposito > 0:
            self.balance = deposito
            print("------------------------------------------")
            print(f"Se ha realizado el depósito de {deposito}$ con éxito")
            print("------------------------------------------")
        else:
            print("------------------------------------------")
            print("El monto a depositar no es válido")
            print("------------------------------------------")

    def retirar(self,retiro):
        if retiro > 0:
            self.balance -= retiro
            print("------------------------------------------")
            print("Se ha realizado el retiro de {retiro}$ con éxtio")
            print("------------------------------------------")
        else:

            print("------------------------------------------")
            print("El monto a retirar no es válido")
            print("------------------------------------------")

    def aplicar_cuota_manejo(self):
        self.balance -= self.balance * 0.02
        print("------------------------------------------")
        print(f"Se ha realizado el cobro de la cuota de manejo, su nuevo balance es: {self.balance}")
        print("------------------------------------------")

    def mostrar_detalles(self):
        print("----------ESTADO DE CUENTA--------------")
        print(f"Detalles de la cuenta bancaria con número {self.numero_cuenta}")
        print(f"El/los propietario/s de la cuenta es: {self.propietarios}")
        print(f"El balance de la cuenta actualmente es de: {self.balance}$")
        print("------------------------------------------")

#Se crea la instancia de la clase
cuenta_bancaria = CuentaBancaria(12345,["Pablo", "Felipe"],0)

#Se imprime el balance y se realiza el depósito, para después comprobar que el depósito si se realizó
print(f"El balance de la cuenta es: {cuenta_bancaria.balance}")
cuenta_bancaria.depositar(100000)
print(f"El balance de la cuenta es: {cuenta_bancaria.balance}")

#Se hace el retiro y se comprueba nuevamente el balance
cuenta_bancaria.retirar(50000)
print(f"El balance de la cuenta es: {cuenta_bancaria.balance}")

#Se aplica cuota de manejo
cuenta_bancaria.aplicar_cuota_manejo()

#Se muestran los detalles de la cuenta
cuenta_bancaria.mostrar_detalles()

        
