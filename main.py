from datetime import datetime
from json import dumps
from terminal_text_color import text_color
from hashlib import sha256 #
class Block():
    # Cada bloque contiene información como índice, prueba de trabajo, 
    # señal ECG, sello de tiempo y hash anterior. Al crear una instancia 
    # de la clase, se imprime su información y se genera un hash SHA-256 
    # basado en su contenido. El método __str__ imprime el bloque con su 
    # información y hash
    def __init__(self, index:int, proof, ecg_signal:[float], previousHash:str) -> None:
        self.index = index # numero de bloque
        self.proof = proof
        self.data_signal = ecg_signal
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.previousHash = previousHash # imprimimos su informacion
        print(self)

    def __str__(self) -> str:
        # imprime y devuelve el hash generado
        return f'Nuevo bloque generado\n{vars(self)}\nHash: {self.generateHash()}'

    def generateHash(self) -> bytes:
        # función que toma el bloque, y lo codifica en un hash a base de json.
        return sha256(dumps(vars(self), sort_keys=True).encode()).hexdigest()

class Blockchain():
    def __init__(self) -> None:
        self.chain = []
        self.create_block(proof=1, data=[1,2,3,4,5,6,7,8,9,0], previous_hash="0")

    def create_block(self, proof:int, data, previous_hash:str):
        # creamos un nuevo bloque, el cual es una instancia de la clase bloque
        nuevo_bloque = Block(index=len(self.chain)+1, proof=proof, ecg_signal=data, previousHash=previous_hash)
        self.chain.append(nuevo_bloque) # agregamos a la cadena principal
        return nuevo_bloque

    def getPreviousBlock(self):
        # retorna el bloque anterior
        return self.chain[-1]
    
if __name__ == "__main__":
    # bloque = Block(1, 1, "esta es una senal ecg", "previous_hash")
    cadena = Blockchain()
    cadena.create_block(cadena.chain[0].proof, [10,20,30,40,50,60,70,80,90,00], cadena.chain[0].generateHash())
    print(len(cadena.chain))