#!/usr/bin/env python3

# import sys
# sys.stderr.write("Log this to the console")
# sys.stderr.write("User Current Version:-" + sys.version)

from lib import iterm2


async def get_tabs(connection):
    app = await iterm2.async_get_app(connection)
    sessions = []
    for window in app.terminal_windows:
        for tab in window.tabs:
            for session in tab.sessions:
                sessions.append(session)

    names = [o.name.replace('\\', '') for o in sessions]
    print("\n".join(names))


iterm2.run_until_complete(get_tabs)
