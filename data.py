import pandas as pd
# from get_similar_products import *

df = pd.read_csv(r'/home/chantal/Downloads/vision_product_search_product_catalog.csv')

df_new = df.iloc[:, 0:2]
df_new.columns = ['col1', 'col2']
df_new.set_index('col2')
print(df_new.sample(5))