import pandas as pd
import os
#%%
url_starte=r'https://dataset-upload-kosmos.s3.us-west-2.amazonaws.com/Youtube/pictures/'
path=r'B:\PycharmProjects\spoof-detection\youtube1\vids1\pictures'
list=os.listdir(path)
#%%
links=[]
name=[]
for person in list:
    pictures=os.listdir(os.path.join(path,person))
    for pic in pictures:
        name.append(pic)
        link=url_starte+person+'/'+'live'+'/'+pic
        links.append(link)
#%%
df=pd.DataFrame({'Links':links,'Name':name})
#%%
df.to_csv('list.csv')
#%%
df2=pd.read_csv('list.csv')
