Anatomy of Blocks
=================

When we refer to blocks we mean anything that contains both an opening ``{`` and a closing ``}``.

.. warning::
    
    Carl-bot will always evaluate brackets so because of this behaviour, you may not have  ``{`` or ``}`` in any block.

    There is no way to bypass this while writing your code.

Block Names
-----------

Block names are what's inside the curly brackets, these will always be the first thing after ``{`` and is mandatory for every block.

.. note::

    An exception is made for variables in which you can literally define variables to be "blank" ``{=():}``, if you don't understand this, don't worry, it's not important right now.

Some examples include:

.. ansi-block::

    [1;31m{[1;32muser[1;31m}[1;37m
    [1;31m{[1;32mcommand[1;31m}[1;37m
    [1;31m{[1;32mlet[1;31m}[1;37m

The name of the block will determine how the parameters and payload are evaluated.

Parameters and Payloads
-----------------------

Parameters
~~~~~~~~~~

Parameters will be defined straight after the block name ``{block(PARAMETERS)}``, parameters will usually let us alter the payload depending on what we put in it.

.. ansi-block::

    [1;31m{[1;32muser[1;34m([1;37mPARAMETERS[1;34m)[1;31m}[1;37m
    [1;31m{[1;37mcommand[1;34m([1;37mPARAMETERS[1;34m)[1;31m}[1;37m
    [1;31m{[1;32mlet[1;34m([1;37mPARAMETERS[1;34m)[1;31m}[1;37m

.. warning::

    You also may not have any ``(`` or ``)`` in parameters.

Payloads
~~~~~~~~

Payloads will also be defined after the command name using a ``:``, unless parameters were added, in that case, it will go straight after parameters instead. Payloads are the text that we want to alter/use.

.. ansi-block::

    [1;31m{[1;32muser[1;34m([1;37mPARAMETERS[1;34m)[1;34m:[1;37mPAYLOAD[1;31m}[1;37m
    [1;31m{[1;37mcommand[1;34m:[1;37mPAYLOAD[1;31m}[1;37m

.. note::

    Payloads may contain ``:``

.. note::

    When working with conditional blocks such as ``if``, ``or``, or ``and``, you may not be able to use vertical pipes ``|``, as it can break the *else* condition.


.. note::

    Remember that payloads and parameters can be optional, meaning all of these are possible with the right blocks.

    .. ansi-block::

        [1;31m{[1;37mblock[1;34m([1;37mPARAMETERS[1;34m)[1;31m}[1;37m
        [1;31m{[1;37mblock[1;34m:[1;37mPAYLOAD[1;31m}[1;37m
        [1;31m{[1;37mblock[1;34m([1;37mPARAMETERS[1;34m)[1;34m:[1;37mPAYLOAD[1;31m}[1;37m

Examples
--------

.. ansi-block::
    
    The blocks' parameter in this case is "avatar"
    [1;31m{[1;32muser[1;34m([1;35mavatar[1;34m)[1;31m}[1;37m

    The blocks' payload in this case is "lock server"
    [1;31m{[1;32mcommand[1;34m:[1;37mlock server[1;31m}[1;37m

    The blocks' parameter here is "tagscript"[1;33m,[1;37m while the payload is "cool"  
    [1;31m{[1;32mlet[1;34m([1;37mtagscript[1;34m)[1;34m:[1;37mcool[1;31m}[1;37m

.. important::

    It's strongly advised that you familiarize yourself with basic anatomy to avoid common errors, this will also later be essential to understand more advanced concepts such as blanks and switches.

.. raw:: html

    <meta property="og:title" content="Tagscript Unofficial Docs" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="By _Leg3ndary#5759">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="The unofficial but better docs for Carl-bots Tagscript, not affiliated with Botlabs or Carl-bot" />
    <meta name="theme-color" content="#9C20BC">
