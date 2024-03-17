# reading csv file 
import pandas as pd


def getProduct():
    df = pd.read_csv("flipkart_com-ecommerce_sample.csv")
    product = df['product_name'] 
    product_drop = product.dropna()
    productObj = product_drop.drop_duplicates(keep=False)

    return productObj


def getProductUrl():
    df = pd.read_csv("flipkart_com-ecommerce_sample.csv")
    product_url = df["product_url"]
    product_drop = product_url.dropna()
    productUrlObj  = product_drop.drop_duplicates(keep=False)
    return productUrlObj


def getRetailPrice():
    df = pd.read_csv("flipkart_com-ecommerce_sample.csv")
    retail_price = df["retail_price"]
    retail_price_drop = retail_price.dropna()
    retail_price_dropObj  = retail_price_drop.drop_duplicates(keep=False)
    return retail_price_dropObj

