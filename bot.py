import requests
import discord
import json
from random import shuffle

def GetRandomTrivia():
    response = json.loads(requests.get(url).text)
    correct_answer = response['results'][0]['correct_answer']
    incorrect_answers = response['results'][0]['incorrect_answers']
    answers = incorrect_answers
    answers.append(correct_answer)
    shuffle(answers)

    stuff = {"question" : response['results'][0]['question'], "answers" : answers, "correct_answer" : correct_answer}
    return stuff

#.extend(response['results'][0]['incorrect_answers'])

client = discord.Client()
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

url = 'https://opentdb.com/api.php?amount=1&type=multiple'

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!trivia'):
    trivia = GetRandomTrivia()
    msg = trivia['question'] + "\n" + str(trivia['answers']) + "\n" + "[Paste the right answer]" 
    await message.channel.send(msg)

  if message.content.startswith('!answer'):
    try:
      if message.content.replace('!answer ', '') == trivia['correct_answer']:
        await message.channel.send("That's correct!")
      else:
        await message.channel.send("That's not correct.")
    except:
      await message.channel.send("error lmaoooo")

@client.event
async def on_ready():
       print('Logged in as')
       print(client.user.name)
       print(client.user.id)
       print('------')

client.run(TOKEN)
