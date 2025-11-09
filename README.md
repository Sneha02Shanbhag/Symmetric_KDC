# 🔐 Symmetric Key Distribution using KDC (Visual Simulation)

This project demonstrates **Symmetric Key Distribution using a Key Distribution Center (KDC)** with an interactive **graphical dashboard**.  
It visually explains how Alice and Bob obtain a **shared session key** through the KDC, and then use that key to **encrypt and securely exchange messages**.

---

## 🎯 Features

- Single unified **visual dashboard**
- **Animated communication flow arrows**
- Step-by-step guided process:
  1. Generate Session Key (KDC → Alice)
  2. Send Ticket to Bob (Alice → Bob)
  3. Secure Encrypted Messaging (Alice ↔ Bob)
- Ticket explanation popup for viva clarity
- Clean & modern **CustomTkinter UI**
- Uses **Fernet symmetric encryption**

---

## 🏛 System Architecture

| Entity | Description |
|-------|-------------|
| **Alice** | Initiates secure communication |
| **KDC** | Generates and distributes session key |
| **Bob** | Receives session key securely |

Session key (`K_s`) is encrypted and exchanged using **pre-shared master keys**.

---

## 📁 Folder Structure

KDC-Symmetric-Key-Distribution/
-│
-├── requirements.txt
-└── src/
├── main.py
├── kdc.py
└── client.py

---

## ⬇️ Clone the Repository

```bash
git clone https://github.com/<your-username>/KDC-Symmetric-Key-Distribution.git
cd KDC-Symmetric-Key-Distribution
```

## 📦 Install Dependencies

pip install customtkinter cryptography
---

## ▶️ Run the Project
-cd src
-python main.py



