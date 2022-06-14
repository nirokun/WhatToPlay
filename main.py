import discord
from random import choice, randint
import random
import discord_webhook
from discord.ext import commands
from timeit import timeit

# Token Bot
TOKEN = 'OTYyNDUwNjA1MTA2OTM3OTE3.YlHt-Q.wvloMo1zJ7G9bzjXsO1EC5RfWfQ'

# Bot instance and prefix
bot = commands.Bot(command_prefix='!')

# Variables
game_list = []

# Methods
@bot.event
async def on_ready():
    print('Discord Bot What to Play ready!'.format(bot))


@bot.command(name='hello')
async def greatings(message):
    await message.send(f"```Hello! I'm working {message.author.name}, don't bother me.```")

@bot.command(name='addgames')
async def addgames(message, *games):
    global game_list
    lon = len(list(games))
    init_len = len(game_list)
    not_added = 0
    for x in range(0,lon):
        if games[x].lower() not in game_list:
            game_list.append(games[x].lower())
        else:
            not_added += 1
    if not_added > 0:
        await message.send(f"```{len(game_list)-init_len} {'game' if (len(game_list)-init_len) == 1 else 'games'} added correctly. {not_added} already {'were' if not_added > 1 else 'was'} on the list.```")
    else:
        await message.send(f"```Games added correctly.```")

@bot.command(name='games')
async def games(message):
    games = ''
    for x in game_list:
        games += str('-' + x.capitalize() + '\n')
    if games == '':
        await message.send(f"```There are no games in the list. Please add one at least.```")
    else:
        await message.send(f"```This is the game list:\n{games}```")

@bot.command(name='random')
async def choose_game(message):
    global game_list
    if len(game_list) == 0:
        await message.send(f"```There are no games in the list. Please add one at least.```")
        return

    # First option. Search game and remove it from the list.
    game = choice(game_list)
    game_list.remove(game)

    # Second option. Get random position and pop it from the list.
    # i = randint(0, len(game_list))
    # game = game_list.pop(i)

    await message.send(f"```🎉🎉🎉{game.upper()}🎉🎉🎉```")

@bot.command(name='clear')
async def clear_list(message):
    global game_list
    game_list.clear()
    await message.send(f"```Your list is now empty. Enjoy (?).```")


bot.run(TOKEN)
