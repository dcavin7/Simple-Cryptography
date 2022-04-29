from tkinter import *
from simpleCryptography import *

# TO DO:
# - Finish Scytale window layout
# - Finish Scytale window functionality
# - Button to capitalize and/or remove spaces?
# - Info window

class CaesarWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Caesar Cipher")
        # self.geometry("255x300")

        cae_shift_label = Label(self, text = "Shift amount:")
        cae_shift_label.grid(row=0, column=0, pady = 5)

        cae_shift_entry = Entry(self, width = 5)
        cae_shift_entry.grid(row=0, column=1)

        cae_dir = StringVar(self)
        cae_dir.set("Left")

        cae_shift_dir_menu = OptionMenu(self, cae_dir, "Left", "Right")
        cae_shift_dir_menu.config(width = 5)
        cae_shift_dir_menu.grid(row = 0, column = 2)

        cae_text_label = Label(self, text = "Text to encrypt/decrypt:")
        cae_text_label.grid(row=1, columnspan=3)

        cae_text_entry = Text(self, height = 5, width = 30)
        cae_text_entry.grid(row=2, columnspan=3, pady = 5, padx = 5)

        cae_result_text = "Your Result Here"

        def get_cae_result():
            try:
                input_shift = int(cae_shift_entry.get())
            except:
                input_shift = None
            shift_dir = cae_dir.get()
            input_text = cae_text_entry.get("1.0",'end-1c')
            cae_result_text = caesar(input_text, input_shift, shift_dir)
            cae_result_box.delete("1.0", END)
            cae_result_box.insert("1.0", cae_result_text)

        cae_result_button = Button(self, text = "Get Result", command = lambda: get_cae_result())
        cae_result_button.grid(row=3, column=0, columnspan=3)

        cae_result_frame = LabelFrame(self, text = "Result")
        cae_result_frame.grid(row=4, column = 0, columnspan = 3, pady = 15)

        cae_result_box = Text(cae_result_frame, height = 5, width = 30)
        cae_result_box.insert("1.0", cae_result_text)
        cae_result_box.pack()

class AtbashWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Atbash Cipher")
        # self.geometry("255x300")

        atb_text_label = Label(self, text = "Text to encrypt/decrypt:")
        atb_text_label.grid(row=1, columnspan=2)

        atb_text_entry = Text(self, height = 5, width = 30)
        atb_text_entry.grid(row=2, columnspan=2, pady = 5, padx = 5)

        atb_result_text = "Your Result Here"

        def get_atb_result():
            input_text = atb_text_entry.get("1.0",'end-1c')
            atb_result_text = atbash(input_text)
            atb_result_box.delete("1.0", END)
            atb_result_box.insert("1.0", atb_result_text)

        atb_result_button = Button(self, text = "Get Result", command = lambda: get_atb_result())
        atb_result_button.grid(row=3, column=0, columnspan=2)

        atb_result_frame = LabelFrame(self, text = "Result")
        atb_result_frame.grid(row=4, column = 0, columnspan = 2, pady = 15)

        atb_result_box = Text(atb_result_frame, height = 5, width = 30)
        atb_result_box.insert("1.0", atb_result_text)
        atb_result_box.pack()

class ScytaleWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Scytale Cipher")
        # self.geometry("300x300")

class BFCWindow(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Brute Force Caesar Decryption")
        bfc_label_1 = Label(self, text = "Et tu, Brute (force)?\n")
        bfc_label_1.grid(row=0)
        
        bfc_text_label = Label(self, text = "Text to decrypt:")
        bfc_text_label.grid(row=1)

        bfc_text_entry = Text(self, height = 5, width = 60)
        bfc_text_entry.grid(row=2, pady = 5, padx = 5)

        bfc_result_text = "Your Result Here"

        def get_bfc_result():
            input_text = bfc_text_entry.get("1.0",'end-1c')
            bfc_result_text = brute_force_caesar(input_text)
            bfc_result_box.delete("1.0", END)
            bfc_result_box.insert("1.0", bfc_result_text)

        bfc_result_button = Button(self, text = "Get Result", command = lambda: get_bfc_result())
        bfc_result_button.grid(row=3)

        bfc_result_frame = LabelFrame(self, text = "Result")
        bfc_result_frame.grid(row=4, pady = 15)

        bfc_result_box = Text(bfc_result_frame, height = 26, width = 60)
        bfc_result_box.insert("1.0", bfc_result_text)
        bfc_result_box.pack()

root = Tk()
root.title('Cryptography')
root.geometry('250x200')

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

extras_frame = LabelFrame(root, text = "Extras")
extras_frame.pack(expand = True)

bfc_button = Button(extras_frame, text = "Brute Force Caesar")
info_button = Button(extras_frame, text = "Info")

bfc_button.bind("<Button>", lambda bfc_w: BFCWindow(root))

bfc_button.grid(column = 0, row = 0, padx = 5, pady = 10)
info_button.grid(column = 1, row = 0, padx = 5, pady = 10)

root.mainloop()