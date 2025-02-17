# Discord Meme Bot

This is a Discord bot that fetches and shares memes via API integration.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/discord_meme_bot.git
   cd discord_meme_bot
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Discord token:
   ```plaintext
   DISCORD_TOKEN=your_discord_token_here
   ```

5. Run the bot:
   ```sh
   python bot.py
   ```

## Usage

- `$meme`: Fetches a random meme from the meme API and shares it in the channel.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.