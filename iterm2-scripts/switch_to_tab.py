#!/usr/bin/env python3

import sys
from lib import iterm2

tab_name = str(sys.argv[1])


async def switch_to_tab(connection):
    app = await iterm2.async_get_app(connection)

    for window in app.terminal_windows:
        for tab in window.tabs:
            for session in tab.sessions:
                if session.name.replace('\\', '') == tab_name:
                    # sys.stderr.write('SUCCESS')
                    await app.async_activate()
                    await session.async_activate()
                    break


iterm2.run_until_complete(switch_to_tab)
