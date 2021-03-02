import tkinter as tk
import tkinter.messagebox
import string,random


class App(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title("Password Generator")
        self.geometry("350x200")
        self.resizable(False,False)
        self.iconbitmap("icon.icns")
        
        #---------- Variabes -----------#
        self.letters_count_var = tk.IntVar()
        self.numbers_count_var = tk.IntVar()
        self.characters_count_var = tk.IntVar()
        self.password_var = tk.StringVar()
        #---------- Variabels -----------#


        #------------------------------ Fields ---------------------------------#
        #---------- Letters Field -----------#
        self.letters_frame = tk.Frame(self)
        self.letters_count_label = tk.Label(self.letters_frame,text="Letters count",fg="black")
        self.letters_count_label.pack(side=tk.LEFT,padx=10)
        self.letters_count_entry = tk.Entry(self.letters_frame,textvariable=self.letters_count_var)
        self.letters_count_entry.focus()
        self.letters_count_entry.select_range(0,tk.END)
        self.letters_count_entry.pack(side=tk.RIGHT,padx=10)
        self.letters_frame.pack(side=tk.TOP,fill=tk.X)
        #---------- Letters Field -----------#

        #---------- Numbers Field -----------#
        self.numbers_frame = tk.Frame(self)
        self.numbers_count_label = tk.Label(self.numbers_frame,text="Numbers count",fg="black")
        self.numbers_count_label.pack(side=tk.LEFT,padx=10)
        self.numbers_count_entry = tk.Entry(self.numbers_frame,textvariable=self.numbers_count_var)
        self.numbers_count_entry.pack(side=tk.RIGHT,padx=10)
        self.numbers_frame.pack(side=tk.TOP,fill=tk.X)
        #---------- Numbers Field -----------#

        #---------- Characters Field -----------#
        self.charachters_frame = tk.Frame(self)
        self.charachters_count_label = tk.Label(self.charachters_frame,text="Charachters count",fg="black")
        self.charachters_count_label.pack(side=tk.LEFT,padx=10)
        self.charachters_count_entry = tk.Entry(self.charachters_frame,textvariable=self.characters_count_var)
        self.charachters_count_entry.pack(side=tk.RIGHT,padx=10)
        self.charachters_frame.pack(side=tk.TOP,fill=tk.X)
        #---------- Characters Field -----------#

        #---------- Result Field -----------#
        self.result_frame = tk.Frame(self)
        self.result_label = tk.Label(self.result_frame,text="Password",fg="black")
        self.result_label.pack(side=tk.LEFT,padx=10)
        self.result_entry = tk.Entry(self.result_frame,state="disabled",textvariable=self.password_var)
        self.result_entry.pack(side=tk.RIGHT,padx=10)
        self.result_frame.pack(side=tk.TOP,fill=tk.X)
        #---------- Result Field -----------#
        #------------------------------ Fields ---------------------------------#


        #------------------------------ Buttons ---------------------------------#
        self.buttons_frame = tk.Frame(self)
        self.generate_button = tk.Button(self.buttons_frame,text="Generate",fg="black",command=self.generate_password)
        self.generate_button.pack(side=tk.LEFT,padx=3)
        self.rest_button = tk.Button(self.buttons_frame,text="Rest",fg="black",command=self.rest)
        self.rest_button.pack(side=tk.LEFT,padx=3)
        self.copy_button = tk.Button(self.buttons_frame,text="Copy",fg="black",command=self.copy)
        self.copy_button.pack(side=tk.LEFT,padx=3)
        self.close_button = tk.Button(self.buttons_frame,text="Close",fg="black",command=self.close)
        self.close_button.pack(side=tk.LEFT,padx=3)
        self.buttons_frame.pack(side=tk.TOP,fill=tk.X)
        #------------------------------ Buttons ---------------------------------#

    def generate_password(self):
        """
        Generate random password depends on letters and numbers and characters counts
        """
        l= self.letters_count_var.get()
        n= self.numbers_count_var.get()
        c= self.characters_count_var.get()
        
        all_letters = string.ascii_letters
        all_numbers = string.digits
        all_characters = string.punctuation

        if l > len(all_letters) or n > len(all_numbers) or c > len(all_characters):
            tk.messagebox.showerror("Error","Please enter valid values")
            return None
        else:
            choises_letters = random.sample(all_letters,l)
            choises_numbers = random.sample(all_numbers,n)
            choises_characters = random.sample(all_characters,c)
            
            all_data = []
            all_data.extend(choises_letters)
            all_data.extend(choises_numbers)
            all_data.extend(choises_characters)
            
            random.shuffle(all_data)
            
            password = ""
            for i in all_data:
                password+=i
            self.password_var.set(password)

    def rest(self):
        """
        Rest everything to default value
        """
        self.letters_count_var.set(0)
        self.numbers_count_var.set(0)
        self.characters_count_var.set(0)
        self.password_var.set("")
        self.letters_count_entry.focus()
        self.letters_count_entry.select_range(0,tk.END)

    def copy(self):
        if len(self.password_var.get()) != 0:
            self.clipboard_clear()
            self.clipboard_append(self.password_var.get())
            tk.messagebox.showinfo("Password is ready","Password is copied")
        else:
            tk.messagebox.showerror(title="Error",message="Please generate password first",icon="error")
    def close(self):
        self.destroy()
    

app = App()
app.mainloop()

