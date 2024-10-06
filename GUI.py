import tkinter as tk
import backend as back
from time import sleep as s

# Create the main window
root = tk.Tk()
root.title("decimal_hexa_binary")
root.geometry("600x350")

# Create a label widget
title = tk.Label(
    root, 
    text="Please click on \n1 for decimal to binary \n2 for decimal to hexadecimal \n3 for binary to decimal \n4 hexadecimal to decimal \n5 for hexadecimal to binary \n6 binary to hexadecimal \n",
    anchor="w",                
    justify="left",
    font=("Ariel", 15)
)
title.pack()

# State variables
mode = ""
pressed = False  # Tracks whether a main button is pressed
button_pressed = tk.StringVar()

# A global reference to Yes/No buttons
buttonY = None
buttonN = None

# Handle main button click
def on_button_click(button_id):
    global pressed
    if not pressed:  # Prevent multiple actions from overlapping
        button_pressed.set(button_id)
        is_sure()
        pressed = True  # Set pressed to True when a button is clicked
        make_yes_or_no_buttons()

def is_sure():
    # Update title to reflect user's selection and prompt confirmation
    title.config(text=f"You clicked {button_pressed.get()}. \nAre you sure?")

    global mode

    mode = button_pressed.get()

# Create and manage Yes/No buttons
def make_yes_or_no_buttons():
    global buttonY, buttonN
    # Hide the main conversion buttons
    for i in range(1, 7):
        button_name = f"button{i}"
        globals()[button_name].grid_forget()

    # Create Yes/No buttons
    buttonY = tk.Button(button_frame, text="Yes", command=lambda: handle_confirmation(True))
    buttonY.grid(row=0, column=0, padx=10, pady=10)

    buttonN = tk.Button(button_frame, text="No", command=lambda: handle_confirmation(False))
    buttonN.grid(row=0, column=1, padx=10, pady=10)

# Handle the Yes/No confirmation
def handle_confirmation(is_yes):
    global pressed, buttonY, buttonN
    # Destroy Yes/No buttons
    if buttonY and buttonN:
        buttonY.destroy()
        buttonN.destroy()

    # Process user's confirmation
    if is_yes:
        # Call conversion or additional logic here
        put_label_and_text_area()
    else:
        title.config(text="Please make another selection.")
        pressed = False  # Reset pressed state so new buttons can be clicked
        reset_main_buttons()

# Reset main buttons after Yes/No are handled
def reset_main_buttons():
    global pressed
    pressed = False  # Reset flag to allow new clicks
    # Recreate the main buttons
    title.config(text="Please click on \n1 for decimal to binary \n2 for decimal to hexadecimal \n3 for binary to decimal \n4 hexadecimal to decimal \n5 for hexadecimal to binary \n6 binary to hexadecimal \n")
    button1.grid(row=0, column=0, padx=10, pady=10)
    button2.grid(row=0, column=1, padx=10, pady=10)
    button3.grid(row=1, column=0, padx=10, pady=10)
    button4.grid(row=1, column=1, padx=10, pady=10)
    button5.grid(row=2, column=0, padx=10, pady=10)
    button6.grid(row=2, column=1, padx=10, pady=10)

# Just for demonstration: creating entry fields after confirmation
def put_label_and_text_area():

    global entry, result, convert_button, back

    title.config(text=f"Please enter your input:")

    entry = tk.Entry(button_frame, width=40)
    entry.grid(row=1, column=1, padx=10, pady=10)

    convert_button = tk.Button(button_frame, text="Convert", command=lambda: convert(convert=button_pressed.get()))
    convert_button.grid(row=2, column=1, padx=10, pady=10)

    result = tk.Label(button_frame, text="", width=30)
    result.grid(row=3, column=1, padx=10, pady=10)

    back = tk.Button(button_frame, text="Back", command=lambda: go_back())
    back.grid(row=4, column=1, padx=10, pady=10)

def convert(convert):

    if convert == "1. decimal to binary conversion":
        result1 = back.decimal_to_binary(int(entry.get()))

    elif convert == "2. decimal to hexadecimal conversion":
        result1 = back.decimal_to_hexadecimal(int(entry.get()))

    elif convert == "3. binary to decimal conversion":
        result1 = back.binary_to_decimal(int(entry.get()))

    elif convert == "4. hexadecimal to decimal conversion":
        result1 = back.hexadecimal_to_decimal(entry.get())

    elif convert == "5. hexadecimal to binary conversion":
        result1 = back.hexadecimal_to_binary(entry.get())

    elif convert == "6. binary to hexadecimal conversion":
        result1 = back.binary_to_hexadecimal(int(entry.get()))

    result.config(text=f"Result: {result1}")


def go_back():

    global convert_button, entry, result, back

    convert_button.grid_forget()
    entry.grid_forget()
    result.grid_forget()
    back.grid_forget()

    reset_main_buttons()



# Create the main buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

button1 = tk.Button(button_frame, text="1. decimal to binary conversion", command=lambda: on_button_click("1. decimal to binary conversion"))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(button_frame, text="2. decimal to hexadecimal conversion", command=lambda: on_button_click("2. decimal to hexadecimal conversion"))
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(button_frame, text="3. binary to decimal conversion", command=lambda: on_button_click("3. binary to decimal conversion"))
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = tk.Button(button_frame, text="4. hexadecimal to decimal conversion", command=lambda: on_button_click("4. hexadecimal to decimal conversion"))
button4.grid(row=1, column=1, padx=10, pady=10)

button5 = tk.Button(button_frame, text="5. hexadecimal to binary conversion", command=lambda: on_button_click("5. hexadecimal to binary conversion"))
button5.grid(row=2, column=0, padx=10, pady=10)

button6 = tk.Button(button_frame, text="6. binary to hexadecimal conversion", command=lambda: on_button_click("6. binary to hexadecimal conversion"))
button6.grid(row=2, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()