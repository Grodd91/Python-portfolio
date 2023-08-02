import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import re

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=tk.YES, fill=tk.BOTH)

        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Find", command=self.find_text)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            content = self.text_area.get("1.0", tk.END)
            with open(file_path, "w") as file:
                file.write(content)

    def find_text(self):
        search_text = simpledialog.askstring("Find", "Enter text to find:")
        if search_text:
            content = self.text_area.get("1.0", tk.END)
            matches = re.finditer(re.escape(search_text), content)
            self.text_area.tag_remove("search", "1.0", tk.END)
            for match in matches:
                start = match.start()
                end = match.end()
                self.text_area.tag_add("search", f"1.0+{start}c", f"1.0+{end}c")
                self.text_area.tag_configure("search", background="yellow")

def main():
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
