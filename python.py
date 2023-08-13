# import requests
import requests

# define the api key and base url
API_KEY =  "6005a8fdfc81f42b248a7193df394aa4"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# welcome message and instructions
print("-"*90)
print("###  Welcome to the weather app the app show you the weather \n in any city in the world if want to exit the app enter 'exit' or 'q'  ###")
print("-"*90+"\n")

# making the app run forever 
while True:

    # get the city name from user
    city_name = input("Enter city name : ")

    # create the complete url
    requests_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"

    # send the http request to the server
    response = requests.get(requests_url)

    if city_name == "exit" or city_name == "q":
        break

    # check the status for request success or not 200 => success
    if response.status_code == 200:

        data = response.json()

        # print(data) # for testing

        print("-"*50)
        
        # get the data from the json file
        cityName = data['name']
        print(f"- City Name => {cityName} -")

        theCountry = data['sys']['country']
        print(f"- the country => {theCountry} -" )

        theDescription = data['weather'][0]['description']
        print(f"- the description : {theDescription} -")

        theTemperature = round(data['main']['temp'] - 273.15, 2)
        print(f"- the Temperature : {theTemperature} celcius -")

        theWindSpeed = data['wind']['speed']
        print(f"- wind speed : {theWindSpeed} km\h ")

        theCloud = data['clouds']['all']
        print(f"- the cloud : {theCloud} KPa \n")

        print("- Thanks for using our app -")
        print("-"*50,)

    # if the request failed
    else:   
            print("Error in the HTTP request")
            break

# close the app and connection
print("- Closing the app and connection ...")

# close  the connection
response.close()

