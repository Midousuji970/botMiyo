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

@botMiyo.command()
async def nelliaT(ctx:commands.Context): 
    #inicia o embed
    nelliaT_embed = discord.Embed()
    #Autor tipo um titulo
    puni = discord.File(R"img/elementos/puni.png","puni.png")
    nelliaT_embed.set_author(name="Nellia (T)",icon_url="attachment://puni.png")
    #Background
    nelliaT_bg = discord.File('img/nelliaT/nelliaT_bg3.png', 'nelliaT_bg.png')
    nelliaT_embed.set_image(url='attachment://nelliaT_bg.png')
    #Emojis para o bot
    sacer = "<:sacer:1248071116279255180>"
    rankT = "<:RankT:1252411149769510984>"
    #descricao com emoji
    nelliaT_embed.description = f"Classe:{sacer}  Rank {rankT}"
    nelliaT_embed.add_field(name="Equipamento", value="PVE:", inline=False)
    #thmbunail
    nelliaT_thumb = discord.File("img/nelliaT/nelliaT_Thumb.png", "nelliaT_thumb.png")
    nelliaT_embed.set_thumbnail(url="attachment://nelliaT_thumb.png")
    #cor lateral
    nelliaT_embed.color = discord.Color.dark_purple()
    #mensagem
    await ctx.reply(files=[nelliaT_bg,nelliaT_thumb,puni],embed=nelliaT_embed)

@botMiyo.command()
async def veigasT(ctx:commands.Context):
    veigasT_embed = discord.Embed()    
    puni = discord.File(R"img/elementos/puni.png","puni.png")

    veigasT_embed.set_author(name="Veigas (T)",icon_url="attachment://puni.png")

    veigasT_bg = discord.File("img/equip/RangerGreen.png", "RangerGreen.png")
    veigasT_embed.set_image(url="attachment://RangerGreen.png")
    await ctx.reply(files=[puni,veigasT_bg],embed=veigasT_embed)
#####################################################################################################################
#botoes
@botMiyo.command()
async def testeBtn(ctx:commands.Context):
    async def res_btn(interact:discord.Interaction):
        await interact.response.send_message("Miyo Viado!",ephemeral=True)#ephemeral é mensagem que só o usuario pode ver
        #A segunda mensagem é como se fosse uma continuação ja que nao se pode usar dois response.send_message no mesmo comando
        await interact.followup.send("Urubu do Pix 50 reais viram 5000",ephemeral=True)

    view = discord.ui.View()#Core de refente aos menus e botoes
    botao = discord.ui.Button(label="Botão", style=discord.ButtonStyle.blurple)# label é o texto do botao e style a cor dele
    botao.callback = res_btn # aqui ele chama a função do res_btn
    #botao com link
    btn_url = discord.ui.Button(label="Teste",url="https://www.youtube.com/watch?v=fdOfkOfD5_k")
    #adicione na view o botao
    view.add_item(botao)
    view.add_item(btn_url)

    await ctx.reply(view=view)

@botMiyo.command()
async def menuTeste(ctx:commands.Context):
    async def res_menu(interact:discord.Interaction):
        num1 = 0
        while num1 < 2:
            jogos = {'1':'Grand Chase','2':'Elsword','3':'Priconne'}
            match num1:
                case 0:
                    escolha = interact.data["values"][0]                    
                    jogo_es = jogos[escolha]
                case 1:
                    escolha2 = interact.data["values"][1]    
                    jogo_es2= jogos[escolha2]
            num1 += 1
        
        await interact.response.send_message(F"Jogos Escolhidos: {jogo_es} e {jogo_es2}",ephemeral=True)

    menuSele = discord.ui.Select(placeholder="Selecione Algum!",max_values=2)
    opcoes = [
        discord.SelectOption(label="Grand Chase",value=1),
        discord.SelectOption(label="Elsword",value=2),
        discord.SelectOption(label="Priconne",value=3)
    ]
    menuSele.options = opcoes
    menuSele.callback = res_menu
    view = discord.ui.View()
    view.add_item(menuSele)
    await ctx.send(view=view)

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
