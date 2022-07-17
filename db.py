
import psycopg2
from psycopg2.errors import SerializationFailure

import logging

conn = psycopg2.connect("postgresql://chantal:hackrunway2022@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dhackrunway2022-2943")

def info(conn):
    with conn.cursor() as cur:
        cur.execute(
             "CREATE TABLE IF NOT EXISTS users_table (number INT, num_of_searches INT)"),
        cur.execute(
             "CREATE TABLE IF NOT EXISTS wa_table (img_url VARCHAR(600), name VARCHAR(60), description VARCHAR(60), category VARCHAR(60) )")
        cur.execute(
             "CREATE TABLE IF NOT EXISTS search_table (img_url VARCHAR(600), name VARCHAR(60), extern_link VARCHAR(600), price INT, product_img_link VARCHAR(600) )")
      
      
      
        logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)
       
    
    conn.commit()  
    
def get_conn(): return conn

def insert_img_wa(img_url):
    with conn.cursor() as cur:
        cur.execute(
            f"UPSERT INTO wa_table (img_url) VALUES ('{img_url}')"
        )
        logging.debug("wa_tables(): status message: %s",
                      cur.statusmessage)
    conn.commit()

def insert_img_search(img_url):
    with conn.cursor() as cur:
        cur.execute(
            f"UPSERT INTO search_table (img_url, name, extern_link, price) VALUES ('{img_url}', '1', '2', 3)"
        )
        logging.debug("wa_tables(): status message: %s",
                      cur.statusmessage)
    conn.commit()

def insert_wa_tables(conn, img_url, name, description, category):
    with conn.cursor() as cur:
        # if any parameter is None, don't update it.
        # full: f"UPDATE wa_table SET name='{name}', description='{description}', category='{category}' WHERE img_url = '{img_url}' "
        if not img_url:
            return
        elif name:
            print(name, 'ehoeh')
            q = f"UPDATE wa_table SET name='{name}' WHERE img_url = '{img_url}' "
        elif description:
            q = f"UPDATE wa_table SET description='{description}' WHERE img_url = '{img_url}' "
        elif category:
            q = f"UPDATE wa_table SET category='{category}' WHERE img_url = '{img_url}' "
        
        cur.execute(
            q
        )
        logging.debug("wa_tables(): status message: %s",
                      cur.statusmessage)
    conn.commit()

def delete_img(conn,img_url):
    with conn.cursor() as cur:
        cur.execute(
            f"DELETE FROM wa_table WHERE img_url = '{img_url}' "
        )
        logging.debug("wa_tables(): status message: %s",
                      cur.statusmessage)
    conn.commit()

def get_where_link_is(img_url):
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT * FROM search_table WHERE product_img_link = '{img_url}' "
        )
        logging.debug("wa_tables(): status message: %s",
                      cur.statusmessage)
        result = cur.fetchall()
    conn.commit()
    # give back data
    return result 

def update_search_table_image_url(img_url, new_url):
    with conn.cursor() as cur:
        cur.execute(
            f"UPDATE search_table SET img_url='{new_url}' WHERE product_img_link = '{img_url}'"
        )
        logging.debug("wa_tables(): status message: %s",
                      cur.statusmessage)
    conn.commit()


def insert_search_table(img_url, name, extern_link, price, product_img_link):
    with conn.cursor() as cur:
        cur.execute(
            f"INSERT INTO search_table (img_url, name, extern_link, price, product_img_link) VALUES ('{img_url}', '{name}','{extern_link}',{price}, '{product_img_link}' )"
        )
        logging.debug("wa_tables(): status message: %s",
                      cur.statusmessage)
    conn.commit()


def get_search_table():
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT * FROM search_table"
        )
        logging.debug("wa_tables(): status message: %s",
                      cur.statusmessage)
        result = cur.fetchall()
    conn.commit()
    # give back data
    print(result) 
        


    

info(conn)
# insert_wa_tables(conn, img_url="https://api.twilio.com/2010-04-01/Accounts/AC25b264f295b2e06eff7efc77a3ff2132/Messages/MM6951950182a8763bbc558626b55d4ee0/Media/ME08965de80890f6f515252a49bacff03b", name='thi sname', description= None, category= None)
# delete_img(conn, img_url="gs://hack-the-runway.appspot.com/blue-plaid-pleated-jumper-2.jpg")
# insert_img_search('some url')
# insert_img_search('second url')
# insert_img_search('second url11')
# insert_img_search('second url111')
# insert_img_search('second url1111')
# insert_img_search('second url111111')
# x = get_where_link_is('second url')
# print(x)
# update_search_table_image_url(img_url="img1", new_url="real_img1")
# insert_search_table(img_url="img1", name="Pink Mini Dress Ringer Sheath Dress 90s Party", extern_link="https://www.etsy.com/listing/1036443637/pink-mini-dress-ringer-sheath-dress-90s", price=54.8, product_img_link="https://storage.cloud.google.com/cloud-ai-vision-data/product-search-tutorial/images/46923d6670ba11e89f5bd20059124800.jpg")
