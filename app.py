import hashlib


timing = datetime.now()
time_string = timing.strftime('%Y-%m-%d %H:%M:%S.%f')

encoded_block = json.dumps(block, sort_key = True).encode()
hash_operation = hashlib.sha256(encoded_block).hexdigest()