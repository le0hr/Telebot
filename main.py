import requests, json
file = open('hello.txt')
hellotext = file.read()
file.close()
a = 0

url = {
    'getUpdates':"https://api.telegram.org/bot6765342240:AAHOUXXT9Pex5ZiO7kfyQ41jxTSTkth2eHs/getUpdates",
    'sendMessage':"https://api.telegram.org/bot6765342240:AAHOUXXT9Pex5ZiO7kfyQ41jxTSTkth2eHs/sendMessage",
    'getWeather':"https://api.open-meteo.com/v1/forecast"
}
Params = {
    'getUpdates':{"offset":0},
    'start':{"chat_id":0, "text":0, "reply_markup": {"inline_keyboard": [
      [
        {
          "text": "Cherkasy",
          "callback_data":"Cherkasy"
        },
        {
          "text": "Button2",
          "url": "https://example2.com"
        }
      ]
    ]}},
    'forecast':{"chat_id":0, "text":0, "reply_markup": {"inline_keyboard": [
      [
        {
          "text": "Monday",
          "callback_data":"Mon"
        },
        {
          "text": "Tuesday",
          "callback_data":"Tue"
        },
        {
          "text": "Wednesday",
          "callback_data":"Wed"
        },
        {
          "text": "Thursday",
          "callback_data":"Thu"
        }
      ],
      [
          {
          "text": "Friday",
          "callback_data":"Fri"
        },
        {
          "text": "Sanday",
          "callback_data":"San"
        },
        {
          "text": "Saturday",
          "callback_data":"Sat"
        }
          
      ]
    ]}},
    'getWeather':{"latitude":52.52, "longitude":13.41, "daily":["temperature_2m_max","temperature_2m_min","rain_sum","showers_sum","snowfall_sum","wind_speed_10m_max","wind_direction_10m_dominant"] }
}

def listen (answ):
    message = requests.get(url['getUpdates'])
    message = message.json()

    if len(message['result']) >0:
        if not answ:
            Params['getUpdates']['offset']= message['result'][0]['update_id'] + 1
            requests.post(url['getUpdates'], json=Params['getUpdates'])
            print(type(message))
            return True, message
        elif answ:
            Params['getUpdates']['offset']= message['result'][0]['update_id'] + 1
            requests.post(url['getUpdates'], json=Params['getUpdates'])
            if message['result'][0]['callback_query']['data'] == "Cherkasy":
                city = "Cherkasy"
                return True, city
    else:
        return False, 0

def start ():
    Params['start']['chat_id']=message['result'][0]['message']['from']['id']
    Params['start']['text']=hellotext
    r = requests.post(url['sendMessage'], json=Params['start'])
    print(0)
    excpetansw = 1
    return excpetansw

def weather(city):
    Params['forecast']['chat_id']=message['result'][0]['message']['from']['id']
    r = requests.post(url['sendMessage'], json=Params['forecast'])
    weather = requests.post(url['getWeather'], data = Params['getWeather'])
    weather = weather.json()
    while True:
        dayOfTheWeek = requests.get(url['getUpdates'])
        dayOfTheWeek = dayOfTheWeek.json()
        if len(dayOfTheWeek['result']) >0:
            Params['getUpdates']['offset']= dayOfTheWeek['result'][0]['update_id'] + 1
            requests.post(url['getUpdates'], json=Params['getUpdates'])
            if dayOfTheWeek['result'][0]['callback_query']['data'] == "Mon":
                dayOfTheWeek = 0
                break
    q = requests.post(url['sendMessage'], json={"chat_id":message['result'][0]['message']['from']['id'], "text":weather["daily"]["temperature_2m_max"][dayOfTheWeek]})
    print(q.text)
    

while True:
    
    status, message = listen(a)
    
    if status:
        if message =="Cherkasy":
            city = message
            a = 0

        elif message['result'][0]['message']['text'] == "/start":
            a = start()
        elif message['result'][0]['message']['text'] == "/weather":
            weather(city)


    


