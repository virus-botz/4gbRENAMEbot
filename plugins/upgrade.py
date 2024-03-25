from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0
	
	**🥉 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 30  ind /🌎 0.40$  per Month
	
	**🥇 Standard**
	Daily Upload limit 50GB
	Price Rs 65  ind /🌎 0.80$  per Month
	
	**🏅 Pro**
	Daily Upload limit 100GB
	Price Rs 129  ind /🌎 1.5$  per Month
	
	
	For Pay Using Upi I'd `Contact- @RolexLeoDas`
	
	After Payment Send Screenshots Of 
        Payment To Admin @RolexLeoDas"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👨‍💻 Admin",url = "https://t.me/RolexLeoDas")], 
        			[InlineKeyboardButton("📢 Channel",url = "https://t.me/Virus_Botz"),
        			InlineKeyboardButton("💬 Group",url = "https://t.me/VIRUS_BOTZ_SUPPORT_GROUP")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0
	
	**🥉 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 30  ind /🌎 0.40$  per Month
	
	**🥇 Standard**
	Daily Upload limit 50GB
	Price Rs 65  ind /🌎 0.80$  per Month
	
	**🏅 Pro**
	Daily Upload limit 100GB
	Price Rs 129  ind /🌎 1.5$  per Month
	
	
	For Pay Using Upi I'd `Contact- @RolexLeoDas`
	
	After Payment Send Screenshots Of 
        Payment To Admin @RolexLeoDas"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👨‍💻 Admin",url = "https://t.me/RolexLeoDas")], 
        			[InlineKeyboardButton("📢 Channel",url = "https://t.me/Virus_Botz"),
        			InlineKeyboardButton("💬 Group",url = "https://t.me/VIRUS_BOTZ_SUPPORT_GROUP")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
