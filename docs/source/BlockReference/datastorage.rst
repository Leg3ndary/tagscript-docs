Data Storage/Variables
----------------------

.. note::
    
    Tags cannot store data between invocations through regular means, you have other options though! See link (to blanks)

.. ansi-block::

    [1;31m{[1;32m=[1;34m([1;37mVARIABLE NAME[1;34m)[1;34m:[1;37mVARIABLE CONTENT[1;31m}[1;37m

    [1;31m{[1;32m=[1;34m([1;37mtag_name[1;34m)[1;34m:[1;37mafk[1;31m}[1;37m
    [1;31m{[1;37mtag_name[1;31m}[1;37m [1;31m-[1;35m>[1;37m afk

    [1;31m{[1;32mlet[1;34m([1;37mnew nick[1;34m)[1;34m:[1;37mDefault User[1;31m}[1;37m
    [1;31m{[1;37mnew nick[1;31m}[1;37m [1;31m-[1;35m>[1;37m Defualt User

    [1;31m{[1;32mvar[1;34m([1;37mformulaEQ[1;34m)[1;34m:[1;37m5[1;31m+[1;37m6[1;34m([1;37mx[1;31m-[1;37m1[1;34m)[1;31m}[1;37m
    [1;31m{[1;37mformulaEQ[1;31m}[1;37m [1;31m-[1;35m>[1;37m 5[1;31m+[1;37m6[1;34m([1;37mx[1;31m-[1;37m1[1;34m)[1;37m

    [1;31m{[1;32massign[1;34m([1;37muserGoal[1;34m)[1;34m:[1;37m1[1;33m,[1;37m000[1;33m,[1;37m000 Members![1;31m}[1;37m
    [1;31m{[1;32muser[1;37mGoal[1;31m}[1;37m [1;31m-[1;35m>[1;37m 1[1;33m,[1;37m000[1;33m,[1;37m000 Members!

An extremely important block, the variable block allows you to save data per command invocation and use/alter it.

To define a variable, you just need to give it a name, and content, which may be empty.

After that, to call it, all you have to do is put brackets around the variables name.

.. warning::

    You cannot name variables, names of existing blocks, for example, you cannot name a variable ``user``, as that already exists (See Discord.rst)