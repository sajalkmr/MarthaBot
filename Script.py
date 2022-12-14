class script(object):
    START_TXT = """ğğğ¥ğ¥ğ¨ {},
ğ'ğ¦ <a href=https://t.me/{}>{}</a>, ağ§ğ ğ ğğğ§ ğ©ğ«ğ¨ğ¯ğ¢ğğ ğ²ğ¨ğ® ğğ¨ğ¯ğ¢ğğ¬, ğğ¡ğ¨ğ°ğ¬ & ğğ§ğ¢ğ¦ğ. ğğ®ğ¬ğ­ ğğğ ğ¦ğ ğ­ğ¨ ğ²ğ¨ğ®ğ« ğ ğ«ğ¨ğ®ğ© ğğ¬ ğğğ¦ğ¢ğ§ ğğ§ğ ğ¬ğğ :)"""
    HELP_TXT = """ğğğ² {}
ğğğ«ğ ğ¢ğ¬ ğ­ğ¡ğ ğ¡ğğ¥ğ© ğğ¨ğ« ğ¦ğ² ğğ¨ğ¦ğ¦ğğ§ğğ¬."""
    ABOUT_TXT = """â¯ ğ¼ğ ğ½ğ°ğ¼ğ´: {}
â¯ ğ²ğğ´ğ°ğğ¾ğ: <a href=https://t.me/sajalkmr>Sajal</a>
â¯ ğ»ğ¸ğ±ğğ°ğğ: ğ¿ğğğ¾ğ¶ğğ°ğ¼
â¯ ğ»ğ°ğ½ğ¶ğğ°ğ¶ğ´: ğ¿ğğğ·ğ¾ğ½ ğ¹
â¯ ğ³ğ°ğğ° ğ±ğ°ğğ´: ğ¼ğ¾ğ½ğ¶ğ¾ ğ³ğ±
â¯ ğ±ğ¾ğ ğğ´ğğğ´ğ: ğ·ğ´ğğ¾ğºğ
â¯ ğ±ğğ¸ğ»ğ³ ğğğ°ğğğ: v1.0.1 [ ğ±ğ´ğğ° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is an open source project. 
- Source code: <a href=https://github.com/sajalkmr/MarthaBot>GitHub</a>

<b>Owner:</b>
- Sajal : <a href=https://github.com/sajalkmr>GitHub</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Martha will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Martha should have admin privilege.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Martha Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Martha supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/sajalkmr)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of Martha bot

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ğğ¾ğğ°ğ» ğµğ¸ğ»ğ´ğ: <code>{}</code>
â ğğ¾ğğ°ğ» ğğğ´ğğ: <code>{}</code>
â ğğ¾ğğ°ğ» ğ²ğ·ğ°ğğ: <code>{}</code>
â ğğğ´ğ³ ğğğ¾ğğ°ğ¶ğ´: <code>{}</code> ğ¼ğğ±
â ğµğğ´ğ´ ğğğ¾ğğ°ğ¶ğ´: <code>{}</code> ğ¼ğğ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
