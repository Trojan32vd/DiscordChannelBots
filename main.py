import threading
from ImageFilter import bot as image_bot
from LinkFilterBot import bot as link_bot
from keep_alive import keep_alive

def run_image_bot():
    image_bot.run(image_bot.TOKEN)

def run_link_bot():
    link_bot.run(link_bot.TOKEN)

if __name__ == "__main__":
    keep_alive()
    
    # Start each bot in a separate thread
    t1 = threading.Thread(target=run_image_bot)
    t2 = threading.Thread(target=run_link_bot)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
