import streamlit as st

# Título de la aplicación
st.title("Introducción a Docker Compose")

# Información sobre Docker Compose
st.header("1. ¿Qué es Docker Compose?")
st.write("""
Docker Compose es una herramienta diseñada para simplificar el proceso de manejo de aplicaciones multi-contenedor en Docker. Utiliza un archivo YAML para definir múltiples contenedores y sus configuraciones, permitiéndote administrarlos como un único servicio. Con Docker Compose, puedes iniciar, detener y reconstruir servicios, gestionar volúmenes, redes y otras configuraciones de manera sencilla y eficiente.
""")

st.write("""
**Introducción a Docker Compose**: Permite orquestar y coordinar varios contenedores de Docker (como bases de datos, aplicaciones web, y servicios back-end) como si fueran una única aplicación. Esto es ideal para entornos de desarrollo, pruebas y producción.
""")

# Sección de creación de archivo docker-compose.yml
st.header("2. Creación de `docker-compose.yml`: Definir servicios, redes y volúmenes")
st.write("""
El archivo `docker-compose.yml` es el corazón de Docker Compose y se utiliza para definir los servicios, redes y volúmenes.
""")

# Sub-sección de Servicios
st.subheader("Servicios")
st.write("""
En este archivo, defines los servicios que necesitará tu aplicación. Cada servicio puede ser construido a partir de una imagen Docker existente o a través de un Dockerfile específico. Puedes especificar configuraciones como dependencias, puertos, variables de entorno, etc.
""")

# Sub-sección de Redes
st.subheader("Redes")
st.write("""
Docker Compose permite definir redes personalizadas para facilitar la comunicación entre los contenedores. Puedes configurar diferentes redes para aislar contenedores en distintos ambientes de red.
""")

# Sub-sección de Volúmenes
st.subheader("Volúmenes")
st.write("""
Los volúmenes son utilizados para persistir y compartir datos entre contenedores y el host de Docker. En el archivo `docker-compose.yml`, puedes definir volúmenes para asegurar que los datos no se pierdan cuando los contenedores se reinicien o actualicen.
""")

# Ejecución principal de Streamlit
if __name__ == '__main__':
    st.write("¡Explora las funcionalidades de Docker Compose en esta introducción!")
