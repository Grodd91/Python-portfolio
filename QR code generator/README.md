## QR Code Generator

This program generates a QR code based on the data entered by the user. It provides a graphical user interface (GUI) using the `tkinter` library in Python.

### Prerequisites

Before running the program, ensure that you have the following libraries installed:

- `qrcode`
- `tkinter`
- `PIL` (Python Imaging Library)

You can install these libraries using the pip package manager with the following command:
pip install qrcode pillow

### How to Use

1. Run the program using a Python interpreter.

2. The main window titled "QR Code Generator" will appear.

3. Enter the data you want to encode into the "Enter data" text field.

4. Click the "Generate QR Code" button.

5. The generated QR code will be displayed in the window.

### Program Explanation

The program uses the `qrcode` library to generate the QR code based on the provided data. The `tkinter` library is used to create the GUI elements.

The `generate_qr_code` function is called when the "Generate QR Code" button is clicked. It retrieves the data from the text entry field, generates the QR code, and displays it in the GUI.

The main window is created using `tkinter.Tk()`. It includes a label and a text entry field for the data input, a button to trigger the code generation, and a label to display the QR code.

The program uses the `PIL` library to resize and display the generated QR code image in the GUI.

### Dependencies

- qrcode
- tkinter
- PIL


