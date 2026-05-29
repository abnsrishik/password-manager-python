from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from password_generator import PasswordGenerator
FONT = ("Arial",20,'normal')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    password_class = PasswordGenerator()
    generated_password = password_class.create_password()
    password_entry.insert(0,generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear():
    website_entry.delete(0,END)
    password_entry.delete(0,END)

def save():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            'email' : email,
            'password' : password,
        }
    }
    if len(password) != 0 and len(website) != 0:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: "
                                                                   f"\nWebsite: {website} \nEmail: {email}\nPassword: {password}.")
        if is_ok:
            try:
                with open("data.json", 'r') as data_file:
                    #Reading our old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json",'w') as data_file:
                    json.dump(new_data, data_file,indent=4)

            except JSONDecodeError:
                with open("data.json",'w') as data_file:
                    json.dump(new_data, data_file,indent=4)

            else:
                # updating with new data
                data.update(new_data)
                # saving the updated data
                with open("data.json",'w') as data_file:
                    json.dump(data, data_file,indent=4)
            finally:
                clear()
    else:
        messagebox.askokcancel(title="OOPS", message="Please don't leave any fields empty.")


# ---------------------------- Search PASSWORD  ------------------------------- #
def search_password():
    website = website_entry.get().lower()
    try:
        with open("data.json", 'r') as data_file:
            # Reading our old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}"
                                                                f"\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PassWord Manager")
window.config(padx=50, pady= 50, bg = "white",highlightthickness=0)

canvas = Canvas(width=200, height= 200,bg = "white",highlightthickness = 0)
lock_image = PhotoImage(file ="logo.png")
canvas.create_image(100,100, image = lock_image)
canvas.grid(row=0,column=1)

#labels
website_label = Label(text = "Website:",bg = "white", highlightthickness = 0)
website_label.grid(row = 1, column= 0)

email_label = Label(text = "Email/Username:",bg = "white", highlightthickness = 0)
email_label.grid(row = 2, column= 0)

password_label = Label(text = "Password:",bg = "white", highlightthickness = 0)
password_label.grid(row = 3, column= 0)

#entries
website_entry = Entry(width=30,bg = "white", highlightthickness = 0)
website_entry.grid(row = 1, column= 1)
website_entry.focus()

email_entry = Entry(width=30,bg = "white",highlightthickness = 0)
email_entry.grid(row = 2, column= 1)
email_entry.insert(0, "rishikcr72401@gmail.com")

password_entry = Entry(width=17,bg = "white", highlightthickness = 0)
password_entry.grid(row = 3, column= 1)

#buttons
generate_password = Button(text = "Generate Password",bg = "white", highlightthickness = 0, command=password)
generate_password.grid(row = 3, column=2)

add = Button(width=36, text="Add",bg = "white", highlightthickness = 0, command= save)
add.grid(row = 4, column= 1, columnspan=2)

search = Button(width = 14, text = "Search", bg = "white", highlightthickness = 0, command= search_password)
search.grid(row = 1, column=2)

window.mainloop()