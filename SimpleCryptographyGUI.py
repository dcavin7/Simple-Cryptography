from tkinter import *
from simpleCryptography import *

# TO DO:
# - Finish Caesar window layout
# - Finish Atbash window layout
# - Finish Scytale window layout
# - Finish Caesar window functionality
# - Finish Atbash window functionality
# - Finish Scytale window functionality
# - Add buttons that open cipher descriptions / help windows
# --- Link to respective Wikipedia pages
# - Button to capitalize and/or remove spaces

class CaesarWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Caesar Cipher")
        self.geometry("255x300")

        cae_shift_label = Label(self, text = "Shift amount:")
        cae_shift_label.grid(row=0, column=0, pady = 5)

        cae_shift_entry = Entry(self, width = 10)
        cae_shift_entry.grid(row=0, column=1)

        cae_text_label = Label(self, text = "Text to encrypt/decrypt:")
        cae_text_label.grid(row=1, columnspan=2)

        cae_text_entry = Text(self, height = 5, width = 30)
        cae_text_entry.grid(row=2, columnspan=2, pady = 5, padx = 5)

        # WORK IN PROGRESS
        cae_result_button = Button(self, text = "Get Result")
        cae_result_button.grid(row=3, column=0, columnspan=2)

        cae_result_frame = LabelFrame(self, text = "Result")
        cae_result_frame.grid(row=4, column = 0, columnspan = 2, pady = 15)

        cae_result_label = Label(cae_result_frame, text = "work in progress")
        cae_result_label.pack()

class AtbashWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Atbash Cipher")
        self.geometry("300x300")
        label = Label(self, text = "Atbash Cipher Encryption and Decryption")
        label.pack()

class ScytaleWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Scytale Cipher")
        self.geometry("300x300")
        label = Label(self, text = "Scytale Cipher Encryption and Decryption")
        label.pack()

root = Tk()
root.title('Simple Cryptography')
root.geometry('300x200')

welcome_label = Label(root, text = "Welcome!")
welcome_label.pack(fill = "both", expand = "yes")

frame = LabelFrame(root, text = "Please choose a cipher type.")
frame.pack(expand = True)

caesar_button = Button(frame, text = "Caesar")
atbash_button = Button(frame, text = "Atbash")
scytale_button = Button(frame, text = "Scytale")

caesar_button.bind("<Button>", lambda cae_w: CaesarWindow(root))
atbash_button.bind("<Button>", lambda atb_w: AtbashWindow(root))
scytale_button.bind("<Button>", lambda scy_w: ScytaleWindow(root))

caesar_button.grid(column = 0, row = 0, padx = 5, pady = 10)
atbash_button.grid(column = 1, row = 0, padx = 5, pady = 10)
scytale_button.grid(column = 2, row = 0, padx = 5, pady = 10)



root.mainloop()