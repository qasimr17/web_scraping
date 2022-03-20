## Web Scraping with Scrapy 

Scraping the [website](https://www.magnatiles.com/products/) to obtain all the products' names, skus and prices across all available pages. 
This is implemented using Python's Scrapy framework, with the data parsed to a csv file. 

To run the code and get the results, cd into the `magna_tiles` folder and run:

```
scrapy crawl tiles -O tiles.csv
```

Note: You may replace `tiles.csv` above with the output file name of your choosing. Data may be exported as a .json file as well.

To install the relevant dependencies/libraries in your environment, run:

```
pip install -r requirements.txt
```
