from tkinter import *
from tkinter import messagebox
import string
import random


def reset_fields():
    textfield.delete(0, 25)
    length_textfield.delete(0, 25)
    generated_password_textfield.delete(0, 25)


def accepted():
    flag = generate_pass()
    if flag == 0:
        messagebox.showerror("Error", "Password can't be Encrypted")
        return
    else:
        messagebox.showinfo("Accepted", "Password Encrypted successfully")
        return


def generate_pass():
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    chars = list(string.punctuation)
    numbers = list(string.digits)
    name = textfield.get()
    length_ = length_textfield.get()
    ci = 0

    if name == "":
        messagebox.showerror("Error", "Name cannot be empty")
        return ci

    if not name.isalpha():
        messagebox.showerror("Error", "Name must be a string")
        textfield.delete(0, 25)
        return ci

    le = int(length_)

    if le < 6:
        messagebox.showerror("Error", "Password must be atleast 6 characters long")
        return ci
    else:
        ci = 1
        blank_label1.configure(text="")
        generated_password_textfield.delete(0, le)
        u = random.randint(1, le - 3)
        l = random.randint(1, le - 2 - u)
        c = random.randint(1, le - 1 - u - l)
        n = le - u - l - c
        password = random.sample(upper, u) + random.sample(lower, l) + random.sample(chars, c) + random.sample(numbers,
                                                                                                               n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        generated_password_textfield.insert(0, gen_passwd)
        return ci


root = Tk()
root.title('Password Generator')
root.geometry('660x500')
n_username = StringVar()
n_passwordlen = IntVar()
n_generatedpassword = StringVar()
label = Label(text="Password Generator", fg='darkblue', font='arial 20 bold underline')
label.grid(row=0, column=1)

blank_label1 = Label(text="")
blank_label1.grid(row=1, column=0, columnspan=2)

blank_label2 = Label(text="")
blank_label2.grid(row=2, column=0, columnspan=2)

blank_label2 = Label(text="")
blank_label2.grid(row=3, column=0, columnspan=2)

user = Label(text="Enter user name: ", font='times 15')
user.grid(row=4, column=0)

textfield = Entry(textvariable=n_username, font='times 15', bd=6, relief='ridge')
textfield.grid(row=4, column=1)
textfield.focus_set()

blank_label3 = Label(text="")
blank_label3.grid(row=5, column=0)

length = Label(text="Enter password length: ", font='times 15')
length.grid(row=6, column=0)

length_textfield = Entry(textvariable=n_passwordlen, font='times 15', bd=6, relief='ridge')
length_textfield.grid(row=6, column=1)

blank_label3 = Label(text="")
blank_label3.grid(row=5, column=0)

length = Label(text="Enter password length: ", font='times 15')
length.grid(row=6, column=0)

length_textfield = Entry(textvariable=n_passwordlen, font='times 15', bd=6, relief='ridge')
length_textfield.grid(row=6, column=1)

blank_label4 = Label(text="")
blank_label4.grid(row=7, column=0)

generated_password = Label(text="Generated password: ", font='times 15')
generated_password.grid(row=8, column=0)

generated_password_textfield = Entry(textvariable=n_generatedpassword, font='times 15', bd=6,
                                     relief='ridge', fg='darkgreen')
generated_password_textfield.grid(row=8, column=1)

blank_label5 = Label(text="")
blank_label5.grid(row=9, column=0)

blank_label6 = Label(text="")
blank_label6.grid(row=10, column=0)

generate = Button(text="GENERATE PASSWORD", bd=3, relief='solid', padx=1, pady=1, font='arial 15 bold',
                  fg='white', bg='darkblue', command=generate_pass)
generate.grid(row=11, column=1)

blank_label5 = Label(text="")
blank_label5.grid(row=12, column=0)

accept = Button(text="ACCEPT", bd=3, relief='solid', padx=1, pady=1, font='arial 15', fg='darkblue',
                bg='white', command=accepted)
accept.grid(row=13, column=1)

blank_label1 = Label(text="")
blank_label1.grid(row=14, column=1)

reset = Button(text="RESET", bd=3, relief='solid', padx=1, pady=1, font='arial 15', fg='darkblue',
               bg='white', command=reset_fields)
reset.grid(row=15, column=1)

root.mainloop()