from tkinter import *
from tkinter import ttk, messagebox
import requests

def data_get():
    city = city_name.get()
    if city:
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6e0b060c5b7b5b246418e71147f400de"
            data = requests.get(url).json()
            
            # Update labels with weather data
            if "weather" in data:
                W_label1.config(text=data["weather"][0]["main"])
                Wb_label1.config(text=data["weather"][0]["description"])
            if "main" in data:
                temp_celsius = data["main"]["temp"] - 273.15
                temp_label1.config(text=f"{temp_celsius:.1f} °C")
                pre_label1.config(text=data["main"]["pressure"])
            else:
                messagebox.showerror("Error", "City not found. Please check the spelling.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")
    else:
        messagebox.showwarning("Input Error", "Please select a city/state")

# Initialize the main window
win = Tk()
win.title("Weather App")
win.config(bg="blueviolet")
win.geometry("900x900")

# Label for the application title
name_label = Label(win, text="Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x=200, y=60, height=50, width=450)

# Combobox for city selection
city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
             "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, text="Select City/State", values=list_name, font=("Times New Roman", 12))
com.place(x=200, y=120, height=50, width=450)
com.config(textvariable=city_name)

# Labels for weather information
W_label = Label(win, text="Weather Condition", font=("Times New Roman", 12))
W_label.place(x=100, y=400, height=30, width=210)
W_label1 = Label(win, text="", font=("Times New Roman", 12))
W_label1.place(x=400, y=400, height=30, width=210)

Wb_label = Label(win, text="Weather Description", font=("Times New Roman", 12))
Wb_label.place(x=100, y=440, height=30, width=210)
Wb_label1 = Label(win, text="", font=("Times New Roman", 12))
Wb_label1.place(x=400, y=440, height=30, width=210)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 12))
temp_label.place(x=100, y=480, height=30, width=210)
temp_label1 = Label(win, text="", font=("Times New Roman", 12))
temp_label1.place(x=400, y=480, height=30, width=210)

pre_label = Label(win, text="Pressure", font=("Times New Roman", 12))
pre_label.place(x=100, y=520, height=30, width=210)
pre_label1 = Label(win, text="", font=("Times New Roman", 12))
pre_label1.place(x=400, y=520, height=30, width=210)

# Button to fetch weather data
done_button = Button(win, text="Fetch Data", font=("Times New Roman", 14, "bold"), command=data_get)
done_button.place(x=300, y=600, height=50, width=120)

win.mainloop()
