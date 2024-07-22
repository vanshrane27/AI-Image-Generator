import tkinter as tk

def guii():
    def resize(event):
        canvas.config(width=root.winfo_width(), height=root.winfo_height())
        draw_partitions()

    def draw_partitions():
        canvas.delete("all")
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        partition1_width = int(width * 0.3)
        partition2_width = int(width * 0.7)

        canvas.create_rectangle(0, 0, partition1_width, height, fill="blue", outline="")
        canvas.create_rectangle(partition1_width, 0, width, height, fill="red", outline="")

    root = tk.Tk()
    root.title("Horizontal Partition")
    root.geometry("1300x700")

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill="both", expand=True)

    root.bind("<Configure>", resize)
    root.mainloop()
