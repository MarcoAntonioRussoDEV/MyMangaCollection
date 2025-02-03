import sys,os


def get_executable_path():
    """Restituisce la directory in cui si trova l'eseguibile o lo script."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)  # Percorso dell'eseguibile
    return os.path.dirname(os.path.abspath(__file__))  # Percorso dello script

# Percorsi per salvare i file
base_path = get_executable_path()
csv_path = os.path.join(base_path, "mangas.csv")
images_folder = os.path.join(base_path, "images")
public_folder = os.path.join(base_path, "public")
icon_path = os.path.join(public_folder, "icon.ico")

# Esempio: Creare la cartella images e public se non esiste
os.makedirs(images_folder, exist_ok=True)
os.makedirs(public_folder, exist_ok=True)


