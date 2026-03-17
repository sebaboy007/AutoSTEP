import streamlit as st
import cadquery as cq
import os

# Setăm titlul paginii web
st.title("📦 Generator de Fișiere .STEP")
st.write("Apasă butonul de mai jos pentru a genera și descărca un cub 3D (10x10x10).")

# Creăm un buton în interfață
if st.button("Generează Cubul"):
    with st.spinner('Așteaptă un moment, generăm modelul...'):
        
        # 1. Logica ta de CadQuery
        cub = cq.Workplane("front").box(10, 10, 10)
        nume_fisier = "model_generat.step"
        
        # 2. Salvăm fișierul pe serverul Streamlit
        cq.exporters.export(cub, nume_fisier)
        
        st.success("Fișierul a fost generat cu succes!")
        
        # 3. Creăm butonul de descărcare pentru utilizator
        with open(nume_fisier, "rb") as file:
            st.download_button(
                label="📥 Descarcă fișierul .STEP",
                data=file,
                file_name=nume_fisier,
                mime="application/octet-stream"
            )
