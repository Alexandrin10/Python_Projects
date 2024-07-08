import onetimepad
from tkinter import *
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64encode, b64decode

root = Tk()
root.title("CipherLab")
root.geometry("850x550")

background_image = PhotoImage(file="cyber_background.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# One-time pad functions
def encryptMessage():
    pt = e1.get("1.0", END).strip()
    ct = onetimepad.encrypt(pt, 'random')
    e2.delete("1.0", END)
    e2.insert("1.0", ct)

def decryptMessage():
    ct1 = e3.get("1.0", END).strip()
    pt1 = onetimepad.decrypt(ct1, 'random')
    e4.delete("1.0", END)
    e4.insert("1.0", pt1)

# AES functions
def aes_encrypt():
    pt = e5.get("1.0", END).strip().ljust(32)  # pad the plaintext to 32 bytes
    key = b'Sixteen byte key'  # AES requires a 16 byte key
    cipher = AES.new(key, AES.MODE_ECB)
    ct = b64encode(cipher.encrypt(pt.encode('utf-8'))).decode('utf-8')
    e6.delete("1.0", END)
    e6.insert("1.0", ct)

def aes_decrypt():
    ct = b64decode(e7.get("1.0", END).strip())
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(ct).decode('utf-8').strip()
    e8.delete("1.0", END)
    e8.insert("1.0", pt)

# RSA functions
def rsa_encrypt():
    pt = e9.get("1.0", END).strip()
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    ct = b64encode(cipher.encrypt(pt.encode('utf-8'))).decode('utf-8')
    e10.delete("1.0", END)
    e10.insert("1.0", ct)
    global private_key
    private_key = key.export_key()  # save the private key for decryption

def rsa_decrypt():
    ct = b64decode(e11.get("1.0", END).strip())
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    pt = cipher.decrypt(ct).decode('utf-8')
    e12.delete("1.0", END)
    e12.insert("1.0", pt)

# Caesar cipher functions
def caesar_encrypt():
    pt = e13.get("1.0", END).strip()
    shift = int(e15.get())
    ct = ''.join([chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper()
                  else chr((ord(char) - 97 + shift) % 26 + 97) if char.islower()
                  else char for char in pt])
    e14.delete("1.0", END)
    e14.insert("1.0", ct)

def caesar_decrypt():
    ct = e14.get("1.0", END).strip()
    shift = int(e15.get())
    pt = ''.join([chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper()
                  else chr((ord(char) - 97 - shift) % 26 + 97) if char.islower()
                  else char for char in ct])
    e16.delete("1.0", END)
    e16.insert("1.0", pt)

# GUI setup
label1 = Label(root, text='Plain Text', fg='white', bg='black', highlightthickness=0)
label1.grid(row=0, column=1)
label2 = Label(root, text='Encrypted Text', fg='white', bg='black', highlightthickness=0)
label2.grid(row=1, column=1)
label3 = Label(root, text='Cipher Text', fg='white', bg='black', highlightthickness=0)
label3.grid(row=0, column=3)
label4 = Label(root, text='Decrypted Text', fg='white', bg='black', highlightthickness=0)
label4.grid(row=1, column=3)

e1 = Text(root, height=2, width=30)
e1.grid(row=0, column=2)
e2 = Text(root, height=2, width=30)
e2.grid(row=1, column=2)
e3 = Text(root, height=2, width=30)
e3.grid(row=0, column=4)
e4 = Text(root, height=2, width=30)
e4.grid(row=1, column=4)

ent = Button(root, text="Encrypt OTP", bg="red", fg="white", command=encryptMessage)
ent.grid(row=2, column=2)
b2 = Button(root, text="Decrypt OTP", bg="green", fg="white", command=decryptMessage)
b2.grid(row=2, column=4)

# AES Section
label5 = Label(root, text='Plain Text', fg='white', bg='black', highlightthickness=0)
label5.grid(row=3, column=1)
label6 = Label(root, text='Encrypted Text', fg='white', bg='black', highlightthickness=0)
label6.grid(row=4, column=1)
label7 = Label(root, text='Cipher Text', fg='white', bg='black', highlightthickness=0)
label7.grid(row=3, column=3)
label8 = Label(root, text='Decrypted Text', fg='white', bg='black', highlightthickness=0)
label8.grid(row=4, column=3)

e5 = Text(root, height=2, width=30)
e5.grid(row=3, column=2)
e6 = Text(root, height=2, width=30)
e6.grid(row=4, column=2)
e7 = Text(root, height=2, width=30)
e7.grid(row=3, column=4)
e8 = Text(root, height=2, width=30)
e8.grid(row=4, column=4)

ent_aes = Button(root, text="Encrypt AES", bg="red", fg="white", command=aes_encrypt)
ent_aes.grid(row=5, column=2)
b2_aes = Button(root, text="Decrypt AES", bg="green", fg="white", command=aes_decrypt)
b2_aes.grid(row=5, column=4)

# RSA Section
label9 = Label(root, text='Plain Text', fg='white', bg='black', highlightthickness=0)
label9.grid(row=6, column=1)
label10 = Label(root, text='Encrypted Text', fg='white', bg='black', highlightthickness=0)
label10.grid(row=7, column=1)
label11 = Label(root, text='Cipher Text', fg='white', bg='black', highlightthickness=0)
label11.grid(row=6, column=3)
label12 = Label(root, text='Decrypted Text', fg='white', bg='black', highlightthickness=0)
label12.grid(row=7, column=3)

e9 = Text(root, height=2, width=30)
e9.grid(row=6, column=2)
e10 = Text(root, height=2, width=30)
e10.grid(row=7, column=2)
e11 = Text(root, height=2, width=30)
e11.grid(row=6, column=4)
e12 = Text(root, height=2, width=30)
e12.grid(row=7, column=4)

ent_rsa = Button(root, text="Encrypt RSA", bg="red", fg="white", command=rsa_encrypt)
ent_rsa.grid(row=8, column=2)
b2_rsa = Button(root, text="Decrypt RSA", bg="green", fg="white", command=rsa_decrypt)
b2_rsa.grid(row=8, column=4)

# Caesar Cipher Section
label13 = Label(root, text='Plain Text', fg='white', bg='black', highlightthickness=0)
label13.grid(row=9, column=1)
label14 = Label(root, text='Encrypted Text', fg='white', bg='black', highlightthickness=0)
label14.grid(row=10, column=1)
label15 = Label(root, text='Shift', fg='white', bg='black', highlightthickness=0)
label15.grid(row=9, column=3)
label16 = Label(root, text='Decrypted Text', fg='white', bg='black', highlightthickness=0)
label16.grid(row=10, column=3)

e13 = Text(root, height=2, width=30)
e13.grid(row=9, column=2)
e14 = Text(root, height=2, width=30)
e14.grid(row=10, column=2)
e15 = Entry(root, width=30)  # Use Entry for single line input
e15.grid(row=9, column=4)
e16 = Text(root, height=2, width=30)  # Corrected grid position
e16.grid(row=10, column=4)

ent_caesar = Button(root, text="Encrypt Caesar", bg="red", fg="white", command=caesar_encrypt)
ent_caesar.grid(row=11, column=2)
b2_caesar = Button(root, text="Decrypt Caesar", bg="green", fg="white", command=caesar_decrypt)
b2_caesar.grid(row=11, column=4)

root.mainloop()

