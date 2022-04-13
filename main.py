from telethon import TelegramClient, events
from environs import Env

env = Env()
env.read_env()

api_id=env.int('api_id')
api_hash=env.str('api_hash')

from telethon import TelegramClient, events
client = TelegramClient('anon', api_id, api_hash)

BLOCK_LIST = (2105729169,1362660853,)

@client.on(events.NewMessage)
async def myhandler(event):    
    sender_id = event.sender_id
        
    if sender_id in BLOCK_LIST:
        print("BLOCKED USER")
        await event.delete()


async def main(client):
    me = await client.get_me()
    print("Working with", me.first_name)
    await client.send_message("@example", "example")
    

with client:
    client.start()
    client.loop.run_until_complete(main(client))
    client.run_until_disconnected()
        

