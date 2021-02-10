 #Horraires d'arrets


import pprint
import json
import requests
import csv
import datetime
import os
from pandas import DataFrame


class SNCF_time():


    def __init__(self):

        self.url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
        self.headers = {"Authorization": "e782509f-272a-4868-9bd0-ea9a3bea6463"}
        self.file_json= "stop_areas_rac"
        self.file="stop_rac.txt"
        self.stop_list=[]
        self.corrected_departure_time=[]
        self.arrival_time=[]
        self.departure_time=[]
        self.corrected_arrival_time=[]
        

    def write_json(self): 

        r= requests.get(self.url, headers=self.headers)

        with open(self.file_json + ".json", "w") as file:
            json.dump(r.json(), file)

    def time_stops(self):

        with open(self.file_json + ".json", "r") as file:
            data = json.load(file)

        stop_acess=data["journeys"][0]["sections"][1]["stop_date_times"]

        for stop in stop_acess:

            print(stop["stop_point"]["name"])
            self.stop_list.append(stop["stop_point"]["name"]) #print the names of stops

            self.arrival_time=stop["base_arrival_date_time"]
            self.corrected_arrival_time=datetime.datetime.strptime(self.arrival_time, "%Y%m%dT%H%M%S")
            print('The train arrives at', self.corrected_arrival_time)

            self.departure_time=stop["base_departure_date_time"]#print(departure_time)
            self.corrected_departure_time=datetime.datetime.strptime(self.departure_time, "%Y%m%dT%H%M%S")
     
            print('The train leaves at',self.corrected_departure_time) 
          
            self.stop_time_in_the_train_station=(self.corrected_departure_time - self.corrected_arrival_time)
            
            print('time stop:' , self.stop_time_in_the_train_station)



# let instanciate the SNCF_time class to get the time of arrival and departure between Paris and Lyon:
s=SNCF_time()
s.write_json()
s.time_stops()



 
            