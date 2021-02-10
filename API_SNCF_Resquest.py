

import pprint
import json
import requests
import csv
import pandas as pd
import numpy as np


class Stop_area():


    def __init__(self):

        self.url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
        self.headers = {"Authorization": "e782509f-272a-4868-9bd0-ea9a3bea6463"}
        self.file_json= "stop_areas"
        self.file_csv="stop_areas.csv"

        self.list_ids = []
        self.list_name= []
        self.list_label= []
        self.list_timezone= []
        self.data=[]
      

    def write_json(self): 

        r= requests.get(self.url, headers=self.headers)

        with open(self.file_json + ".json", "w") as file:
            json.dump(r.json(), file)



    def Finder(self):

        with open(self.file_json + ".json", "r") as file:
            data = json.load(file)    

        areas = data["stop_areas"]

        for loop_area in areas:
            if type(loop_area) == dict:
               if "id" in loop_area.keys(): 
                 local_id = loop_area["id"]
                 list_ids.append(local_id)
               else:
                    print("Missing key id")
            else: 
                 print(f"Unexpected format {type(loop_area)}")

        for loop_area in areas:
            if type(loop_area) == dict:
                if "name" in loop_area.keys(): #!!!!!!
                   local_name= loop_area["name"]
                   self.list_name.append(local_name)
                else:
                    print("Missing key name")
            else:
                print(f"Unexpected format {type(loop_area)}")


        for loop_area in areas:
           if type(loop_area) == dict:
              if "timezone" in loop_area.keys():
                 local_timezone= loop_area["timezone"]
                 self.list_timezone.append(local_timezone)
              else:
                  print("Missing key name")
           else:
               print(f"Unexpected format {type(loop_area)}")


        for loop_area in areas:
           if type(loop_area) == dict:
               if "label" in loop_area.keys(): #!!!!!!
                  local_label= loop_area["label"]
                  self.list_label.append(local_label)
               else:
                   print("Missing key name")
           else:
                print(f"Unexpected format {type(loop_area)}")

        data= zip(self.list_ids,self.list_name,self.list_timezone,self.list_label)

    def write_file(self):
        self.data= zip(self.list_ids,self.list_name,self.list_timezone,self.list_label)
        df=pd.DataFrame(data=self.data,columns=self.head)
        df.to_csv(self.file_csv, index=True, sep=";") 



s=Stop_area()
s.write_json()
s.Finder()
s.write_file()

'''

def csv(self):
data= set(zip(list_ids,list_name,list_timezone,list_label))

# exporter en csv vec le module CSV

with open("apiStopAreas.csv","w") as file:
    head = ["ids","name","timezone","label"]
    fileWriter = csv.writer(file,delimiter=";")
    fileWriter.writerow(i for i in head)

    for row in data:
         fileWriter.writerow(row)
'''
# exporter en CSV avec Pands

  