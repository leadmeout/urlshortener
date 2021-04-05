import pyshorteners

# get url
original_url = input("Please enter the url: \n")
# initialize shortner
url_shortener = pyshorteners.Shortener()

# short main_url with tinyurl.short method of Shortener class

while True:
    try:
        short_url = url_shortener.tinyurl.short(original_url)
    except ReadTimeoutError:
        continue
    finally:
        print(f"\nThe short url is: \n{short_url}")
    break
