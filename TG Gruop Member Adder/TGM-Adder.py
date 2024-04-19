import telebot

# Set up your Telegram API token and initialize your bot
API_TOKEN = 'YOUR_API_TOKEN_HERE'
bot = telebot.TeleBot(API_TOKEN)

# Set up your source and target group IDs
source_group_id = -1234567890  # Replace with the ID of the source group
target_group_id = -9876543210  # Replace with the ID of the target group

# Define a function to add members from the source group to the target group
def add_members_from_group():
    # Get a list of members from the source group
    source_group_members = bot.get_chat_members(source_group_id)
    
    # Iterate over the members and add them to the target group
    for member in source_group_members:
        try:
            bot.add_chat_member(target_group_id, member.user.id)
        except telebot.apihelper.ApiException as e:
            print(f"Failed to add member {member.user.id}: {e}")

# Call the function to add members from the source group to the target group
add_members_from_group()
