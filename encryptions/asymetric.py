from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.exceptions import InvalidSignature
import hashlib

import base64

class Assymetric():
    
    def __init__(self):
        self.privateKey = None
        self.publicKey = None

    def get_keys(self):
        """Getter for keys

        Returns:
            [RSAObject]: Array of RSAObject keys 
        """
        return [self.privateKey, self.publicKey]

    def set_keys(self, private_pem_key, public_pem_key):
        """Simple setter for private keys and public key from pem

        Args:
            private_pem_key ([pem]): Private key
            public_pem_key ([pem]): Public key
        """
        self.privateKey = load_pem_private_key('\n'.join(private_pem_key.splitlines()[1:-1]), password=None, backend=default_backend())
        self.publicKey = load_pem_public_key('\n'.join(public_pem_key.splitlines()[1:-1]))

    def generate_keys(self):
        """Generates keys, sets for class and returns in OpenSSL format

        Returns:
            [OpenSSL] : Array of keys in open ssl format
        """
        private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )
        
        self.privateKey = private_key
        self.publicKey = private_key.public_key()

        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        pub_pem = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return {"Private key" : pem, "Public key" : pub_pem}
    
    @staticmethod
    def generate_ssh_keys():
        """Generates new SSH keys

        Returns:
            [SSH]: Array of keys in SSH format
        """
        private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend())

        ssh = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_ssh = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        )

        return {"Private key" : ssh, "Public key" : public_ssh}

    def encrypt(self, text : str):
        """Encrypts text with set key

        Args:
            text (str): Text to encrypt

        Returns:
            (str): Encrypted text in hex
        """
        return self.publicKey.encrypt(base64.b64encode(text.encode('utf-8')), padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None)).hex() if self.publicKey != None else "Public key not set, please set the key :)"

    def decrypt(self, text): 
        """Decrypts text with set key

        Args:
            text (str): Hex text to decrypt

        Returns:
            (str): Decrypted key
        """
        print(self.privateKey.key_size)
        print(len(base64.b64decode(text.encode('utf-8'))))
        return self.privateKey.decrypt(
            base64.b64decode(text.encode('utf-8')), 
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
        )) if self.privateKey != None else "Private key not set, please set the key :)"

    def verify(self, signature, message):
        """Verify if the message was signed with given signature 

        Args:
            signature ([type]): Signature to verify
            message (str): Message to verify

        """
        
        prehashed_msg = hashlib.sha256(message.encode('ascii')).hexdigest()
        decoded_sig = base64.b64decode(signature)
        try:
            self.publicKey.verify(
                decoded_sig,
                bytes(prehashed_msg.encode('ascii')),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            ) if self.publicKey != None else "Public key not set, please set the key :)"
            return True
        except InvalidSignature: 
            return False

    def sign(self, message):
        """

        Args:
            message (str): Message to sign
            
        """
       
        return base64.b64encode(self.privateKey.sign(
            bytes(message, 'utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )) if self.privateKey != None else "Private key not set, please set the key :)"