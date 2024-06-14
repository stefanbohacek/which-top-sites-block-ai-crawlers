# Analyze robots.txt files of popular sites for AI crawler rules

To build the dataset:

1. Update the list of websites inside `domains.txt` as needed. (Currently uses a list of sites from https://en.wikipedia.org/wiki/List_of_most-visited_websites).
2. Run `node download.js` to download robots.txt files for domains listed inside inside `domains.txt`.
3. Run `python analyze.py` to process the downloaded robots.txt files inside the `robots` folder and save results into a `results.csv` file.

Note that not all sites will let you download their `robots.txt` file, but you can visit those manually by visiting `example.com/robots.txt` in your browser.
