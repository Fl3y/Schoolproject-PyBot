
import datetime
import os
from unicodedata import name
import dotenv
import humanfriendly
import discord
import ffmpeg
from discord.ext import commands, tasks
import json 
import re
import music
import ReputationScore
import random
from discord import ButtonStyle
from discord.ui import Button, View
from ReputationScore import standart_Ctzn_Score
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cogs = [music, ReputationScore]

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

if os.path.exists(os.getcwd() + "/Questions.json"):
    with open("./config.json") as q:
        configData = json.load(q)

        


bannedWords = configData["bannedWords"]

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')

cred = credentials.Certificate("serviceAccountKey.json")
databaseApp = firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://amplified-cache-305320-default-rtdb.europe-west1.firebasedatabase.app/"
})

intents = discord.Intents.all()

client = commands.Bot(command_prefix='.', intents=intents)

for i in range(len(cogs)):
    cogs[i].setup(client)

Question = str
answerA = ""
answerB = ""
answerC = ""
answerD = ""
trueAnswer = str
answerClicked = bool
WhoWaspicked = str



class myView(discord.ui.View):

    global Question
    global answer1
    global answer2
    global answer3
    global answer4
    global trueAnswer
    global answerClicked 


    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label="A", style=ButtonStyle.grey, disabled=False)
    async def button1_callback(self, button1, interaction):
        global answerA
        global answerB
        global answerC
        global answerD

        global trueAnswer
        global answerClicked 

        role = discord.utils.get(interaction.channel.guild.roles, name = "Question")

        if trueAnswer == answerA and answerClicked != True and role in interaction.user.roles:
            button1.label = "Your answer is correct"
            button1.style = ButtonStyle.success
            button1.disabled = True
            answerClicked = True
            user = interaction.user
            ref =  db.reference("Users")
            Score = ref.child(str(user.id)).child('Ctzn_Score').get()
            newScore = Score + 100
            ref.update({
                user.id:{
                    "Ctzn_Score": newScore
                }
            })
            await interaction.response.edit_message(view = self)
        elif answerClicked == True:
            button1.label = "You already answered the Question"
            button1.style = ButtonStyle.danger
            button1.disabled = True
            answerClicked = True
            await interaction.response.edit_message(view = self)
        elif trueAnswer != answerA and role in interaction.user.roles:
            button1.label = "Your answer is wrong"
            button1.style = ButtonStyle.red
            button1.disabled = True
            answerClicked = True
            user = interaction.user
            ref = db.reference("Users")
            Score = ref.child(str(user.id)).child('Ctzn_Score').get()
            newScore = Score - 50
            ref.update({
                    user.id:{
                            "Ctzn_Score": newScore
                            }    
                    })
            if Score <= 0:
                await user.ban(reason = "You have been executed for treason")
            await interaction.response.edit_message(view = self)

    @discord.ui.button(label="B", style=ButtonStyle.grey, disabled=False)
    async def button2_callback(self, button2, interaction):
        global answerClicked
        global trueAnswer
        global answerA
        global answerB
        global answerC
        global answerD

        role = discord.utils.get(interaction.channel.guild.roles, name = "Question")

        if trueAnswer == answerB and answerClicked != True and role in interaction.user.roles:
            button2.label = "Your answer is correct"
            button2.style = ButtonStyle.success
            button2.disabled = True
            answerClicked = True
            user = interaction.user
            ref =  db.reference("Users")
            Score = ref.child(str(user.id)).child('Ctzn_Score').get()
            newScore = Score + 100
            ref.update({
                user.id:{
                    "Ctzn_Score": newScore
                }
            })
            await interaction.response.edit_message(view = self)
        elif answerClicked == True:
            button2.label = "You already answered the Question"
            button2.style = ButtonStyle.danger
            button2.disabled = True
            answerClicked = True
            await interaction.response.edit_message(view = self)
        elif trueAnswer != answerB and role in interaction.user.roles:
            button2.label = "Your answer is wrong"
            button2.style = ButtonStyle.red
            button2.disabled = True
            answerClicked = True
            user = interaction.user
            ref = db.reference("Users")
            Score = ref.child(str(user.id)).child('Ctzn_Score').get()
            newScore = Score - 50
            ref.update({
                    user.id:{
                            "Ctzn_Score": newScore
                            }    
                    })
            if Score <= 0:
                await user.ban(reason = "You have been executed for treason")
            await interaction.response.edit_message(view = self)
                    
    @discord.ui.button(label="C", style=ButtonStyle.grey, disabled=False)
    async def button3_callback(self, button3, interaction):
        global answerClicked
        global answerA
        global answerB
        global answerC
        global answerD

        role = discord.utils.get(interaction.channel.guild.roles, name = "Question")

        if trueAnswer == answerC and answerClicked != True and role in interaction.user.roles:
            button3.label = "Your answer is correct"
            button3.style = ButtonStyle.success
            button3.disabled = True
            answerClicked = True
            user = interaction.user
            ref =  db.reference("Users")
            Score = ref.child(str(user.id)).child('Ctzn_Score').get()
            newScore = Score + 100
            ref.update({
                user.id:{
                    "Ctzn_Score": newScore
                }
            })
            await interaction.response.edit_message(view = self)
        elif answerClicked == True:
            button3.label = "You already answered the Question"
            button3.style = ButtonStyle.danger
            button3.disabled = True
            await interaction.response.edit_message(view = self)
        elif trueAnswer != answerC and role in interaction.user.roles:
            button3.label = "Your answer is wrong"
            button3.style = ButtonStyle.red
            button3.disabled = True
            answerClicked = True
            user = interaction.user
            ref = db.reference("Users")
            Score = ref.child(str(user.id)).child('Ctzn_Score').get()
            newScore = Score - 50
            ref.update({
                    user.id:{
                            "Ctzn_Score": newScore
                            }    
                    })
            if Score <= 0:
                await user.ban(reason = "You have been executed for treason")
            await interaction.response.edit_message(view = self)
    
    @discord.ui.button(label="D", style=ButtonStyle.grey, disabled=False)
    async def button4_callback(self, button4, interaction):
        global answerClicked
        global answerA
        global answerB
        global answerC
        global answerD

        role = discord.utils.get(interaction.channel.guild.roles, name = "Question")

        if trueAnswer == answerD and answerClicked != True and role in interaction.user.roles:
            button4.label = "Your answer is correct"
            button4.style = ButtonStyle.success
            button4.disabled = True
            answerClicked = True
            user = interaction.user
            ref =  db.reference("Users")
            Score = ref.child(str(user.id)).child('Ctzn_Score').get()
            newScore = Score + 100
            ref.update({
                user.id:{
                    "Ctzn_Score": newScore
                }
            })
            await interaction.response.edit_message(view = self)
        elif answerClicked == True:
            button4.label = "You already answered the Question"
            button4.style = ButtonStyle.danger
            button4.disabled = True
            answerClicked = True
            await interaction.response.edit_message(view = self)
        elif trueAnswer != answerD and role in interaction.user.roles:
            button4.label = "Your answer is wrong"
            button4.style = ButtonStyle.red
            button4.disabled = True
            answerClicked = True
            user = interaction.user
            ref = db.reference("Users")
            Score = ref.child(str(user.id)).child('Ctzn_Score').get()
            newScore = Score - 50
            ref.update({
                    user.id:{
                            "Ctzn_Score": newScore
                            }    
                    })
            if Score <= 0:
                await user.ban(reason = "You have been executed for treason")
            await interaction.response.edit_message(view = self)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    return



