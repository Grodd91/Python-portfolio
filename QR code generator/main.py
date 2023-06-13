import qrcode
import tkinter as tk
from PIL import ImageTk, Image

def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image = image.resize((300, 300))
    qr_image = ImageTk.PhotoImage(image)

    qr_label.configure(image=qr_image)
    qr_label.image = qr_image

# Creating the main window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("400x400")

# Label and text entry for the data
label = tk.Label(window, text="Enter data:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Label to display the QR code
qr_label = tk.Label(window)
qr_label.pack()

# Running the main loop
window.mainloop()
