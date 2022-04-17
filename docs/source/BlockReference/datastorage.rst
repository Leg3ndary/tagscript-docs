Data Storage/Variables
----------------------

.. note::
    
    Tags cannot store data between invocations through regular means, you have other options though! See :doc:`here. </AdvancedConcepts/tag_saving>`

.. tagscript::

    {=(VARIABLE NAME):VARIABLE CONTENT}

    {=(tag_name):afk}
    {tag_name} -> afk

    {let(new nick):Default User}
    {new nick} -> Default User

    {var(formulaEQ):5+6(x-1)}
    {formulaEQ} -> 5+6(x-1)

    {assign(userGoal):1,000,000 Members!}
    {userGoal} -> 1,000,000 Members!

An extremely important block, the variable block allows you to save data per command invocation and use/alter it.

To define a variable, you just need to give it a name, and content, which may be empty.

After that, to call it, all you have to do is put brackets around the variables name.

.. warning::

    You cannot name variables, names of existing blocks, for example, you cannot name a variable ``user``, as that already exists (See Discord.rst)

.. raw:: html

    <meta property="og:title" content="Data Storage" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Block Reference">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Variables Usage" />
    <meta name="theme-color" content="#F62658">