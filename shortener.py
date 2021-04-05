from tkinter import *
import pyperclip
import pyshorteners


def url_shortener():

    shortener = pyshorteners.Shortener()

    while True:
        try:
            url = shortener.tinyurl.short(original_url.get())
            # set global short url
            short_url.set(url)
        except ReadTimeout:
            continue
        break



def copy_url():
    # copy short url to clipboard
    pyperclip.copy(short_url.get())


if __name__ == "__main__":

    root = Tk()
    root.geometry("700x700")
    root.title("Mark's URL Shortener")
    root.configure(bg="#49A")

    original_url = StringVar()
    short_url = StringVar()

    # Pack is used to align widget in the center of the frame
    # padx and pady determine the extra space around the button box
    # padx adds empty space vertically
    # pady adds empty space horizontally

    Label(root, text="Enter the url you would like to shorten",
          font="poppins").pack(pady=5)
    Entry(root, textvariable=original_url, width=100).pack(pady=5)
    Button(root, text="Generate short URL", command=url_shortener).pack(pady=5)

    Label(root, text="Shortened URL", font="poppins").pack(pady=5)
    Entry(root, textvariable=short_url, width=50).pack(pady=5)
    Button(root, text="Copy short URL", command=copy_url).pack(pady=5)

    root.mainloop()
