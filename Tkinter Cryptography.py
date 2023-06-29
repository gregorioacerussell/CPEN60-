from cryptography.fernet import Fernet
import customtkinter as ctk
import tkinter as tk

# Create the main window
ctkwindow = ctk.CTk()
ctkwindow.title('Capsule Proposal')
ctkwindow.geometry('600x450')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# widgets
frame = ctk.CTkFrame(master=ctkwindow, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label1 = ctk.CTkLabel(master=frame, text="Password Encryptor", font=('Century Gothic', 20))
label1.place(x=60, y=40)

entry1 = ctk.CTkEntry(master=frame, width=220, placeholder_text="Enter a password to encrypt", show='•')
entry1.place(x=50, y=80)

def password_visibility1():
    show_password = checkbox1.get()
    if show_password:
        entry1.configure(show='')
        entry2.configure(show='')
    else:
        entry1.configure(show='•')
        entry2.configure(show='•')

checkbox1 = ctk.CTkCheckBox(master=frame, command=password_visibility1, checkbox_height=20, checkbox_width=20, text='Show Password')
checkbox1.place(x=50, y=150)

entry2 = ctk.CTkEntry(master=frame, width=220, placeholder_text="Confirm password", show='•')
entry2.place(x=50, y=115)

label2 = ctk.CTkLabel(master=frame, text="make security your priority", font=('Lorem Ipsum', 11, 'italic'), text_color='gray')
label2.place(x=90, y=175)

entry3 = ctk.CTkEntry(master=frame, width=220, placeholder_text="                  Encrypted Text", show='')
entry3.place(x=50, y=210)

label3 = None

# encryption process
def encryption():
    global label3
    plaintext1 = entry1.get().strip()
    plaintext2 = entry2.get().strip()
    if not plaintext1 or not plaintext2:
        if label3 is not None:
            label3.destroy()
        label3 = ctk.CTkLabel(master=frame, text="Note: Please enter a password in both fields", font=('Lorem Ipsum', 11, 'italic'), text_color='red')
        label3.place(x=50, y=280)
        return
    if plaintext1 != plaintext2:
        if label3 is not None:
            label3.destroy()
        label3 = ctk.CTkLabel(master=frame, text="Note: Passwords do not match", font=('Lorem Ipsum', 11, 'italic'), text_color='red')
        label3.place(x=50, y=280)
        return
    if label3 is not None:
        label3.destroy()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    plain_text = entry1.get().encode()
    cipher_text = cipher_suite.encrypt(plain_text)
    entry3.delete(0, tk.END)
    entry3.insert(0, cipher_text)

button1 = ctk.CTkButton(master=frame, width=220, text='Encrypt', corner_radius=6, command=encryption)
button1.place(x=50, y=250)

# run
ctkwindow.mainloop()
