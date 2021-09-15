import speech_recognition as sr
from telethon import TelegramClient, events, sync
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

# initialize the recognizer
r = sr.Recognizer()
# initialize the microphone
m = sr.Microphone()

user_id = "%USER_ID%"
api_id = "%API_ID%"
api_hash = "%HASH%"

client = TelegramClient('', api_id, api_hash)
client.start()
client.iter_dialogs()
client.get_entity(PeerChannel('%CHANNEL_ID%'))

while True:

    with m as source:
    try:
        r.adjust_for_ambient_noise(source)
        # read the audio data from the default microphone
        print('Listening...')
        audio_data = r.listen(source)
        print('Parsing...')
        # convert speech to text
        text = r.recognize_google(audio_data, language='es-ES')
        print('Sending...')
        client.send_message(
            PeerChannel('%CHANNEL_ID%'),  # to which entity you are forwarding the messages
            text  # the messages (or message) to forward
        )
    except:
        print('Nothing.')
