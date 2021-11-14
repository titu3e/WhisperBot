from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}

I am the Master of Shadows (like Shadows Of [Sungjinwoo](t.me/Sungjinwooarc). Enjoy Using me ).

You can use me to send Shadow Message to your Subordinate's in groups and channels (even if I'm not there).
Only that Subordinate and you will be able to read the message even though others are in same group. 

To see how to Summon me press 'How to Use' below.

By @Sungjinwooarc
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 Send a Shadow 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 Send a Shadow 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("How to Summon ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/Sungjinwooarc")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/Sungjinwooarc")],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

`@shadow_Whisper_Robot your_message Subordinates_username/id`
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @Sungjinwooarc

Source Code : You Wont get it. Its not public 

Inspired By : My Friends bullying 

Language : Human 😂

Developer : @Sungjinwoo
    """
