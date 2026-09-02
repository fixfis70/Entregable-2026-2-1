#Imagen del docker
FROM python:3.12-slim

#La carpeta dentro del doker donde va a estar el codigo
WORKDIR /app

COPY requeriments.txt .

#Instalamos las dependencias
RUN pip install --no-cache-dir streamlit

# mover el codigo al docker (a /app)
COPY . .

#Decimos q puerto queremos
EXPOSE 8501

#El cmds q ejecutará la app
#Se usa "--server.address=0.0.0.0" para irnos fuera del docker
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
