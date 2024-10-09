import streamlit as st

# Título principal de la aplicación
st.title("Guía Completa de Docker Compose")

# Sección 1: ¿Qué es Docker Compose?
st.header("1. ¿Qué es Docker Compose?")
st.write("""
Docker Compose es una herramienta diseñada para simplificar el proceso de manejo de aplicaciones multi-contenedor en Docker. Utiliza un archivo YAML para definir múltiples contenedores y sus configuraciones, permitiéndote administrarlos como un único servicio. Con Docker Compose, puedes iniciar, detener y reconstruir servicios, gestionar volúmenes, redes y otras configuraciones de manera sencilla y eficiente.
""")
st.write("""
**Introducción a Docker Compose**: Permite orquestar y coordinar varios contenedores de Docker (como bases de datos, aplicaciones web y servicios back-end) como si fueran una única aplicación. Esto es ideal para entornos de desarrollo, pruebas y producción.
""")

# Sección 2: Creación de `docker-compose.yml`
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

# Sección 3: Comandos Básicos de Docker Compose
st.header("3. Comandos Básicos de Docker Compose")
st.write("""
Docker Compose viene con una variedad de comandos útiles para gestionar el ciclo de vida de tus aplicaciones.
""")

# Sub-sección: `docker-compose up`
st.subheader("`docker-compose up`")
st.write("""
Este comando se utiliza para iniciar todos los servicios definidos en tu archivo `docker-compose.yml`. Puedes usar la opción `-d` para ejecutarlos en modo desacoplado (en segundo plano).
""")

# Sub-sección: `docker-compose down`
st.subheader("`docker-compose down`")
st.write("""
Detiene y elimina todos los recursos creados por `docker-compose up`, incluyendo contenedores, redes definidas y los volúmenes por defecto.
""")

# Sub-sección: `docker-compose ps`
st.subheader("`docker-compose ps`")
st.write("""
Muestra una lista de los contenedores en ejecución relacionados con el archivo `docker-compose.yml` en el directorio actual.
""")

# Sub-sección: `docker-compose exec`
st.subheader("`docker-compose exec`")
st.write("""
Permite ejecutar comandos en contenedores específicos. Por ejemplo, puedes usar `docker-compose exec web sh` para iniciar una shell en un contenedor llamado "web".
""")

# Sección de Conclusión
st.header("Conclusión")
st.write("""
Docker Compose es una herramienta fundamental dentro del ecosistema de Docker que simplifica el manejo de aplicaciones compuestas por múltiples contenedores. Al definir los servicios, volúmenes y redes de una aplicación en un archivo `docker-compose.yml`, Docker Compose permite a los desarrolladores y administradores de sistemas orquestar toda la infraestructura de su aplicación con unos pocos comandos simples.
""")
st.write("""
Esta capacidad de manejar de forma coherente y predecible las dependencias y los componentes de la aplicación facilita considerablemente el desarrollo, las pruebas y la implementación en producción.
""")
st.write("""
En resumen, Docker Compose ofrece un enfoque robusto y eficiente para gestionar aplicaciones contenerizadas, lo que permite escalar y mantener sistemas complejos con menos esfuerzo y mayor precisión. Esto lo convierte en una herramienta invaluable para equipos que buscan optimizar sus flujos de trabajo en desarrollo y operaciones, asegurando que las aplicaciones se comporten de manera uniforme a través de diferentes entornos y reduciendo los problemas comunes asociados con las diferencias entre entornos de desarrollo y producción.
""")

# Pie de página o mensaje adicional
st.write("¡Gracias por explorar Docker Compose con esta guía interactiva en Streamlit!")


# Ejecución principal de Streamlit
if __name__ == '__main__':
    st.write("¡Explora las funcionalidades de Docker Compose en esta introducción!")
