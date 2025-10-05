import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Clima y Café App", layout="centered")

departamentos_el_salvador = [
    "chalatenango", "san salvador", "san miguel", "sonsonate", "santa ana",
    "ahuachapán", "la libertad", "la paz", "la unión", "morazán",
    "san vicente", "usulután", "cabañas", "cuscatlán"
]


API_KEY = "ff6b70c868da677f5e3ff4332fb40a73"  

clima_container = st.container()

with clima_container:
    st.title(" Situación Climática en El Salvador")
    st.write("Seleccione el departamento:")
    
    departamento = st.selectbox("Departamento", options=departamentos_el_salvador, index=0)
    
    if st.button("Consultar Clima", type="primary"):
        if departamento:
       
            url = f"https://api.openweathermap.org/data/2.5/weather?q={departamento},El Salvador&appid={API_KEY}&units=metric&lang=es"
            
            try:
                with st.spinner('Buscando información climática...'):
                    response = requests.get(url)
                    data = response.json()

                if response.status_code == 200:
                    st.success(" Datos climáticos obtenidos:")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Temperatura", f"{data['main']['temp']}°C")
                        st.metric("Humedad", f"{data['main']['humidity']}%")
                        st.metric("Viento", f"{data['wind']['speed']} km/h")
                    
                    with col2:
                        st.metric("Ciudad", data['name'])
                        st.metric("País", data['sys']['country'])
                        st.metric("Condición", data['weather'][0]['description'].title())
                
                elif response.status_code == 401:
                    st.error(" API Key inválida o no activada")
                    st.info("""
                    **Solución:**
                    1. Ve a https://home.openweathermap.org/api_keys
                    2. Verifica que tu key esté activa
                    3. Las keys nuevas pueden tardar 10-20 minutos en activarse
                    4. Si no funciona, genera una nueva key
                    """)
                    
                else:
                    st.error(f"Error {response.status_code}: No se pudo encontrar {departamento}")
                    
            except Exception as e:
                st.error(f"Error de conexión: {e}")
        else:
            st.warning("Por favor, selecciona un departamento")




