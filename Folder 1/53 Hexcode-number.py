import re


print("true" if re.fullmatch("#[A-F0-9a-f]{6}", input()) is not None else "false")
