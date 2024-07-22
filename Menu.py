import tkinter as tk
from PIL import Image, ImageTk
from Text_to_Image import ttoi
from Text_to_Anime import anime
from Text_to_Portrait import portrait
from Text_to_Vector import vector
from Image_to_Image import i2i
def display_menu():
    def disable_maximize():
        root.resizable(False, False)  # Disallow resizing

    def execute_text_to_image():
        # Call the function from Menu.py directly
        ttoi()
        # Close the window of the first program
        root.destroy()

    def execute_text_to_anime():
        # Call the function from Menu.py directly
        anime()
        # Close the window of the first program
        root.destroy()

    def execute_text_to_portrait():
        # Call the function from Menu.py directly
        portrait()
        # Close the window of the first program
        root.destroy()

    def execute_text_to_vector():
        # Call the function from Menu.py directly
        vector()
        # Close the window of the first program
        root.destroy()

    def execute_image_to_image():
        # Call the function from Menu.py directly
        i2i()
        # Close the window of the first program
        root.destroy()



    # Create the Tkinter window
    root = tk.Toplevel()
    root.title("Imagica AI")
    root.geometry("1300x700")
    root.resizable(width=False, height=False)

    # Load and display the background image
    image = Image.open("Menu.png")  # Replace "Menu.png" with the path to your background image
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Disable maximize button
    disable_maximize()

    # Button font
    button_font = ("Helvetica", 12, "bold")

    # Create "Next" button
    next_button = tk.Button(root, text="Next", font=button_font, width=10, height=1, command=execute_text_to_image)
    next_button.place(x=600, y=245)  # Position at coordinates (600, 600)

    next_button = tk.Button(root, text="Next", font=button_font, width=10, height=1, command=execute_text_to_anime)
    next_button.place(x=600, y=332)  # Position at coordinates (600, 600)

    next_button = tk.Button(root, text="Next", font=button_font, width=10, height=1, command=execute_text_to_portrait)
    next_button.place(x=600, y=417)  # Position at coordinates (600, 600)

    next_button = tk.Button(root, text="Next", font=button_font, width=10, height=1, command=execute_text_to_vector)
    next_button.place(x=600, y=500)  # Position at coordinates (600, 600)

    next_button = tk.Button(root, text="Next", font=button_font, width=10, height=1, command=execute_image_to_image)
    next_button.place(x=600, y=583)  # Position at coordinates (600, 600)

    root.mainloop()
