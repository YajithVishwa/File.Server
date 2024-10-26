# config.py
import os

class Config:
    DEBUG = True
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'D:/Workspace/Python Project/File.Server/app/upload'
