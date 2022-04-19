Discord Objects
===============

Discord related default variables

User/Target
-----------

.. tagscript::
    
    {user}
    {target}

    {user(name)}
    {target(avatar)}

One of the most used blocks is the target block, it allows you to access other users data.

``user`` is the user who invoked the tag, while ``target`` is the first user that was pinged in the commands arguments. If no one is pinged, ``target`` is equivalent to ``user``.


.. note::

    It's common to check if someone was pinged in the command, to do this you compare user against target

    .. tagscript::

        {if({user(id)}=={target(id)}):You need to ping someone|You pinged {target}}

Parameters/Properties
~~~~~~~~~~~~~~~~~~~~~

Parameters can be specified within parenthesis after the block name: ``{user(PARAMETER)}`` or ``{user(PARAMETER)}``. When used without a parameter (``{user}`` or ``{target}``), the block will output the nickname of the user/target.

+------------+-----------------------------------------------------------------------------------------------------------------------+
| Parameter  |                                                        Output                                                         |
+============+=======================================================================================================================+
| avatar     | A link to the user's avatar                                                                                           |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| icon       | Same as avatar                                                                                                        |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| id         | The user's ID                                                                                                         |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| mention    | @'s/Mentions the user                                                                                                 |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| created_at | Date and time that the account was created in the form of ``yyyy-mm-dd HH:MM:SS``                                     |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| joined_at  | Date and time that the user joined this server in the form of ``yyyy-mm-dd HH:MM:SS``                                 |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| color      | The user's hexadecimal role color with the leading ``#`` included                                                     |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| name       | The user's discord username                                                                                           |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| proper     | The user's username + discriminator/tag, example ``_Leg3ndary#5759``                                                  |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| roleids    | A list of every role (id) the user has from lowest to highest separated by a space                                    |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| position   | The user's position in the role hierarchy, starts with 0 for @everyone and increases by 1 for each role in the server |
+------------+-----------------------------------------------------------------------------------------------------------------------+

Server
------

.. tagscript::

    {server}

    {server(roles)}

Contains details about the server

Parameters
~~~~~~~~~~

When used without a parameter, the block will output the servers name

.. warning::

    Some of these are deprecated.

+--------------------------+------------------------------------------------------------------------------+
|        Parameter         |                                    Output                                    |
+==========================+==============================================================================+
| icon                     | A link to the servers avatar                                                 |
+--------------------------+------------------------------------------------------------------------------+
| id                       | The servers id                                                               |
+--------------------------+------------------------------------------------------------------------------+
| owner                    | The username + discriminator of the owner                                    |
+--------------------------+------------------------------------------------------------------------------+
| random                   | The username + discriminator of a random user                                |
+--------------------------+------------------------------------------------------------------------------+
| randomonline DEPRECATED  | The username + discriminator of a random  online user                        |
+--------------------------+------------------------------------------------------------------------------+
| randomoffline DEPRECATED | The username + discriminator of a random offline user                        |
+--------------------------+------------------------------------------------------------------------------+
| members                  | The number of members in the server                                          |
+--------------------------+------------------------------------------------------------------------------+
| bots DEPRECATED          | The number of bots in the server                                             |
+--------------------------+------------------------------------------------------------------------------+
| humans BROKEN            | The number of humans in the server, returns members right now as it's broken |
+--------------------------+------------------------------------------------------------------------------+
| roles                    | The number of roles in the server                                            |
+--------------------------+------------------------------------------------------------------------------+
| channels                 | The number of channels in the server                                         |
+--------------------------+------------------------------------------------------------------------------+
| created_at               | When the server was created in the format yyyy-mm-dd HH:MM:SS                |
+--------------------------+------------------------------------------------------------------------------+

Channel
-------

.. tagscript::

    {channel}

    {channel(topic)}

Contains details about the channel

Parameters
~~~~~~~~~~

When used without a parameter, the block will output the channel name

+-----------+---------------------------------------------------------------------------------------+
| Parameter |                                        Output                                         |
+===========+=======================================================================================+
| id        | The channels id                                                                       |
+-----------+---------------------------------------------------------------------------------------+
| topic     | The channels topic                                                                    |
+-----------+---------------------------------------------------------------------------------------+
| slowmode  | The channels discord slowmode delay in seconds                                        |
+-----------+---------------------------------------------------------------------------------------+
| position  | The channels position, in the order of which channels were created, 0 being the first |
+-----------+---------------------------------------------------------------------------------------+
| mention   | Clickable link to the channel                                                         |
+-----------+---------------------------------------------------------------------------------------+

.. raw:: html

    <meta property="og:title" content="Discord Objects" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Block Reference">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Discord user, channel and server blocks" />
    <meta name="theme-color" content="#F62658">
