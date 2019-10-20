# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

replies = pd.read_csv('C:/Users/huangxing/.spyder-py3/rumor_project/rumor_dataset/replies.csv')
article_replies = pd.read_csv('C:/Users/huangxing/.spyder-py3/rumor_project/rumor_dataset/article_replies.csv')
articles = pd.read_csv('C:/Users/huangxing/.spyder-py3/rumor_project/rumor_dataset/articles.csv')

article_merge = pd.merge(articles, article_replies, on=['articleId'], how='inner')
article_merge = pd.merge(article_merge, replies, on=['replyId'], how='inner')

del article_replies,articles,replies

'''

article_merge.to_excel('article_merge.xls')
print(article_merge.info())
text_x 是articles_text
text_y 是replies_text
#print(article_merge['replyType'])

'''

article_merge=article_merge.drop(['userIdsha256_x' ,'references' , 'tags' , 'appId_x', 'hyperlinks', 'userIdsha256_y' , 'appId' ,'userIdsha256'  , 'type','appId_y'],axis=1)

#print(article_merge.info());

    
    
index=[]
for x in range(len(article_merge)):
    if(article_merge.replyType[x] == "NOT_ARTICLE"):
         index.append(x)
    elif(article_merge.replyType[x] == "OPINIONATED"):
        index.append(x)

for x in range(len(article_merge)):
     if(article_merge.status[x] == "DELETED"):
         index.append(x)

article_merge=article_merge.drop(index)


article_merge=article_merge.sort_values(by='articleId')
article_merge['adde']=article_merge.duplicated('articleId') #添增新的add欄位 
article_merge=article_merge.reset_index() #重置index
del index

#print(article_merge.info());
#print(article_merge.duplicated('articleId'))




x_len=0
for x in range(len(article_merge)):
    x_len=x_len+1

my_ind=[]
logic=False
x_len=x_len-1


while x_len>-1:
    if(logic==True):
        my_ind.append(x_len)
        logic=False
    if(article_merge.adde[x_len] == True):
        my_ind.append(x_len)
        logic=True

    x_len=x_len-1


'''for x in range(len(my_ind)):
    print(my_ind[x]) 
'''    
   
 
my_ind=list(set(my_ind))
my_ind.sort()



article_control=article_merge
x_count=0
my_ind_con=[] #


for x in range(len(article_control)):
    if(x_count == len(my_ind)):
        my_ind_con.append(x)
    else:
        if(my_ind[x_count] != x):
            my_ind_con.append(x)
        if(my_ind[x_count] == x):
            x_count=x_count+1
        
article_control=article_control.drop(my_ind_con)
article_control=article_control.reset_index() 

my_ind_rumor=[]
my_ind_notrumor=[]

for x in range(len(article_control)):
    if(article_control.replyType[x]=='RUMOR'):
        my_ind_rumor.append(x)
    if(article_control.replyType[x]=='NOT_RUMOR'):
        my_ind_rumor.append(x)

      
        
'''
a = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
a = pd.DataFrame(a) 

print(a)
print('\n')
print(a.drop(0,axis = 1))
print('\n')
print(a.drop(0))

''' 

'''
前處理要做的事情
    簡體轉中文
    刪除多餘的空白見

用謠言做分群，用非監督式分群(找柯文哲或韓國瑜分群)
討探這件事為什麼有謠言。

'''

'''
index=[]
for x in range(len(replies)):
    if(replies.type[x] == "NOT_ARTICLE"):
         index.append(x)
    elif(replies.type[x] == "OPINIONATED"):
        index.append(x)
        
        
replies=replies.drop(index)

print(replies['text'])
'''

del logic,x_len