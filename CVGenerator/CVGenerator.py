import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

class CVGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("CV Generator")

        self.label_personal_info = tk.Label(master, text="Personal Information")
        self.label_personal_info.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=1, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        self.label_email = tk.Label(master, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_experience = tk.Label(master, text="Experience:")
        self.label_experience.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.text_experience = tk.Text(master, width=50, height=5)
        self.text_experience.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.label_education = tk.Label(master, text="Education:")
        self.label_education.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.text_education = tk.Text(master, width=50, height=5)
        self.text_education.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.label_skills = tk.Label(master, text="Skills:")
        self.label_skills.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        self.text_skills = tk.Text(master, width=50, height=5)
        self.text_skills.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        self.label_interests = tk.Label(master, text="Interests:")
        self.label_interests.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
        self.text_interests = tk.Text(master, width=50, height=5)
        self.text_interests.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

        self.button_generate = tk.Button(master, text="Generate CV", command=self.generate_cv)
        self.button_generate.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

    def generate_cv(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        experience = self.text_experience.get("1.0", tk.END)
        education = self.text_education.get("1.0", tk.END)
        skills = self.text_skills.get("1.0", tk.END)
        interests = self.text_interests.get("1.0", tk.END)

        if name.strip() == '' or email.strip() == '':
            messagebox.showerror("Error", "Please enter your name and email.")
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="CV", ln=True, align="C")
        pdf.cell(200, 10, txt="", ln=True, align="C")

        pdf.cell(200, 10, txt="Name: " + name, ln=True)
        pdf.cell(200, 10, txt="Email: " + email, ln=True)
        pdf.cell(200, 10, txt="", ln=True)

        pdf.cell(200, 10, txt="Experience:", ln=True)
        pdf.multi_cell(0, 10, txt=experience)
        pdf.cell(200, 10, txt="", ln=True)

        pdf.cell(200, 10, txt="Education:", ln=True)
        pdf.multi_cell(0, 10, txt=education)
        pdf.cell(200, 10, txt="", ln=True)

        pdf.cell(200, 10, txt="Skills:", ln=True)
        pdf.multi_cell(0, 10, txt=skills)
        pdf.cell(200, 10, txt="", ln=True)

        pdf.cell(200, 10, txt="Interests:", ln=True)
        pdf.multi_cell(0, 10, txt=interests)

        pdf.output("CV_" + name.replace(" ", "_") + ".pdf")

        messagebox.showinfo("Success", "CV generated successfully!")

def main():
    root = tk.Tk()
    app = CVGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
