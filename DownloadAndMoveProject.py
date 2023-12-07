import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/samue/Downloads"
to_dir = "D:/Arquivos-baixados"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Olá, {event.scr_path} foi criado!")
    
    def on_deleted(self, event):
        print(f"Opa! Alguém excluiu {event.src_path}!")

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt: 
    print('Interrompido!')
    observer.stop()