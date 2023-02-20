#!/usr/bin/env python3

from lib import iterm2


async def main(connection):
    # Your code goes here. Here's a bit of example code that adds a tab to the current window:
    app = await iterm2.async_get_app(connection)
    sessions = []
    for window in app.terminal_windows:
        for tab in window.tabs:
            for session in tab.sessions:
                sessions.append(session)

    names = [o.name for o in sessions]
    print("\n".join(names))


iterm2.run_until_complete(main)
