# Play Store Scraper

This project is a Python script that scrapes app images from the Google Play Store based on a user-provided search query. It downloads screenshots for each app found and organizes them into folders under the `images/` directory.

## Features

- Searches the Play Store for apps matching a query.
- Extracts app titles and screenshots.
- Downloads images into organized folders.

## Requirements

- Python 3.x
- [beautifulsoup4](requirements.txt)

## Usage

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the scraper:
   ```sh
   python Scraper.py
   ```
3. Enter your search query when prompted.

## Output

Downloaded images are saved in the `images/` directory, with each app’s images in a separate folder.

## License

This project is for educational purposes.
