Discord Objects
===============

Discord related default variables

User/Target
-----------

.. code:: CSS
    
    {user}
    {target}

    {user(name)}
    {target(avatar)}

One of the most used blocks is the target block, it allows you to access other users data.

User is the user who invoked the tag, while target is the first user that was pinged in the commands arguments, when no one is pinged, target is equivalent to user.


.. note::

    It's common to check if someone was pinged in the command, to do this you compare user against target

    ``{if({user(id)}=={target(id)}):You need to ping someone|You pinged {target}}``

Parameters/Properties
~~~~~~~~~~~~~~~~~~~~~

When used without a parameter (``{user}/{target}``), the block will output the nickname of the user/target.

+------------+-----------------------------------------------------------------------------------------------------------------------+
| Parameter  | Output                                                                                                                |
+============+=======================================================================================================================+
| avatar     | A link to the users avatar                                                                                            |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| icon       | Alias for avatar                                                                                                      |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| id         | The id of the user                                                                                                    |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| mention    | @'s/Mentions the user                                                                                                 |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| created_at | When the account was created in the form of yyyy-mm-dd HH:MM:SS                                                       |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| joined_at  | When the user joined this server in the form of yyyy-mm-dd HH:MM:SS                                                   |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| color      | The users hexadecimal role color, # included                                                                          |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| name       | The users discord username                                                                                            |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| proper     | The users username + discriminator, example _Leg3ndary#5759                                                           |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| roleids    | A list of every role (id) the user has from lowest to highest separated by a space                                    |
+------------+-----------------------------------------------------------------------------------------------------------------------+
| position   | The user's position in the role hierarchy, starts with 0 for @everyone and increases by 1 for each role in the server |
+------------+-----------------------------------------------------------------------------------------------------------------------+

Server
------

.. code:: CSS

    {server}

    {server(roles)}

Contains details about the server

Parameters
~~~~~~~~~~

When used without a parameter, the block will output the servers name

.. warning:: 

    Some of these are depreciated.

+---------------------------+------------------------------------------------------------------------------+
| Parameter                 | Output                                                                       |
+===========================+==============================================================================+
| icon                      | A link to the servers avatar                                                 |
+---------------------------+------------------------------------------------------------------------------+
| id                        | The servers id                                                               |
+---------------------------+------------------------------------------------------------------------------+
| owner                     | The username + discriminator of the owner                                    |
+---------------------------+------------------------------------------------------------------------------+
| random                    | The username + discriminator of a random user                                |
+---------------------------+------------------------------------------------------------------------------+
| randomonline DEPRECIATED  | The username + discriminator of a random  online user                        |
+---------------------------+------------------------------------------------------------------------------+
| randomoffline DEPRECIATED | The username + discriminator of a random offline user                        |
+---------------------------+------------------------------------------------------------------------------+
| members                   | The number of members in the server                                          |
+---------------------------+------------------------------------------------------------------------------+
| bots DEPRECIATED          | The number of bots in the server                                             |
+---------------------------+------------------------------------------------------------------------------+
| humans BROKEN             | The number of humans in the server, returns members right now as it's broken |
+---------------------------+------------------------------------------------------------------------------+
| roles                     | The number of roles in the server                                            |
+---------------------------+------------------------------------------------------------------------------+
| channels                  | The number of channels in the server                                         |
+---------------------------+------------------------------------------------------------------------------|
| created_at                | When the server was created in the format yyyy-mm-dd HH:MM:SS                |
+---------------------------+------------------------------------------------------------------------------+

Channel
-------

.. code:: CSS

    {channel}

    {channel(topic)}

Contains details about the channel

Parameters
~~~~~~~~~~

When used without a parameter, the block will output the channel name

+-----------+---------------------------------------------------------------------------------------+
| Parameter | Output                                                                                |
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
