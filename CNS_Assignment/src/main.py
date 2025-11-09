import customtkinter as ctk
from kdc import KDC
from client import Client
from tkinter import messagebox

def show_ticket_explanation():
    messagebox.showinfo(
        "🎟️ What is the Ticket?",
        "The session key (K_s) is created by the KDC.\n\n"
        "Alice needs K_s + Bob must also get K_s securely.\n\n"
        "So KDC encrypts the session key twice:\n"
        "  • One copy is encrypted with Alice's master key KA.\n"
        "  • One copy (called TICKET) is encrypted with Bob's master key KB.\n\n"
        "Alice cannot read or modify the ticket.\n"
        "She simply forwards it to Bob.\n"
        "Bob decrypts his ticket using KB and obtains the same session key.\n\n"
        "This ensures **secure key distribution** ✅"
    )

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk(fg_color="#f5f7fb")
app.title("🔐 Symmetric Key Distribution using KDC (Visual Flow)")
app.geometry("1000x600")

kdc = KDC()
alice = Client("Alice", kdc)
bob = Client("Bob", kdc)
ticket = None

# Title
ctk.CTkLabel(app, text="🔐 Symmetric Key Distribution with KDC", font=("Arial", 26, "bold")).pack(pady=10)

# Canvas for arrows
canvas = ctk.CTkCanvas(app, width=900, height=100, bg="#a3f2e5", highlightthickness=0)
canvas.pack(pady=5)

# Draw static nodes
canvas.create_text(150, 50, text="👩 Alice", font=("Arial", 18, "bold"))
canvas.create_text(450, 50, text="🏦 KDC", font=("Arial", 18, "bold"))
canvas.create_text(750, 50, text="🧑 Bob", font=("Arial", 18, "bold"))

# Draw arrows
arrow1 = canvas.create_line(200, 50, 400, 50, arrow="last", width=3, fill="gray")
arrow2 = canvas.create_line(500, 50, 700, 50, arrow="last", width=3, fill="gray")
arrow3 = canvas.create_line(200, 80, 700, 80, arrow="last", width=3, fill="gray")

status = ctk.CTkLabel(app, text="Step 1: Generate session key using KDC", font=("Arial", 14), text_color="red")
status.pack(pady=5)

# Main communication frame
frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=20, fill="both", expand=True)

# Alice Panel
alice_frame = ctk.CTkFrame(frame, corner_radius=12)
alice_frame.pack(side="left", fill="both", expand=True, padx=10)

ctk.CTkLabel(alice_frame, text="👩 Alice", font=("Arial", 20, "bold")).pack(pady=10)
alice_log = ctk.CTkTextbox(alice_frame, height=300, width=480)
alice_log.pack(pady=5, padx=10)

# Bob Panel
bob_frame = ctk.CTkFrame(frame, corner_radius=12)
bob_frame.pack(side="right", fill="both", expand=True, padx=10)

ctk.CTkLabel(bob_frame, text="🧑 Bob", font=("Arial", 20, "bold")).pack(pady=10)
bob_log = ctk.CTkTextbox(bob_frame, height=300,width=480)
bob_log.pack(pady=10, padx=10)

# Logic buttons
def animate_arrow(arrow, color):
    canvas.itemconfig(arrow, fill=color)
    app.after(1200, lambda: canvas.itemconfig(arrow, fill="light blue"))

def step1():
    global ticket
    enc = alice.request_key("Bob")
    ticket = alice.receive_from_kdc(enc)

    animate_arrow(arrow1, "blue")
    status.configure(text="Step 2: Send the ticket to Bob", text_color="orange")

    alice_log.insert("end", "✅ KDC generated session key and ticket.\n")
    alice_log.insert("end", "Click Step 2 to send ticket → Bob.\n\n")

    # Show popup explaining ticket
    show_ticket_explanation()


def step2():
    bob.receive_ticket(ticket)
    status.configure(text="Step 3: Secure communication established!", text_color="green")
    animate_arrow(arrow2, "green")
    alice_log.insert("end", "🎟️ Ticket sent securely to Bob.\n\n")
    bob_log.insert("end", "🔑 Bob now has the session key.\n\n")

def step3():
    msg = msg_entry.get()
    msg_entry.delete(0, "end")
    enc = alice.encrypt(msg)
    dec = bob.decrypt(enc)
    animate_arrow(arrow3, "purple")
    alice_log.insert("end", f"Alice → Bob\nPlain: {msg}\nEncrypted: {enc}\n\n")
    bob_log.insert("end", f"Bob decrypted: {dec}\n\n")

ctk.CTkButton(app, text="Step 1: Generate Session Key", command=step1, width=200).pack(pady=4)
ctk.CTkButton(app, text="Step 2: Send Ticket to Bob", command=step2, width=200).pack(pady=4)

msg_entry = ctk.CTkEntry(app, placeholder_text="Message to Bob…", width=400)
msg_entry.pack(pady=5)

ctk.CTkButton(app, text="Step 3: Send Secure Message", command=step3, width=200).pack(pady=6)

app.mainloop()
