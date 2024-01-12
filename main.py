import hashlib
import datetime as date


## Criando a classe referente aos blocos
class Block:
    
    ## Construtor
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp= timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
       
    ## Função par calcular qual o hash 
    def calculate_hash(self):
        ## Usando o método .sha256() para criar um hash
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        ## Retornando o sha em hexadecimal
        return sha.hexdigest()

## Criando a classe Blockchain que ficará responsável por criar esse controle e registro dos blocos
class Blockchain:

        def __init__(self):
            self.chain = [self.create_genesis_block()]
         
        ## Função para criar o Bloco Gênesis   
        def create_genesis_block(self):
            return Block(0, date.datetime.now(), 'Genesis Block', '0')
        
        ## Função para adicionar um novo bloco
        def add_block(self, new_block):
            new_block.previou_hash = self.chain[-1].hash
            new_block.hash = new_block.calculate_hash()
            self.chain.append(new_block)
        
        ## Função para validar o bloco
        def is_valid(self):
            for i in range(1, len(self.chain)):
                current_block = self.chain[i]
                previous_block = self.chain[i-1]
                
                if current_block.hash != current_block.calculate_hash():
                    return False
                if current_block.previous_hash != previous_block.hash:
                    return False
                
                return True
            
my_blockchain = Blockchain()

compra = {
    'item': 'Ford Mustang',
    'valor': 100.000,
    'comprador': '@beu_io',
    'vendedor': '@vendedor'
}

compra2 = {
    'item': 'documento_seila',
    'valor_pago': 100,
    'comprador': '@beu_io',
    'vendedor': '@cartorio'
}

my_blockchain.add_block(Block(1, date.datetime.now(),compra, my_blockchain.chain[-1].hash)) 
my_blockchain.add_block(Block(1, date.datetime.now(),compra2, my_blockchain.chain[-1].hash))

print(f'Essa blockchain está válida? {str(my_blockchain.is_valid())}')