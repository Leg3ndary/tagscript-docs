Home
====

.. attention::

    This is not affiliated in any way with Botlabs or Carl-bot.

.. attention::

    Really would like to thank `readthedocs.org <https://readthedocs.org>`_ for making this possible, thank you!

This is an unofficial guide to Carl-bot's tagscript, started by `_Leg3ndary#5759 <https://discordapp.com/users/360061101477724170/>`_, you may view all contributors :doc:`here. </contributing>`


.. note::
    
    All of this documentation contains custom tagscript syntax highlighting through ansi!

    .. tagscript::

        {=(L1):{lower:{1}}}
        {=(A2+):{replace(|, - ):{args(2+)}}}
        {=(error):You must follow the `afk` command with either `on` or `off`.}
        {=(on):add}
        {=(off):del}
        {=(template):c:ar {{L1}} {user(id)}>{if({L1}==on): {if({list(0):{join(,):{A2+}}}!=):{A2+}|{replace(|, - ):{user}} is afk right now, send them a PM or wait for them to return.}}}
        {=(sel):{if({contains({L1}):on off}==false):error|{template}}}
        {override}{{sel}}

        Raffael#1372's AFK Tag

.. tip::

    If you just want a quick refresher on blocks, this tag will contains everything you need to know: `?tse <block> <https://carl.gg/t/204246>`_

.. note::

    This documentation is still under development.

.. toctree::
    :caption: Info
    :maxdepth: 0
    :hidden:

    info/contributing
    info/credits

.. toctree::
    :caption: Frequently Asked Questions
    :maxdepth: 5
    :hidden:

    FAQ/tag_limits

.. toctree::
    :caption: Getting Started
    :maxdepth: 5
    :hidden:

    GettingStarted/creating_tags

.. toctree::
    :caption: Block Reference
    :maxdepth: 5
    :hidden:

    BlockReference/anatomy
    BlockReference/default
    BlockReference/discord
    BlockReference/meta
    BlockReference/commands
    BlockReference/control
    BlockReference/datastorage
    BlockReference/parsing
    BlockReference/embed
    BlockReference/manipulation

.. toctree::
    :caption: Advanced Concepts
    :maxdepth: 5
    :hidden:

    AdvancedConcepts/tag_saving

.. toctree::
    :caption: Custom Tags
    :maxdepth: 2
    :hidden:

    CustomTags/_Leg3ndary

.. raw:: html

    <meta property="og:title" content="Tagscript Unofficial Docs" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="By _Leg3ndary#5759">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="The unofficial but better docs for Carl-bots Tagscript, not affiliated with Botlabs or Carl-bot" />
    <meta name="theme-color" content="#2980B9">