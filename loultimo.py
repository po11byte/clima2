import streamlit as st
import requests

st.set_page_config(page_title="Clima y Café App", layout="centered")

departamentos_el_salvador = [
    "San Salvador", "Santa Ana", "San Miguel", "La Libertad", "Sonsonate",
    "Usulután", "San Vicente", "Chalatenango", "Cuscatlán", "La Paz",
    "La Unión", "Morazán", "Ahuachapán", "Cabañas"
]

# PRUEBA CON ESTA KEY (puede tener límites)
API_KEY = "ff6b70c868da677f5e3ff4332fb40a73"

with st.container():
    st.title("🌤️ Situación Climática en El Salvador")
    
    departamento = st.selectbox("Seleccione el departamento:", departamentos_el_salvador)
    
    if st.button("Consultar Clima", type="primary"):
        # URL mejorada
        url = f"http://api.openweathermap.org/data/2.5/weather?q={departamento},SV&appid={API_KEY}&units=metric&lang=es"
        
        try:
            with st.spinner('Buscando información climática...'):
                response = requests.get(url, timeout=10)
                
            if response.status_code == 200:
                data = response.json()
                st.success("✅ Datos obtenidos correctamente")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("🌡️ Temperatura", f"{data['main']['temp']}°C")
                    st.metric("💧 Humedad", f"{data['main']['humidity']}%")
                    st.metric("🌬️ Viento", f"{data['wind']['speed']} m/s")
                
                with col2:
                    st.metric("🏙️ Ciudad", data['name'])
                    st.metric("🇸🇻 País", data['sys']['country'])
                    st.metric("☁️ Condición", data['weather'][0]['description'].title())
                    
            elif response.status_code == 401:
                st.error("🔑 ERROR: API Key Inválida o No Activada")
                st.markdown("""
                **📝 Pasos para solucionar:**
                1. Ve a [OpenWeatherMap](https://home.openweathermap.org/api_keys)
                2. **Genera una NUEVA API Key**
                3. **Espera 20-30 minutos** (las keys nuevas tienen delay)
                4. **Copia y pega la nueva key** en el código
                """)
                
            else:
                st.error(f"❌ Error {response.status_code}: {response.json().get('message', 'Error desconocido')}")
                
        except requests.exceptions.Timeout:
            st.error("⏰ Timeout: La API tardó demasiado en responder")
        except Exception as e:
            st.error(f"🚨 Error: {e}")
