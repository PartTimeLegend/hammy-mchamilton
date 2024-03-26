# Hammy McHamilton Discord Quiz Bot

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

This is a Discord bot written in Python that hosts a quiz game with questions and answers on from the RSGB Amateur Radio Examination questions list. The bot randomly selects questions from a predefined quiz data set and prompts users to answer them within a specified time limit.

![.... --- .-- / -.. --- . ... / .- / -... .- ... - .- .-. -.. --..-- / --- .-. .--. .... .- -. --..-- / ... --- -. / --- ..-. / .- / .-- .... --- .-. . / .- -. -.. / .- / ... -.-. --- - ... -- .- -. --..-- / -.. .-. --- .--. .--. . -.. / .. -. / - .... . / -- .. -.. -.. .-.. . / --- ..-. / .- / ..-. --- .-. --. --- - - . -. / ... .--. --- - / .. -. / - .... . / -.-. .- .-. .. -... -... . .- -. / -... -.-- / .--. .-. --- ...- .. -.. . -. -.-. . --..-- / .. -- .--. --- ...- . .-. .. ... .... . -.. --..-- / .. -. / ... --.- ..- .- .-.. --- .-. / --. .-. --- .-- / ..- .--. / - --- / -... . / .- / .... . .-. --- / .- -. -.. / .- / ... -.-. .... --- .-.. .- .-. ..--..](docs/hammy.jpg?raw=true "Hammy McHamilton")

## Features

- Hosts a quiz game on a Discord server.
- Randomly selects questions from a predefined set.
- Allows users to answer questions within a specified time limit.
- Provides feedback on correct and incorrect answers.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/HamHangOut/hammy-mchamilton.git
   ```

2. Navigate to the project directory:

   ```bash
   cd hammy-mchamilton
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up a Discord bot and obtain its token.

5. Create a `.env` file in the project directory and add your Discord bot token:

   ```plaintext
   TOKEN=your_discord_bot_token
   ```

6. Run the bot:

   ```bash
   python main.py
   ```

## Usage

Once the bot is running and connected to your Discord server, users can start a quiz by sending the `!quiz` command in any text channel where the bot is present.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or feature implementations, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
