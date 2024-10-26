# config.py
import os

class Config:
    DEBUG = True
    USERNAME = os.environ.get('USERNAME') or 'test.local'
    PASSWORD = os.environ.get('PASSWORD') or 'test123'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or '/uploads'
