import tkinter as tk
from PIL import Image, ImageTk
from Menu import display_menu  # Importing the function from Menu.py

def disable_maximize():
    root.resizable(False, False)  # Disallow resizing

def execute_second_program():
    # Call the function from Menu.py directly
    display_menu()
    # Close the window of the first program
    root.destroy()

# Create the Tkinter window
root = tk.Tk()
root.title("Imagica AI")
root.geometry("1300x700")
root.resizable(width=False, height=False)

# Load the background image
image = Image.open("background.png")  # Replace "background_image.jpg" with the path to your image
background_image = ImageTk.PhotoImage(image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.image = background_image  # Retain reference to the image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the position adjustments for the button
x_position = 350  # Adjust the x position
y_position = 450  # Adjust the y position

# Create a font for the button text
button_font = ("Helvetica", 14, "bold")  # Change the font as desired

# Create a button labeled "Get Started" at the adjusted position with the specified font
button = tk.Button(root, text="Get Started", font=button_font, width=13, height=2, command=execute_second_program)
button.place(x=x_position, y=y_position)

root.mainloop()
