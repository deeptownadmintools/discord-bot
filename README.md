# Discord bot
[![Build Status](https://www.travis-ci.org/deeptownadmintools/discord-bot.svg?branch=master)](https://www.travis-ci.org/deeptownadmintools/discord-bot)

#### Website: [dtat.hampl.space](http://dtat.hampl.space)
#### Bot: [invite](https://discordapp.com/oauth2/authorize?client_id=557340294971129856&permissions=2048&scope=bot)
#### API: [Postman](https://documenter.getpostman.com/view/5414817/S1LsXq6g)
#### Suport: [paypal.me](https://www.paypal.me/dtatdonate)

## Running the bot
1) To run the server, you will need url to a running [main server](https://github.com/deeptownadmintools/main-server). You can either host it yourself, or connect to the one hosted at [dtat.hampl.space](http://dtat.hampl.space/).
1) Create a [virtual environment](https://docs.python.org/3/library/venv.html)  with Python 3.6 (discord.py doesn't support v3.7)
1) Enter into virtual environment
1) Install requirements `pip install -e .`
1) Set up a `conf.py` file by copying the `conf_example.py` file and insert your bot token. You can get your token by creating a [discord app](https://discordapp.com/developers/applications/), and making it into a bot user.
1) Within the `conf.py` file set propper url to access the main server or its proxy.
1) You are now all set and you cna start the bot with `python dtat_discord.py`

## Contributing
1) If you want to contribute to the main repository please ensure, that your code is following the PEP8 convention. You can do that with the use of flake8 and autopep8, which you can install using `pip install -r dev-requirements.txt`, after activating your virtual environment.

## Bugs & Improvements
If you have found a bug, or you have an idea for new feature please create an issue here on github. You can also contact me using email: [dtat@hampl.space](mailto:dtat@hampl.space)

## Documentation
1) To generate documentation you will need to install requirements by `pip install -e .` and `pip install sphinx`.
1) Move into the `docs` directory and use `make html`
1) Your documentation is now generated in the `docs/build/html` directory
