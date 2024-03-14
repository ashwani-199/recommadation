# reading csv file 
import pandas as pd


def getProduct():
    df = pd.read_csv("flipkart_com-ecommerce_sample.csv")
    product = df['product_name'] 
    product_drop = product.dropna()
    productObj = product_drop.drop_duplicates(keep=False)
    product_list = []
    for prod in productObj:
        product_list.append(prod)
    
    return product_list

def getProductUrl():
    df = pd.read_csv("flipkart_com-ecommerce_sample.csv")
    product_url = df["product_url"]
    product_drop = product_url.dropna()
    productUrlObj  = product_drop.drop_duplicates(keep=False)
    product_url = []
    for prod in productUrlObj:
        product_url.append(prod)
    
    return product_url


def getRetailPrice():
    df = pd.read_csv("flipkart_com-ecommerce_sample.csv")
    retail_price = df["retail_price"]
    retail_price_drop = retail_price.dropna()
    retail_price_dropObj  = retail_price_drop.drop_duplicates(keep=False)
    retail_price = []
    for prod in retail_price_dropObj:
        retail_price.append(prod)
    
    return retail_price

