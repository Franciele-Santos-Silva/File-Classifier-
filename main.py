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
    "outros": [".csv", ".json", ".xml", ".html", ".css", ".js"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}") 
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
        os.rename("caminho/nome_antigo", "aminho/novo_nome")
