dockerfile per l'estrazione di tutti file .p7m contenuti in una cartella passata tramite variabili di ambiente o di defoult creare una cartella p7m_files e inserire dentro i file p7m
docker build -t extract_p7m
docker run -it --rm -v percorso/della/cartella/con/i/file_p7m:/app  extract_p7m  

