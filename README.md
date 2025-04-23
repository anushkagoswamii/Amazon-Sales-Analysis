Amazon Laptop Sales Analysis-
This project focuses on end-to-end analysis of laptop sales data from Amazon. It includes web scraping, data cleaning and exploration, storage in a SQL database, and visualization using Power BI. The objective is to understand pricing strategies, ratings distribution, and revenue trends across different laptop models.

Project Overview-
The pipeline follows these major steps:
HTML Retrieval – Raw page content is saved using Retrieving_HTML.py.
Web Scraping – Data is extracted from saved HTML using bs4_scrapping.py.
Data Storage – Cleaned and structured data is stored in laptops.csv and the SQL database amazon_laptops.db.
Data Analysis – Insights are derived through exploratory data analysis in EDA.ipynb.
Visualization – Results are visualized using Power BI (file not included in the current directory).

File Descriptions-
web_scrapping/	Directory that may contain auxiliary scripts or saved HTML files.
amazon_laptops_all_pages.html	Combined HTML content of all scraped pages from Amazon.
amazon_laptops_data_cleaned.csv	Cleaned dataset saved after scraping and preprocessing.
amazon_laptops.db	SQLite database file containing structured laptop data.
bs4_scrapping.py	Script to parse HTML files and extract structured data using BeautifulSoup.
EDA.ipynb	Jupyter Notebook for performing exploratory data analysis with Pandas, NumPy, and Matplotlib.
laptops.csv	Another version of the dataset (likely raw or intermediate).
Retrieving_HTML.py	Script to download and save HTML content from Amazon product listings.

Technologies Used-
Python
BeautifulSoup for web scraping
Pandas and NumPy for data manipulation
Matplotlib for basic plots
SQL (SQLite)
Data persistence and query execution
Power BI

Interactive dashboard creation for business insights-
Key Analysis Areas
Price distribution (MRP vs selling price)
Rating distribution and correlation with sales
Most popular and highly rated laptop models
Revenue estimation per brand or model
Discount trends and brand-level pricing patterns

