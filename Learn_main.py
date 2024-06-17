import discord
from discord.ext import commands
# permissoes dele
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True
# Prefixo do bot
botMiyo = commands.Bot(command_prefix="-",intents=permissoes)

@botMiyo.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author # Pega o nome do usuario que fez o comando
    usuario.mention
     # ctx.reply responde o usuario, e ctx.send só manda a mensagem
    await ctx.reply(F"Ola {usuario.display_name}")
     # se for .name =  nome do discord global, .display_name nome do servidor

#exemplo de soma
@botMiyo.command()
async def somar(ctx:commands.Context, num1:float, num2:float):
    res = num1 + num2
    await ctx.reply(f"A soma de {num1} + {num2} = {res}")

# miyo repetindo os outros    
#@botMiyo.command()
#async def falar(ctx:commands.Context, *,frase): #só coloque o *, antes se for a frase todoa e não a primeira palavra
    #await ctx.send(frase)
    
# envia o calendario    
@botMiyo.command()
async def calendario(ctx:commands.Context):
    link = "https://i.imgur.com/uibyKGY.png"
    await ctx.reply(link)

@botMiyo.command()
async def miyo(ctx:commands.Context):
    await ctx.reply("O Miyo Adora rolas! ")
# Verifica se esta online
@botMiyo.event
async def on_ready():
    print("Estou pronto")

#responde a ultima mensagem
@botMiyo.event
async def on_message(msg:discord.message):
    autor = msg.author
    if autor.bot:
        return
    await botMiyo.process_commands(msg)


# quando um canal é criado
#@botMiyo.event
#async def on_guild_channel_create(canal:discord.abc.GuildChannel):
    #await canal.send(f"Novo anal: {canal.name}")

# quando entrar um membro
#@botMiyo.event    
#async def on_member_join(membro:discord.member):
    #canal = botMiyo.get_channel(799475754635231275)
    #await canal.send(f"{membro.display_name} Entro no servidor!\n Me Come!")

# quando alguem sai
#@botMiyo.event
#async def on_member_remove(membro:discord.member):
    #canal = botMiyo.get_channel(799475754635231275)
    #await canal.send(f"{membro.display_name} Vagabundo!")
#Iniciar o bot

with open("token.txt", "r") as token_file:
    txtToken = token_file.read().strip()

botMiyo.run(txtToken)