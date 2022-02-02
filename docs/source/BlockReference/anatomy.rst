Anatomy of Blocks
=================

When we refer to blocks we mean anything that contains both an opening ``{`` and a closing ``}``.

.. warning::
    
    Carl will always evaluate brackets so because of this behaviour, you may not have any ``{`` or ``}`` in any block.

Some examples include

.. code:: css

    {user}
    {command}
    {let}

In addition blocks may have parameters and or a payload.

Parameters will be defined straight after the block name ``{block(PARAMETERS)}``

.. warning::

    You also may not have any ``(`` or ``)`` in parameters.

Payloads will also be defined after the command name using a ``:``, unless parameters were added, in that case, it will go straight after parameters instead

``{block:PAYLOAD}``
``{block(PARAMETERS):PAYLOAD}``

.. note::

    Paylods unlike parameters and blocks may contain ``:``, note when working with conditional blocks such as if, or, or and, you may not be able to use ``|`` as it can break the else condition

.. code:: css
    
    // The blocks parameter in this case is "avatar"
    {user(avatar)}

    // The blocks payload in this case is "lock server"
    {command:lock server}

    // The blocks parameter here is "tagscript", while the payload is "cool"  
    {let(tagscript):cool}

.. important::

    It's strongly advised that you familiarize yourself with tags basic anatomy to avoid common errors, this will also later be essential to understand more advanced concepts such as blanks and switches