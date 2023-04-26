#!/usr/bin/env python3


import sys
sys.stderr.write("Log this to the console")
sys.stderr.write("User Current Version:-" + sys.version)

from lib import iterm2


async def switch_to_tab(connection):
    app = await iterm2.async_get_app(connection)

iterm2.run_until_complete(switch_to_tab)
