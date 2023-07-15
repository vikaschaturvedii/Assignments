import tkinter as tk
import webbrowser

def navigate_to_faq():
    site = site_var.get()
    faq_url = ""

    if site == "Instagram Ads":
        faq_url = "https://www.example.com/faq-instagram"
    elif site == "YouTube Ads":
        faq_url = "https://www.example.com/faq-youtube"
    # Add more options for other sources if needed

    print(f"Navigating to FAQ page for {site}")
    webbrowser.open(faq_url)

root = tk.Tk()

label = tk.Label(root, text="Course Enquiry Form")
label.pack()

site_var = tk.StringVar()
site_label = tk.Label(root, text="Where did you come to know about the course?")
site_label.pack()

instagram_ads = tk.Radiobutton(root, text="Instagram Ads", variable=site_var, value="Instagram Ads")
instagram_ads.pack()

youtube_ads = tk.Radiobutton(root, text="YouTube Ads", variable=site_var, value="YouTube Ads")
youtube_ads.pack()

# Add more options for other sources if needed

submit_button = tk.Button(root, text="Submit", command=navigate_to_faq)
submit_button.pack()

root.mainloop()
