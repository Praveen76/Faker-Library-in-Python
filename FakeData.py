# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:54:25 2018

@author: praveenanwla
"""

from faker import Faker
import json            # To create a json file                 
from random import randint      # For student id 
fake = Faker() 

#==============================================================================

import random

from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

# Our custom provider inherits from the BaseProvider
class TravelProvider(BaseProvider):
    def Eduation(self):
        destinations = ['High School', 'Graduation', 'Post Graduation', 'PHD']
        return random.choice(destinations)
        
    def FamilySize(self):
        Strength = ['0', '1', '2', '3', '4']
        return random.choice(Strength)
        
    def Ethnicity(self):
        People = ['Mexican', 'Dominican', 'Asian', 'Hispanic']
        return random.choice(People) 
        
    def Nationality(self):
        Peoples = ['German', 'Indian', 'American', 'African','French']
        return random.choice(Peoples)         
    def City(self):
        Cities=['New York','Los Angeles','Chicago','Philadelphia','Dallas']
        return random.choice(Cities)
                

# Add the TravelProvider to our faker object
fake.add_provider(TravelProvider)
#==============================================================================
    
from dateutil.relativedelta import *
from datetime import date
import pandas as pd
from random import randint
import datetime


data = pd.DataFrame()

Email=[]
City=[]
Address=[]
Gender=[]
DOB=[]
#State=[]
#Occupation=[]
Eduation=[]
FamilySize=[]
Ethnicity=[]
Nationality=[]

for i in range(0,500):
    Email.append(fake.email())
    Address.append(fake.address())
    Gender.append(fake.simple_profile()['sex'])
    Eduation.append(fake.Eduation())
    FamilySize.append(fake.FamilySize())
    Ethnicity.append(fake.Ethnicity())
    Nationality.append(fake.Nationality())
    
City=[]
for i in range(0,500):
    City.append(fake.City())
    

  
    
    
data['City']=City
data['Email']=Email
data['City']=City
data['Address']=Address
data['Gender']=Gender

data['State']=State

data['Eduation']=Eduation
data['FamilySize']=FamilySize
data['Ethnicity']=Ethnicity
data['Nationality']=Nationality


data['State']=0
for index, row in data.iterrows():
    if(row['City']== 'New York'  ):
         data['State'].iloc[index]='New York'
    if(row['City']== 'Los Angeles'  ): 
        data['State'].iloc[index]='California'    
    if(row['City']== 'Chicago'  ): 
        data['State'].iloc[index]='Illinois' 
    if(row['City']== 'Philadelphia'  ): 
        data['State'].iloc[index]='Pennsylvania'  
    if(row['City']== 'Dallas'  ): 
        data['State'].iloc[index]='Texas'  


#create DOB ranging from 1960 to 1985
data['DOB']=0
for index,row in data.iterrows():
    data['DOB'].iloc[index]=datetime.date(randint(1960,1985), randint(1,12),randint(1,28))  


#==============================================================================
   
   
   
data['Age']=0
for index,row in data.iterrows():          
   data['Age'].iloc[index]=relativedelta(date.today(), row['DOB']).years


data['HireDate']=0

for index,row in data.iterrows():
    data['HireDate'].iloc[index]=datetime.date(randint(2017,2018), randint(1,12),randint(1,28))    
    #data['HireDate'].iloc[index]=str(date.year)+'/'+ str(date.month) +'/'+ str(date.day)



#Zip Code

data['ZipCode']=0

for index,row in data.iterrows():
    data['ZipCode'].iloc[index]=row['Address'][-5:]



data.head()
