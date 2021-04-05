import pyshorteners

# get url
original_url = "http://www.cp24.com"
# initialize shortner
url_shortener = pyshorteners.Shortener()

# short main_url with tinyurl.short method of Shortener class
short_url = url_shortener.tinyurl.short(original_url)


# printout url
print(f"The short url is: \n{short_url}")
