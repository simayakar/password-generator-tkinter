from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_input = website_entry.get()
    mail_username_input = mail_username_entry.get()
    password_input = password_entry.get()

    if len(website_input) == 0 or len(mail_username_input) == 0 or len(password_input) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"Details entered: \nEmail: "
                                                         f"{mail_username_input}\nPassword: {password_input}\n\nIs it ok to save? ")
        if is_ok:
            website_entry.delete(0, END)
            mail_username_entry.delete(0, END)
            password_entry.delete(0, END)

            with open("data.txt", "a") as data_file:
                data_file.write(website_input + " | " + mail_username_input + " | " + password_input + "\n")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

mail_username_label = Label(text="Email/Username:")
mail_username_label.grid(row=2, column=0)

mail_username_entry = Entry(width=35)
mail_username_entry.insert(0, "@gmail.com")
mail_username_entry.grid(row=2, column=1, columnspan=2)


password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()