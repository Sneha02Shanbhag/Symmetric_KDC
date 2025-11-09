from cryptography.fernet import Fernet
import json

class KDC:
    def __init__(self):
        self.master_keys = {
            "Alice": Fernet.generate_key(),
            "Bob": Fernet.generate_key()
        }

    def generate_session_key(self):
        return Fernet.generate_key()

    def create_ticket(self, requester, receiver):
        session_key = self.generate_session_key()

        f_req = Fernet(self.master_keys[requester])
        f_rec = Fernet(self.master_keys[receiver])

        ticket_for_bob = f_rec.encrypt(json.dumps({
            "session_key": session_key.decode(),
            "from": requester
        }).encode()).decode()

        encrypted_for_alice = f_req.encrypt(json.dumps({
            "session_key": session_key.decode(),
            "receiver": receiver,
            "ticket": ticket_for_bob
        }).encode())

        return encrypted_for_alice
