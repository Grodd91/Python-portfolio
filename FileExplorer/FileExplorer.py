import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")
        self.root.geometry("600x400")

        self.path_var = tk.StringVar()
        self.path_var.set(os.getcwd())

        self.create_widgets()

    def create_widgets(self):
        self.path_entry = tk.Entry(self.root, textvariable=self.path_var)
        self.path_entry.pack(fill=tk.BOTH, expand=True)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        self.file_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)

        self.open_button = tk.Button(self.root, text="Open File", command=self.open_file)
        self.open_button.pack()

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.path_var.set(directory)
            self.show_files(directory)

    def show_files(self, directory):
        self.file_listbox.delete(0, tk.END)
        for item in os.listdir(directory):
            self.file_listbox.insert(tk.END, item)

    def open_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.file_listbox.get(selected_index)
            full_path = os.path.join(self.path_var.get(), selected_file)
            try:
                with open(full_path, "r") as file:
                    content = file.read()
                    self.show_file_content(selected_file, content)
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")
            except Exception as e:
                messagebox.showerror("Error", f"Unable to open file: {str(e)}")

    def show_file_content(self, filename, content):
        content_window = tk.Toplevel(self.root)
        content_window.title(f"File Content - {filename}")
        
        text_widget = tk.Text(content_window)
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, content)

def main():
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
