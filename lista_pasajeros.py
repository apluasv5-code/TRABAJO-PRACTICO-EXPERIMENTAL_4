# ==============================================================
#  AeroLista - Lista simplemente enlazada de pasajeros
# ==============================================================

from pasajero import Pasajero


class Nodo:
    """Almacena un pasajero y la referencia al siguiente nodo."""

    def __init__(self, data):
        self.data = data
        self.next = None


class ListaPasajeros:
    """Gestiona las reservas en orden de llegada mediante nodos enlazados."""

    # ----------------------------------------------------------
    # Constructor e inserción al final
    # ----------------------------------------------------------
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def ingresar(self, pasajero):
        nuevo = Nodo(pasajero)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo

        self.cantidad = self.cantidad + 1
        return True

    # ----------------------------------------------------------
    # Estado y recorrido de la lista
    # ----------------------------------------------------------
    def esta_vacia(self):
        """Retorna True cuando no hay pasajeros registrados."""
        return self.head is None

    def longitud(self):
        """Retorna la cantidad de pasajeros registrados."""
        return self.cantidad

    def listar(self):
        """Retorna los pasajeros en orden, desde la cabeza hasta el final."""
        resultado = []
        actual = self.head

        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next

        return resultado

    # ----------------------------------------------------------
    # Búsquedas lineales
    # ----------------------------------------------------------
    def buscar(self, numero):
        """Retorna el pasajero de una reserva o None si no existe."""
        actual = self.head

        while actual is not None:
            if actual.data.numero == numero:
                return actual.data
            actual = actual.next

        return None

    def buscar_por_asiento(self, asiento):
        """Retorna el pasajero que ocupa un asiento o None si está libre."""
        actual = self.head

        while actual is not None:
            if actual.data.asiento == asiento:
                return actual.data
            actual = actual.next

        return None

    def buscar_por_cedula(self, cedula):
        """Retorna el pasajero con esa cédula o None si no existe."""
        actual = self.head

        while actual is not None:
            if actual.data.cedula == cedula:
                return actual.data
            actual = actual.next

        return None

    # ----------------------------------------------------------
    # Modificación y eliminación
    # ----------------------------------------------------------
    def modificar(self, numero, nuevo_nombre, nueva_edad, nuevo_asiento):
        """Actualiza los datos de la reserva sin mover su nodo."""
        pasajero = self.buscar(numero)

        if pasajero is None:
            return False

        pasajero.nombre = nuevo_nombre
        pasajero.edad = nueva_edad
        pasajero.asiento = nuevo_asiento
        return True

    def eliminar(self, numero):
        """Desengancha la reserva indicada y retorna su pasajero o None."""
        if self.head is None:
            return None

        if self.head.data.numero == numero:
            quitado = self.head
            self.head = quitado.next
            self.cantidad = self.cantidad - 1
            return quitado.data

        anterior = self.head
        while anterior.next is not None and anterior.next.data.numero != numero:
            anterior = anterior.next

        if anterior.next is None:
            return None

        quitado = anterior.next
        anterior.next = quitado.next
        self.cantidad = self.cantidad - 1
        return quitado.data

    # ----------------------------------------------------------
    # Filtro por clase
    # ----------------------------------------------------------
    def filtrar_por_clase(self, clase):
        """Retorna los pasajeros de la clase solicitada, en su orden."""
        resultado = []
        actual = self.head

        while actual is not None:
            if actual.data.clase() == clase:
                resultado.append(actual.data)
            actual = actual.next

        return resultado
