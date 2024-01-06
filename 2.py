import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter and Resizer")

        self.input_path = ""
        self.output_path = ""
        self.new_size = (0, 0)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Input Image
        self.input_label = tk.Label(self.root, text="Select Input Image:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.pack()

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_input)
        self.browse_button.pack()

        # Output Image
        self.output_label = tk.Label(self.root, text="Select Output Path:")
        self.output_label.pack()

        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.pack()

        self.browse_output_button = tk.Button(self.root, text="Browse", command=self.browse_output)
        self.browse_output_button.pack()

        # Resize Image
        self.resize_label = tk.Label(self.root, text="Resize Image (Width x Height):")
        self.resize_label.pack()

        self.width_label = tk.Label(self.root, text="Width:")
        self.width_label.pack()

        self.width_entry = tk.Entry(self.root)
        self.width_entry.pack()

        self.height_label = tk.Label(self.root, text="Height:")
        self.height_label.pack()

        self.height_entry = tk.Entry(self.root)
        self.height_entry.pack()

        # Convert and Resize Button
        self.convert_button = tk.Button(self.root, text="Convert and Resize", command=self.convert_and_resize)
        self.convert_button.pack()

    def browse_input(self):
        self.input_path = filedialog.askopenfilename()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.input_path)

    def browse_output(self):
        self.output_path = filedialog.asksaveasfilename(defaultextension=".png")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_path)

    def convert_and_resize(self):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            self.new_size = (width, height)

            with Image.open(self.input_path) as img:
                resized_img = img.resize(self.new_size)
                resized_img.save(self.output_path)

            tk.messagebox.showinfo("Success", "Image converted and resized successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()