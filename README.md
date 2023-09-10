This is a Telegram bot written in Python using the aiogram library. The bot provides information about discounted knives and gloves. It collects data from a source and displays it to the users.
Prerequisites

    1. Python 3.7 or higher
    2. aiogram library
    3. config.py file containing the bot token

Installation

  1. Clone the repository
          git clone https://github.com/your_username/your_repository.git

  2. Install the required dependencies:
          pip install -r requirements.txt
  
  3. Create a config.py file in the project directory and add your bot token:
          TOKEN = 'your_bot_token'

Usage
  -Run the bot:
          python main.py

-Start the bot in Telegram by sending the /start command.
  -Choose a category by clicking on one of the provided buttons.
  -The bot will collect data and display it to you. Each item will include a link, discount percentage, and price.
