from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

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
        self.privateKey = load_pem_private_key(private_pem_key, password=None, backend=default_backend())
        self.publicKey = load_pem_public_key(public_pem_key)

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
        backend=default_backend()
        )
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
        return self.publicKey.encrypt(text.encode('utf-8'), padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None)).hex() if self.publicKey != None else "Public key not set, please set the key :)"

    def decrypt(self, text : str): 
        """Decrypts text with set key

        Args:
            text (str): Hex text to decrypt

        Returns:
            (str): Decrypted key
        """
        return self.privateKey.decrypt(text, padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )) if self.privateKey != None else "Private key not set, please set the key :)"

    def verify(self, signature, message : str):
        """Verify if the message was signed with given signature 

        Args:
            signature ([type]): Signature to verify
            message (str): Message to verify

        """
        return self.publicKey.verify(
            signature,
            message.encode('UTF-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        ) if self.publicKey != None else "Public key not set, please set the key :)"

    def sign(self, message: str):
        """

        Args:
            message (str): Message to sign
            
        """
        return self.privateKey.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        ) if self.privateKey != None else "Private key not set, please set the key :)"