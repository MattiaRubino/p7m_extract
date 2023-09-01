docker per l'estrazione di tutti file .p7m contenuti in una cartella passata tramite variabili di ambiente o di default creare una cartella p7m_files e inserire li i file .p7m

con variabili env di default:
docker build -t extract_p7m
docker run -it --rm -v percorso/per la/cartella/(file_p7m):/app  extract_p7m  

con variabili env :
docker run -it --rm -v C:\Users\xxx\yyy\:/app -e INPUT_FILE_PATH=/app/Nome_Cartella:Input -e OUTPUT_FILE_PATH=/app/Nome_Cartella_Output extract_p7m
