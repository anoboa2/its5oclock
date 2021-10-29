# its5oclock
Plays calling (lose my mind) at 21:00 utc

## Background
After a trip to happiest places on earth, D'jais, my roommate and I asked ourselves "why not make every day feel like a Belmar happy hour?"  In tribute to one of the most iconic songs on the Jersey Shore, this program plays Calling by Alesso and Sebastian Ingrosso via Spotify.  


## Installation
This program uses the [Spotipy](https://github.com/plamere/spotipy) python module to make interacting with the Spotify Web API seamless.  You can install all packages used through the Pipfile.
'''bash
pipenv install
'''

## Usage
In order to use this program for yourself you will need a Spotify Premium account and proper app registration with you Spotify account to use.  A Client ID, Client Secret, and Redirect URI will be established through registration, which should be passed as environment variables into your implementation.

The scheduler executes this app at 21:00 utc, or 5:00pm ET, which is right when D'jais itself will be blasting Calling on the dance floor.