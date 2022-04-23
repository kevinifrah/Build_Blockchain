import datetime
from datetime import datetime as dt
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse
from fastecdsa import curve, ecdsa, keys
import zmq
import threading
from flask_mysqldb import MySQL

class Blockchain:

    def create_genesis_block():
        the_time = dt.now()

        block = {}
        block['index'] = 1
        block['prev_hash'] = '0000000000'
        block['nonce'] = 456
        block['data'] = 'This is the genesis block of the network'
        block['timestamp'] = the_time.strftime('%Y-%m-%d %H:%M:%S.%f')

        encoded_block = json.dumps(block, sort_key = True).encode()
        new_hash = hashlib.sha256(encoded_block).hexdigest()
        block['new_hash'] = new_hash

        print(block)

blockchain = Blockchain()

blockchain.create_genesis_block()