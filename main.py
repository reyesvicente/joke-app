import requests
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename='darkly')
root.title('Joke App')
root.geometry('1280x900')

def get_joke():
    url = "https://icanhazdadjoke.com"
    headers = {'Accept': 'application/json'}
    joke_time = requests.get(url, headers=headers).json().get('joke')
    label.config(text=joke_time)
    print(joke_time)

label = tb.Label(text="", font=("Poppins", 16), bootstyle='default')
label.pack(padx=5, pady=10)
btn = tb.Button(text="Get Joke!", command=get_joke)
btn.pack(padx=5, pady=10)


root.mainloop()