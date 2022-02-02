Discord Objects
===============

Discord related default variables

User/Target
-----------

.. code:: css
    
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

+------------+----------------------------------------------+
| Parameter  | Output                                       |
+============+==============================================+
| avatar     | A link to the users avatar                   |
+------------+----------------------------------------------+
| icon       | Alias for avatar                             |
+------------+----------------------------------------------+
| id         | The id of the user                           |
+------------+----------------------------------------------|
| mention    | @'s/Mentions the user                        |
+------------+----------------------------------------------+
| created_at | When the account was created in the form of  |
|            | yyyy-mm-dd HH:MM:SS                          |
+------------+----------------------------------------------+
| joined_at  | When the user joined this server in the form |
|            | of yyyy-mm-dd HH:MM:SS                       |
+------------+----------------------------------------------+
| color      | The users hexadecimal role color, # included |
+------------+----------------------------------------------+
| name       | The users discord username                   |
+------------+----------------------------------------------+
| proper     | The users username + discriminator, example  |
|            | _Leg3ndary#5759                              |
+------------+----------------------------------------------+
| roleids    | A list of every role (id) the user has from  |
|            | lowest to highest separated by a space       |
+------------+----------------------------------------------+
| position   | The user's position in the role hierarchy,   |
|            | starts with 0 for @everyone and increases by |
|            | 1 for each role in the server                |
+------------+----------------------------------------------+

Server
------

.. code:: css

    {server}

    {server(roles)}

Contains details about the server

Parameters
~~~~~~~~~~

.. warning:: 

    Some of these are depreciated.

+---------------+----------------------------------------------+
| Parameter     | Output                                       |
+===============+==============================================+
| icon          | A link to the servers avatar                 |
+---------------+----------------------------------------------+
| id            | The servers id                               |
+---------------+----------------------------------------------|
| owner         | The username + discriminator of the owner    |
+---------------+----------------------------------------------+
| random        | The username + discriminator of a random     |
|               | user                                         |
+---------------+----------------------------------------------+
| randomonline  | The username + discriminator of a random     |
| DEPRECIATED   | online user                                  |
+---------------+----------------------------------------------+
| randomoffline | The username + discriminator of a random     |
| DEPRECIATED   | offline user                                 |
+---------------+----------------------------------------------+
| members       | The number of members in the server          |
+---------------+----------------------------------------------+
| bots          | The number of bots in the server             |
| DEPRECIATED   |                                              |
+---------------+----------------------------------------------+
| humans        | The number of humans in the server           |
| BROKEN        | Returns members instead                      |
+---------------+----------------------------------------------+
| roles         | The number of roles in the server            |
+---------------+----------------------------------------------+
| channels      | The number of channels in the server         |
+---------------+----------------------------------------------|
| created_at    | When the server was created in the format    |
|               | yyyy-mm-dd HH:MM:SS                          |
+---------------+----------------------------------------------+