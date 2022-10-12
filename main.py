#weather detection app
import requests
from tkinter import *


root=Tk()
root.geometry("500x500")
root.config(bg="black")
root.title("weather app")

enter_city=Entry(root,font="lucinda 20 bold")
enter_city.pack()

def search():
    my_url="http://api.openweathermap.org/data/2.5/weather"
    api_key="e170aa40f3631125e4a20447689e9eb7"
    parameters={
        "q":enter_city.get(),
        "appid":api_key

    }

    response=requests.get(url=my_url,params=parameters)
    temp_data_kelvin=response.json()["main"]["temp"]
    temp_data_celsius=temp_data_kelvin-273.15

    text_temp.config(text=f" current temparature \n of {enter_city.get()} is :{int(temp_data_celsius)} degree C")


b1=Button(root,text="seach location",font="lucinda 30 bold",fg="black",bg="black",command=search)
b1.pack(padx=20,pady=20)

text_temp = Label(text=".....",font="lucinda 25 bold")
text_temp.pack(padx=20, pady=20)

root.mainloop()

