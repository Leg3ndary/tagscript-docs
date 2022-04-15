Control
=======

Control blocks "control" what happens based on the condition we give it

Consider the following:

.. tagscript::

    If I, am hungry, I will eat, if not, I will drink some water.

    To convert this into tagscript we first create an if statement

    {if}

    Now we create our condition

    {if(I==hungry)}

    Now we add the payload or what will happen

    {if(I==hungry):Eat}

    Finally we add the else

    {if(I==hungry):Eat|Drink}

.. note::
    
    This just pseudo code! If you run this, it will always say Drink Water as I is not the same as hungry!

Boolean Operators (Parameters)
------------------------------

.. tagscript::

    {if(CONDITION):true|false}

    {if(carl==carl):true|false} -> true

    {if(carl!=carl):true|false} -> false

    {if(5>1):true|false} -> true

    {if(5<1):true|false} -> false

This is how we determine what to do, in this case we just print out true or false

.. tabbed:: ==
     
    If the left side is exactly the same as the right side, space and case sensitive

.. tabbed:: !=
    
    If the left side is different from the right side, space and case sensitive

.. tabbed:: >=

    Greater than or equal too

.. tabbed:: <=

    Lesser than or equal too

.. tabbed:: >

    Greater than

.. tabbed:: <

    Lesser Than

.. tip::
    
    An extremely common question, is how we check if a user was pinged!

    We can easily check this by comparing the user id, to target id

    .. tagscript::

        {if({user(id)}=={target(id)}):You need to ping someone!|You pinged {target}}

Then/Else (Payload)
-------------------

.. tagscript::

    {if({user(id)}==235148962103951360):THEN|ELSE}

    {if({uses}>10):This command has been used more then 10 times|This command has only been used {uses} times!}

    {and({target}==Carl-bot|{target(id)}!=235148962103951360):How dare you impersonate me!}

The payload for conditional blocks can either be a then without an else, or both, you separate these with a pipe ``|``.

If
--

.. tagscript::
    
    {if(CONDITION):THEN|ELSE}

The simplest of conditional blocks, checks a singular condition.

Any/Or
------

.. tagscript::

    {any(CONDITION|CONDITION|CONDITION):THEN|ELSE}

If you want to check if any condition out of whatever you provide are true, you can use an any block, just separate every condition with a ``|``.

All/And
-------

.. tagscript::

    {and(CONDITION|CONDITION|CONDITION):THEN|ELSE}

Nearly identical to the any block, this block just checks if every condition you provide is true.

Break/Shortcircuit
------------------

.. tagscript::

    {break(CONDITION):THEN}

When used, if the condition given is true, the tags text output will only be whatever you put as the payload.

.. danger::

    This will not prevent command blocks from running or the embed from the embed builder from sending.

.. raw:: html

    <meta property="og:title" content="Tagscript Unofficial Docs" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="By _Leg3ndary#5759">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="The unofficial but better docs for Carl-bots Tagscript, not affiliated with Botlabs or Carl-bot" />
    <meta name="theme-color" content="#9C20BC">