import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from flask import Flask, redirect

# Load environment variables
load_dotenv()

# Set up Flask app
app = Flask(__name__)

# Set up Spotify OAuth
spotify_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URI"),
    scope="user-top-read",
)


@app.route("/login")
def login():
    """Redirects user to Spotify login page"""
    return redirect(spotify_oauth.get_authorize_url())


@app.route("/callback")
def callback():
    """Handles callback from Spotify OAuth"""
    pass


# Run Flask app on port 5000
if __name__ == '__main__':
    app.run(port=5000)
