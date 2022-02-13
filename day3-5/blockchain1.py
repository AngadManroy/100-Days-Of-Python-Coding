# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:22:27 2022

@author: hp
"""
import datetime
import hashlib
import json
from flask import Flask, jsonify

#creating a blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1,previous_hash = '0')
    
    def create_block(self, proof, previous_hash):
        block = {'index':len(self.chain) + 1,
                 'timestamp':str(datetime.datetime.now()),
                 'proof':proof,
                 'previous_hash':previous_hash}
        self.chain.append(block)
        return block
    
    def get_prev(self):
        return self.chain[-1]
    
    def proof_work(self, previous_proof):
        new_proof =1
        check_proof=False
        while check_proof is False:
            hash_operation = hashlib.sha256(str((new_proof**4 - 3*(previous_proof**2)).encode()).hexdigest())
            if hash_operation[:4]=='0000':
                check_proof=True
            else:
                new_proof+=1
            return new_proof 
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def isValid(self, chain):
        previous_block = chain[0]
        block_index = 1 
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof =block['proof']
            hash_operation = hashlib.sha256(str((proof**4 - 3*(previous_proof**2)).encode()).hexdigest())
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
#Mining the blockchain
#Create web app
app = Flask(__name__)
#create a blockchain
blockchian = Blockchain()

@app.route('/mine_block',methods = ['GET'])

def mine_block():
    previous_block = blockchian.get_prev()
    previous_proof = previous_block['proof']
    proof = blockchian.proof_work(previous_proof)
    previous_hash = blockchian.hash(previous_block)
    block = blockchian.create_block(proof, previous_hash)
    response = {'message':'Congratulations!, You just mined a block',
                'index':block['index'],
                'timestamp':block['timestamp'],
                'proof': block['proof'],
                'previous_hash':block['previous_hash']}
    return jsonify(response), 200



    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            