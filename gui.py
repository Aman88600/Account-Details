import customtkinter
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.minsize(400, 200)

# Setting Title of the screen
app.title("Account Details")

# setting the counter
count = 0

def set_name():
    global count # Declare count as global to modify it
    output = name.get()
    if output:
        new_entry = customtkinter.CTkButton(app, text = output, width = 200)
        new_entry.pack()
        count += 1
        with open("data.json", "r") as file:
            data = json.load(file)
        data[f"{count}"] = output
        with open("data.json", "w") as file:
            json.dump(data, file, indent = 4)

name = customtkinter.CTkEntry(app, placeholder_text="Entry Name", width = 200)
name.pack()

name_button = customtkinter.CTkButton(app, text = "Create New Entry", width = 200, command = set_name)
name_button.pack()

app.mainloop()