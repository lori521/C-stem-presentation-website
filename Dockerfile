# Folosim o imagine oficială de Python, versiunea "slim" pentru a fi mai ușoară
FROM python:3.9-slim

# Setăm directorul de lucru în container
WORKDIR /app

# Copiem fișierul cu cerințe și instalăm bibliotecile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul fișierelor din proiect în container
COPY . .

# Expunem portul pe care rulează Streamlit
EXPOSE 8501

# Comanda care pornește aplicația când containerul este rulat
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
