#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = os.environ['DISCORD_BOT_TOKEN']#トークン
CHANNEL_ID = 687937024581173251 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M:%A')
    if now == '07:00:Wednesday':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('
キ
  ン
    タ
     マ
       キ
        ラ
         キ
          ラ
          金
       曜日
 
   
           


')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
