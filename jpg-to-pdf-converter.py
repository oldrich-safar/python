from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import img2pdf


root = Tk()
root.title("JPEG to PDF Converter")
root.geometry("600x450")

image_formats= [("JPEG", "*.jpg")]

# Choose image files to convert
def files():
	global images
	images = filedialog.askopenfilenames(parent=root,title='Choose a file',filetypes=image_formats)
	if images == "":
		messagebox.showinfo('Choosen Files', 'No files was added')
	else:
		messagebox.showinfo('Choosen Files', f'{images} was added')

# Choose, where to save output PDF file
def save_as_file():
	global save_file
	save_file = filedialog.asksaveasfilename(parent=root, defaultextension=".pdf")
	if save_file == "":
		messagebox.showinfo('Save to file', 'No output PDF file was added')
	else:
		messagebox.showinfo('Save to file', f'Output PDF will be saved to {save_file}')

# Function to convert images to PDF
def convert():
	img_path = "".join(images)
	with open(f"{save_file}","wb") as f:
		f.write(img2pdf.convert(images))
	myLabel = Label(root, text="Converted")
	myLabel.pack()


header = Label(root, text="JPEG to PDF Converter", font=("Arial Bold", 48))
header.pack()


imagesButton = Button(root, text="Choose Files to Convert", command=files)
imagesButton.pack()

pdfOutputButton = Button(root, text="Choose Output PDF File", command=save_as_file)
pdfOutputButton.pack()


convertButton = Button(root, text="Convert to PDF", command=convert)
convertButton.pack()

root.mainloop()
