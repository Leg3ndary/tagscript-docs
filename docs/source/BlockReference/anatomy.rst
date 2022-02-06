Anatomy of Blocks
=================

When we refer to blocks we mean anything that contains both an opening ``{`` and a closing ``}``.

.. warning::
    
    Carl will always evaluate brackets so because of this behaviour, you may not have any ``{`` or ``}`` in any block.

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

.. warning::

    You also may not have any ``(`` or ``)`` in parameters.

Payloads
~~~~~~~~

Payloads will also be defined after the command name using a ``:``, unless parameters were added, in that case, it will go straight after parameters instead. Payloads are the text that we want to alter/use.

.. ansi-block::

    [1;31m{[1;37mblock[1;34m:[1;37mPAYLOAD[1;31m}[1;37m
    [1;31m{[1;37mblock[1;34m([1;37mPARAMETERS[1;34m)[1;34m:[1;37mPAYLOAD[1;31m}[1;37m

.. note::

    Paylods unlike parameters and blocks may contain ``:``, note when working with conditional blocks such as if, or, or and, you may not be able to use ``|`` as it can break the else condition

Examples
--------

.. ansi-block::
    
    The blocks parameter in this case is "avatar"
    [1;31m{[1;32muser[1;34m([1;35mavatar[1;34m)[1;31m}[1;37m

    The blocks payload in this case is "lock server"
    [1;31m{[1;32mcommand[1;34m:[1;37mlock server[1;31m}[1;37m

    The blocks parameter here is "tagscript"[1;33m,[1;37m while the payload is "cool"  
    [1;31m{[1;32mlet[1;34m([1;37mtagscript[1;34m)[1;34m:[1;37mcool[1;31m}[1;37m

.. important::

    It's strongly advised that you familiarize yourself with tags basic anatomy to avoid common errors, this will also later be essential to understand more advanced concepts such as blanks and switches

.. raw:: html

    |metatags|