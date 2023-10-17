from datetime import datetime
from json import dumps
from hashlib import sha256 #
from time import sleep
class Block():
    # Cada bloque contiene información como índice, prueba de trabajo, 
    # señal ECG, sello de tiempo y hash anterior. Al crear una instancia 
    # de la clase, se imprime su información y se genera un hash SHA-256 
    # basado en su contenido. El método __str__ imprime el bloque con su 
    # información y hash
    def __init__(self, index:int, proof, ecg_signal:str, previousHash:str) -> None:
        self.index = index # numero de bloque
        self.proof = proof
        self.ecg_signal =  ecg_signal # ira la ruta de la señal ecg
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.previousHash = previousHash
        print(self) # imprimimos su informacion

    def __str__(self) -> str:
        # imprime y devuelve el hash generado
        return f'Nuevo bloque generado\n{vars(self)}\nHash: {self.genereteHash()}'

    def genereteHash(self) -> bytes:
        # función que toma el bloque, y lo codifica en un hash a base de json.
        return sha256(dumps(vars(self), sort_keys=True).encode()).hexdigest()

class Blockchain():
    def __init__(self) -> None:
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof:int, previous_hash:str):
        # creamos un nuevo bloque, el cual es una instancia de la clase bloque
        nuevo_bloque = Block(len(self.chain)+1, proof, "esta es una senal ecg", previous_hash)
        self.chain.append(nuevo_bloque) # agregamos a la cadena principal
        return nuevo_bloque

    def getPreviousBlock(self):
        # retorna el bloque anterior
        return self.chain[-1]
    
    def proofOfWork(self, previous_proof):
        # La prueba de trabajo es un concepto que evita el abuso de la cadena de bloques. 
        # Simplemente, su objetivo es identificar un número que resuelva un problema 
        # después de realizar una cierta cantidad de trabajo de cómputo.
        # Si el nivel de dificultad para identificar el número es alto, 
        # se desalienta el spam y la manipulación de la cadena de bloques.
        new_proof = 1  # Inicializa la variable que almacena la prueba (proof) con 1.
        check_proof = False  # Inicializa la bandera para comprobar si se encontró una prueba válida.

        while not check_proof:  # Inicia un bucle mientras no se haya encontrado una prueba válida.
            hash_operation = self.calculateHash(previous_proof, new_proof)  # Calcula un nuevo hash usando las pruebas previa y actual.

            if hash_operation[:4] == '0000':  # Comprueba si los primeros cuatro caracteres del nuevo hash son '0000'.
                check_proof = True  # Si se cumple, se establece la bandera para indicar que se encontró una prueba válida.
            else:
                new_proof += 1  # Si no se cumple, incrementa el valor de la prueba y continúa buscando.

        # Cuando se encuentra una prueba válida, se sale del bucle y se devuelve el valor de "new_proof" como resultado.
        return new_proof

    
    def ValidateChain(self, chain) -> bool:
        previous_block = chain[0]  # Inicializa con el primer bloque (bloque génesis).
        block_index = 1  # Inicializa un índice para recorrer la cadena.

        while block_index < len(chain):  # Comienza un bucle para recorrer la cadena.
            block = chain[block_index]  # Obtiene el bloque actual.

            # Comprueba si el campo 'previousHash' del bloque actual coincide con el hash del bloque anterior.
            if block['previousHash'] != block[block_index-1].generateHash():
                return False  # Si no coincide, la cadena no es válida y se devuelve False.

            previous_proof = previous_block['proof']  # Obtiene la "prueba" (proof) del bloque anterior.
            proof = block['proof']  # Obtiene la "prueba" (proof) del bloque actual.

            # Calcula un nuevo hash utilizando las pruebas del bloque anterior y del bloque actual.
            hash_operation = self.calculateHash(previous_proof, proof)

            # Comprueba si los primeros cuatro caracteres del nuevo hash no son '0000'.
            if hash_operation[:4] != '0000':
                return False  # Si no se cumple, la cadena no es válida y se devuelve False.

            previous_block = block  # Actualiza el bloque anterior para la próxima iteración.
            block_index += 1  # Incrementa el índice para pasar al siguiente bloque.

        # Si se llega a este punto, la cadena se validó completamente, y la función devuelve True.
        return True


    def calculateHash(previous_proof, new_proof):
        # Calcula un hash utilizando las pruebas anterior y actual.
        return sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()


if __name__ == "__main__":
    # bloque = Block(1, 1, "esta es una senal ecg", "previous_hash")
    cadena = Blockchain()