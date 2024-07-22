import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
import PIL
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler

def i2i():
    global output_image_label  # Define output_image_label as a global variable

    # Initialize StableDiffusionInstructPix2PixPipeline
    model_id = "timbrooks/instruct-pix2pix"
    pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16,
                                                                  safety_checker=None)
    pipe.to("cuda")
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

    # Function to download image from URL
    def download_image(url):
        image = PIL.Image.open(requests.get(url, stream=True).raw)
        image = PIL.ImageOps.exif_transpose(image)
        image = image.convert("RGB")
        return image

    # Function to handle image generation based on input file and prompt
    def generate_image():
        global input_image_path

        # Check if input image is selected
        if input_image_path:
            # Check if prompt is entered
            prompt_text = prompt_entry.get().strip()
            if prompt_text:
                try:
                    # Load input image
                    input_image = Image.open(input_image_path)
                    input_image = input_image.convert("RGB")

                    # Generate modified image
                    images = pipe(prompt_text, image=input_image, num_inference_steps=10, image_guidance_scale=1).images

                    # Display modified image
                    output_image = images[0]
                    output_image.thumbnail((300, 300))
                    output_image_tk = ImageTk.PhotoImage(output_image)
                    output_image_label.config(image=output_image_tk)
                    output_image_label.image = output_image_tk
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")
            else:
                messagebox.showerror("Error", "Please enter a prompt.")
        else:
            messagebox.showerror("Error", "Please select an input image.")

    # Function to select input image file
    def select_input_image():
        global input_image_path
        input_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if input_image_path:
            input_image_label.config(text=f"Selected Input Image: {input_image_path}")

    # Create tkinter window
    root = tk.Toplevel()
    root.title("Imagica AI")
    root.geometry("1300x700")  # Set your desired width and height here
    root.resizable(width=False, height=False)

    # Global variable to store input image path
    input_image_path = None

    # File input area
    input_image_button = tk.Button(root, text="Select Input Image", command=select_input_image)
    input_image_button.pack(pady=10)

    input_image_label = tk.Label(root, text="Selected Input Image:")
    input_image_label.pack()

    # Prompt text box
    prompt_label = tk.Label(root, text="Enter Prompt:")
    prompt_label.pack()

    prompt_entry = tk.Entry(root, width=50)
    prompt_entry.pack()

    # Submit button
    submit_button = tk.Button(root, text="Generate Modified Image", command=generate_image)
    submit_button.pack(pady=10)

    # Output image area
    output_image_label = tk.Label(root)
    output_image_label.pack()

    root.mainloop()

