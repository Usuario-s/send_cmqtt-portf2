import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

st.set_page_config(
    page_title="SPACE CONTROL",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: radial-gradient(ellipse at top, #142d49, #050b14 65%, #02060c);
    color: #e8fbff;
}

[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.hero {
    text-align: center;
    padding: 25px 0 35px;
}

.hero-title {
    font-size: 44px;
    font-weight: 900;
    letter-spacing: 5px;
    color: #61f7ff;
    text-shadow: 0 0 12px #00d9ff, 0 0 35px #007cbd;
}

.hero-subtitle {
    color: #7699b3;
    font-size: 11px;
    letter-spacing: 4px;
    margin-top: 12px;
}

.panel {
    background: linear-gradient(145deg, #11263b, #050e1a);
    border: 1px solid rgba(0, 230, 255, 0.35);
    border-radius: 15px;
    padding: 24px;
    margin: 10px 0 20px;
    box-shadow: 0 0 25px rgba(0, 225, 255, 0.06);
}

.panel-heading {
    color: #61f7ff;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.panel-description {
    color: #7899af;
    font-size: 11px;
    letter-spacing: 1.5px;
}

.stButton > button {
    width: 100%;
    min-height: 52px;
    border: 1px solid #19dff4;
    border-radius: 8px;
    background: linear-gradient(135deg, #10334a, #091726);
    color: #61f7ff;
    font-weight: 800;
    letter-spacing: 2px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    color: white;
    border-color: white;
    background: #07516b;
    box-shadow: 0 0 22px rgba(0, 225, 255, 0.3);
    transform: translateY(-2px);
}

.stSlider [role="slider"] {
    background: #62f7ff !important;
    border: 3px solid white !important;
    width: 23px !important;
    height: 23px !important;
    box-shadow: 0 0 8px #00eaff, 0 0 20px #00eaff !important;
}

.stSlider [data-testid="stSliderTrackFill"] {
    background: linear-gradient(90deg, #087cbd, #00f5ff) !important;
}

.power-card {
    background: linear-gradient(135deg, #0b2033, #06101c);
    border: 1px solid rgba(0, 230, 255, 0.4);
    border-radius: 12px;
    padding: 25px 20px;
    text-align: center;
    margin: 12px 0 20px;
}

.power-label {
    font-size: 11px;
    color: #7fa5b9;
    letter-spacing: 4px;
}

.power-number {
    font-size: 60px;
    font-weight: 900;
    color: #61f7ff;
    text-shadow: 0 0 20px rgba(0, 225, 255, 0.6);
    margin: 12px 0;
}

.power-number span {
    font-size: 22px;
}

.power-track {
    height: 9px;
    width: 100%;
    background: #152c40;
    border-radius: 20px;
    overflow: hidden;
    margin-top: 20px;
}

.power-fill {
    height: 100%;
    background: linear-gradient(90deg, #087cbd, #00f5ff);
    box-shadow: 0 0 14px #00eaff;
}

.power-caption {
    margin-top: 13px;
    color: #66899f;
    font-size: 10px;
    letter-spacing: 2px;
}

.tech-box {
    border: 1px solid rgba(0, 230, 255, 0.18);
    background: rgba(4, 14, 25, 0.7);
    border-radius: 10px;
    padding: 18px;
    color: #85a9bd;
    font-size: 12px;
    line-height: 2;
}

.footer-tech {
    text-align: center;
    font-size: 10px;
    color: #4e7288;
    letter-spacing: 3px;
    padding: 25px 0;
}

@media (max-width: 600px) {
    .hero-title {
        font-size: 30px;
        letter-spacing: 2px;
    }

    .panel {
        padding: 17px;
    }
}
</style>
""", unsafe_allow_html=True)


# VARIABLES
values = 0.0
act1 = "OFF"
message_received = ""


# FUNCIONES MQTT
def on_publish(client, userdata, result):
    print("El dato ha sido publicado\n")


def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = message.payload.decode("utf-8")
    print(message_received)


# BROKER
broker = "157.230.214.127"
port = 1883

client1 = paho.Client("secundeta")
client1.on_message = on_message


# CABECERA
st.markdown("""
<div class="hero">
    <div class="hero-title">🚀 SPACE CONTROL</div>
    <div class="hero-subtitle">
        ADVANCED MQTT CONTROL SYSTEM // COMMAND CENTER
    </div>
</div>
""", unsafe_allow_html=True)


# INFORMACIÓN
st.markdown("""
<div class="panel">
    <div class="panel-heading">▰ SYSTEM INFORMATION</div>
    <div class="panel-description">
        MISSION CONTROL // SYSTEM DIAGNOSTICS
    </div>
</div>
""", unsafe_allow_html=True)

col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("""
    <div class="tech-box">
        <b style="color:#61f7ff">PYTHON VERSION</b>
    </div>
    """, unsafe_allow_html=True)
    st.write(platform.python_version())

with col_info2:
    st.markdown(f"""
    <div class="tech-box">
        <b style="color:#61f7ff">MQTT BROKER</b><br>
        IP: {broker}<br>
        PORT: {port}<br>
        PROTOCOL: MQTT / TCP
    </div>
    """, unsafe_allow_html=True)


# CONTROL ON / OFF
st.markdown("""
<div class="panel">
    <div class="panel-heading">▰ MAIN ENGINE CONTROL</div>
    <div class="panel-description">
        ACTUATOR 01 // DIGITAL COMMAND INTERFACE
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("▲ ACTIVATE ENGINE — ON", key="btn_on"):
        act1 = "ON"
        client1 = paho.Client("secundeta")
        client1.on_publish = on_publish

        try:
            client1.connect(broker, port, 60)
            message = json.dumps({"Act1": act1})
            result = client1.publish("cm1", message)
            result.wait_for_publish(timeout=3)
            st.success("Comando ON enviado.")
        except Exception as e:
            st.error(f"Error MQTT: {e}")
        finally:
            if client1.is_connected():
                client1.disconnect()

with col2:
    if st.button("▼ SHUT DOWN — OFF", key="btn_off"):
        act1 = "OFF"
        client1 = paho.Client("secundeta")
        client1.on_publish = on_publish

        try:
            client1.connect(broker, port, 60)
            message = json.dumps({"Act1": act1})
            result = client1.publish("cm1", message)
            result.wait_for_publish(timeout=3)
            st.success("Comando OFF enviado.")
        except Exception as e:
            st.error(f"Error MQTT: {e}")
        finally:
            if client1.is_connected():
                client1.disconnect()


# CONTROL ANALÓGICO
st.markdown("""
<div class="panel">
    <div class="panel-heading">▰ THRUST CONTROL SYSTEM</div>
    <div class="panel-description">
        ENGINE POWER // ANALOGUE THROTTLE ADJUSTMENT
    </div>
</div>

<div style="
    text-align:center;
    color:#61f7ff;
    font-size:12px;
    letter-spacing:4px;
    padding:12px 0;
">
    ◀ ENGINE THRUST REGULATOR ▶
</div>
""", unsafe_allow_html=True)

values = st.slider(
    "🚀 Selecciona la potencia de la nave",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.1,
    key="thrust_slider"
)

st.markdown(f"""
<div class="power-card">
    <div class="power-label">CURRENT ENGINE THRUST</div>
    <div class="power-number">{values:.1f}<span>%</span></div>
    <div class="power-track">
        <div class="power-fill" style="width:{values}%;"></div>
    </div>
    <div class="power-caption">
        ENGINE OUTPUT // {values:.1f}% // THROTTLE CONTROL
    </div>
</div>
""", unsafe_allow_html=True)

st.write("Values:", values)


# ENVIAR VALOR ANALÓGICO
if st.button("🚀 TRANSMIT ANALOG POWER", key="btn_analog"):
    client1 = paho.Client("secundeta")
    client1.on_publish = on_publish

    try:
        client1.connect(broker, port, 60)
        message = json.dumps({"Analog": float(values)})
        result = client1.publish("cm2", message)
        result.wait_for_publish(timeout=3)
        st.success(f"Potencia enviada: {values:.1f}%")
    except Exception as e:
        st.error(f"Error MQTT: {e}")
    finally:
        if client1.is_connected():
            client1.disconnect()


# PIE DE PÁGINA
st.markdown("""
<div class="footer-tech">
    SPACE CONTROL SYSTEM // MQTT TRANSMISSION INTERFACE
</div>
""", unsafe_allow_html=True)




