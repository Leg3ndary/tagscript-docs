Control
=======

Control blocks "control" what happens based on the condition we give it

Consider the following:

.. ansi-block::

    If I, am hungry, I will eat, if not, I will drink some water.

    To convert this into tagscript we first create an if statement

    [1;31m{[1;33mif[1;31m}[1;37m

    Now we create our condition

    [1;31m{[1;33mif[1;34m([1;37mI[1;35m==[1;37mhungry[1;34m)[1;31m}[1;37m

    Now we add the payload or what will happen

    [1;31m{[1;33mif[1;34m([1;37mI[1;35m==[1;37mhungry[1;34m)[1;34m:[1;37mEat[1;31m}[1;37m

    Finally we add the else

    [1;31m{[1;33mif[1;34m([1;37mI[1;35m==[1;37mhungry[1;34m)[1;34m:[1;37mEat[1;35m|[1;37mDrink[1;31m}[1;37m

.. note::
    
    This just pseudo code! If you run this, it will always say Drink Water as I is not the same as hungry!

The following explains what everything means

Boolean Operators (Parameters)
------------------------------

.. ansi-block::

    [1;31m{[1;33mif[1;34m([1;37mCONDITION[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m

    [1;31m{[1;33mif[1;34m([1;37mcarl[1;35m==[1;37mcarl[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m [1;31m-[1;35m>[1;37m [4;36mtrue[1;37m

    [1;31m{[1;33mif[1;34m([1;37mcarl[1;35m!=[1;37mcarl[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m [1;31m-[1;35m>[1;37m [4;36mfalse[1;37m

    [1;31m{[1;33mif[1;34m([1;37m5[1;35m>[1;37m1[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m [1;31m-[1;35m>[1;37m [4;36mtrue[1;37m

    [1;31m{[1;33mif[1;34m([1;37m5[1;35m<[1;37m1[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m [1;31m-[1;35m>[1;37m [4;36mfalse[1;37m

This is how we determine what to do, in this case we just print out true or false

.. table:: Boolean Equations

    :widths: auto

    ========  ================================================================================
    Operator  Explanation
    ========  ================================================================================
    \==       If the left side is exactly the same as the right side, space and case sensitive
    !=        If the left side is different from the right side, space and case sensitive
    >=        Greater than or equal too
    <=        Lesser than or equal too
    >         Greater than
    <         Lesser Than
    ========  ================================================================================

Then/Else (Payload)
-------------------

.. ansi-block::

    {if({user(id)}==235148962103951360):PAYLOAD}



If
--

aa

Any/Or
------

aa

All/And
-------

aa

Break/Shortcircuit
------------------

aa
