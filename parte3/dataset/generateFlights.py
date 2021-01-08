import pandas as pd
import datetime

from random import seed
from random import randint
from random import choice

# Modify this parameters as required
MAX_RECORDS = 1000
READ_PATH = r'C:\Users\10034\Downloads\arangoDB-demo(1)\arangoDB-demo\parte3\dataset\Datos_Aeropuertos_Limpios.json'
WRITE_PATH = r'C:\Users\10034\Downloads\arangoDB-demo(1)\arangoDB-demo\parte3\dataset\flights_'+str(MAX_RECORDS)+'.json'

# Method to load data from a json file determined by READ_PATH
def loadData():
    df = pd.read_json(READ_PATH)
    return df 

# Method to extract the _key column from a dataframe and return it as a list 
def getAirportsKey(df):
    claves = df["_key"].values.tolist()
    return claves

# Method to format data into UTC timestamp
def generateDateUTC(day, month, year, hours, minutes, seconds):

    new_month = "0"+str(month) if month < 10 else str(month)
    new_day = "0"+str(day) if day < 10 else str(day)
    new_hours = "0"+str(hours) if hours < 10 else str(hours)
    new_minutes = "0"+str(minutes) if minutes < 10 else str(minutes)
    new_seconds = "0"+str(seconds) if seconds < 10 else str(seconds)

    timeUTC = "2021-"+new_month+"-"+new_day+" "+new_hours+":"+new_minutes+":"+new_seconds
    return timeUTC

# Method to format desired time
def generateTime(hours, minutes, seconds):
    new_hours = "0"+str(hours) if hours < 10 else str(hours)
    new_minutes = "0"+str(minutes) if minutes < 10 else str(minutes)
    new_seconds = "0"+str(seconds) if seconds < 10 else str(seconds)

    time = new_hours+":"+new_minutes+":"+new_seconds
    return time 

# From a list it generates random combinations into a json format (with _key, _from and _to indexes) required for ArangoDB
def generateJsonData(list): 
    seed(2)
    keyCount = 100
    jsonDoc = "["
    
    for i in range (0,MAX_RECORDS):
        origen = ""
        destino = "" 
        while (origen == destino):
            origen = randint(0, len(list)-1)
            destino = randint(0, len(list)-1) 

        departureDate = datetime.datetime.today()
        departureDate = departureDate.replace(hour=0, minute=0, second=0, microsecond=0)
        
        days = randint(1,365)
        minutes = choice([0,5,10,15,20,25,30,35,40,45,50,55])
        hours = randint(9, 22)
        seconds = 0

        departureDate = departureDate + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        day = departureDate.day
        month = departureDate.month
        year = departureDate.year

        departureUTC = generateDateUTC(day, month, year, hours, minutes, seconds)
        departureTime = generateTime(hours, minutes, seconds)
        
        jsonDoc += "{\"_key\":\""+str(keyCount)+"\",\"_from\":\"airports/"+list[origen]+"\",\"_to\":\"airports/"+list[destino]+"\","
        jsonDoc += "\"day\":\""+str(day)+"\",\"month\":\""+str(month)+"\",\"year\":\""+str(year)+"\",\"departureTimeUTC\":\""+departureUTC+"\",\"departureTime\":\""+departureTime+"\"}" 

        keyCount += 1
        if (i+1 != MAX_RECORDS):
            jsonDoc += ","

    jsonDoc += "]"
    return jsonDoc

# Method to write a string of data into a file determined by WRITE_PATH
def writeFileJson(data):
    f = open(WRITE_PATH, "a")
    f.write(data)
    f.close()


def main():
    data = loadData()
    airportKeys = getAirportsKey(data)
    jsonData = generateJsonData(airportKeys)
    writeFileJson(jsonData)

if __name__ == "__main__":
    main()

