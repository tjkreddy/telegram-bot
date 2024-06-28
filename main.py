import logging
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Application

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
BOT_TOKEN = 'bot tooen'

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the menu data
menu_data = {
    "Monday": {
        "Breakfast": "Scrambled eggs",
        "Lunch": "Grilled chicken salad",
        "Dinner": "Pasta with marinara sauce"
    },
    "Tuesday": {
        "Breakfast": "Oatmeal with fruits",
        "Lunch": "Vegetable stir-fry",
        "Dinner": "Baked salmon with rice"
    },
    "Wednesday": {
        "Breakfast": "Yogurt with granola",
        "Lunch": "Quinoa salad",
        "Dinner": "Steak with mashed potatoes"
    },
    "Thursday": {
        "Breakfast": "Smoothie bowl",
        "Lunch": "Caprese sandwich",
        "Dinner": "Shrimp scampi"
    },
    "Friday": {
        "Breakfast": "Pancakes with syrup",
        "Lunch": "Tomato soup with grilled cheese",
        "Dinner": "Tacos with salsa"
    },
    "Saturday": {
        "Breakfast": "Avocado toast",
        "Lunch": "Caesar salad",
        "Dinner": "Chicken curry with naan"
    },
    "Sunday": {
        "Breakfast": "Bagel with cream cheese",
        "Lunch": "Mushroom risotto",
        "Dinner": "Beef stew"
    }
}

# Command handler for the start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! I am your Menu Bot. Send /menu <day> to get the menu for a specific day.')

# Command handler for the menu command
async def menu(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        await update.message.reply_text('Please provide a day. Example: /menu Monday')
        return

    day = context.args[0].capitalize()
    if day in menu_data:
        day_menu = menu_data[day]
        menu_text = f"Menu for {day}:\n"
        for meal, items in day_menu.items():
            menu_text += f"\n{meal.capitalize()}:\n{items}"
        await update.message.reply_text(menu_text)
    else:
        await update.message.reply_text('Invalid day provided. Please enter a valid day of the week.')

# Main function to set up the bot
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))

    # Start the Bot
    application.run_polling(stop_signals=None)
    logger.info("Bot is starting...")

if __name__ == '__main__':
    main()
