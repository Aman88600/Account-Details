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
        details["name"] = str(output)
        print(details)
        with open("data.json", "w") as fp:
            json.dump(details, fp, indent=4)

name = customtkinter.CTkEntry(app, placeholder_text="Enter Your Name", width = 200)
name.grid(row = 0, column = 0, padx = 100, pady = 20)
name_button = customtkinter.CTkButton(app, text = "Enter", width = 200, command = set_name)
name_button.grid(row=1, column=0, padx = 100)
app.mainloop()