## Step 0: create a Discord Bot, retrieve the token, invite the bot to your server
Guide: https://www.writebots.com/discord-bot-token/

## Step 1: create a virtual environment

Windows:

`python -m venv venv`

Unix:

`python3 -m venv venv`

Activate the virtual environment

Windows:

`source venv/Scripts/activate`

Unix:

`source venv/bin/activate`

## Step 2: install the dependancies

`pip install -r requirements.txt`

## Step 3: export the bot's token as an envoirnment variable

`export DISCORD_BOT_TOKEN=AzUzODQ2MzQzMjQ3NzI0NTg0.X1sIHg.Qi4WWImkrAc02D-b_OTAABFxyW0`

## Step 4: make sure a "student_data.csv" file exists

## Step 5: run util.py to parse the .csv file into a JSON file 
Note: If you made changes to the csv file simply run util.py again to update the student data
these changes will be reflected in the Bot as well!

## Step 6: run bot.py to start the bot
Note: Make sure step 3 is done!
