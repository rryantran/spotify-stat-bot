import subprocess

# Start the Flask server and the Discord bot
flask_process = subprocess.Popen(["python3", "spotify.py"])
discord_process = subprocess.Popen(["python3", "bot.py"])

# Wait for the processes to finish
flask_process.wait()
discord_process.wait()
