import discord
import asyncio
import random
import pickle
import os
import sys
from pymarketcap import *
import json
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name=' Rich Chigga music'))
@client.event
async def on_message(message):
	"""
	#chance for ledan stare
	if message.author.id != '376550967413309441':
		chance_ledan_stare = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
		chance_ledan_stare_choice = random.choice(chance_ledan_stare)
		if chance_ledan_stare_choice == 3:
			await client.send_message(message.channel, '*Ledan stares at you in the distance*')
	"""

	if message.author == client.user:
		return

	if message.content.startswith("hello") or message.content.startswith("Hello") or message.content.startswith("Hi") or message.content.startswith("hi"):
		await client.send_message(message.channel, "Hello!")

	#bot response to deep
	if message.author.id == '128683786379591680':
		if 'chhang' in message.content or 'Chhang' in message.content:
			await client.send_message(message.channel, 'Sah Deep')

	#bot response to aakash
	if message.author.id == '131515629852164097':
		if 'bm' in message.content:
			await client.send_message(message.channel, "No, you're bm")
		elif 'league' in message.content or 'rank' in message.content:
			await client.send_message(message.channel, "No")
		elif 'clang' in message.content:
			await client.send_message(message.channel, "Sah akukash")

	#bot response to ledan
	if message.author.id == '129403786639835136':
		stfu_chance = [0,1,2]
		stfu_choice = random.choice(stfu_chance)
		if stfu_choice == 2:
			await client.send_message(message.channel, 'Stfu ledan')

	#!rank = dice roll for league rank
	if message.content.startswith('!rank'):
		rank_options = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Masters', 'Challenger']
		rank_choice = random.choice(rank_options)
		if rank_choice == 'Bronze':
			rank_message = 'You rolled "Bronze". DO NOT PLAY RANKED GAMES AT ALL COSTS. I\'M WARNING YOU'
		elif rank_choice == 'Silver':
			rank_message = 'You rolled "Silver". Eh, hope the enemies are bad.'
		elif rank_choice == 'Gold':
			rank_message = 'You rolled "Gold". Time to be completely average.'
		elif rank_choice == 'Platinum':
			rank_message = 'You rolled "Platinum". Time to hit plat.'
		elif rank_choice == 'Diamond':
			rank_message = 'You rolled "Diamond". Literally Spencer Chu PogChamp'
		elif rank_choice == 'Masters':
			rank_message = 'You rolled "Masters". Holy crap time to carry'
		elif rank_choice == 'Challenger':
			rank_message = 'You rolled "Challenger". Time to get a jacket'
		await client.send_message(message.channel, rank_message)

	#!rc song = prints out a Rich Chigga song
	if message.content.startswith('!rc song'):
		rc_song_options = ['Dat $tick', 'Who Dat Be', 'Seventeen', 'Back At It', 'Glow Like Dat', 'Bankroll', 'Gospel', 'Chaos', 'Working For It', 'Crisis']
		rc_song_choice = random.choice(rc_song_options)
		await client.send_message(message.channel, rc_song_choice)

	#!best = @me is the best
	if message.content.startswith('!best'):
		myid = '<@128685936740532226>'
		await client.send_message(message.channel, ' %s is the best ' % myid)

	#!help = send help
	if message.content.startswith('!help'):
		await client.send_message(message.author, "Does you really thinking that I'll helping you Patelli? lol")

	#!botoff = turn off bot (Error atm)
	if message.content.startswith('!botoff'):
		sys.exit("Turning off the bot")

	#!rc pic = random rich chigga pic
	if message.content.startswith('!rc pic'):
		rc_picture_options = range(1,62)
		rc_picture_choice = str(random.choice(rc_picture_options))
		await client.send_file(message.channel, 'rc_pics/rc' + rc_picture_choice + '.jpg')

	#!ledan pic = random ledan pic
	if message.content.startswith('!ledan pic'):
		ledan_picture_options = range(1,26)
		ledan_picture_choice = str(random.choice(ledan_picture_options))
		await client.send_file(message.channel, 'ledan_pics/ledan' + ledan_picture_choice + '.jpg')

	#!ledan quote = random ledan quote
	if message.content.startswith('!ledan quote'):
		ledan_quote_options = ['Good morning', 'Don\'t touch me', 'Hmph', '*not saying Thank you*', 'no', 
								'Ez', ':thumbs up:', 'Just getting a feel for the game', 'Offense is the best defense', 
								'I can take off all my clothes',' I\'m a tree', 'Yolo', 'Jonathan rides me like a horse', '*makes a kissing sound with his mouth*']
		ledan_quote_choice = random.choice(ledan_quote_options)
		await client.send_message(message.channel, 'Ledan says "' + ledan_quote_choice + '"')

	#!jonathan quote = random jonathan quote
	if message.content.startswith('!jonathan quote'):
		jonathan_quote_options = ['Hello hello', 'You\'re adopted', 'Jaeha why are you naked?', 
									'Ledan is my BEST FRIEND', 'ខ្ញុំហើយ', 'Party at Ledan\'s house and Ledan\'s not invited.', 
									'Deep stfu', 'You\'re adoctored', 'You\'re a square', 'Why is the world full of triangles?',
									'*really loud keyboard typing*', 'Ledan where are you? You\'re useless.',
									'Chang is my friend', 'Don\'t worry', 'Pomf pomf kimochi', 'Jaeha', 'Hi Robin',
									'Role playing RPG', 'What\'d I do?', '*farts* Chang why\'d you fart?']
		jonathan_quote_choice = random.choice(jonathan_quote_options)
		await client.send_message(message.channel, 'Jonathan says "' + jonathan_quote_choice + '"')

	#!chang quote = random chang quote
	if message.content.startswith('!chang quote'):
		chang_quote_options = ['I love white people', 'Ledan stfu', 'No Aakash', 'Remember to drink water',
								'Are there any white people here?', 'How do you know, Deep?', 'Christmas died on the cross for us',
								'Guys it\'s my first time being straight, take it easy on me','I\'m a second time virgin', 'spchu']
		chang_quote_choice = random.choice(chang_quote_options)
		await client.send_message(message.channel, 'Chang says "' + chang_quote_choice + '"')

	#!phang quote = random phang quote
	if message.content.startswith('!phang quote'):
		phang_quote_options = ['Stfu white person', 'China numba won. China numba won. China numba won', 
								'Ok, whatever', 'Don\'t tell me what to do', 'What\'s the password?',
								'Ledan always gets invited to everything', 'Yes', 'Henry/Ledan where is behind us? You guys have to use the compass',
								'Who\'s breathing so loud?', 'Panha with a winky face emoji', 'Not just any thot, Jonathot'
								, 'Downright Darius', 'AHHHHKUSH AHHHHKUSH']
		phang_quote_choice = random.choice(phang_quote_options)
		await client.send_message(message.channel, 'Phang says "' + phang_quote_choice + '"')

	coinmarketcap = Pymarketcap()
	if message.content.startswith('!price'):
		#.split splits the message into parts separated by the space, blah becomes the first string, coin becomes the second string
		user_message = message.content.split(" ")
		#tries to get the json list from the ticker, ex: BTC, ETH, LTC
		coin = user_message[1]
		now = datetime.now()
		try:
			json_list = coinmarketcap.ticker(coin.upper())
		except:	#should i do except KeyError, or catch all exceptions?
			try:
				#else, tries to get the list from the actual coin name, ex: Bitcoin, Ethereum, Litecoin
				modified_coin_spelling = coin[0].upper() + coin[1:].lower()
				json_list = coinmarketcap.ticker(modified_coin_spelling)
			except:
				await client.send_message(message.channel, 'Error: {0} is not a valid ticker/coin'.format(coin))
			else:
				await client.send_message(message.channel, 'The price of {0} is ${1}'.format(modified_coin_spelling, json_list['price_usd']))
				await client.send_message(message.channel, '24hr: {0}%'.format(json_list['percent_change_24h']))
		else:
				await client.send_message(message.channel, 'The price of {0} is ${1}'.format(coin, json_list['price_usd']))
				await client.send_message(message.channel, '24hr: {0}%'.format(json_list['percent_change_24h']))
	
	#!price                ticker won't work, need a better split
	#should add functionality to create an array of coins a certain user likes, ex: my list would be ETH, NEO, XRB, etc.
	#add functionality to append or remove from the array 

client.run('Mzc2NTUwOTY3NDEzMzA5NDQx.DOACjw.yklqdoS0DTk9S57OZawKkciSr-s')
