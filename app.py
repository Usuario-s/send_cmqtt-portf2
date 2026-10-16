```python
import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# ==================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==================================================

st.set_page_config(
    page_title="SPACE CONTROL | MQTT",
    page_icon="🚀",
    layout="wide"
)

# ==================================================
# DISEÑO FUTURISTA
# ==================================================

st.markdown("""
<style>

/* FONDO GENERAL */
.stApp {
    background:
        radial-gradient(ellipse at 50% 0%, #142d49 0%, transparent 55%),
        linear-gradient(145deg, #050b14, #071321 55%, #02060c);
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
    padding-bottom: 3rem;
}

/* TEXTOS */
h1, h2, h3, p, label {
    color: #e8fbff !important;
}

/* CABECERA */
.hero {
    text-align: center;
    padding: 20px 0 30px 0;
}

.hero-title {
    font-size: clamp(30px, 5vw, 48px);
    font-weight: 900;
    letter-spacing: 5px;
    color: #61f7ff;
    text-shadow: 0 0 12px #00d9ff, 0 0 35px #007cbd;
}

.hero-subtitle {
    margin-top: 12px;
    color: #7699b3;
    font-size: 11px;
    letter-spacing: 4px;
}

/* PANELES */
.panel {
    background: linear-gradient(
        145deg,
        rgba(17, 38, 59, 0.96),
        rgba(5, 14, 26, 0.98)
    );
    border: 1px solid rgba(0, 230, 255, 0.30);
    border-radius: 15px;
    padding: 24px;
    margin: 10px 0 20px 0;
    box-shadow:
        0 0 25px rgba(0, 225, 255, 0.06),
        inset 0 0 20px rgba(0, 225, 255, 0.025);
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
    line-height: 1.8;
}

/* BOTONES */
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
    box-shadow: 0 0 10px rgba(0, 225, 255, 0.06);
}

.stButton > button:hover {
    color: #ffffff;
    border-color: #ffffff;
    background: linear-gradient(135deg, #07516b, #12374f);
    box-shadow: 0 0 22px rgba(0, 225, 255, 0.25);
    transform: translateY(-2px);
}

.stButton > button:active {
    transform: scale(0.98);
}

/* SLIDER */
.stSlider {
    padding-top: 15px;
    padding-bottom: 10px;
}

.stSlider [data-baseweb="slider"] > div {
    cursor: pointer;
}

.stSlider [role="slider"] {
    background: #62f7ff !important;
    border: 3px solid #ffffff !important;
    width: 23px !important;
    height: 23px !important;
    box-shadow:
        0 0 8px #00eaff,
        0 0 20px #00eaff !important;
}

.stSlider [data-testid="stSliderTrackFill"] {
    background: linear-gradient(90deg, #087cbd, #00f5ff) !important;
}

/* ESCALA DEL SLIDER */
.stSlider [data-testid="stTickBar"] {
    background: transparent;
}

/* INDICADOR DE POTENCIA */
.power-card {
    background: linear-gradient(135deg, #0b2033, #06101c);
    border: 1px solid rgba(0, 230, 255, 0.38);
    border-radius: 12px;
    padding: 25px 20px;
    text-align: center;
    margin: 12px 0 20px 0;
    box-shadow: inset 0 0 25px rgba(0, 230, 255, 0.025);
}

.power-label {
    font-size: 11px;
    color: #7fa5b9;
    letter-spacing: 4px;
}

.power-number {
    font-size: clamp(45px, 7vw, 68px);
    font-weight: 900;
    color: #61f7ff;
    text-shadow: 0 0 20px rgba(0, 225, 255, 0.55);
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
    border-radius: 20px;
    background: linear-gradient(90deg, #087cbd, #00f5ff);
    box-shadow: 0 0 14px #00eaff;
}

.power-caption {
    margin-top: 13px;
    color: #66899f;
    font-size: 10px;
    letter-spacing: 2px;
}

/* INFORMACIÓN TÉCNICA */
.tech-box {
    border: 1px solid rgba(0, 230, 255, 0.18);
    background: rgba(4, 14, 25, 0.7);
    border-radius: 10px;
    padding: 18px;
    color: #85a9bd;
    font-size: 12px;
    line-height: 2;
}

/* PIE */
.footer-tech {
    text-align: center;
    font-size: 10px;
    color: #4e7288;
    letter-spacing: 3px;
    padding: 25px 0 5px 0;
}

hr {
    border-color: rgba(0, 230, 255, 0.18);
}

@media (max-width: 600px) {
    .hero-title {
        letter-spacing: 2px;
    }

    .hero-subtitle {
        letter-spacing: 2px;
    }

    .panel {
        padding: 17px;
    }
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# VARIABLES ORIGINALES
# ==================================================

values = 0.0
act1 = "OFF"

# ==================================================
# FUNCIONES MQTT ORIGINALES
# ==================================================

def on_publish(client, userdata, result):
    print("el dato ha sido publicado \n")
    pass


def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)


# ==================================================
# BROKER ORIGINAL
# ==================================================

broker = "157.230.214.127"
port = 1883

client1 = paho.Client("secundeta")
client1.on_message = on_message

# ==================================================
# CABECERA
# ==================================================

st.markdown("""
<div class="hero">
    <div class="hero-title">🚀 SPACE CONTROL</div>
    <div class="hero-subtitle">
        ADVANCED MQTT CONTROL SYSTEM // COMMAND CENTER
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# INFORMACIÓN DEL SISTEMA
# ==================================================

st.markdown("""
<div class="panel">
    <div class="panel-heading">▰ SYSTEM INFORMATION</div>
    <div class="panel-description">
        MISSION CONTROL // SYSTEM DIAGNOSTICS
    </div>
</div>
""", unsafe_allow_html=True)

info1, info2 = st.columns(2)

with info1:
    st.markdown("""
    <div class="tech-box">
        <b style="color:#61f7ff">PYTHON VERSION</b><br>
    """, unsafe_allow_html=True)

    st.write("Versión de Python:", platform.python_version())

    st.markdown("</div>", unsafe_allow_html=True)

with info2:
    st.markdown(f"""
    <div class="tech-box">
        <b style="color:#61f7ff">MQTT BROKER</b><br>
        IP: {broker}<br>
        PORT: {port}<br>
        PROTOCOL: MQTT / TCP
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# CONTROL DEL ACTUADOR
# ==================================================

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
    if st.button("▲  ACTIVATE ENGINE — ON", key="btn_on"):
        act1 = "ON"

        client1 = paho.Client("secundeta")
        client1.on_publish = on_publish
        client1.connect(broker, port)

        message = json.dumps({"Act1": act1})
        ret = client1.publish("cm1", message)

        st.success("Comando ON enviado.")

        client1.disconnect()

with col2:
    if st.button("▼  SHUT DOWN — OFF", key="btn_off"):
        act1 = "OFF"

        client1 = paho.Client("secundeta")
        client1.on_publish = on_publish
        client1.connect(broker, port)

        message = json.dumps({"Act1": act1})
        ret = client1.publish("cm1", message)

        st.success("Comando OFF enviado.")

        client1.disconnect()

# ==================================================
# CONTROL ANALÓGICO / ACELERADOR DE LA NAVE
# ==================================================

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

# Slider original: rango 0.0 a 100.0
values = st.slider(
    "🚀 Selecciona la potencia de la nave",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.1,
    key="thrust_slider"
)

# Indicador dinámico de potencia
st.markdown(f"""
<div class="power-card">
    <div class="power-label">CURRENT ENGINE THRUST</div>

    <div class="power-number">
        {values:.1f}<span>%</span>
    </div>

    <div class="power-track">
        <div class="power-fill" style="width:{values}%;"></div>
    </div>

    <div class="power-caption">
        ENGINE OUTPUT // {values:.1f}% // THROTTLE CONTROL
    </div>
</div>
""", unsafe_allow_html=True)

# Valor original
st.write("Values:", values)

# Envío del valor analógico original
if st.button("🚀  TRANSMIT ANALOG POWER", key="btn_analog"):

    client1 = paho.Client("secundeta")
    client1.on_publish = on_publish
    client1.connect(broker, port)

    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cm2", message)

    st.success(f"Potencia enviada: {values:.1f}%")

    client1.disconnect()

# ==================================================
# PIE DE PÁGINA
# ==================================================

st.markdown("""
<div class="footer-tech">
    SPACE CONTROL SYSTEM // MQTT TRANSMISSION INTERFACE
</div>
""", unsafe_allow_html=True)
```




