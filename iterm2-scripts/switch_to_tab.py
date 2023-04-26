#!/usr/bin/env python3

import sys
# sys.stderr.write("Log this to the console")
# sys.stderr.write("User Current Version:-" + sys.version)

from lib import iterm2

sys.stderr.write(str(sys.argv))

async def switch_to_tab(connection):
    app = await iterm2.async_get_app(connection)

    # Foreground the app
    await app.async_activate()

    for window in app.terminal_windows:
        for tab in window.tabs:
            for session in tab.sessions:
                sys.stderr.write(session.name)

iterm2.run_until_complete(switch_to_tab)
