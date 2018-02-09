A very simple script that fetch a lyric song from AZLyrics and save it in PDF file.

# Installation

Install using PIP

```bash
pip3 install git+https://github.com/JohnBidwellB/azlyrics-to-pdf
```

# Usage

Use with `azlyrics "artistName" "songName" `, also, you can add the flag `-s` to save the lyric in PDF.

### Example

```bash
azlyrics "Bon Jovi" "Livin on a prayer" -s
```

# Documentation

`AZLyrics` class have 5 methods:

* `formatArtistAndSong()`: It join the artist's name and song's name and make every letter lower.
* `url()`: To get the URL of the song.
* `getPage()`: Get the HTML of the song, in case that this is not available, the execution of the script ends.
* `getLyrics()`: Extract the lyrics from the HTML.
* `getPDF()`: Save the lyric as PDF file.
