from win10toast import ToastNotifier
import requests
notfy = ToastNotifier()

def main():
    city = "hyderabad"
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=5d82bd007e89d3d09e87df9f526cd725"
    city_weather = requests.get(url.format(city)).json()
    print(city_weather['main']['temp'])
    print('-----------start -0---------------------------')
    notfy.show_toast('Weather',"temperature" + str(city_weather['main']['temp']), icon_path='icon/icon.ico', duration=10)
    print('-----------end -0---------------------------')



if __name__ == '__main__':
    main()
