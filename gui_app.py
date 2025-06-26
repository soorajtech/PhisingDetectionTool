import tkinter as tk
from tkinter import messagebox
from predict import predict_phishing

def check_url():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return
    result = predict_phishing(url)
    result_label.config(text=f"Result: {result}", fg="green" if "Legitimate" in result else "red")

app = tk.Tk()
app.title("Trogen Phishing Detection Tool")
app.geometry("400x220")

tk.Label(app, text="Trogen Phishing Detection Tool", font=("Arial", 14, "bold")).pack(pady=5)
tk.Label(app, text="Developed by Sooraj", font=("Arial", 10, "italic")).pack()

tk.Label(app, text="Enter URL to Check:", font=("Arial", 12)).pack(pady=10)
url_entry = tk.Entry(app, width=40)
url_entry.pack()

tk.Button(app, text="Check Now", command=check_url, bg="#007acc", fg="white", width=15).pack(pady=10)
result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.pack()

app.mainloop()