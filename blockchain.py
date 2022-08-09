import hashlib
def hashgenerator(data):
  result=hashlib.sha256(data.encode())
  return result.hexdigest()

class Block:
   def __init__(self,data,hash,prev_hash):
     self.data=data
     self.hash=hash
     self.prev_hash=prev_hash

class Blockchain:
       def __init__(self):
        data="keshav->roshan 10 btc"
        hash=hashgenerator(data)
        prev_hash=00000
        genesis=Block("genesis-block",hash,prev_hash)
        self.chain=[genesis] 
       
       def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashgenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)

dataadder=Blockchain()
dataadder.add_block("1")
dataadder.add_block("2")
dataadder.add_block("3")
dataadder.add_block("4")
dataadder.add_block("5")

for block in dataadder.chain:
  print(block.__dict__)

