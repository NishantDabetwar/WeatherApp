import requests
import json
import win32com.client as wincom

x=input("Enter the location: ")
url = f'https://api.weatherapi.com/v1/current.json?key=cb2fe38d026448a3954111202232005&q={x}'

r= requests.get(url)
print(r.text)
weatherdict= json.loads(r.text)
temp= weatherdict["current"]["temp_c"]

print("The Current temperature of " ,x, "is" ,temp)
ans = f"The Current temperature of  {x} is {temp}"
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(ans)