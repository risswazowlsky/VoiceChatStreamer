'''
VoiceChatStreamer, An Telegram Bot Project
Copyright (c) 2021 Anjana Madu <https://github.com/AnjanaMadu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
'''

import os, asyncio
from pyrogram import Client, filters
from pytgcalls import GroupCallFactory
from bot import vcusr, CHAT_ID, ADMINS
from bot.plugins.player import group_call, vc_live, music_queue

vc_paused = False
    
@Client.on_message(filters.command("pause", "!"))
async def pause_vc(client, message):
    global vc_paused
    if not message.chat.id == CHAT_ID: return
    if not message.from_user.id in ADMINS: return
    if vc_paused is False:
        await group_call.set_pause(True)
        await message.reply("__🙅 Video Di Jeda__")
        vc_paused = True
    elif vc_paused is True:
        return await message.reply("__🤦 Sudah Di Jeda__")
          
@Client.on_message(filters.command("resume", "!"))
async def resume_vc(client, message):
    global vc_paused
    if not message.chat.id == CHAT_ID: return
    if not message.from_user.id in ADMINS: return
    if vc_paused is True:
        await group_call.set_pause(False)
        await message.reply("__⏺️ VC Resumed__")
        vc_paused = False
    elif vc_paused is False:
        return await message.reply("__⏺️ VC not Paused.__")

@Client.on_message(filters.command("help", "!"))
async def help_vc(client, message):
    text = '''====== MENU MUSIC @Rafens ======
**🎧 Menu Memutar Audio**
- !play __(reply to audio / youtube url / search query)__
- !radio __(radio stream url)__

**🎬 Menu Streaming Video**
- !stream __(reply to video / youtube url / search query)__
- !live __(youtube live stream url)__

**Extra/Tambahan**
- !endvc: Keluar dari VCG/OS.
- !skip: Skip Lagu/Video Yang Di Play.
- !pause: Pause Video/Lagu.
- !resume: Resume Video/Lagu.
- !video: Download Video Atau Mencari Video Dengan Format.
- !audio: Download Lagu Atau Mencari Lagu Dengan Format.'''
    await message.reply(text)
