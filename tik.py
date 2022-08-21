import TikTokApi
from TikTokApi import TikTokApi
import json
import pandas as pd
import sys
import copy


def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = [value , dict_1[key]]
   return dict_3


def get_Data(hashtag):  
    with TikTokApi() as api:
         dict_t = dict()
         tag = api.hashtag(hashtag)
         i=0
         for video in tag.videos():
                dict_c= video.as_dict  # imbrication de dictionnaire mon dieu s'était dieu
                dict_t[i]=dict_c
                i=i+1
                #print(dict_t)
             #print("le contenu :",video)
             #dict_4=mergeDictionary(dict_t,dict_c)
             #dict_t=copy.deepcopy(dict_4)
             #print("num "+str(i),dict_c.__sizeof__)
             #i = i+1
    
    with open('export.json', 'w') as f:
             json.dump(dict_t, f, indent=2)
    df=pd.read_json('export.json',orient='index')
    df.to_csv('tiktokdata.csv',index=True,header=True)


if __name__== '__main__':
     get_Data(sys.argv[1])
     
     
  







