#import requests
import urllib.request, urllib.error
import argparse
import re
from bs4 import BeautifulSoup
import pdfkit
import os
from sys import exit

class AZLyrics:
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        self.lyric = self.getLyrics()

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
            exit()

    def getLyrics(self):
        soup = BeautifulSoup(self.getPage(), 'html.parser')
        lyric_with_tags = soup.find("div", attrs={"class": None, "id": None})
        return lyric_with_tags.text.strip()

    def getPDF(self):
        homedir = os.path.expanduser('~')
        savedir = homedir+"/documents/azlyrics"

        txt = open(savedir+"/{} - {}.txt".format(self.artist, self.song), "w")
        txt.write("{} - {}\n\n".format(self.artist, self.song).title())
        txt.write(self.lyric)
        txt.close()

        if os.path.exists(savedir) == False:
            os.mkdir(savedir)
        pdfkit.from_file(savedir+"/{} - {}.txt".format(self.artist, self.song), savedir+"/{} - {}.pdf".format(self.artist, self.song))
        os.remove(savedir+"/{} - {}.txt".format(self.artist, self.song))

def run():
    parser = argparse.ArgumentParser(
        prog = "AZLyrics",
        description="Search a song's lyric from AZLyrics",
        epilog = "Thank you for using it!",
    )
    parser.add_argument("artist", metavar = "A", type = str, help= "Name of the artist")
    parser.add_argument("song", metavar = "S", type = str, help = "Name of the song")
    parser.add_argument("-s", "--save", dest = "path", action = "store_true", help = "Save song's lyric as PDF file")

    args = parser.parse_args()

    search = AZLyrics(args.artist, args.song)
    #lyric = search.extractLyrics()

    if args.path:
        search.getPDF()
    else:
        print(search.lyric)
        #os.system("say %s"%(lyric))
