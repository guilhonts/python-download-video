from pytube import YouTube

link = input("URL: ") #Link do video que vai ser baixado
path = input("Save in: ") #Pasta onde o video vai ser salvo

yt = YouTube(link)

result = {
    "Title": yt.title,
}

print(result)

ys = yt.streams.get_highest_resolution()
print("Downloading...")

ys.download()
print("Download complete!")
