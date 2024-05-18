import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ycrmGMKE97Lv1OZa5auJ1lwKaoDG8DzS"

while True:
   orig = input("Ciudad de origen: ")
   if orig == "quit" or orig == "q":
        break
   dest = input("Ciudad de destino: ")
   if orig == "quit" or orig == "q":
        break
   url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
   print("url: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data ["info"] ["statuscode"]
   if json_status == 0:
    print("API Status: " + str(json_status) + " = Una llamada de ruta exitosa.\n ") 
    print("=============================================")
    print("Desde " + (orig) + " a " + (dest))
    print("Duracion de viaje: " + (json_data["route"]["formattedTime"]))
    print("Kilometros:" + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    print("Combustible (Ltr):" + str("{:.2f}".format((json_data["route"]["distance"])*3.78)))
    print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    print("=============================================\n")