@client.event 
async def on_member_join(member):
    print(f"{member} has joined the server,")
    Users = "Users"
    user = member.id
    ref = db.reference(f"/")
    ref.update({
        Users:{
            user:{
                "Ctzn_Score": standart_Ctzn_Score
            }    
        }
    })

    return

@client.event 
async def on_member_remove(member):
    print(f"{member} has left the server,")
    return

def msg_contains_words(msg, word):
    return re.search(fr'\b({word})\b', msg) is not None  

@client.event
async def on_message(message):
    messageAuthor = message.author
    global bannedWords
    print (bannedWords)
 
    if bannedWords != None and (isinstance(message.channel, discord.channel.DMChannel) == False and not messageAuthor.bot):
        for bannedWord in bannedWords:
            if msg_contains_words(message.content.lower(), bannedWord):
                    user = message.author
                    print(user.id)
                    ref = db.reference("Users")
                    Score = ref.child(str(user.id)).child('Ctzn_Score').get()
                    newScore = Score - 50
                    ref.update({
                            user.id:{
                                "Ctzn_Score": newScore
                            }    
                    })
                    Score = ref.child(str(user.id)).child('Ctzn_Score').get()
                    if Score <= 0:
                        await user.ban(reason = "You have been executed for treason")
                    await message.delete()
      
                    await message.channel.send(f"{messageAuthor.mention} your message was removed as it contains a banned word.")

    await client.process_commands(message)
    return




@tasks.loop(seconds=50)
async def loyaltyQuestion():
    await client.wait_until_ready()

    names = list()
    channel = client.get_channel(950532739579379766)
    print(channel.name)

    roletoRemove = discord.utils.get(channel.guild.roles, name = "Question")

    for member in channel.guild.members:
        try:
            await member.remove_roles(roletoRemove)
        except:
            print("role cant be removed")

    global answerClicked
    answerClicked = False

    for user in channel.guild.members:
        if user.bot:
            continue
        else:
            names.append(user)
            print()
            print(len(names))

    personToPick = random.randint(0,len(names)- 1)
    WhoWaspicked = names[personToPick]
    print(WhoWaspicked)
    

    role = discord.utils.get(channel.guild.roles, name = "Question")
    await WhoWaspicked.add_roles(role)

    global Question
    global trueAnswer
    global answerA
    global answerB
    global answerC
    global answerD

    with open("./Questions.json", "r") as q:
        data = json.load(q)
        print(data)
    



    Question = random.choice(list(data.keys()))
    All_Answers = str(data[Question])
    Answers= All_Answers.split(", ", 4)
    print(Answers)
    charactersToRemove = "[]'"
    answer1 = Answers[0]
    answerA = answer1.strip(charactersToRemove)

    answer2 = Answers[1]
    answerB = answer2.strip(charactersToRemove)

    answer3 = Answers[2]
    answerC = answer3.strip(charactersToRemove)

    answer4 = Answers[3]
    answerD = answer4.strip(charactersToRemove)

    answer5 = Answers[4]
    trueAnswer = answer5.strip(charactersToRemove)

    view = myView()
    await channel.send(f"{WhoWaspicked.mention}, You were picked for a public interogation, \n {Question} \n :regional_indicator_a: {answerA} \n :regional_indicator_b: {answerB} \n :regional_indicator_c: {answerC} \n :regional_indicator_d: {answerD}", view = view)
     

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")
    answerBtn1 = Button(style=ButtonStyle.red, label="Test")
    view = View()
    view.add_item(answerBtn1)
    await ctx.send

@client.command()
async def schlafen(ctx, member : discord.Member,time = None, *, reason=None):
    time = humanfriendly.parse_timespan(time)
    await member.timeout(until = discord.util9s.utcnow() + datetime.timedelta(seconds = time), reason=reason)
    await ctx.send(f"{member} has been timed out for {time} | Reason: {reason}")


loyaltyQuestion.start()

client.run(TOKEN)
