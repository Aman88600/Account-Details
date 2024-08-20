import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")

def button_function():
    print("button pressed")
    button1 = customtkinter.CTkButton(master=app, text="new Button")
    button1.pack()
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.pack()

app.mainloop()