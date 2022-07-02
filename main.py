import requests
BaseUrl = "https://api.weatherapi.com/v1/current.json?key=70f12e3920634091b11154453220207&q="

Location = input("Enter city name:")
FinalLink = BaseUrl + Location

r = requests.get(FinalLink)
data = r.json()
print("Current Weather: ",data["current"]["temp_c"], "C")

print("Wind Speed: ", data["current"]["wind_kph"])
print("Humidity:" ,data["current"]["humidity"])
print("Cloud:" , data["current"]["cloud"])
