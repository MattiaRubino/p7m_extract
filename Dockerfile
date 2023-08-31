# Usa un'immagine di Debian come base
FROM debian:latest

# Installa Python, OpenSSL e le dipendenze necessarie
RUN apt-get update && \
    apt-get install -y python3 openssl && \
    rm -rf /var/lib/apt/lists/*


# Imposta il lavoro nella directory dell'app
WORKDIR /app

ENV INPUT_FILE_PATH /app/p7m_files
ENV OUTPUT_FILE_PATH /app/p7m_files

# Avvia lo script Python quando il container viene eseguito
CMD ["python3", "p7m.py"]
