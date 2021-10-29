import time
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pytz import timezone
from apscheduler.schedulers.blocking import BlockingScheduler

load_dotenv()

scope = "user-read-playback-state streaming"
track = ["spotify:track:6LNjIsgHNs4q75uPt4rYf6"]

def playCalling():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    devices = sp.devices()

    available_devices = {}
    for device in devices['devices']:
        available_devices[device['name']] = device['id']

    cattano_id = available_devices['Cattano']

    sp.start_playback(device_id=cattano_id, uris=track)


if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone='utc')
    scheduler.add_job(playCalling, 'cron', day_of_week='mon-fri', hour=21,)
    scheduler.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

