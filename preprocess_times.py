#Importing necessary libraries
import numpy as np
import pandas as pd

def times_preprocess(filename):
    '''This function does the required preprocessing for the Times dataset
       such as:
           1) Fill in missing values with 0
           2)make the columns whose entries are non-uniform into uniform values
           3)Convert numbers in string format into float/int accordingly
           4) The world rank in some cases are specified like 201-250, 251-300
              and so on, so converting those into numbers such as 201,202,..
              is also done.
              
         ####Function Parameters####
         Input params: filename- type str, the Times Dataset CSV file name
         Returns: df- A pandas dataframe'''
         
         
    assert isinstance(filename,str)
    assert filename[-4:]=='.csv'
    df=pd.read_csv(filename)
    df= df.replace('-', 0)
    df=df.fillna(value=0, axis=None, inplace=False, limit=None, downcast=None)
    df['world_rank']=df['world_rank'].str.split("-").str[0]
    df['world_rank'] = df['world_rank'].map(lambda x: x.lstrip('='))
    df['world_rank']= df['world_rank'].astype('int')
    df['income']=df['income'].astype(float)
    df['international_students']=df['international_students'].str.split('%').str[0]
    print(df.head())
    df['international']=df['international'].astype(float)
    start_year=2011
    end_year=2016
    len_list=[]
    for i in range(start_year,end_year+1):
        len_list.append(len(df[df.year==i]))
    print(len_list)
    total=0 
    for i in len_list:
        for j in range(i):
            df.loc[j+total,"world_rank"]=int(j+1)
        total+=i
    return df


def times_nation_top_100(df,nation,startyear,endyear):
    '''This function takes in the Times dataset Pandas dataframe
       and finds out the number of universities from that country
       in the top 100 of the Times Rankings in every year in the closed 
       interval [startyear,endyear] and returns a list of the same.
       
       ####Function Parameters####
         Input params: df-Pandas dataframe of Times dataset
                       nation-The nation for which we want the 
                              number of top 100 universities. Type str
                       startyear-The year to start checking from. Type int
                       endyear-The year to end check. Type int
        
        Returns:res- List of number of top 100 universities from
                     the specified nation from startyear to endyear.'''
                     
       
    assert isinstance(df,pd.DataFrame)
    assert isinstance(nation,str)
    assert nation in df['country'].unique()
    assert isinstance(startyear,int) and isinstance(endyear,int)
    assert endyear>startyear
    assert startyear>=2011 and startyear<2016
    assert endyear>2011 and endyear<=2016
    res=[]
    for i in range(startyear,endyear+1):
        res.append(df[df.year==i]['country'][:100][df.country==nation].count())
    return res


def times_univ_ranking_list(df,univ):
    '''This function takes in the Times dataset pandas dataframe and gives
       out the world ranking of the specified university 'univ' over the 
       years 2011-2016 as a list.
       
       ####Function Parameters####
       Input params: df- Pandas dataframe of Times dataset
                     univ-The university whose rankings over the years
                          we need.
                          
       Returns: res- A list of rankings of that university'''
       
    assert isinstance(df,pd.DataFrame)
    assert isinstance(univ,str)
    assert univ in df['university_name'].unique()
    res=list(df['world_rank'][df['university_name']==univ])
    return res

    
def times_univ_dataframe(df,univ):
    '''This function takes in the Times dataset pandas dataframe and
       filters the dataframe by the university name given by the string 
       'univ'
       
       ####Function Parameters####
       Input params: df- Pandas dataframe of Times dataset
                     univ-The university based on which we want to
                          filter the dataframe
       Returns: The Filtered Pandas dataframe'''
    
    assert isinstance(df,pd.DataFrame)
    assert isinstance(univ,str)
    assert univ in df['university_name'].unique()
    return df[df['university_name']==univ]

    
    

