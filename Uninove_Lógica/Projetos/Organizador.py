
from genericpath import exists
from msilib.schema import Patch
import os 
import sys
import shutil
import asyncio


#lista de extensoes

organizado = False

import PySimpleGUI as sg

sg.theme('DarkAmber')

caminho = sg.popup_get_folder('Teste')
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def on_moved(event):
    print('Movido')
def on_modified(event):
    print('Modificado')
def on_created(event):
    print('Modificado')
def on_deleted(event):
    print('Modificado')
def criar_pasta(pasta,id):
    os.makedirs(pasta[id])
async def mover_arquivo(arq,past,id):
    await asyncio.sleep(1)
    try:
        shutil.move(arq,past[id])
    except:
        print("a")
def id_pastas(extensoes):
    id=0
    print(extensoes)
    if extensoes == ".exe":
        id=0
    elif extensoes == ".xlsx":
        id=1
    elif (extensoes == ".png" or extensoes == ".jpg" or extensoes == ".jpeg"):
        id=2
    elif (extensoes == ".pdf" or extensoes == ".PDF") :
        id=3
    elif (extensoes == ".zip" or extensoes == ".rar"):
        id=4
    elif extensoes == ".ino":
        id=5
    elif (extensoes == ".doc" or extensoes == ".rtf" or extensoes == ".docx" or extensoes == ".txt"):
        id=6
    elif extensoes == ".sql":
        id=7
    elif extensoes == ".gif":
        id=9
    elif extensoes == ".html":
        id=10
    elif extensoes == ".php":
        id=11
    elif (extensoes == ".mp3" or extensoes == ".mp4"):
        id=12
    elif extensoes == ".py":
        id=13
    return id
async def main():
    if __name__ == "__main__":
        event_handler = FileSystemEventHandler()
        event_handler.on_moved= on_moved
        event_handler.on_moved= on_modified
        event_handler.on_moved= on_created
        event_handler.on_moved= on_deleted
        path=caminho
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            print('Monitorando')
            while True:
                time.sleep(1)
                organizado=False
                while organizado != True:
                    lista = os.listdir(caminho)
                    for arquivo in lista :
            
                        pastas =  f"{caminho}/Executaveis",f"{caminho}/Excel",f"{caminho}/Imagens",f"{caminho}/PDF",f"{caminho}/Zip",f"{caminho}/Arduino",f"{caminho}/Arquivos de Texto",f"{caminho}/Banco de Dados",f"{caminho}/ETEC",f"{caminho}/GIF",f"{caminho}/HTML",f"{caminho}/PHP",f"{caminho}/Musicas",f"{caminho}/Python",f"{caminho}/Desorganizado"

                        ext = ".exe",".png",".pdf",".jpg",".zip",".rar",".ino",".txt",".docx",".sql",".gif",".html",".php",".mp3",".rtf",".doc",".mp4",".jpeg",".xlsx",".py",".PDF"
                        arquivos=caminho+"/"+arquivo
                        for extensoes in ext:   
                            if extensoes in arquivo:
                                id = id_pastas(extensoes)
                                print(id)   
                                if not os.path.exists(pastas[id]):
                                    criar_pasta(pastas,id)
                                    await (mover_arquivo(arquivos, pastas,id))
                                else:
                                    await (mover_arquivo(arquivos, pastas,id))
                        if arquivos in pastas:
                            print("Não Passou")
                            print("Aqui ",arquivos)
                        else:
                            print("a")
                            if not os.path.exists(pastas[14]):
                                criar_pasta(pastas,14)
                            else:
                                print("Moveu")
                                print("Aqui ",arquivos)
                                await (mover_arquivo(arquivos, pastas,14))
                        organizado = True
        finally:
            observer.stop()
            observer.join()
asyncio.run(main())
