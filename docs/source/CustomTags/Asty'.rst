USERNAME#DISCRIMINATOR
======================

MAKE SURE TO ADD THIS TO THE index.rst FILE, LOOK FOR toctree AND CustomTags/TEMPLATE

.. contents:: Table of Tags

The Best Embed Maker Command
----------------------------

Have you ever dreamt of creating an Embed Message with images, a footer, a custom side color... easily with just a command?

As you may already know, Carl-bot has the embed command that limits you to only a title, a description and a side color, and the ``cembed`` command that requires you to know about what ``JSON`` even is (which is not the majority, let's face it), and is a pain to use on a regular basis (or even once to be honest).

This is why out of frustration and as a huge QoL (Quality of Life) improvement for you all, I built this ``buildembed`` custom command (``be`` for short), which is very easy and convenient to use, while being powerful!

**Features**

- Each field name has Substring Matching, meaning you can for example type t for title, desc for description, c or col for color and it will still recognize it!

- You can specify any field in the order of your choice! Unlike other embed commands, if you want to specify a footer, then a thumbnail, then a title, you can!

- For the color field, you can specify either a color name, a hexadecimal code (like #eeaaee), or even self for your own color.

- Custom-made blocks to use in some fields, such as user {avatar} and server {icon} in image fields, {server} and {channel} in text fields, and {channel(mention)} in the Description field.

- Even if you don't have Nitro, ability to use custom emojis from other servers, by using <emoji (literally) followed by the emoji ID and >.


**Usage**

.. tagscript::

    !be fieldName:Content|fieldName:Content|fieldName:Content...

`Available Fields <https://i.imgur.com/uTQ7q0i.png>`_ and `Colors <https://i.imgur.com/XX5NWSI.png>`_

.. dropdown:: Source Code

    .. tagscript::

        {=(COMMENT):User Settings}
        {=(prefix):!}
        {=(tagName):buildembed|be}

        {=(offsetFromUTC):0}

        {=(example):{prefix}{tagName} title:My title|desc:My description|thumb:https://i.imgur.com/0l0ZBCm.png|footer:My footer|color:blurple}

        {=(defaultColor):2f3136}
        {=(defaultFooter):{prefix}{tagName} title:My title|desc:My description|color:red}
        {=(defaultFooter):{example}}

        {=(COMMENT):Only the roles specified in there (separated by a comma) will be able to use that command. Leave empty if you don't mind.}
        {=(requiredRoles):}
        {=(COMMENT):The error message to output to the user when they don't have the required role. Leaving it empty will react to the user's message with the ⚠️ emoji, and leaving a space " " character won't return an error message at all}
        {=(requiredRolesErrorMessage):}


        {=(COMMENT):Adding or subtracting (depending on if the offset is positive or negative) the offset from UTC specified above to the current unix time.}
        {=(unixTimezone):{m:trunc({unix}+({offsetFromUTC}*3600))}}

        {=(defaultTime):{strf({unixTimezone}):%FT%T.000Z}}

        {=(delimiter):|}

        {=(r):replace}
        {=(i):index}
        {=(l):lower}
        {=(j):join}
        {=(ct):contains}
        {=(fb):None}
        {=(del):{delimiter}}
        {=(pl):%&$}
        {=(uav):{user(avatar)}}
        {=(sic):{server(icon)}}

        {=(COMMENT):Curly brace snippet}
        {=( ):{ }}
        {=(b):{ (1)}}
        {=(d):{ (2)}}

        {=(emojiPrefix):<emoji}

        {=(isAChannelSpecified):{in(true true):{in(<#):{1}} {in(>):{1}}}}
        {=(channelToSend):{{r}(false,{channel(id)}):{{r}(true,{1}):{isAChannelSpecified}}}}


        {=(COMMENT):Separating arguments into their own list variables. Replaces the delimiter with ~ in the process.}
        {=(sanitizedArgs):{{r}({emojiPrefix},<:emoji:):{{r}(",\"):{args}}}}
        {=(argumentToParse):{{if({isAChannelSpecified}==true):sanitizedArgs(2+)|sanitizedArgs}}}
        {=(jargs):{{r}({del},~):!~{argumentToParse}}}
        {=(a1):{list(1):{jargs}}}
        {=(a2):{list(2):{jargs}}}
        {=(a3):{list(3):{jargs}}}
        {=(a4):{list(4):{jargs}}}
        {=(a5):{list(5):{jargs}}}
        {=(a6):{list(6):{jargs}}}
        {=(a7):{list(7):{jargs}}}
        {=(a8):{list(8):{jargs}}}
        {=(a9):{list(9):{jargs}}}
        {=(a10):{list(10):{jargs}}}
        {=(a11):{list(11):{jargs}}}
        {=(a12):{list(12):{jargs}}}

        {=(fieldsName):image title titleurl name color nameicon nameurl description thumbnail footer footericon timestamp {fb} !}

        {=(COMMENT):Processes a substring matching on the keyword/field name of every argument up to the 12th and returns it.}
        {=(COMMENT):Raw argument word, substring matched word, and then word content}
        {=(w1):{{l}:{a1(1)::}}}
        {=(word1):{fieldsName({{i}({w1}):{{r}({w1},. {w1} .):{fieldsName}}})}}
        {=(content1):{a1(2+)::}}

        {=(w2):{{l}:{a2(1)::}}}
        {=(word2):{fieldsName({{i}({w2}):{{r}({w2},. {w2} .):{fieldsName}}})}}
        {=(content2):{a2(2+)::}}

        {=(w3):{{l}:{a3(1)::}}}
        {=(word3):{fieldsName({{i}({w3}):{{r}({w3},. {w3} .):{fieldsName}}})}}
        {=(content3):{a3(2+)::}}

        {=(w4):{{l}:{a4(1)::}}}
        {=(word4):{fieldsName({{i}({w4}):{{r}({w4},. {w4} .):{fieldsName}}})}}
        {=(content4):{a4(2+)::}}

        {=(w5):{{l}:{a5(1)::}}}
        {=(word5):{fieldsName({{i}({w5}):{{r}({w5},. {w5} .):{fieldsName}}})}}
        {=(content5):{a5(2+)::}}

        {=(w6):{{l}:{a6(1)::}}}
        {=(word6):{fieldsName({{i}({w6}):{{r}({w6},. {w6} .):{fieldsName}}})}}
        {=(content6):{a6(2+)::}}

        {=(w7):{{l}:{a7(1)::}}}
        {=(word7):{fieldsName({{i}({w7}):{{r}({w7},. {w7} .):{fieldsName}}})}}
        {=(content7):{a7(2+)::}}

        {=(w8):{{l}:{a8(1)::}}}
        {=(word8):{fieldsName({{i}({w8}):{{r}({w8},. {w8} .):{fieldsName}}})}}
        {=(content8):{a8(2+)::}}

        {=(w9):{{l}:{a9(1)::}}}
        {=(word9):{fieldsName({{i}({w9}):{{r}({w9},. {w9} .):{fieldsName}}})}}
        {=(content9):{a9(2+)::}}

        {=(w10):{{l}:{a10(1)::}}}
        {=(word10):{fieldsName({{i}({w10}):{{r}({w10},. {w10} .):{fieldsName}}})}}
        {=(content10):{a10(2+)::}}

        {=(w11):{{l}:{a11(1)::}}}
        {=(word11):{fieldsName({{i}({w11}):{{r}({w11},. {w11} .):{fieldsName}}})}}
        {=(content11):{a11(2+)::}}

        {=(w12):{{l}:{a12(1)::}}}
        {=(word12):{fieldsName({{i}({w12}):{{r}({w12},. {w12} .):{fieldsName}}})}}
        {=(content12):{a12(2+)::}}

        {=(COMMENT):Fields variables from input. This is where we call our default values as their content if any.}
        {=(COMMENT):Order of the variables assignments in the same order as the embed builder.}

        {=(f.name):}
        {=(f.nameicon):}
        {=(f.nameurl):}

        {=(f.title):}
        {=(f.titleurl):}

        {=(f.description):}

        {=(f.image):}
        {=(f.thumbnail):}

        {=(f.footer):}
        {=(f.footericon):}

        {=(f.timestamp):}

        {=(f.color):{defaultColor}}

        {=(f.{word1}):{content1}}
        {=(f.{word2}):{content2}}
        {=(f.{word3}):{content3}}
        {=(f.{word4}):{content4}}
        {=(f.{word5}):{content5}}
        {=(f.{word6}):{content6}}
        {=(f.{word7}):{content7}}
        {=(f.{word8}):{content8}}
        {=(f.{word9}):{content9}}
        {=(f.{word10}):{content10}}
        {=(f.{word11}):{content11}}
        {=(f.{word12}):{content12}}

        {=(COMMENT):Allowing the word "now" to be used for the "timestamp" field.}
        {=(f.timestamp):{if({{l}:{f.timestamp}}==now):{{r}(now,{defaultTime}):{{l}:{f.timestamp}}}}}

        {=(COMMENT):Although I'm allowing "self" and other keywords for user color, this is allowing the custom user color TagScript block to work beforehand.}
        {=(f.color):{{r}({b}user(color){d},{user(color)}):{{j}():{f.color}}}}

        {=(COMMENT):Allowing custom blocks like user avatar and server icon to be used in image fields as arguments.}
        {=(f.image):{{r}({b}icon{d},{sic}):{{r}({b}server(icon){d},{b}icon{d}):{{r}({b}avatar{d},{uav}):{{r}({b}user(avatar){d},{b}avatar{d}):{f.image}}}}}}

        {=(f.nameicon):{{r}({b}icon{d},{sic}):{{r}({b}server(icon){d},{b}icon{d}):{{r}({b}avatar{d},{uav}):{{r}({b}user(avatar){d},{b}avatar{d}):{f.nameicon}}}}}}
        {=(f.nicon):{{r}({b}icon{d},{sic}):{{r}({b}server(icon){d},{b}icon{d}):{{r}({b}avatar{d},{uav}):{{r}({b}user(avatar){d},{b}avatar{d}):{f.nico}}}}}}

        {=(f.thumbnail):{{r}({b}icon{d},{sic}):{{r}({b}server(icon){d},{b}icon{d}):{{r}({b}avatar{d},{uav}):{{r}({b}user(avatar){d},{b}avatar{d}):{f.thumbnail}}}}}}

        {=(f.footericon):{{r}({b}icon{d},{sic}):{{r}({b}server(icon){d},{b}icon{d}):{{r}({b}avatar{d},{uav}):{{r}({b}user(avatar){d},{b}avatar{d}):{f.footericon}}}}}}

        {=(COMMENT):Allowing custom blocks in text fields.}
        {=(f.title):{{r}({b}channel{d},{channel}):{{r}({b}server{d},{server}):{{r}({b}user{d},{user}):{f.title}}}}}
        {=(f.name):{{r}({b}channel{d},{channel}):{{r}({b}server{d},{server}):{{r}({b}user{d},{user}):{f.name}}}}}
        {=(f.footer):{{r}({b}channel{d},{channel}):{{r}({b}server{d},{server}):{{r}({b}user{d},{user}):{f.footer}}}}}
        {=(f.description):{{r}({b}channel(mention){d},{channel(mention)}):{{r}({b}channel{d},{channel}):{{r}({b}server{d},{server}):{{r}({b}mention{d},{user(mention)}):{{r}({b}user(mention){d},{b}mention{d}):{{r}({b}user{d},{user}):{f.description}}}}}}}}

        {=(COMMENT):Spaces out the color, then removes the first and last added space}
        {=(sepColor):{{r}(, ):{f.color}}}
        {=(sepColor):{sepColor(2+)}}
        {=(sepColor):{sepColor(+-1)}}
        {=(COMMENT):Sanitize our color to only keep our first 6 characters of it, remove the # sign if any and make every letter uppercase}
        {=(sanitizedColor):{{r}(#,):{lower:{{j}():{sepColor}}}}}

        {=(COMMENT):Dictionary of color names, returned as hex. https://htmlcolorcodes.com/color-names/}
        {=(cl.{f.color}):{sanitizedColor(+6)}}
        {=(cl.white):FFFFFF}
        {=(cl.silver):C0C0C0}
        {=(cl.gray):808080}
        {=(cl.grey):{cl.gray}}
        {=(cl.slategray):708090}
        {=(cl.slategrey):{cl.slategray}}
        {=(cl.black):000000}
        {=(cl.red):FF0000}
        {=(cl.yellow):FFFF00}
        {=(cl.lime):00FF00}
        {=(cl.green):008000}
        {=(cl.cyan):00FFFF}
        {=(cl.blue):0000FF}
        {=(cl.navy):000080}
        {=(cl.purple):800080}
        {=(cl.salmon):FA8072}
        {=(cl.pink):FFC0CB}
        {=(cl.coral):FF7F50}
        {=(cl.orange):FFA500}
        {=(cl.gold):FFD700}
        {=(cl.magenta):FF00FF}
        {=(cl.violet):EE82EE}
        {=(cl.indigo):4B0082}
        {=(cl.slateblue):6A5ACD}
        {=(cl.midnightblue):191970}
        {=(cl.wheat):F5DEB3}
        {=(cl.chocolate):F5DEB3}

        {=(cl.discord):2F3136}
        {=(cl.embed):{cl.discord}}
        {=(cl.blurple):7289DA}

        {=(cl.self):{user(color)}}
        {=(cl.myself):{cl.self}}
        {=(cl.me):{cl.self}}

        {=(finalHexColor):{upper:{cl.{lower:{{j}():{f.color}}}}}}

        {=(COMMENT):Spacing out our hexadecimal code}
        {=(spacedHex):{{r}(F,15):{{r}(E,14):{{r}(D,13):{{r}(C,12):{{r}(B,11):{{r}(A,10):{{r}(, ):{finalHexColor}}}}}}}}}
        {=(spacedHex):{spacedHex(2+)}}
        {=(spacedHex):{{j}(~):{spacedHex(+-1)}}}

        {=(COMMENT):Hex to decimal part}
        {=(finalDecimalColor):{m:trunc({{j}():{spacedHex(0):~}*16^0 + {spacedHex(-1):~}*16^1 + {spacedHex(-2):~}*16^2 + {spacedHex(-3):~}*16^3 + {spacedHex(-4):~}*16^4 + {spacedHex(-5):~}*16^5)}}}

        {=(finalJSON):{ "url":"{f.titleurl}",
            "title": "{f.title}",
            "description": "{f.description}",
            "thumbnail": {
                "url": "{f.thumbnail}"
                },
            "image": {
                "url": "{f.image}"
                },
            "author": {
                "name":"{f.name}",
                "url": "{f.nameurl}",
                "icon_url": "{f.nameicon}"
                },
            "color": {finalDecimalColor},
            "footer": {
                "icon_url": "{f.footericon}",
                "text": "{f.footer}"
                },
            "timestamp": "{f.timestamp}"
                }}

        {=(allFields):{{j}():{{r}({fb},):{word1} {word2} {word3} {word4} {word5} {word6} {word7} {word8} {word9} {word10} {word11} {word12}}}}

        {=(areAllFieldsEmpty):{{ct}({pl}):{allFields}{pl}}}
        {=(isNoArg):{{ct}({pl}):{a1}{pl}}}

        {=(errJSON):{ "description": "No field detected.\nExample:
            `{example}`",
            "color": {finalDecimalColor}
        }
        }

        {=(errJSON):{ "fields": [
            { "name": 
                "Features","value":"• **Substring Matching** on each field name (`t` works for `title`, `desc` for `description`, etc.)\n• Fields names can all be filled and in **any order** of your choice!\n• Built-in **error messages**, to let you know what's wrong and when.\n• Ability to specify a color name, hexadecimal color, or even `self` for your own color.\n• **Custom-made blocks** to use in some fields, like user `{avatar}` and server `{icon}` in image fields, `{server}` and `{channel}` in text fields, and `{channel(mention)}` in the Description field.\n• Even for non-Nitro users, ability to use **custom emojis** **from other servers**, by using `<emoji` followed by the **emoji ID** and `>`. For example, `<emoji803680930841362442>` would display <:TagScript:803680930841362442>.\n","inline":false
            },
            { "name":
                    "Usage",
                "value":
                    "`!be fieldName:Content|fieldName:Content`\n```yaml\n!be t:My title|d:My description|thumb:https://i.imgur.com/0l0ZBCm.png|image:https://i.imgur.com/0l0ZBCm.png|f:My footer|color:blurple|time:now\n```",
                "inline":
                    false
            }],
            "title":
                "Build A Custom Embed",
            "description":
                "Forget about the built-in `!embed` and `!cembed` commands, that are not customizable nor very user friendly, as they require specific syntax, and the latter a minimum knowledge of what JSON even is, which is not the average person.",
            "image":{
                "url":
                    "https://i.imgur.com/SlCjHKv.png"
                },
                "color":3092790,
                "footer": {
                    "text":"Custom command made with ♥ for TagScript by Asty'#8926"
                }
            }
        }

        {=(JSONs):errJSON finalJSON}
        {=(shouldErr):{in(true):{areAllFieldsEmpty} {isNoArg}}}

        {=(JSONIdx):{{i}(true):! {shouldErr} true}}

        {=(JSONToSend):{{JSONs({JSONIdx})}}}

        {=(debug):__Debug:__
        jargs: {jargs}

        1: {w1} `{word1}` {content1}
        2: {w2} `{word2}` {content2}
        3: {w3} `{word3}` {content3}
        4: {w4} `{word4}` {content4}
        5: {w5} `{word5}` {content5}
        6: {w6} `{word6}` {content6}
        7: {w7} `{word7}` {content7}
        8: {w8} `{word8}` {content8}
        9: {w9} `{word9}` {content9}
        10: {w10} `{word10}` {content10}
        11: {w11} `{word11}` {content11}
        12: {w12} `{word12}` {content12}

        f.image: {f.image}
        f.title: {f.name}
        f.titleurl: {f.name}
        f.name: {f.name}
        f.nameicon: {f.nameicon}
        f.nameurl: {f.nameurl}

        **Color**
        f.color: {f.color} - sepColor: {sepColor} - sanitizedColor: {sanitizedColor}
        spacedHex: `{spacedHex}`
        finalHexColor: `{finalHexColor}`
        finalDecimalColor: `{finalDecimalColor}`

        f.description: {f.description}
        f.thumbnail: {f.thumbnail}
        f.footer: {f.footer}
        f.footericon: {f.footericon}

        f.timestamp: {f.timestamp}
        }

        {=(testing):Example:```css
        {example}```
        FINAL JSON:```json
        {finalJSON}
        ```}

        {=(debug2):__Debug 2:__
        areAllFieldsEmpty: {areAllFieldsEmpty}
        isNoArg: {isNoArg}

        JSONToSend:```json
        {JSONToSend}
        ```
        }
        {c:cembed {channelToSend} {JSONToSend}}
        {override}
        {require({requiredRolesErrorMessage} ):{requiredRoles}}
    
.. link-button:: https://carl.gg/t/1157946

    :type: url
    :text: Tag Import
    :classes: btn-outline-primary btn-block

.. raw:: html

    <meta property="og:title" content="USERNAME#DISCRIMINATOR's Tags" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:site_name" content="Custom Tags">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Find USERNAME#DISCRIMINATOR's tags here!" />
    <meta name="theme-color" content="#2980B9">