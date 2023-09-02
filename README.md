# GameEnergyInfraV2 - Development
Just a fork used to implement new features and improve existing ones.

## Breaking changes

Compared to the original repository, this fork has the following *breaking* changes:

- The `Bot.env` file has been renamed to `bot.env` to be consistent with the other files.
- The path to the SSH key is now fixed at `./key.pem` instead of being configurable in the `bot.env` file.
- The E-Mail password is now stored in `bot.env` instead of being hard coded for obvious security reasons.
- The `KEY` variable in `bot.env` has been renamed to `PTERODACTYL_KEY` to make clearer what the key is needed for.
- There are example files for `bot.env` and `config.json` named `bot-example.env` and `config-example.json`
  respectively to show how the files should be structured.

## Coming changes

- Since `activity_levels.py`, `channel_description.py`, parts of `giveaway.py`
  and `fast_command.py` are all just hard coded message templates,
  they will all get merged into a new `/template` command that will allow the user to edit the templates directly
  in Discord.
- The `/giveaway` command will have more arguments to avoid hard coding the giveaway message.