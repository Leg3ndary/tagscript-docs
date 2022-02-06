Data Storage/Variables
----------------------

.. note::
    
    Tags cannot store data between invocations through regular means, you have other options though! See link (to blanks)

.. ansi-block::

    [1;31m{[1;32m=[1;34m([1;37mVARIABLE NAME[1;34m)[1;34m:[1;37mVARIABLE CONTENT[1;31m}[1;37m

    {=(tag_name):afk}
    {tag_name} -> afk

    {let(new nick):Default User}
    {new nick} -> Defualt User

    {var(formulaEQ):5+6(x-1)}
    {formulaEQ} -> 5+6(x-1)

    {assign(userGoal):1,000,000 Members!}
    {userGoal} -> 1,000,000 Members!

An extremely important block, the variable block allows you to save data per command invocation and use/alter it.

To define a variable, you just need to give it a name, and content, which may be empty.

After that, to call it, all you have to do is put brackets around the variables name.

.. warning::

    You cannot name variables, names of existing blocks, for example, you cannot name a variable ``user``, as that already exists (See Discord.rst)