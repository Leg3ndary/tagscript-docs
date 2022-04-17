Manipulation
============

Ordinal Abbreviation
~~~~~~~~~~~~~~~~~~~~

.. tagscript::
    
    {ord:INT}

    {ord:1} returns 1st
    {ord:22} returns 22nd
    {ord:37} returns 3th
    {ord:456} returns 456th

The ordinal abbreviation block returns exactly what you'd expect it to, the ordinal abbreviation of the number.

.. note::
    
    If you don't supply a number or the number has commas/decimals, this block will return ``<ord error>``.

Case Blocks
~~~~~~~~~~~

.. tagscript::

    {lower:Whoozard is a Wizard} -> whoozard is a wizard
    {upper:carl-bot best bot} -> CARL-BOT BEST BOT

Case blocks also do exactly what'd you'd expect them too, they either upper or lower what you want, this is often used to make inputs case insensitive.

Text Replacement
~~~~~~~~~~~~~~~~

.. tagscript::

    {join(STRING):TEXT}
    {replace(FIRST STRING,SECOND STRING):TEXT}
    {urlencode(SPACE ENCODING):URL}

    {join(_):Carl-bot is cool} -> Carl-bot_is_cool
    {replace(, ):Carl-bot is cool} -> C a r l - b o t   i s   c o o l
    {replace(l-bot,w-bot):Carl-bot is cool} -> Carw-bot is cool
    {urlencode:Hey there, how are you?} -> Hey%20there%2C%20how%20are%20you%3F
    {urlencode(+):Hey there, how are you?} -> Hey+there%2C+how+are+you%3F

Text replacement blocks also do what you would expect them too.

Join will join the strings spaces with whatever string you provide it with, this means it's the equivalent of ``{replace( ,STRING):TEXT}``.

Replace is similar to join but you separate what you want to replace and what it will be replaced with, with a comma. This can be used to space variables ``{replace(, ):TEXT}``.

Urlencode will encode any text (Usually URLs obviously) into percent form. The only possible value for SPACE ENCODING is ``+``.

.. note::

    Since you must separate what you want to replace with comma, you aren't able to replace commas.

.. raw:: html

    <meta property="og:title" content="Manipulation" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="By _Leg3ndary#5759">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Value manipulation, different from parsing" />
    <meta name="theme-color" content="#F62658">