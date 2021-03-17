#!/usr/bin/env python
# coding: utf-8

# # test, plus bas il y a l'exercices

# In[10]:


pwd


# In[119]:


import pandas as pd
import os
import numpy as np
df = pd.read_csv(r"/home/jovyan/work/mower_market_snapshot.csv", delimiter=";")
df.head()


# In[22]:


import pandas as pd
import os
df = pd.read_csv(r"/home/jovyan/work/mower_market_snapshot.csv", delimiter=";")
df


# In[23]:


import pandas as pd
import os
df = pd.read_csv(r"/home/jovyan/work/mower_market_snapshot.csv", delimiter=";")
df.head(20)


# In[25]:


series = pd.Series([1,2,np.nan, 10])
series


# In[27]:


df2 = pd.DataFrame(np.arange(1, 7501).reshape(500,15))
df2.head(4)


# In[52]:


df.sort_values("quality")


# In[37]:


df.sort_values("capacity")


# In[39]:


df.sort_values("id")


# In[54]:


df.sort_values(by='capacity', ascending=False).head()


# In[55]:


df.sort_values(by='capacity', ascending=False)


# In[47]:


df.sort_values(by='capacity').head()


# In[51]:


df.loc[0,:]


# In[56]:


df.loc[:,'capacity' :'margin']


# In[57]:


df.loc[1,'capacity' :'margin']


# In[58]:


df.loc[0,'capacity' :'market_share']


# In[68]:


df[df['capacity'].isin([5.3, 2.7])]


# In[263]:


df.iloc[:,0:4].head(10)


# In[74]:


df.groupby(['capacity', 'price']).sum()


# # EXERCICES A FAIRE POUR MERCREDI 17
exo1 afficher le tableau
# In[411]:


import pandas as pd
import numpy as np
def csvReader():
    return pd.read_csv(r"/home/jovyan/work/mower_market_snapshot.csv", delimiter=";")
df = csvReader()
df

exo 3 on affiche la colonne qu'on a besoin prod_cost il ya 2 manières avec le numéro de la colonne ou bien le nom
# In[380]:


def colProd():
    return df.iloc[:,5].head()
df = colProd()
df


# In[383]:


def colProd():
    return df.loc[:,'prod_cost']
df = colProd()
df

la on filtre les valeurs non attribués unknown
# In[337]:


def colProd():
    return df.loc[df.prod_cost=='unknown',:]
df = colProd()
df

exo 4 on additionner les valeurs null 
# In[390]:


def sumNull(df):    
    return df.isnull().sum()
sumNull(df)

isoler la colonne prod_cost
# In[341]:


df.isnull().loc[:,'prod_cost'].sum()

exo 5 convertir la colonne object en float sinon bloquer, puis additionner et diviser 1400 puis on écrit sur le csv et remplacer les valeurs null
# In[360]:


print(df.dtypes)


# In[376]:


def afficherMoy(am):
    x = 0.0
    tab = pd.to_numeric(df.loc[:,'prod_cost'], errors='coerce')
    tab = tab.replace(np.nan, 0, regex=True)
    for i in tab :
        x += i

    m = x/1400 
    print(m)

    df.loc[:,'prod_cost'] = df.loc[:,'prod_cost'].replace(np.nan, moy, regex=True)


    return df.isnull().sum()

afficherMoy(df)

exo 6 afficher les valeurs unique de warranty
# In[247]:



df.iloc[:,8]


# In[423]:


def warrantyUnique(wu):
    print(df['warranty'].unique())
warrantyUnique(df)

exo 7 harmoniser les valeurs uniques, recuperer les valeurs et mettre dans des tableaux vides on les tries chaque valeur 1 2 3, par exemple 3 ans va dans la tab 3, 2ans., va dans la tab 2, puis quand c'est trier on va les remplacer par la valeur qu'on a mis

# In[249]:



df_new = df.drop_duplicates(subset = "warranty")

print(df_new.sort_values(by = 'warranty', ascending = False))


# In[418]:


def replace(r):
    tab = df['warranty'].unique()
    t1,t2,t3=[],[],[]
    for i in tab:
        if i[0] == '1':
            t1.append(i)
        if i[0] == '2':
            t2.append(i)
        if i[0] == '3':
            t3.append(i)    
    df.loc[:,'warranty'] = df.loc[:,'warranty'].replace(t1, 1, regex=True)
    df.loc[:,'warranty'] = df.loc[:,'warranty'].replace(t2, 2, regex=True)
    df.loc[:,'warranty'] = df.loc[:,'warranty'].replace(t3, 3, regex=True)
    print(df['warranty'].unique())
    
replace(df)

une autre manière pour remplacer
# In[251]:


df.loc[:,'warranty'].replace(['3ans' '3 ans.' '3_ans' '3 anss' '3ans.' '3 ans' '3_ans.' '3_anss'
 '3anss'], value='3 ans', regex=True)

exo 8 afficher les 3 valeurs unique warranty
# In[407]:


def warrantyUnique(wu):
    print(df['warranty'].unique())
warrantyUnique(df)

exo 9 grouper les valeurs dans 3 tableaux et remplacer
# In[405]:


t1,t2,t3=[],[],[]
for x in df['price']:
    if x > 0 and x <= 300:
        t1.append(x)
    if x > 300 and x <= 500:
        t2.append(x)
    if x > 500:
        t3.append(x)
print(t1)
print(t2)
print(t3)
    df.loc[:,'price'] = df.loc[:,'price'].replace(t1, "0-300", regex=True)
    df.loc[:,'price'] = df.loc[:,'price'].replace(t2, "301-500", regex=True)
    df.loc[:,'price'] = df.loc[:,'price'].replace(t3, "501-++", regex=True)
df.loc[:,'price']


# In[ ]:


simplifier


# In[408]:


def catPrice(cp):
    for x in df['price']:
        if x > 0 and x <= 300:
          df.loc[:,'price'] = df.loc[:,'price'].replace(x, "0-300", regex=True)
        if x > 300 and x <= 500:
           df.loc[:,'price'] = df.loc[:,'price'].replace(x, "301-500", regex=True)
        if x > 500:
           df.loc[:,'price'] = df.loc[:,'price'].replace(x, "501-++", regex=True)
    return df.loc[:,'price']
catPrice(df)

 ex 10 on créer 3 colonne numériques
# In[409]:


def replaceTypeProduct(rtp):
    tab = df['product_type'].unique()

    for i in range(len(tab)):
        df.loc[:,'product_type'] = df.loc[:,'product_type'].replace(tab[i], (i+1), regex=True)

    print(df['product_type'].unique())
replaceTypeProduct(df)

ex 11 on renomme les 3 colonnes numeriquesj'ai pas trouver de solutions pour l'erreur :(
# In[422]:


def addColonnes(ac):
    df.insert(11, "auto-portee",0)
    df.insert(12, "electrique", 0)
    df.insert(13, "essence", 0)
    
    for i in range(len(df.loc[:,'product_type'])):
        if df.loc[:,'product_type'][i] == 1:
            df.loc[:,'auto-portee'][i] = 1
        elif df.loc[:,'product_type'][i] == 2:
            df.loc[:,'electrique'][i] = 1
        elif df.loc[:,'product_type'][i] == 3:
            df.loc[:,'essence'][i] = 1


    return df.loc[:,('product_type','auto-portee','electrique','essence')]
display(addColonnes(df))

