import os

class Config:
    TELEGRAM_TOKEN=os.environ['5856143550:AAGdqv_ZwCcMC3r9Vf9m6da-XggJ9rY_rLA']
    SUDOS=os.environ['5868178288']
    TELEGRAM_APP_HASH=os.environ['c81d1c06212c1c9624f44e159c651a5c']
    TELEGRAM_APP_ID=int(os.environ['20256702'])
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
