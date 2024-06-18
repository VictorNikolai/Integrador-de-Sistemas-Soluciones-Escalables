import streamlit as st
import pandas as pd

def app():
    st.markdown(
        """
        <style>
        .centered-title {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            margin-bottom: 20px; /* Espacio debajo del título */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='centered-title'>Bienvenido a la Página de Inicio</h1>", unsafe_allow_html=True)

    st.write("Aquí puedes comenzar a explorar las funcionalidades de la plataforma.")

    st.header("Selecciona una sección para comenzar:")

    selected_page = st.sidebar.selectbox(
        "Selecciona una sección",
        ["Home", "Modelar Salones", "Modelar Ambientes", "Modelar Cursos",
         "Requerimiento de Ambientes", "Asignación de Alumnos", "Optimización de Horarios"]
    )

    if selected_page == "Home":
        show_home_content()
    elif selected_page == "Modelar Salones":
        show_modelar_salones()
    elif selected_page == "Modelar Ambientes":
        show_modelar_ambientes()
    elif selected_page == "Modelar Cursos":
        show_modelar_cursos()
    elif selected_page == "Requerimiento de Ambientes":
        show_requerimiento_ambientes()
    elif selected_page == "Asignación de Alumnos":
        show_asignacion_alumnos()
    elif selected_page == "Optimización de Horarios":
        show_optimizacion_horarios()

    st.write("¡Explora y disfruta de la plataforma!")


def show_home_content():
    st.write("Contenido de la página de inicio")


def show_modelar_salones():
    st.write("Contenido para modelar salones")


def show_modelar_ambientes():
    st.write("Contenido para modelar ambientes")


def show_modelar_cursos():
    st.write("Contenido para modelar cursos")


def show_requerimiento_ambientes():
    st.write("Contenido para requerimiento de ambientes")


def show_asignacion_alumnos():
    st.write("Contenido para asignación de alumnos")


def show_optimizacion_horarios():
    st.write("Contenido para optimización de horarios")
