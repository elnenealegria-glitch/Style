import streamlit as st
import random
import datetime

# Base de datos ampliada (puedes expandir esta lista con todos tus 359 outfits)
outfits = {
    "invierno": [
        {"desc": "Polera Blanca + Camisa Cuadros azul + Abrigo gris claro", "pants": "Jeans azul oscuro recto", "shoes": "Vans Negros", "extra": "Bufanda Azul"},
        {"desc": "Polera Café + Camisa Vino + Chaqueta cuero negro", "pants": "Pantalón vestir beige", "shoes": "Zapatos Blancos", "extra": "Bufanda Negra"},
    ],
    "verano": [
        {"desc": "Polera Blanca + Sin capa + Sin chaqueta", "pants": "Jeans azul claro", "shoes": "Zapatos Negros", "extra": "Tote Bag"},
        {"desc": "Polera Rosa + Sin capa + Sin chaqueta", "pants": "Jeans azul oscuro", "shoes": "Vans Negros", "extra": "Sin bolsa"},
    ]
}

tips = [
    "Dante Vesper no tiene prisa; deja que la camisa sobresalga ligeramente de tu poleron.",
    "El cobre rosado es tu energía; combina tonos tierra con un accesorio metálico.",
    "Menos es más. Si el abrigo es protagonista, deja que el resto de tu outfit sea de colores neutros.",
    "Tu mirada es el flash. Asegúrate de que tus zapatos estén impecables, son la base de tu templo."
]

st.title("Dante Vesper: Style App")

# 1. Selector de Calendario
fecha_seleccionada = st.date_input("Planifica tu look para el día:", datetime.date.today())

# 2. Selector de Temporada
temporada = st.radio("Temporada:", ["invierno", "verano"], horizontal=True)

# 3. Botón de Generar
if st.button("Generar Outfit Soft Boy"):
    selection = random.choice(outfits[temporada])
    st.success(f"### Look para el {fecha_seleccionada}")
    st.write(f"**Capas:** {selection['desc']}")
    st.write(f"**Pantalón:** {selection['pants']}")
    st.write(f"**Zapatos:** {selection['shoes']}")
    st.write(f"**Accesorio:** {selection['extra']}")
    
    # 4. Tip Diario
    st.divider()
    st.caption("✨ Tip de Dante Vesper:")
    st.write(random.choice(tips))
    st.balloons()
  
