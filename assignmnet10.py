import tkinter as tk
import webbrowser

def navigate_to_site():
    site_url = entry.get()
    print(f"Navigating to: {site_url}")
    webbrowser.open(site_url)

root = tk.Tk()

label = tk.Label(root, text="Enter a website URL:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Navigate", command=navigate_to_site)
button.pack()

root.mainloop()
