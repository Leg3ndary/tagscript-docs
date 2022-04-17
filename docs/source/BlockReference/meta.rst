Meta
====

Meta blocks are blocks that will change a tags overall behaviour, this includes changing where it replies, deleting the invocation, and interacting with users.

Delete
------

.. tagscript::

    {delete}
    {del}

Deletes the message which invoked the commmand

Silent
------

.. tagscript::

    {silent}
    {silence}

Silences any command block outputs

Override
--------

.. tagscript::

    {override}

Overrides any permissions needed to run a command

.. danger::

    Use this with caution.

.. warning::
    
    This still respects hierarchy, for example if you're trying to add a role to yourself, using carl, or someone who has a higher role then you. This will not work.

Direct Message
--------------

.. tagscript::

    {dm}

This will instead send the output to a users direct messages (DMS)

.. note::

    This won't ever be able to send anything to another users dms. The bot will only dm you if you use a tag with this block in it.

Redirect
--------

.. tagscript::

    {redirect:channel_id}

Redirect will redirect the output to whatever channel id you provide

.. warning::

    The user must have the ``send_messages`` permission for this to work, or you can add an :ref:`override-label` block

Require/Blacklist
-----------------

.. important::

    You can use technically use the role/channel name though it is heavily discouraged, if that name ever changes, the tag will cease to work properly, while using ids will stay the same forever.

.. tagscript::
    
    {require(Optional Error Message):Required Roles, Channels}
    {blacklist(Optional Error Message):Blacklisted Roles, Channels}

    {require(You aren't a moderator, or you aren't using this in the right channel):209797471608635392,465563733981265921}
    {blacklist(Muted users aren't allowed to use this command, if you aren't muted, use #bot-commands):469237398279159818,456625369974308866}

Require is the easiest way to require a user to have a role, or use it in a specific channel.

Blacklist is also an easy way for blacklisting certain channels and or roles from using tags.

**Require Blocks:** Separate the channels or roles by a ``,`` with no spaces inbetween, and as long as they have one of the roles, and one of the channels (If you have both) they will be able to use the tag.

**Blacklist Blocks:** Also separate the channels or roles by a ``,`` with no spaces inbetween, if they have any of the roles or are using it in any of the channels, the tag will output your error message

Parameters
~~~~~~~~~~

.. tagscript::

    {require(ERROR MESSAGE):209797471608635392}

    {blacklist(ERROR MESSAGE):469237398279159818}

.. note::
    
    This is optional, you can simply do ``{require:209797471608635392}`` or ``{blacklist:469237398279159818}``

The error message that will output when the user doesn't have one of the roles or isn't using it in a channel listed.

The error message that will output when the user is using the tag when they have a role or are using it in a blacklisted channel.

.. warning::

    If you do choose to omit the parameter for either blacklist or require, carl will react with a ⚠️ emoji instead, to avoid this simply make the error message a space like so

    ``{require( ):209797471608635392}`` or ``{blacklist( ):469237398279159818}``

.. warning::

    This is exclusive to tags

Payload
~~~~~~~

.. tagscript::

    {require(You aren't a moderator!):ID LIST}

    {require(You can't use this command here!):ID LIST}

A list of role or channel ids separated by ``,`` with no spaces inbetween.

As long as the user using the tag has one of the role ids, and one of the channel ids (If you have both) they will be able to use the tag.

.. important::

    When using blacklist, you can blacklist the server id to automatically break the tag if you want, this is most often used when you want to prevent an embed from posting

React(u)
---------

.. tagscript::
    
    {react: :turtle: :robot:}
    {reactu: :turtle: :robot:}

React blocks will react to what carl outputs, while reactu blocks will react to the tags invocation.

.. attention::

    In tags you're limited to 1 reaction without premium, and 5 with premium

    In triggers you're limited to 3 reactions without premium, and 5 with premium \*I believe

Payload
~~~~~~~

.. tagscript::

    {react:EMOJI LIST}
    {reactu:EMOJI LIST}

The emoji list should be separated by spaces, for custom discord emojis, send a ``\`` in front of it and send it to a channel, use what you then see.

.. raw:: html

    <meta property="og:title" content="Meta Blocks" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Block Reference">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Tag behaviour alterations" />
    <meta name="theme-color" content="#F62658">