# import pandas as pd
# # from get_similar_products import *

# df = pd.read_csv(r'/home/chantal/Downloads/vision_product_search_product_catalog.csv')

# df_new = df.iloc[:, 0:2]
# df_new.columns = ['col1', 'col2']
# df_new.set_index('col2')
# print(df_new.sample(5))

# img = 

# df2=df.query('Fee == 25000')['Courses']

# # results -> json -> all the details
# # results -> get the actual link
# # [bluedress, redhat] -> (getgslink1&2) -> mapping situation with df -> [link1, link2]
# # [bluedress, redhat] -> access 'link' column of csv -> [link1, link2]
# # replace 'link' column of csv with actual links instead of gs

x = '''
gs://cloud-ai-vision-data/product-search-tutorial/images/46a0cbcf70ba11e89399d20059124800.jpg,image0,product_set0,product_id0,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a1aea370ba11e888d4d20059124800.jpg,image1,product_set0,product_id1,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a1cdb370ba11e8b538d20059124800.jpg,image2,product_set0,product_id2,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a01f0770ba11e88598d20059124800.jpg,image3,product_set0,product_id3,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a03b2670ba11e8b18ad20059124800.jpg,image4,product_set0,product_id4,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a0016b70ba11e896d8d20059124800.jpg,image5,product_set0,product_id5,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a080b870ba11e8aafad20059124800.jpg,image6,product_set0,product_id6,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a159d470ba11e8bcc1d20059124800.jpg,image7,product_set0,product_id7,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a0617070ba11e8b5b4d20059124800.jpg,image8,product_set0,product_id8,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a1121170ba11e8859ed20059124800.jpg,image9,product_set0,product_id9,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46a1975170ba11e8b337d20059124800.jpg,image10,product_set0,product_id10,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/468e4abd70ba11e896ced20059124800.jpg,image11,product_set0,product_id11,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/468e7e2e70ba11e8b290d20059124800.jpg,image12,product_set0,product_id12,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/468ed4f870ba11e8b345d20059124800.jpg,image13,product_set0,product_id13,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/468f1b0c70ba11e8a507d20059124800.jpg,image14,product_set0,product_id14,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/468f3fba70ba11e88028d20059124800.jpg,image15,product_set0,product_id15,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/468f782e70ba11e8941fd20059124800.jpg,image16,product_set0,product_id16,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/468fa24a70ba11e8aac6d20059124800.jpg,image17,product_set0,product_id17,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/468fc8f570ba11e8b821d20059124800.jpg,image18,product_set0,product_id18,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469a4b6e70ba11e8aa44d20059124800.jpg,image19,product_set0,product_id19,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469a08c070ba11e8bd01d20059124800.jpg,image20,product_set0,product_id20,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469a896b70ba11e8be97d20059124800.jpg,image21,product_set0,product_id21,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469ac87870ba11e88fe4d20059124800.jpg,image22,product_set0,product_id22,apparel-v2,,"style=women,category=dress,kids=true",
gs://cloud-ai-vision-data/product-search-tutorial/images/469ae13370ba11e894f4d20059124800.jpg,image23,product_set0,product_id23,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469af76170ba11e8927ed20059124800.jpg,image24,product_set0,product_id24,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469b39f070ba11e8b050d20059124800.jpg,image25,product_set0,product_id25,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469b880770ba11e8911ad20059124800.jpg,image26,product_set0,product_id26,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469bb1ab70ba11e8ae69d20059124800.jpg,image27,product_set0,product_id27,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469bddba70ba11e88c12d20059124800.jpg,image28,product_set0,product_id28,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469bf93370ba11e8b310d20059124800.jpg,image29,product_set0,product_id29,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469c74d470ba11e88377d20059124800.jpg,image30,product_set0,product_id30,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469c334a70ba11e88eb4d20059124800.jpg,image31,product_set0,product_id31,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469cbde170ba11e88510d20059124800.jpg,image32,product_set0,product_id32,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469cff9470ba11e899c8d20059124800.jpg,image33,product_set0,product_id33,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469d4e7a70ba11e8bd19d20059124800.jpg,image34,product_set0,product_id34,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469d794a70ba11e883bcd20059124800.jpg,image35,product_set0,product_id35,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469da8e870ba11e8b136d20059124800.jpg,image36,product_set0,product_id36,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469dd9e670ba11e8b48ad20059124800.jpg,image37,product_set0,product_id37,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469e4d0270ba11e8892fd20059124800.jpg,image38,product_set0,product_id38,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469e07de70ba11e8a336d20059124800.jpg,image39,product_set0,product_id39,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469e902870ba11e8b3d8d20059124800.jpg,image40,product_set0,product_id40,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469ed89770ba11e8a978d20059124800.jpg,image41,product_set0,product_id41,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469f1c5c70ba11e8ae85d20059124800.jpg,image42,product_set0,product_id42,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469f5d8570ba11e8bf68d20059124800.jpg,image43,product_set0,product_id43,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469f9cc070ba11e8a2f3d20059124800.jpg,image44,product_set0,product_id44,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469fc50070ba11e8956ed20059124800.jpg,image45,product_set0,product_id45,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469fe8d970ba11e8bc23d20059124800.jpg,image46,product_set0,product_id46,apparel-v2,,"style=women,category=dress,kids=true",
gs://cloud-ai-vision-data/product-search-tutorial/images/4690d31970ba11e8b615d20059124800.jpg,image47,product_set0,product_id47,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4691aea170ba11e8a1b3d20059124800.jpg,image48,product_set0,product_id48,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4691cb2370ba11e88dfad20059124800.jpg,image49,product_set0,product_id49,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4691f79970ba11e8b25ed20059124800.jpg,image50,product_set0,product_id50,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4692c0e170ba11e892add20059124800.jpg,image51,product_set0,product_id51,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4693a2c770ba11e89d69d20059124800.jpg,image52,product_set0,product_id52,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4693eaee70ba11e8b58bd20059124800.jpg,image53,product_set0,product_id53,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4694b17370ba11e8a74fd20059124800.jpg,image54,product_set0,product_id54,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4694da6370ba11e88c80d20059124800.jpg,image55,product_set0,product_id55,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4695a58a70ba11e8bfc4d20059124800.jpg,image56,product_set0,product_id56,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4695ee2870ba11e89e3ad20059124800.jpg,image57,product_set0,product_id57,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4696b0ba70ba11e88dc4d20059124800.jpg,image58,product_set0,product_id58,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4696d68a70ba11e8bdafd20059124800.jpg,image59,product_set0,product_id59,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4696ff4070ba11e8a81cd20059124800.jpg,image60,product_set0,product_id60,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4697d10c70ba11e8bae3d20059124800.jpg,image61,product_set0,product_id61,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4698a10570ba11e8886ad20059124800.jpg,image62,product_set0,product_id62,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4698cf5970ba11e8a168d20059124800.jpg,image63,product_set0,product_id63,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4698faa370ba11e8bd9fd20059124800.jpg,image64,product_set0,product_id64,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4699c1f870ba11e8a09fd20059124800.jpg,image65,product_set0,product_id65,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46909c5e70ba11e8b052d20059124800.jpg,image66,product_set0,product_id66,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46916b4070ba11e89dbed20059124800.jpg,image67,product_set0,product_id67,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46921af370ba11e8ab49d20059124800.jpg,image68,product_set0,product_id68,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46923d6670ba11e89f5bd20059124800.jpg,image69,product_set0,product_id69,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46929c3d70ba11e88beed20059124800.jpg,image70,product_set0,product_id70,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46930b6b70ba11e89dfdd20059124800.jpg,image71,product_set0,product_id71,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46946de870ba11e89c50d20059124800.jpg,image72,product_set0,product_id72,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46948c8770ba11e8a07cd20059124800.jpg,image73,product_set0,product_id73,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46963fe170ba11e89dabd20059124800.jpg,image74,product_set0,product_id74,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46968f4c70ba11e89d0ad20059124800.jpg,image75,product_set0,product_id75,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46975b0270ba11e8a25fd20059124800.jpg,image76,product_set0,product_id76,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46991e7370ba11e8a1bbd20059124800.jpg,image77,product_set0,product_id77,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/46995a4a70ba11e89604d20059124800.jpg,image78,product_set0,product_id78,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/46997d9170ba11e88553d20059124800.jpg,image79,product_set0,product_id79,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469009b070ba11e8b993d20059124800.jpg,image80,product_set0,product_id80,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469058fa70ba11e8b11fd20059124800.jpg,image81,product_set0,product_id81,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469262fa70ba11e89a19d20059124800.jpg,image82,product_set0,product_id82,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469355b570ba11e88ff2d20059124800.jpg,image83,product_set0,product_id83,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/469445d470ba11e8bdc4d20059124800.jpg,image84,product_set0,product_id84,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/469942d170ba11e89aabd20059124800.jpg,image85,product_set0,product_id85,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4691226e70ba11e8ab97d20059124800.jpg,image86,product_set0,product_id86,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4697844c70ba11e8bb3cd20059124800.jpg,image87,product_set0,product_id87,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4698136e70ba11e8bb30d20059124800.jpg,image88,product_set0,product_id88,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4690366870ba11e8a01bd20059124800.jpg,image89,product_set0,product_id89,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4694187070ba11e8aef4d20059124800.jpg,image90,product_set0,product_id90,apparel-v2,,"style=men,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4695439470ba11e8acedd20059124800.jpg,image91,product_set0,product_id91,apparel-v2,,"style=women,category=shoe",
gs://cloud-ai-vision-data/product-search-tutorial/images/4695830270ba11e8b058d20059124800.jpg,image92,product_set0,product_id92,apparel-v2,,"style=women,category=dress",
gs://cloud-ai-vision-data/product-search-tutorial/images/4697319970ba11e8a7bfd20059124800.jpg,image93,product_set0,product_id93,apparel-v2,,"style=women,category=shoe,kids=true",
gs://cloud-ai-vision-data/product-search-tutorial/images/4698596370ba11e8bf6ad20059124800.jpg,image94,product_set0,product_id94,apparel-v2,,"style=women,category=dress",
'''

