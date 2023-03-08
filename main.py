import pyrogram
from pyrogram import Client, filters

# create a Pyrogram client
app = Client("my_account")

# define a callback function to handle incoming messages
@ app.on_message(filters.private)
def handle_message(client, message):
    # print the message to the console
    print(message)

    # reply to the message
    client.send_message(chat_id=message.chat.id, text="الشخص الذي تريد التواصل معه مشغول في الحين الرجاء الانتظار حتى الرد عليك")

# start the client
app.run()
