import time
from pyrogram import filters, Client

CMD = ["/"]

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pinging....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong 🔥!\n{time_taken_s:.3f} ms")
    return time_taken_s



