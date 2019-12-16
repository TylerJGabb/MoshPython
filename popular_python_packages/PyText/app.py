import sys
from twilio.rest import Client
try:
    from popular_python_packages.PyText import config
except ImportError as imp:
    sys.stderr.write(str(imp) +
         '\nconfig.py file was excluded from source to hide the ACCOUNT_SID and AUTH_TOKEN, you need to add this\n')
    exit(1)


client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)

call = client.messages.create(
    to="+15204013289",
    from_="+14696152371",
    body="this is our first message"
)

