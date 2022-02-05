Commands
========

.. caution::

    Want to stop a command block from conditionally running?

    Remember to use blanks ADD LINK HERE PLEASE

.. ansi-block::

    [1;31m{[1;37mc[1;34m:[1;37mCommand[1;31m}[1;37m
    [1;31m{[1;37mcmd[1;34m:[1;37mrole add _Leg3ndary Red[1;31m}[1;37m
    [1;31m{[1;37mcommand[1;34m:[1;37mban Carl[1;31m-[1;37mbot Useless bot[1;31m}[1;37m

Command blocks execute Carl's commands, it's what allows you to add roles, change nicknames, etc.

.. note::

    Every server is limited to a maximum of **one** command block, an exception is made for premium servers who are allowed up to three.

Payload
-------

.. ansi-block::

    [1;31m{[1;37mc[1;34m:[1;37mCOMMAND YOU WANT TO RUN[1;31m}[1;37m

.. tip::

    If you want to create an alias for an existing command, it's as simple as creating a tag with the alias as it's name and adding a command block with args

    .. ansi-block::

        [1;31m{[1;37mc[1;34m:[1;37mCOMMAND NAME [1;31m{[1;32margs[1;31m}[1;31m}[1;37m

        [1;31m{[1;37mc[1;34m:[1;37mmute [1;31m{[1;32margs[1;31m}[1;31m}[1;37m

        [1;31m{[1;37mc[1;34m:[1;37mban [1;31m{[1;32margs[1;31m}[1;31m}[1;37m

.. warning::

    Tags aren't able to run reactionrole commands nor can they run tag commands, eg tag add, or rr add