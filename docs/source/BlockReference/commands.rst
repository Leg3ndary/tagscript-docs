Commands
========

.. caution::

    Want to stop a command block from conditionally running?

    Remember to use blanks ADD LINK HERE PLEASE

.. tagscript::

    {c:Command}
    {cmd:role add _Leg3ndary Red}
    {command:ban Carl-bot Useless bot}

Command blocks execute Carl's commands, it's what allows you to add roles, change nicknames, etc.

.. note::

    Every server is limited to a maximum of **one** command block, an exception is made for premium servers who are allowed up to three.

Payload
-------

.. tagscript::

    {c:COMMAND YOU WANT TO RUN}

.. tip::

    If you want to create an alias for an existing command, it's as simple as creating a tag with the alias as it's name and adding a command block with args

    .. tagscript::

        {c:COMMAND NAME {args}}

        {c:mute {args}}

        {c:ban {args}}

.. warning::

    Tags aren't able to run reactionrole commands nor can they run tag commands, eg tag add, or rr add

.. raw:: html

    <meta property="og:title" content="Tagscript Unofficial Docs" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="By _Leg3ndary#5759">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="The unofficial but better docs for Carl-bots Tagscript, not affiliated with Botlabs or Carl-bot" />
    <meta name="theme-color" content="#9C20BC">