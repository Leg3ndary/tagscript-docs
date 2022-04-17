Embed
=====

.. tagscript::

    {embed(EMBED PARAMETER):VALUE}

    {embed(title):Embed Title}
    {embed(timestamp):now}

Embed blocks are quite simple, they simply change the value in the embed sent via the embed builder.\

.. attention::

    You **MUST** have a value in the embed builder, anywhere, if the embed builder is empty, the tag will not send the embed.

+------------------+-----------------------------------------------------------------------+
| EMBED PARAMETER  | Output                                                                |
+==================+=======================================================================+
| title            | Sets the embed title                                                  |
+------------------+-----------------------------------------------------------------------+
| url              | Sets the embed url for the title                                      |
+------------------+-----------------------------------------------------------------------+
| description      | Sets the embeds description                                           |
+------------------+-----------------------------------------------------------------------+
| color            | Sets the embeds hex color, must include #                             |
+------------------+-----------------------------------------------------------------------+
| timestamp        | Sets the embeds timestamp, the only possible payload for this is now. |
+------------------+-----------------------------------------------------------------------+

.. raw:: html

    <meta property="og:title" content="Embed Blocks" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Block Reference">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Embed blocks and usage" />
    <meta name="theme-color" content="#F62658">