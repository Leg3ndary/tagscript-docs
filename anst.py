"""
Copyright (c) 2022 Ben

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Dicts are order of when they're parsed

operators_dict = {
    "==": "☺equal☺",
    "!=": "☺notequal☺",
    ">=": "☺greaterequal☺",
    "<=": "☺lesserequal☺",
    "|": "[0;35m|",
    "+": "[0;31m+",
    "/": "[0;31m/",
    "*": "[0;31m*",
    "~": "[1;33m~",
    ",": "[1;33m,",
    "__": "[0;31__",
    "^": "[0;31^",
    "-": "[0;31-",
}

syntax_dict = {
    "{": "[1;31m{",
    "}": "[1;31m}",
    "(": "[1;34m(",
    ")": "[1;34m)",
    ":": "[1;34m:",
}

blocks_dict = {
    ">": "[0;31m>", # I know these 2 are operators, but so that everything get's parsed correctly they have to be here or another dict.
    "<": "[0;31m<",
    "=": "[1;32m=",
    "var": "[1;32mvar",
    "let": "[1;32mlet",
    "assign": "[1;32massign",
    "user": "[1;32muser",
    "target": "[1;32mtarget",
    "server": "[1;32mserver",
    "channel": "[1;32mchannel",
    "if": "[1;33mif",
    "any": "[1;33many",
    "break": "[1;33mbreak",
    "all": "[1;33mall",
    "and": "[1;33mand",
    "or": "[1;33mor",
    "unix": "[1;32munix",
    "uses": "[1;32m",
    "args": "[1;32m",
    "join": "[1;32m",
    "message": "[1;32m",
    "replace": "[1;32m",
    "contains": "[1;32m",
    "strf": "[1;32m",
    "#": "[1;32m",
    "random": "[1;32m",
    "rand": "[1;32m",
    "urlencode": "[1;32m",
    "td": "[1;32m",
    "index": "[1;32m",
    "list": "[1;32m",
    "cycle": "[1;32m",
    "in": "[1;32m",
    "upper": "[1;32m",
    "lower": "[1;32m",
    "math": "[1;32m", # regular math removed because it breaks everything
    "range": "[1;32m",
    "?": "[1;32m",
    "rangef": "[1;32m",
    "embed": "[1;32m",
}

params_dict = {
    "avatar": "[1;35mavatar",
    "id": "[1;35mid",
    "created_at": "[1;35mcreated_at",
    "joined_at": "[1;35mjoined_at",
    "roleids": "[1;35mroleids",
    "color": "[1;35mcolor",
    "name": "[1;35mname",
    "proper": "[1;35mproper",
    "position": "[1;35mposition",
    "icon": "[1;35micon",
    "owner": "[1;35mowner",
    "randomonline": "[1;35mrandomonline",
    "randomoffline": "[1;35mrandomoffline",
    "members": "[1;35mmembers",
    "bots": "[1;35mbots",
    "humans": "[1;35mhumans",
    "roles": "[1;35mroles",
    "channels": "[1;35mchannels",
    "topic": "[1;35mtopic",
    "slowmode": "[1;35mslowmode",
    "mention": "[1;35mmention",
    "trunc": "[1;35mtrunc",
    "round": "[1;35mround",
    "abs": "[1;35mabs",
    "title": "[1;35mtitle",
    "URL": "[1;35mURL",
    "description": "[1;35mdescription",
    "timestamp": "[1;35mtimestamp",
}

meta_dict = {
    "del": "[1;33mdel",
    "delete": "[1;33mdelete",
    "silence": "[1;33msilence",
    "dm": "[1;33mdm",
    "override": "[1;33moverride",
    "blacklist": "[1;33mblacklist",
    "require": "[1;33mrequire",
    "redirect": "[1;33mredirect",
    "react": "[1;33mreact",
    "reactu": "[1;33mreactu",
}

payload_dict = {
    "true": "[4;36mtrue",
    "false": "[4;36mfalse",
    "now": "[4;36mnow",
}

final_operators_dict = {
    "☺equal☺": "[0;35m==",
    "☺notequal☺": "[0;35m!=",
    "☺greaterequal☺": "[0;35m>=",
    "☺lesserequal☺": "[0;35m<=",
}

strf_flags = {
    # Might add later
    """%a %A %w %d %-d %b %B %m %-m %y %Y %H %-H %I %-I %p %M %-M %S %-S %f %z %Z %j %-j %U %W %c %x %X %u %n %i %s %m %-m %s %-s %z %w"""
}

def gen_tag_ansi(text: str) -> str:
    """Generates some tagscript ansi :)"""

    for key, value in operators_dict.items():
        text = text.replace(key, f"{value}[0;0m") # not using concatenation for speed, im pre sure its supposed to be slower as it creates copies of the string to use
    
    for key, value in syntax_dict.items():
        text = text.replace(key, f"{value}[0;0m")

    for key, value in blocks_dict.items():
        text = text.replace(key, f"{value}[0;0m")

    for key, value in params_dict.items():
        text = text.replace(key, f"{value}[0;0m")

    for key, value in meta_dict.items():
        text = text.replace(key, f"{value}[0;0m")

    for key, value in payload_dict.items():
        text = text.replace(key, f"{value}[0;0m")

    for key, value in final_operators_dict.items():
        text = text.replace(key, f"{value}[0;0m")
    
    return text

# literally just shit tons of replaces lol

code = """{=(L1):{lower:{1}}}
{=(A2+):{replace(|,REPLACETHIS):{args(2+)}}}
{=(error):You must follow the `afk` command with either `on` or `off`.}
{=(on):add}
{=(off):del}
{=(template):c:ar {{L1}} {user(id)}>{if({L1}==on): {if({list(0):{join(,):{A2+}}}!=):{A2+}|{replace(|,REPLACETHIS):{user}} is afk right now, send them a PM or wait for them to return.}}}
{=(sel):{if({contains({L1}):on off}==false):error|{template}}}
{override}{{sel}}"""

if not code:
    code = str(input("Input your tag please: "))



new_code = gen_tag_ansi(code)

with open("output.txt", "w") as text_file:
    text_file.write(new_code)

print(new_code)