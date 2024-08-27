from tkinter import Tk, Label, PhotoImage

# Create the main window
win = Tk()
win.title("Image Example")

# Load the image using escaped backslashes
image = PhotoImage(file="C:/Users/HP/Downloads/kani1.webp")  # Escaped backslashes

# Create a Label to display the image
image_label = Label(win, image=image)
image_label.pack()

# Run the Tkinter event loop
win.mainloop()
