import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

with open("amazon_laptops_all_pages.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
soup.prettify()
#print(soup.title.string)

products = soup.find_all("div", attrs={"data-asin": True, "data-component-type": "s-search-result"})

model, rating, lastmonth, mrp, discount = [], [], [], [], []

for product in products:
    # Model
    model_div = product.find("div", attrs={"data-cy": "title-recipe"})
    if model_div:
        span = model_div.find("span")
        if span:
            match = re.match(r'^(\w+\s+\w+)', span.text.strip())
            model.append(match.group(1) if match else "0")
        else:
            model.append("0")
    else:
        model.append("0")

    # Rating
    rating_block = product.find("div", attrs={"data-cy": "reviews-block"})
    found_rating = "0"
    if rating_block:
        spans = rating_block.find_all("span")
        for s in spans:
            txt = s.text.strip()
            if re.match(r'^\d\.\d$', txt):
                found_rating = txt
                break
    rating.append(found_rating)

    # Last Month Bought
    found_lm = "0"
    if rating_block:
        spans = rating_block.find_all("span")
        for s in spans:
            txt = s.text.strip()
            match = re.search(r'(\d+)\+', txt)  
            if match:
                found_lm = match.group(0)  
                break
    lastmonth.append(found_lm)

    # MRP
    price_block = product.find("div", attrs={"data-cy": "price-recipe"})
    found_mrp = "0"
    if price_block:
        for s in price_block.find_all("span"):
            txt = s.text.strip()
            match = re.search(r'M\.R\.P:\s*₹([\d,]+)', txt)
            if match:         
                found_mrp = match.group(1).replace(",", "")
                break
    mrp.append(found_mrp)

    # Discount Price
    found_disc = "0"
    if price_block:
        for s in price_block.find_all("span"):
            txt = s.text.strip()
            match = re.search(r'^₹([\d,]+)$', txt)
            if match:
                found_disc = match.group(1).replace(",", "")
                break
    discount.append(found_disc)

print(len(model), len(rating), len(lastmonth), len(mrp), len(discount))
print("Model =", model)
print("Rating =", rating)
print("Last Month =", lastmonth)
print("MRP =", mrp)
print("Discount =", discount)

#PANDAS DATAFRAME 
data = {
    'Model': model,
    'Rating': rating,
    'LastMonth': lastmonth,
    'MRP': mrp,
    'Discount': discount
}

df = pd.DataFrame(data)
df.to_csv('amazon_laptops_data.csv', index=False)

# Check the shape of the dataframe (rows and columns)
print(df.shape)

# Display the first few rows of the DataFrame
print(df.head())

# Check if there are any columns with issues
print(df.isnull().sum())  # Check for missing values
print(df.columns)

import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

with open("amazon_laptops_all_pages.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
soup.prettify()
#print(soup.title.string)

products = soup.find_all("div", attrs={"data-asin": True, "data-component-type": "s-search-result"})

model, rating, lastmonth, mrp, discount = [], [], [], [], []

for product in products:
    # Model
    model_div = product.find("div", attrs={"data-cy": "title-recipe"})
    if model_div:
        span = model_div.find("span")
        if span:
            match = re.match(r'^(\w+\s+\w+)', span.text.strip())
            model.append(match.group(1) if match else "0")
        else:
            model.append("0")
    else:
        model.append("0")

    # Rating
    rating_block = product.find("div", attrs={"data-cy": "reviews-block"})
    found_rating = "0"
    if rating_block:
        spans = rating_block.find_all("span")
        for s in spans:
            txt = s.text.strip()
            if re.match(r'^\d\.\d$', txt):
                found_rating = txt
                break
    rating.append(found_rating)

    # Last Month Bought
    found_lm = "0"
    if rating_block:
        spans = rating_block.find_all("span")
        for s in spans:
            txt = s.text.strip()
            match = re.search(r'(\d+)\+', txt)  
            if match:
                found_lm = match.group(0)  
                break
    lastmonth.append(found_lm)

    # MRP
    price_block = product.find("div", attrs={"data-cy": "price-recipe"})
    found_mrp = "0"
    if price_block:
        for s in price_block.find_all("span"):
            txt = s.text.strip()
            match = re.search(r'M\.R\.P:\s*₹([\d,]+)', txt)
            if match:         
                found_mrp = match.group(1).replace(",", "")
                break
    mrp.append(found_mrp)

    # Discount Price
    found_disc = "0"
    if price_block:
        for s in price_block.find_all("span"):
            txt = s.text.strip()
            match = re.search(r'^₹([\d,]+)$', txt)
            if match:
                found_disc = match.group(1).replace(",", "")
                break
    discount.append(found_disc)

'''print(len(model), len(rating), len(lastmonth), len(mrp), len(discount))
print("Model =", model)
print("Rating =", rating)
print("Last Month =", lastmonth)
print("MRP =", mrp)
print("Discount =", discount)'''


#PANDAS DATAFRAME 
raw_data = {
    'Model': model,
    'Rating': rating,
    'LastMonth': lastmonth,
    'MRP': mrp,
    'Discount': discount
}
df

df = pd.DataFrame(raw_data)
df.to_csv("amazon_laptops_data.csv", index=False)
print("Scraped data saved to amazon_laptops_data.csv")


'''# Check the shape of the dataframe (rows and columns)
print(df.shape)

# Display the first few rows of the DataFrame
print(df.head())

# Check if there are any columns with issues
print(df.isnull().sum())  # Check for missing values
print(df.columns)

np_array = df[['LastMonth', 'MRP', 'Discount']].to_numpy()

print(np_array)'''

