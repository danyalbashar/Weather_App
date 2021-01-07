from tkinter import *
import requests
import time


#defining function to get city whether from the weather API
#root=None is used so we can all this fuction by enter key as well as inbuilt button as command function dosen't take arguments
#but return key takes arguments

def getweather(root = None):
    city = text.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=APIKEY"

    #API delivers data in jason file format so fetching data using json function & creating a variable
    json_data = requests.get(api).json()

    t= json_data['cod']
    if(t== "404"):
        result1.config(text="City Not Found\n Enter Correct City")

    else:
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        #sorting output data into two strings one for main temperature and other for other values
        info1 = condition + "\n" + str(temp) + "°C"
        info2 = "\n" + "Min Temp:     " + str(min_temp) + "°C" + "\n" + "Max Temp:    " + str(max_temp) + "°C" + "\n" + "Pressure:      " + str(pressure) + " hPa\n" + "Humidity:       " + str(
            humidity) + " %\n" + "Wind Speed:  " + str(wind) + " meter/sec\n" + "Sunrise:         " + sunrise + " AM\n" + "Sunset:          " + sunset + " PM"

        result1.config(text= info1)
        result2.config(text= info2)





#Making the GUI of our Weather APP using Tkinter from here onwards

root = Tk()

#Designing Canvas
root.geometry("500x600")
root.title("Weather App")
root.minsize(300,400)
root.maxsize(500,600)

#defining different fonts
font1= ("comicsansms" , 20 , "bold")
font2= ("courier", 10, "italic")

#defining labels
label1 = Label(root,text = "Enter City Name ", fg= "darkgreen", bd= 4 ,font = font1, relief = RIDGE)
label1.pack(anchor= "n",side=TOP,fill =X,pady=20)

label2 = Label(root, text = "Created By: Danyal Bashar\n Jamia Millia Islamia\n B.Tech(ECE)", fg="blue", font = font2)
label2.pack(anchor= "s",side =BOTTOM)

#Designing dialogue box for taking city name from user
text= Entry(root,justify=CENTER, width=30, font="arial 15 italic", fg="black" )
text.pack(pady =20)
text.focus()
text.bind('<Return>', getweather)            #Binding enter key
text.bind('<Button-1>', getweather)          #Binding Button created below



#Designing Button
b =Button(root, fg="red", width = 10, text="SUBMIT", font = "arial 15 bold", relief = GROOVE, activeforeground = "black", command = getweather)
b.pack(padx=10)

#Formating the outputs
result1=Label(root, fg="purple",font= "comicsansms 16 bold")
result1.pack(pady=20,anchor= "center", side = TOP)

result2=Label(root,fg="magenta3", font= "comicsansms 15 bold",justify= "left")
result2.pack(pady=10, anchor ="center", side =TOP)


root.mainloop()
