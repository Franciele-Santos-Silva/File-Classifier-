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
    nome, extensao = os.path.splitext(arquivo)  
    for pasta in locais:
        if extensao.lower() in locais[pasta]: 
            if not os.path.exists(os.path.join(caminho, pasta)):
                os.mkdir(os.path.join(caminho, pasta))
            os.rename(os.path.join(caminho, arquivo), os.path.join(caminho, pasta, arquivo))
