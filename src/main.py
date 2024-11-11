import requests, datetime

a = 0

url = {
    'getUpdates':"https://api.telegram.org/bot6765342240:AAHOUXXT9Pex5ZiO7kfyQ41jxTSTkth2eHs/getUpdates",
    'sendMessage':"https://api.telegram.org/bot6765342240:AAHOUXXT9Pex5ZiO7kfyQ41jxTSTkth2eHs/sendMessage",
    'getWeather':"https://api.open-meteo.com/v1/forecast"
}
Params = {
    'getUpdates':{"offset":0},
    'start':{"chat_id":0, "text":"Hello, I`m your personal weather☀️.I can tell you actual, and future weather. Let`s set up your bot: ", "reply_markup": {"inline_keyboard": [
      [
        {
          "text": "Seting⚙️",
          "callback_data":"Seting"
        }
      ]
    ]}},
    'day':{"chat_id":0, "text":"For what day you wanna learn forecast?📆", "reply_markup": {"inline_keyboard": [
      [
        {
          "text": "Monday",
          "callback_data":"Monday"
        },
        {
          "text": "Tuesday",
          "callback_data":"Tuesday"
        },
        {
          "text": "Wednesday",
          "callback_data":"Wednesday"
        },
        {
          "text": "Thursday",
          "callback_data":"Thursday"
        }
      ],
      [
          {
          "text": "Friday",
          "callback_data":"Friday"
        },
        {
          "text": "Sanday",
          "callback_data":"Sanday"
        },
        {
          "text": "Saturday",
          "callback_data":"Saturday"
        }
          
      ]
    ]}},
    'getWeather':{"latitude":49.4345, "longitude":32.0541, "daily":["temperature_2m_max","temperature_2m_min","rain_sum","showers_sum","snowfall_sum","wind_speed_10m_max","wind_direction_10m_dominant"] },
    'forecast':{"chat_id":0, "text":0}
}
def listen (answ):
    message = requests.get(url['getUpdates'])
    message = message.json()
    print(message)
    if len(message['result']) > 0 and message['ok']:
      Params["getUpdates"]["offset"]=message['result'][0]['update_id']+1
      requests.post(url['getUpdates'], json = Params["getUpdates"])

      if 'message' in message['result'][0]:
        return 'text', message['result'][0]['message']['text'], message['result'][0]['message']['chat']['id']
      
      elif 'callback_query' in message['result'][0]:
        return 'data', message['result'][0]['callback_query']['data'], message['result'][0]['callback_query']['message']['chat']['id']
      
    return -1, -1, -1

def start (chat_id):
    Params['start']['chat_id']=chat_id
    r = requests.post(url['sendMessage'], json=Params['start'])

def weather_data(day,index , chat_id):
    weather = requests.get(url['getWeather'], params=Params['getWeather'])
    weather = weather.json()
    Params['forecast']['chat_id'] = chat_id
    Params['forecast']['text'] = 'Weather forecast for {0}. \n Max temperature🔥 : {1} °C. \n Min temperature❄️ : {2} °C. \n Rain sum🌧️ : {3} mm. \n Shower sum☔ : {4} mm. \n Snowfall sum🌨️ : {5} mm. \n Wind directhion🧭 : {6} °. \n Max wind speed🍃 : {7} km/h. '.format(day, weather['daily']['temperature_2m_max'][index], weather['daily']['temperature_2m_min'][index], weather['daily']['rain_sum'][index], weather['daily']['showers_sum'][index], weather['daily']['snowfall_sum'][index], weather['daily']['wind_direction_10m_dominant'][index], weather['daily']['wind_speed_10m_max'][index] )                      
    r = requests.post(url['sendMessage'], json=Params['forecast'])

def weather_message(chat_id):
    Params['day']['chat_id']=chat_id
    requests.post(url['sendMessage'], json=Params['day'])

def setting(chat_id):
    requests.post(url['sendMessage'], json={'text':'For quick start, enter your city cootdinates📍 (example: 52.3 33.24)', 'chat_id':chat_id})
    return 1

    

while True:
    
    type, message, chat_id = listen(a)
    
    if type == 'text':
        if message[0] == "/":
            if message == "/start":
              start(chat_id)
            elif message == "/weather":
               weather_message(chat_id)
            elif message == "/seting":
               waitforcoord = setting(chat_id)
        elif waitforcoord:
          try:
            Params['getWeather']['lattitude'] = float(message.split()[0])
            Params['getWeather']['longitude'] = float(message.split()[1])
            weather_message(chat_id)
          except:
             pass
          waitforcoord = 0
    elif type == 'data':
      if message == "Seting":
        waitforcoord = setting(chat_id)
      if message == 'Monday':
        index = (7 - datetime.datetime.today().weekday())%7
        weather_data(message,index, chat_id)
      elif message == "Tuesday":
        index = (8 - datetime.datetime.today().weekday())%7
        weather_data(message,index, chat_id)
      elif message == "Wednesday":
        index = (9 - datetime.datetime.today().weekday())%7
        weather_data(message,index, chat_id)
      elif message == "Thursday":
        index = (10 - datetime.datetime.today().weekday())%7
        weather_data(message,index, chat_id)
      elif message == "Friday":
        index = (11 - datetime.datetime.today().weekday())%7
        weather_data(message,index, chat_id)
      elif message == "Sanday":
        index = (12 - datetime.datetime.today().weekday())%7
        weather_data(message,index, chat_id)
      elif message == "Saturday":
        index = (13 - datetime.datetime.today().weekday())%7
        weather_data(message,index, chat_id)
    else:
      pass


    


