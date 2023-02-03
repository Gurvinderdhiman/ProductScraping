import string
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re

product_name = ['https://www.amazon.in/American-Tourister-AMT-SCH-02/dp/B07CJCGM1M', 'https://www.amazon.in/Wesley-Milestone-Waterproof-Backpack-Business/dp/B084JGJ8PF', 'https://www.amazon.in/Skybags-Brat-Black-Casual-Backpack/dp/B08Z1HHHTD', 'https://www.amazon.in/Kuber-Industries-Handcrafted-Embroidered-Handbag/dp/B082VDVJGM', 'https://www.amazon.in/Fiesto-Fashion-Womens-Handbag-FIESTO33_Blue/dp/B082Z33ZDS', 'https://www.amazon.in/ADISA-women-girls-black-embroided/dp/B08RWBP3H2', 'https://www.amazon.in/Lapis-Lupo-Flower-Embroidery-Handbag/dp/B07RXYSJHF', 'https://www.amazon.in/ADISA-Laptop-Backpack-Office-College/dp/B09TPX22NF', 'https://www.amazon.in/Safari-Backpack-Resistant-Polyester-Travelling/dp/B09B29F66W', 'https://www.amazon.in/Backpack-Small-Black-Water-Repellant/dp/B088XB5XY8', 'https://www.amazon.in/Kleider-Travel-Business-Messenger-Shoulder/dp/B084ZHP97M', 'https://www.amazon.in/AirCase-C34-Laptop-Backpack-Women/dp/B07QN4KXWG', 'https://www.amazon.in/Safari-Spartan-Water-Resistant-Backpack/dp/B09B26MB5M', 'https://www.amazon.in/ADISA-BP005-Weight-Casual-Backpack/dp/B07F3X45WZ', 'https://www.amazon.in/Blue-Tree-Backpack-Cartoon-Spiderman/dp/B097NH6X4C', 'https://www.amazon.in/School-Backpack-Cartoon-Travel-Toddler/dp/B08WWG91Q3', 'https://www.amazon.in/Blue-Tree-Velvet-Spiderman-School/dp/B07HLYW3FF', 'https://www.amazon.in/MosQuick%C2%AE-Drawstring-Organizing-Stationery-multipurpose/dp/B09SB5DP5Y', 'https://www.amazon.in/Amazon-Brand-Solimo-so_flingyrqba_6-Gym/dp/B084DQ182R', 'https://www.amazon.in/Backpack-Toddler-Animal-Cartoon-Travel/dp/B09H3H3898', 'https://www.amazon.in/Backpack-Toddler-Animal-Cartoon-Red-Stawberry/dp/B089WFG3BK', 'https://www.amazon.in/Blue-Tree-Synthetic-Cartton-Minnie/dp/B07CXXYQ5X', 'https://www.amazon.in/Half-Moon-Backpack-Luggage-Compartment/dp/B09VCLZ3K4', 'https://www.amazon.in/ADISA-BP004-Weight-Casual-Backpack/dp/B07G3CG9FC', 'https://www.amazon.in/Safari-Laptop-Backpack-Resistant-Fabric/dp/B09B25Z8M2', 'https://www.amazon.in/Bennett-Mystic-Shoulder-Messenger-Repellent/dp/B08X2T2M8G', 'https://www.amazon.in/Step-Backpack-Small-Water-Repellant/dp/B088XH1BP7', 'https://www.amazon.in/Gear-Black-Laptop-Backpack-LBPASPIRE0104/dp/B075MK4TXP']
for url in product_name:
    page = requests.get(url)
    content = requests.get(url).content
    #print(page)
    #print(page.content)
    soup = bs(page.content,'html.parser')
    #print(soup.prettify())

    title = soup.find("span",attrs={"id": 'productTitle'})
    print(title.text)
    desc = soup.find('a', class_='a-link-normal a-color-tertiary')
    print(desc.text)
    aSIN = soup.find("input", attrs={'name': 'items[0.base][asin]'})
    decoded_content = content.decode()
    asins = set(re.findall(r'/[^/]+/dp/([^"?]+)', decoded_content))
    print(asins)

    df = pd.DataFrame()
    df['Description']=title.text
    print(df)
    df['Product Description']=desc.text
    print(df)
    df['ASIN']=asins
    print(df)
    df.to_csv(r'D:\Part2.xls')


