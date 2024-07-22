import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk
from diffusers import StableDiffusionPipeline
import os
import torch

torch.cuda.empty_cache()


def vector():
    # Function to generate image based on the prompt
    def generate_image():
        prompt = prompt_entry.get()
        if prompt:
            # Append "anime" to the prompt
            prompt += " ,vector image,illustration,4k"

            try:
                global generated_image
                generated_image = pipe(prompt).images[0]

                # Resize the image to fit within the window
                width, height = root.winfo_width() - 500, root.winfo_height() - 100  # Adjusted to fit the image within the window
                generated_image = generated_image.resize((width, height))

                img = ImageTk.PhotoImage(generated_image)
                image_label.config(image=img)
                image_label.image = img
                download_button.config(state=tk.NORMAL)  # Enable download button
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Error", "Please enter a prompt.")

    # Function to download the output image
    def download_image():
        if generated_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if file_path:
                generated_image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")
        else:
            messagebox.showerror("Error", "No image to download.")

    # Function to display enlarged image
    def enlarge_image(event):
        if generated_image:
            enlarged_window = tk.Toplevel(root)
            enlarged_window.title("Enlarged Image")

            # Resize the image to fit the enlarged window
            resized_image = generated_image.resize((800, 600))
            img = ImageTk.PhotoImage(resized_image)

            # Display the image in the enlarged window
            enlarged_label = tk.Label(enlarged_window, image=img)
            enlarged_label.image = img
            enlarged_label.pack()

    # Initialize Tkinter
    root = tk.Toplevel()
    root.title("Imagica AI")
    # Set fixed window size
    root.geometry("1300x700")  # Set your desired width and height here
    root.resizable(width=False, height=False)

    # Load model and move it to GPU
    # model_id = "stabilityai/stable-cascade-prior"
    model_id = "dreamlike-art/dreamlike-photoreal-2.0"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")

    # Create GUI components
    prompt_label = tk.Label(root, text="Enter Prompt:")
    prompt_label.pack()

    prompt_entry = tk.Entry(root, width=50)
    prompt_entry.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    submit_button = tk.Button(button_frame, text="Generate Image", command=generate_image)
    submit_button.pack(side=tk.LEFT)

    download_button = tk.Button(button_frame, text="Download Image", command=download_image,
                                state=tk.DISABLED)  # Initially disabled
    download_button.pack(side=tk.LEFT)

    image_label = tk.Label(root)
    image_label.pack()

    # Bind the click event to the enlarge_image function
    image_label.bind("<Button-1>", enlarge_image)
    root.mainloop()

