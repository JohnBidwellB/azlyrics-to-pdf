from setuptools import setup

setup(
    name = "azlyrics",
    version = "0.0.1",
    description = "Script that generates a PDF file of a song's lyric",
    url = "https://github.com/JohnBidwellB/azlyrics-to-pdf",
    author = "John Bidwell Boitano",
    author_email = "johnbidwellb@gmail.com",
    packages = ['azlyrics'],
    install_requires = ['BeautifulSoup4', 'pdfkit'],
    scripts = ['bin/azlyrics'],
    entry_points = {
          'console_scripts': [
              'azlyrics = azlyrics:run'
          ]
}
)
