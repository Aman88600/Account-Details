import customtkinter
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.minsize(400, 200)

# Setting Title of the screen
app.title("Account Details")

def set_name():
    output = name.get()
    details = {}
    if output:
        details["Entry"] = str(output)
        print(details)
        count = 2
        new_entry = customtkinter.CTkButton(app, text = output, width = 200)
        # new_entry.grid(row = count, column = 0, padx = 100, pady = 20)
        new_entry.pack()
        count += 1
        with open("data.json", "w") as fp:
            json.dump(details, fp, indent=4)

name = customtkinter.CTkEntry(app, placeholder_text="Entry Name", width = 200)
# name.grid(row = 0, column = 0, padx = 100, pady = 20)
name.pack()
name_button = customtkinter.CTkButton(app, text = "Create New Entry", width = 200, command = set_name)
# name_button.grid(row=1, column=0, padx = 100)
name_button.pack()
app.mainloop()