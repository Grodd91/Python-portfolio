import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import subprocess
import json
import csv
import webbrowser  # Import webbrowser to open URLs

# Define the main application class for the YouTube Playlist Auto Organizer (YT-Pao)
class YT_PAO_UI:
    def __init__(self, root):
        self.root = root
        self.root.title("YT-Pao - YouTube Playlist Auto Organizer")  # Set window title
        self.root.geometry("1000x600")  # Set window size
        self.root.resizable(True, True)  # Allow resizing the window
        self.create_widgets()  # Initialize and create the widgets

    # Method to create all widgets (UI components)
    def create_widgets(self):
        # Title Label at the top
        self.title_label = tk.Label(self.root, text="YT-Pao", font=("Arial", 16), bg="#4CAF50", fg="white")
        self.title_label.pack(fill="x", pady=10)

        # Information label below the title
        self.info_label = tk.Label(self.root, text="Organize your YouTube playlists", font=("Arial", 12), bg="#f0f0f0")
        self.info_label.pack(fill="x", pady=5)

        # Playlist link input field
        self.playlist_link_label = tk.Label(self.root, text="Playlist link:", font=("Arial", 10))
        self.playlist_link_label.pack(pady=5)
        self.playlist_link_entry = tk.Entry(self.root, width=40, font=("Arial", 10), bd=2, relief="solid")
        self.playlist_link_entry.pack(pady=5)

        # Result format dropdown menu
        self.result_format_label = tk.Label(self.root, text="Result format:", font=("Arial", 10))
        self.result_format_label.pack(pady=5)
        self.result_format_var = tk.StringVar(value="json")  # Default format is JSON
        self.result_format_menu = tk.OptionMenu(self.root, self.result_format_var, "cmd", "txt", "json", "mySQL", "csv", "html")
        self.result_format_menu.config(font=("Arial", 10), relief="solid", bd=2)
        self.result_format_menu.pack(pady=5)

        # List mode dropdown menu (all, unavailable, available)
        self.list_mode_label = tk.Label(self.root, text="List mode:", font=("Arial", 10))
        self.list_mode_label.pack(pady=5)
        self.list_mode_var = tk.StringVar(value="all")  # Default mode is "all"
        self.list_mode_menu = tk.OptionMenu(self.root, self.list_mode_var, "all", "unavailable", "available")
        self.list_mode_menu.config(font=("Arial", 10), relief="solid", bd=2)
        self.list_mode_menu.pack(pady=5)

        # Button to organize the playlist
        self.organize_button = tk.Button(self.root, text="Organize Playlist", width=30, font=("Arial", 12), bg="#4CAF50", fg="white", command=self.organize_playlist)
        self.organize_button.pack(pady=20)

        # Button to save the playlist
        self.save_button = tk.Button(self.root, text="Save Playlist", width=30, font=("Arial", 12), bg="#2196F3", fg="white", command=self.save_playlist)
        self.save_button.pack(pady=10)

        # Button to quit the application
        self.quit_button = tk.Button(self.root, text="Quit", width=30, font=("Arial", 12), bg="#f44336", fg="white", command=self.root.quit)
        self.quit_button.pack(pady=10)

        # Label for playlist videos section
        self.treeview_label = tk.Label(self.root, text="Playlist Videos:", font=("Arial", 12), bg="#f0f0f0")
        self.treeview_label.pack(fill="x", pady=5)

        # Frame to contain the Treeview widget
        self.treeview_frame = tk.Frame(self.root)
        self.treeview_frame.pack(fill="both", expand=True)

        # Treeview widget to display playlist videos
        self.treeview = ttk.Treeview(self.treeview_frame, columns=("Title", "URL"), show="headings", height=10)
        self.treeview.heading("Title", text="Title")
        self.treeview.heading("URL", text="URL")

        # Vertical scrollbar for the Treeview
        self.treeview_scroll = tk.Scrollbar(self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.config(yscrollcommand=self.treeview_scroll.set)

        # Pack the Treeview and the scrollbar
        self.treeview.pack(fill="both", expand=True)
        self.treeview_scroll.pack(side="right", fill="y")

        # Bind click event to open URL in the browser
        self.treeview.bind("<ButtonRelease-1>", self.on_treeview_click)

    # Event handler when a treeview item is clicked
    def on_treeview_click(self, event):
        item = self.treeview.selection()  # Get the selected item
        if item:
            item_data = self.treeview.item(item)["values"]  # Get item data (Title, URL)
            url = item_data[1]  # Get URL from the second column
            if url:
                webbrowser.open(url)  # Open the URL in the default web browser

    # Method to organize the playlist
    def organize_playlist(self):
        self.playlist_link = self.playlist_link_entry.get()  # Get the playlist link entered by the user
        self.result_format = self.result_format_var.get()  # Get the selected result format
        self.list_mode = self.list_mode_var.get()  # Get the selected list mode

        if not self.playlist_link:
            messagebox.showerror("Error", "Please enter a playlist link.")  # Show an error if no link is entered
            return

        try:
            # Run a subprocess to organize the playlist using the provided link, format, and list mode
            result = subprocess.run(
                ['python', 'main.py',
                 '--playlistLink', self.playlist_link,
                 '--resultFormat', self.result_format,
                 '--listMode', self.list_mode
                ], capture_output=True, text=True, check=True)

            # Clear previous results from the treeview
            for item in self.treeview.get_children():
                self.treeview.delete(item)

            if not result.stdout:
                messagebox.showerror("Error", "No data received from the subprocess.")  # Show an error if no data was returned
                return

            try:
                # Parse the result output as JSON
                playlist_data = json.loads(result.stdout)

                # Insert the playlist videos into the treeview
                for video in playlist_data.get("videos", []):
                    title = video.get("title", "No Title")
                    url = video.get("url", "No URL")
                    self.treeview.insert("", "end", values=(title, url))

                # Show a success message after organizing the playlist
                messagebox.showinfo("Success", f"Playlist organized successfully and saved in {self.result_format.upper()} format!")

            except json.JSONDecodeError:
                messagebox.showerror("Error", "Error parsing playlist data (invalid JSON).")  # Handle JSON decoding errors

        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")  # Handle errors from the subprocess
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"Error parsing playlist data: {e}")  # Handle JSON errors during parsing

    # Method to save the playlist to a file
    def save_playlist(self):
        # Open a file dialog to select where to save the playlist
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv"),
                                                           ("Text files", "*.txt"), ("HTML files", "*.html")])

        if file_path:
            try:
                playlist_data = []
                # Collect playlist data from the treeview
                for child in self.treeview.get_children():
                    item = self.treeview.item(child)['values']
                    playlist_data.append({
                        "title": item[0],
                        "url": item[1]
                    })

                # Save the playlist in the selected format
                if file_path.endswith(".json"):
                    with open(file_path, 'w') as f:
                        json.dump({"playlist": self.playlist_link, "format": self.result_format, "videos": playlist_data}, f, indent=4)
                    messagebox.showinfo("Success", "Playlist saved as JSON!")
                elif file_path.endswith(".csv"):
                    with open(file_path, 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(["Title", "URL"])
                        for video in playlist_data:
                            writer.writerow([video["title"], video["url"]])
                    messagebox.showinfo("Success", "Playlist saved as CSV!")
                elif file_path.endswith(".txt"):
                    with open(file_path, 'w') as f:
                        for video in playlist_data:
                            f.write(f"{video['title']} - {video['url']}\n")
                    messagebox.showinfo("Success", "Playlist saved as TXT!")
                elif file_path.endswith(".html"):
                    with open(file_path, 'w') as f:
                        f.write("<html><body><h1>Playlist</h1>")
                        for video in playlist_data:
                            f.write(f"<p>{video['title']} - <a href='{video['url']}'>{video['url']}</a></p>")
                        f.write("</body></html>")
                    messagebox.showinfo("Success", "Playlist saved as HTML!")

            except Exception as e:
                messagebox.showerror("Error", f"An issue occurred while saving: {e}")  # Handle errors during saving

# Initialize the main application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = YT_PAO_UI(root)  # Create an instance of the YT_PAO_UI class
    root.mainloop()  # Start the Tkinter main event loop
