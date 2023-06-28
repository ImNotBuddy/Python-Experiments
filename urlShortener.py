import pyshorteners

url = input("Enter the URL to shorten: ")
typeTiny = pyshorteners.Shortener()
shortenedUrl = typeTiny.tinyurl.short(url)

print("The Shortened URL is: " + shortenedUrl)