y = '''
gs://cloud-ai-vision-data/product-search-tutorial/images/46a0cbcf70ba11e89399d20059124800.jpg,image0,product_set0,product_id0,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a1aea370ba11e888d4d20059124800.jpg,image1,product_set0,product_id1,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a1cdb370ba11e8b538d20059124800.jpg,image2,product_set0,product_id2,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a01f0770ba11e88598d20059124800.jpg,image3,product_set0,product_id3,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a03b2670ba11e8b18ad20059124800.jpg,image4,product_set0,product_id4,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a0016b70ba11e896d8d20059124800.jpg,image5,product_set0,product_id5,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a080b870ba11e8aafad20059124800.jpg,image6,product_set0,product_id6,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a159d470ba11e8bcc1d20059124800.jpg,image7,product_set0,product_id7,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a0617070ba11e8b5b4d20059124800.jpg,image8,product_set0,product_id8,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a1121170ba11e8859ed20059124800.jpg,image9,product_set0,product_id9,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46a1975170ba11e8b337d20059124800.jpg,image10,product_set0,product_id10,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/468e4abd70ba11e896ced20059124800.jpg,image11,product_set0,product_id11,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/468e7e2e70ba11e8b290d20059124800.jpg,image12,product_set0,product_id12,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/468ed4f870ba11e8b345d20059124800.jpg,image13,product_set0,product_id13,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/468f1b0c70ba11e8a507d20059124800.jpg,image14,product_set0,product_id14,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/468f3fba70ba11e88028d20059124800.jpg,image15,product_set0,product_id15,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/468f782e70ba11e8941fd20059124800.jpg,image16,product_set0,product_id16,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/468fa24a70ba11e8aac6d20059124800.jpg,image17,product_set0,product_id17,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/468fc8f570ba11e8b821d20059124800.jpg,image18,product_set0,product_id18,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469a4b6e70ba11e8aa44d20059124800.jpg,image19,product_set0,product_id19,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469a08c070ba11e8bd01d20059124800.jpg,image20,product_set0,product_id20,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469a896b70ba11e8be97d20059124800.jpg,image21,product_set0,product_id21,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469ac87870ba11e88fe4d20059124800.jpg,image22,product_set0,product_id22,apparel-v2,s,"style=women,category=dress,kids=true"
gs://cloud-ai-vision-data/product-search-tutorial/images/469ae13370ba11e894f4d20059124800.jpg,image23,product_set0,product_id23,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469af76170ba11e8927ed20059124800.jpg,image24,product_set0,product_id24,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469b39f070ba11e8b050d20059124800.jpg,image25,product_set0,product_id25,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469b880770ba11e8911ad20059124800.jpg,image26,product_set0,product_id26,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469bb1ab70ba11e8ae69d20059124800.jpg,image27,product_set0,product_id27,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469bddba70ba11e88c12d20059124800.jpg,image28,product_set0,product_id28,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469bf93370ba11e8b310d20059124800.jpg,image29,product_set0,product_id29,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469c74d470ba11e88377d20059124800.jpg,image30,product_set0,product_id30,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469c334a70ba11e88eb4d20059124800.jpg,image31,product_set0,product_id31,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469cbde170ba11e88510d20059124800.jpg,image32,product_set0,product_id32,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469cff9470ba11e899c8d20059124800.jpg,image33,product_set0,product_id33,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469d4e7a70ba11e8bd19d20059124800.jpg,image34,product_set0,product_id34,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469d794a70ba11e883bcd20059124800.jpg,image35,product_set0,product_id35,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469da8e870ba11e8b136d20059124800.jpg,image36,product_set0,product_id36,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469dd9e670ba11e8b48ad20059124800.jpg,image37,product_set0,product_id37,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469e4d0270ba11e8892fd20059124800.jpg,image38,product_set0,product_id38,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469e07de70ba11e8a336d20059124800.jpg,image39,product_set0,product_id39,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469e902870ba11e8b3d8d20059124800.jpg,image40,product_set0,product_id40,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469ed89770ba11e8a978d20059124800.jpg,image41,product_set0,product_id41,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469f1c5c70ba11e8ae85d20059124800.jpg,image42,product_set0,product_id42,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469f5d8570ba11e8bf68d20059124800.jpg,image43,product_set0,product_id43,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469f9cc070ba11e8a2f3d20059124800.jpg,image44,product_set0,product_id44,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469fc50070ba11e8956ed20059124800.jpg,image45,product_set0,product_id45,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469fe8d970ba11e8bc23d20059124800.jpg,image46,product_set0,product_id46,apparel-v2,s,"style=women,category=dress,kids=true"
gs://cloud-ai-vision-data/product-search-tutorial/images/4690d31970ba11e8b615d20059124800.jpg,image47,product_set0,product_id47,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4691aea170ba11e8a1b3d20059124800.jpg,image48,product_set0,product_id48,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4691cb2370ba11e88dfad20059124800.jpg,image49,product_set0,product_id49,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4691f79970ba11e8b25ed20059124800.jpg,image50,product_set0,product_id50,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4692c0e170ba11e892add20059124800.jpg,image51,product_set0,product_id51,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4693a2c770ba11e89d69d20059124800.jpg,image52,product_set0,product_id52,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4693eaee70ba11e8b58bd20059124800.jpg,image53,product_set0,product_id53,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4694b17370ba11e8a74fd20059124800.jpg,image54,product_set0,product_id54,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4694da6370ba11e88c80d20059124800.jpg,image55,product_set0,product_id55,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4695a58a70ba11e8bfc4d20059124800.jpg,image56,product_set0,product_id56,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4695ee2870ba11e89e3ad20059124800.jpg,image57,product_set0,product_id57,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4696b0ba70ba11e88dc4d20059124800.jpg,image58,product_set0,product_id58,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4696d68a70ba11e8bdafd20059124800.jpg,image59,product_set0,product_id59,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4696ff4070ba11e8a81cd20059124800.jpg,image60,product_set0,product_id60,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4697d10c70ba11e8bae3d20059124800.jpg,image61,product_set0,product_id61,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4698a10570ba11e8886ad20059124800.jpg,image62,product_set0,product_id62,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4698cf5970ba11e8a168d20059124800.jpg,image63,product_set0,product_id63,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4698faa370ba11e8bd9fd20059124800.jpg,image64,product_set0,product_id64,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4699c1f870ba11e8a09fd20059124800.jpg,image65,product_set0,product_id65,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46909c5e70ba11e8b052d20059124800.jpg,image66,product_set0,product_id66,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46916b4070ba11e89dbed20059124800.jpg,image67,product_set0,product_id67,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46921af370ba11e8ab49d20059124800.jpg,image68,product_set0,product_id68,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46923d6670ba11e89f5bd20059124800.jpg,image69,product_set0,product_id69,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46929c3d70ba11e88beed20059124800.jpg,image70,product_set0,product_id70,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46930b6b70ba11e89dfdd20059124800.jpg,image71,product_set0,product_id71,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46946de870ba11e89c50d20059124800.jpg,image72,product_set0,product_id72,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46948c8770ba11e8a07cd20059124800.jpg,image73,product_set0,product_id73,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46963fe170ba11e89dabd20059124800.jpg,image74,product_set0,product_id74,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46968f4c70ba11e89d0ad20059124800.jpg,image75,product_set0,product_id75,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46975b0270ba11e8a25fd20059124800.jpg,image76,product_set0,product_id76,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46991e7370ba11e8a1bbd20059124800.jpg,image77,product_set0,product_id77,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/46995a4a70ba11e89604d20059124800.jpg,image78,product_set0,product_id78,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/46997d9170ba11e88553d20059124800.jpg,image79,product_set0,product_id79,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469009b070ba11e8b993d20059124800.jpg,image80,product_set0,product_id80,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469058fa70ba11e8b11fd20059124800.jpg,image81,product_set0,product_id81,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469262fa70ba11e89a19d20059124800.jpg,image82,product_set0,product_id82,apparel-v2,s,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469355b570ba11e88ff2d20059124800.jpg,image83,product_set0,product_id83,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/469445d470ba11e8bdc4d20059124800.jpg,image84,product_set0,product_id84,apparel-v2,s,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/469942d170ba11e89aabd20059124800.jpg,image85,product_set0,product_id85,apparel-v2,s,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4691226e70ba11e8ab97d20059124800.jpg,image86,product_set0,product_id86,apparel-v2,,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4697844c70ba11e8bb3cd20059124800.jpg,image87,product_set0,product_id87,apparel-v2,,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4698136e70ba11e8bb30d20059124800.jpg,image88,product_set0,product_id88,apparel-v2,,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4690366870ba11e8a01bd20059124800.jpg,image89,product_set0,product_id89,apparel-v2,,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4694187070ba11e8aef4d20059124800.jpg,image90,product_set0,product_id90,apparel-v2,,"style=men,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4695439470ba11e8acedd20059124800.jpg,image91,product_set0,product_id91,apparel-v2,,"style=women,category=shoe"
gs://cloud-ai-vision-data/product-search-tutorial/images/4695830270ba11e8b058d20059124800.jpg,image92,product_set0,product_id92,apparel-v2,,"style=women,category=dress"
gs://cloud-ai-vision-data/product-search-tutorial/images/4697319970ba11e8a7bfd20059124800.jpg,image93,product_set0,product_id93,apparel-v2,,"style=women,category=shoe,kids=true"
gs://cloud-ai-vision-data/product-search-tutorial/images/4698596370ba11e8bf6ad20059124800.jpg,image94,product_set0,product_id94,apparel-v2,,"style=women,category=dress"
'''

print(x == y)