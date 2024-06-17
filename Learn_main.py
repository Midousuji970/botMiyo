import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    raise ValueError("Token não encontrado. Verifique o arquivo .env e a variável DISCORD_TOKEN.")


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

@botMiyo.command()
async def lapis(ctx:commands.Context):
    meu_embed = discord.Embed(title="Lapis",description="abbadon")    
    
    imagem_arquivo = discord.File('img/lapis_bg.png','LapisBG.png')
    meu_embed.set_image(url="attachment://LapisBG.png")

    thumb_arquivo = discord.File("img/lapis_icon.png",'thumb.png')
    meu_embed.set_thumbnail(url='attachment://thumb.png')

    meu_embed.set_footer(text="LapisTeste")
    
    meu_embed.color = discord.Color.pink()
    
    autor_foto = discord.File('img/autor.png','autor.png')
    meu_embed.set_author(name="Midou",icon_url="attachment://autor.png")
   
    meu_embed.add_field(name="Skill",value=10,inline=False)
    meu_embed.add_field(name="Skill2",value="Quazar",inline=False)
    meu_embed.add_field(name="skill3",value="Myst",inline=False)
    
    await ctx.reply(files=[imagem_arquivo, thumb_arquivo, autor_foto], embed=meu_embed)

# miyo repetindo os outros    
#@botMiyo.command()
#async def falar(ctx:commands.Context, *,frase): #só coloque o *, antes se for a frase todoa e não a primeira palavra
    #await ctx.send(frase)
    
# envia o calendario    
@botMiyo.command()
async def calendario(ctx:commands.Context):
    link = "https://i.imgur.com/uibyKGY.png"
    await ctx.reply(link)
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

botMiyo.run(TOKEN)