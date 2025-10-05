import streamlit as st
import requests

st.title("Situación climática")
st.write("Seleccione el departamento: ")


departamentos_el_salvador = [
    "Ahuachapán", "Cabañas", "Chalatenango", "Cuscatlán", "La Libertad",
    "La Paz", "La Unión", "Morazán", "San Miguel", "San Salvador",
    "San Vicente", "Santa Ana", "Sonsonate", "Usulután"
]

API_KEY = "1aefb8a907db6f0953a604ab4d387020"

info = []


departamento = st.selectbox("Seleccione el departamento", options=departamentos_el_salvador)

with st.sidebar:
    
    departamento2 = st.selectbox("Seleccione el departamento", options=departamentos_el_salvador, key="sidebar_select")
    ver_clima_sidebar = st.button("ver clima")


if st.button("Ver clima"):
    if departamento:
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={departamento}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
           
            info = {
                "country" : data["sys"]["country"],
                "city": data["name"],
                "temp" : f"{data['main']['temp']}°C",
                "humidity" : f"{data['main']['humidity']}%",
                "description" : data["weather"][0]["description"],
                "wind" : f"{data['wind']['speed']} km/h"
            }
            st.success(f"{info['city']}")
            st.success(f"{info['temp']}")
            st.success(f"{info['humidity']}")
            st.success(f"{info['description']}")
            st.success(f"{info['wind']}")
            
        else:
            st.error("Error al obtener los datos del clima")
    else:
        st.warning("Por favor, seleccione un departamento")


if ver_clima_sidebar:
    if departamento2:
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={departamento2}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            info = {
                "country" : data["sys"]["country"],
                "city": data["name"],
                "temp" : f"{data['main']['temp']}°C",
                "humidity" : f"{data['main']['humidity']}%",
                "description" : data["weather"][0]["description"],
                "wind" : f"{data['wind']['speed']} km/h"
            }
            st.success(f"{info['city']}")
            st.success(f"{info['temp']}")
            st.success(f"{info['humidity']}")
            st.success(f"{info['description']}")
            st.success(f"{info['wind']}")
            
        else:
            st.error("Error al obtener los datos del clima")
    else:
        st.warning("Por favor, seleccione un departamento")
