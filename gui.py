import customtkinter as ctk
import json
from read_data import get_data
from enter_data import put_data
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.minsize(400, 200)

# Setting Title of the screen
app.title("Account Details")

# Create a canvas and a scrollbar
canvas = ctk.CTkCanvas(app)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ctk.CTkScrollbar(app, orientation="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the content inside the canvas
scrollable_frame = ctk.CTkFrame(canvas)

# Create a window to add inside the scrollable frame
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Update the scroll region of the canvas whenever the frame changes size
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind the configure event of the scrollable frame to update the canvas scroll region
scrollable_frame.bind("<Configure>", on_frame_configure)

# Function to create a new entry
def set_name():
    output = name.get()  # Get the name for the key
    section_number = section.get()  # Get the number of sections

    if output and section_number.isdigit():
        section_number = int(section_number)

        # Create a new window for the sections
        new_window = ctk.CTk()
        new_window.title(f"{output} Sections")
        new_window.geometry("400x300")

        sections = {}  # Initialize the sections dictionary outside the loop

        # Dynamically create sections in the new window
        def get_section():
            # Populate the sections dictionary with section name and data
            for i in range(section_number):
                section_name = section_names[i].get()  # Get the section name
                section_data = section_data_entries[i].get()  # Get the section data
                sections[section_name] = section_data  # Add to the sections dictionary

            # Store the data in a global dictionary (or save it to a file)
            put_data(output, sections)
            # stored_data[output] = sections
            # print(stored_data)  # Print the stored data

        section_names = []  # List to store entry widgets for section names
        section_data_entries = []  # List to store entry widgets for section data

        for i in range(section_number):
            section_label = ctk.CTkLabel(new_window, text=f"Section {i + 1}", font=("Arial", 20))
            section_label.pack(pady=10)

            # Entry for section name
            section_name = ctk.CTkEntry(new_window, placeholder_text=f"Enter Name for section {i + 1}", width=200)
            section_name.pack(pady=5)
            section_names.append(section_name)  # Add the entry to the list

            # Entry for section data
            section_data = ctk.CTkEntry(new_window, placeholder_text=f"Enter Data for section {i + 1}", width=200)
            section_data.pack(pady=5)
            section_data_entries.append(section_data)  # Add the entry to the list

        # Button to get the sections data
        name_button = ctk.CTkButton(new_window, text="Create New Entry", width=200, command=get_section)
        name_button.pack(pady=5)

        # Start the new window loop
        new_window.mainloop()

# Global dictionary to store the data
stored_data = {}

# Create the entry widgets and button
name = ctk.CTkEntry(scrollable_frame, placeholder_text="Entry Name", width=200)
name.pack(pady=5)

section = ctk.CTkEntry(scrollable_frame, placeholder_text="Section Number", width=200)
section.pack(pady=5)

name_button = ctk.CTkButton(scrollable_frame, text="Create New Entry", width=200, command=set_name)
name_button.pack(pady=5)

# Fetch and display data from the `get_data` function
data = get_data()
if data:
    for key, value in data.items():
        label = ctk.CTkLabel(scrollable_frame, text=f"{key}", font=("Arial", 24))
        label.pack(pady=5)
        for key1, value1 in value.items():
            label = ctk.CTkLabel(scrollable_frame, text=f"{key1}: {value1}", font=("Arial", 24))
            label.pack(pady=5)

# Start the main loop
app.mainloop()