import os
import sys
sys.path.append(os.path.join(os.getcwd(),'site-packages'))

import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

info = json.load(open('info.json', 'r'))
formatted_info = json.dumps(info, indent=2)

print(highlight(formatted_info, JsonLexer(), TerminalFormatter()))
print(info["LINE_API_TOKEN"][0]["CHANNEL_ACCESS_TOKEN"])