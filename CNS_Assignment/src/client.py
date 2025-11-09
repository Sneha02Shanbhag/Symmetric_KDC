from cryptography.fernet import Fernet
import json

class Client:
    def __init__(self, name, kdc):
        self.name = name
        self.kdc = kdc
        self.master_key = kdc.master_keys[name]
        self.session_key = None

    def request_key(self, receiver):
        return self.kdc.create_ticket(self.name, receiver)

    def receive_from_kdc(self, msg):
        f = Fernet(self.master_key)
        data = json.loads(f.decrypt(msg).decode())
        self.session_key = data["session_key"].encode()
        return data["ticket"]

    def receive_ticket(self, ticket):
        f = Fernet(self.master_key)
        data = json.loads(f.decrypt(ticket.encode()).decode())
        self.session_key = data["session_key"].encode()

    def encrypt(self, msg):
        return Fernet(self.session_key).encrypt(msg.encode()).decode()

    def decrypt(self, msg):
        return Fernet(self.session_key).decrypt(msg.encode()).decode()
