import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Clima y Café App", layout="centered")


departamentos_el_salvador = [
    "chalatenango", 
    "san salvador", 
    "san miguel", 
    "sonsonate", 
    "santa ana",
    "ahuachapán",
    "la libertad",
    "la paz",
    "la unión",
    "morazán",
    "san vicente",
    "usulután",
    "cabañas",
    "cuscatlán"
]

clima_container = st.container()
cafe_container = st.container()

with clima_container:
    st.title(" Situación Climática en El Salvador")
    st.write("Seleccione el departamento:")
    
    
    departamento = st.selectbox(
        "Departamento", 
        options=departamentos_el_salvador,
        index=0,  
        key="clima_select"
    )
    
    API_KEY = "75edce7dfd6d5640fa37029a0b73ddd2"  
    
    if st.button("Consultar Clima", type="primary"):
        if departamento:
            if not API_KEY or API_KEY == "75edce7dfd6d5640fa37029a0b73ddd2":
                st.error(" Por favor configura tu API Key de OpenWeatherMap")
            else:
              
                lugar_busqueda = f"{departamento}, El Salvador"
                url = f"https://api.openweathermap.org/data/2.5/weather?q={departamento}&appid={API_KEY}&units=metric&lang=es"
                
                try:
                    with st.spinner('Buscando información climática...'):
                        response = requests.get(url)
                        data = response.json()

                    if response.status_code == 200:
                        st.success(" Datos climáticos obtenidos:")
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.metric(" Temperatura", f"{data['main']['temp']}°C")
                            st.metric(" Humedad", f"{data['main']['humidity']}%")
                            st.metric(" Viento", f"{data['wind']['speed']} km/h")
                        
                        with col2:
                            st.metric(" Ciudad", data['name'])
                            st.metric("🇸🇻 País", data['sys']['country'])
                            st.metric(" Condición", data['weather'][0]['description'].title())
                        
                        
                        st.subheader("Más información")
                        col3, col4 = st.columns(2)
                        with col3:
                            st.write(f"**Sensación térmica:** {data['main']['feels_like']}°C")
                            st.write(f"**Temperatura mínima:** {data['main']['temp_min']}°C")
                        with col4:
                            st.write(f"**Temperatura máxima:** {data['main']['temp_max']}°C")
                            st.write(f"**Presión atmosférica:** {data['main']['pressure']} hPa")
                    
                    else:
                        st.error(f" No se pudo encontrar información para: {departamento}")
                        st.info(" Sugerencia: Intente con otro departamento")
                        
                except Exception as e:
                    st.error(f" Error al conectar con la API: {e}")
        else:
            st.warning("Por favor, selecciona un departamento")

st.markdown("---")

