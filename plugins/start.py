from pyrogram import Client, filters, enums
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from info import ADMINS

# /start command handler
@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    user = message.from_user.first_name or "User"

    await message.reply(
        text=(
            f"👋 Hello, **{user}**!\n\n"
            "I'm an Auto-Delete Bot built for Telegram groups.\n"
            "I automatically delete messages after a configured time.\n\n"
            "🔧 **Steps to get started:**\n"
            "1. Add me to your group.\n"
            "2. Grant me admin rights with delete permission.\n"
            "3. Use `/settime` to set the auto-delete delay.\n\n"
            "Only specific user IDs (set in `ADMINS`) can configure me."
        ),
        parse_mode=enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 Help", callback_data="help")],
            [InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{client.me.username}?startgroup=true")]
        ])
    )

# Callback query handler for inline buttons
@Client.on_callback_query()
async def callback_query_handler(client: Client, callback_query: CallbackQuery):
    data = callback_query.data
    msg = callback_query.message

    if data == "help":
        await callback_query.answer()
        await msg.edit_text(
            text=(
                "📚 **Help Menu**\n\n"
                "`/settime 30s` – Auto-delete messages after 30 seconds\n"
                "`/settime 5m` – Delete after 5 minutes\n"
                "`/settime 1hr` – Delete after 1 hour\n\n"
                "`/deltime` – Show current delete timer in the group\n\n"
                "⚙️ Only admin IDs listed in `ADMINS` can use these commands.\n"
                "Supported formats: `10s`, `2m`, `1hr`"
            ),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )
    elif data == "back":
        await callback_query.answer()
        user = msg.from_user.first_name if msg.from_user else "User"
        await msg.edit_text(
            text=(
                f"👋 Hello, **{user}**!\n\n"
                "I'm an Auto-Delete Bot built for Telegram groups.\n"
                "I automatically delete messages after a configured time.\n\n"
                "🔧 **Steps to get started:**\n"
                "1. Add me to your group.\n"
                "2. Grant me admin rights with delete permission.\n"
                "3. Use `/settime` to set the auto-delete delay.\n\n"
                "Only specific user IDs (set in `ADMINS`) can configure me."
            ),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📚 Help", callback_data="help")],
                [InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{client.me.username}?startgroup=true")]
            ])
        )
