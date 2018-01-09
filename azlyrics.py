#import requests
import urllib.request, urllib.error
import argparse
import re
from bs4 import BeautifulSoup
import pdfkit

class AZLyrics:
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song

    def formatArtistAndSong(self):
        patron = re.compile(" ")
        return patron.sub("", self.artist).lower(), patron.sub("", self.song).lower()

    def url(self):
        if not self.artist and not self.song:
            self.artist = "beck"
            self.song = "loser"
        return "https://www.azlyrics.com/lyrics/{}/{}.html".format(*self.formatArtistAndSong())

    def getPage(self):
        try:
            response = urllib.request.urlopen(self.url())
            return response.read()
        except urllib.error.HTTPError:
            print("Song not found")

    def extractLyrics(self):
        soup = BeautifulSoup(self.getPage(), 'html.parser')
        lyric_with_tags = soup.find("div", attrs={"class": None, "id": None})
        lyric = lyric_with_tags.text.strip()
        return lyric

def savePDF(path, lyric, artist, song):
    pdfkit.from_string("{} - {}".format(artist, song), "{} - {}.pdf".format(artist, song))
    #pdfkit.from_string(lyric, "{} - {}.pdf".format(artist, song))
    pdfkit.from_file("{} - {}.txt".format(artist, song), "{} - {}.pdf".format(artist, song))

if __name__=="__main__":

    parser = argparse.ArgumentParser(
        prog = "AZLyrics",
        description="Search a song's lyric from AZLyrics",
        epilog = "Thank you for using it!",
    )
    parser.add_argument("artist", metavar = "A", type = str, help= "Name of the artist")
    parser.add_argument("song", metavar = "S", type = str, help = "Name of the song")
    parser.add_argument("-s", "--save", metavar = "path", dest = "path", default = False, help = "Save song's lyric as PDF file")
    args = parser.parse_args()

    search = AZLyrics(args.artist, args.song)
    lyric = search.extractLyrics()

    if args.path:
        txt = open("{} - {}.txt".format(args.artist, args.song), "w")
        txt.write("{} - {}\n\n".format(args.artist, args.song).title())
        txt.write(lyric)
        txt.close()
        savePDF(args.path, lyric, args.artist, args.song)
    else:
        print(lyric)
