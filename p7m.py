import subprocess
import os

input_file_path = os.environ.get('INPUT_FILE_PATH')
output_file_path = os.environ.get('OUTPUT_FILE_PATH')

if os.path.exists(input_file_path) and os.path.isdir(input_file_path):
    if os.listdir(input_file_path):
        for filename in os.listdir(input_file_path):
            if filename.endswith(".p7m"):
                file_path_p7m = os.path.join(input_file_path, filename)
                split_filename = filename.split(sep=".")
                file_name_decript =f"{output_file_path}/{split_filename[0]}.{split_filename[1]}"

                command = (f"openssl cms -decrypt -verify -inform DER -in \"{file_path_p7m}\" -noverify -out \"{file_name_decript}\"")
                print(command)
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Decrittatura e verifica completate con successo.")
                except subprocess.CalledProcessError as e:
                    print("Si è verificato un errore durante l'esecuzione del comando.")
                    print("Errore:", e)

