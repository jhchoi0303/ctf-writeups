# Imp3rs0nAt0r-1
### misc 
### Forensics + Osint




----

**Open UsrClass.dat file with ShellBagsExplorer.exe**
**Scripts contain .git file**

![](https://i.imgur.com/3Fqeq5E.png)










---

**Search  Github**

![](https://i.imgur.com/lYTrRh4.png)



**bot.py seems suspicious**


![](https://i.imgur.com/T263KUw.png)





---

**Read all messages of all servers that this bot is related to**

```
import discord, base64
from discord.ext import commands

bot = commands.Bot(command_prefix='$', case_insensitive=True)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    for guild in bot.guilds:
        print("Servers:")
        print(guild.name)
```
![](https://i.imgur.com/jYqSEPh.png)





---

**Enter related server** 
**Flag in txt file**

![](https://i.imgur.com/UMtdcEY.png)
