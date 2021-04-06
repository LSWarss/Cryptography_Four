from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import serialization

class Assymetric():
    
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

    @staticmethod
    def generate_keys():
        private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )
        public_key = private_key.public_key()
        return {"Private key" : private_key, "Public key" : public_key}
    
    @staticmethod
    def generate_ssh_keys():
        keys = Assymetric.generate_keys()
        pem = keys["Private key"].private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = keys["Public key"].public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        )

        return {"Private key" : pem, "Public key" : public_pem}

    
