import asyncio
import itertools
from aiogram import types

async def animate_loading(message: types.Message, text="Loading", animation_timeout=1, stop_event: asyncio.Event = None):
    """
    Animates a loading message by adding dots.
    
    Args:
        message: Discord Message object to edit
        text: Base text to show (default: "Loading")
        animation_timeout: Time between animations in seconds (default: 0.5)
    """
    dots = [" ▒▒▒▒▒▒▒▒▒▒0%", " █▒▒▒▒▒▒▒▒▒10%", " ███▒▒▒▒▒▒▒30%", " █████▒▒▒▒▒50%", " ███████▒▒▒70%", " █████████▒90%", "██████████100%"]
    for dot in itertools.cycle(dots):
        if stop_event and stop_event.is_set():
            break
        try:
            await message.edit_text(f"{text}{dot}")
            await asyncio.sleep(animation_timeout)
        except:
            break
    
    try:
        await message.edit_text(f"{text} done!")
    except:
        pass