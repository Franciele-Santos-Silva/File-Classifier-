import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "compactados": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "outros": []
}