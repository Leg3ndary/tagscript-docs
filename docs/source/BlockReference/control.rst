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

Boolean Operators (Parameters)
------------------------------

.. ansi-block::

    [1;31m{[1;33mif[1;34m([1;37mCONDITION[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m

    [1;31m{[1;33mif[1;34m([1;37mcarl[1;35m==[1;37mcarl[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m [1;31m-[1;35m>[1;37m [4;36mtrue[1;37m

    [1;31m{[1;33mif[1;34m([1;37mcarl[1;35m!=[1;37mcarl[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m [1;31m-[1;35m>[1;37m [4;36mfalse[1;37m

    [1;31m{[1;33mif[1;34m([1;37m5[1;35m>[1;37m1[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m [1;31m-[1;35m>[1;37m [4;36mtrue[1;37m

    [1;31m{[1;33mif[1;34m([1;37m5[1;35m<[1;37m1[1;34m)[1;34m:[4;36mtrue[1;35m|[4;36mfalse[1;31m}[1;37m [1;31m-[1;35m>[1;37m [4;36mfalse[1;37m

This is how we determine what to do, in this case we just print out true or false

+----------+----------------------------------------------------------------------------------+
| Operator | Explanation                                                                      |
+==========+==================================================================================+
| ==       | If the left side is exactly the same as the right side, space and case sensitive |
+----------+----------------------------------------------------------------------------------+
| !=       | If the left side is different from the right side, space and case sensitive      |
+----------+----------------------------------------------------------------------------------+
| >=       | Greater than or equal too                                                        |
+----------+----------------------------------------------------------------------------------+
| <=       | Lesser than or equal too                                                         |
+----------+----------------------------------------------------------------------------------+
| >        | Greater than                                                                     |
+----------+----------------------------------------------------------------------------------+
| <        | Lesser Than                                                                      |
+----------+----------------------------------------------------------------------------------+

.. tip::
    
    An extremely common question, is how we check if a user was pinged!

    We can easily check this by comparing the user id, to target id

    .. ansi-block::

        [1;31m{[1;33mif[1;34m([1;31m{[1;32muser[1;34m([1;35mid[1;34m)[1;31m}[1;35m==[1;31m{[1;32mtarget[1;34m([1;35mid[1;34m)[1;31m}[1;34m)[1;34m:[1;37mYou need to ping someone![1;35m|[1;37mYou pinged [1;31m{[1;32mtarget[1;31m}[1;31m}[1;37m

Then/Else (Payload)
-------------------

.. ansi-block::

    [1;31m{[1;33mif[1;34m([1;31m{[1;32muser[1;34m([1;35mid[1;34m)[1;31m}[1;35m==[1;37m235148962103951360[1;34m)[1;34m:[1;37mTHEN[1;35m|[1;37mELSE[1;31m}[1;37m

    [1;31m{[1;33mif[1;34m([1;31m{[1;32muses[1;31m}[1;35m>[1;37m10[1;34m)[1;34m:[1;37mThis command has been used more then 10 times[1;35m|[1;37mThis command has only been used [1;31m{[1;32muses[1;31m}[1;37m times![1;31m}[1;37m

    [1;31m{[1;33mand[1;34m([1;31m{[1;32mtarget[1;31m}[1;35m==[1;37mCarl[1;31m-[1;37mbot[1;35m|[1;31m{[1;32mtarget[1;34m([1;35mid[1;34m)[1;31m}[1;35m!=[1;37m235148962103951360[1;34m)[1;34m:[1;37mHow dare you impersonate me![1;31m}[1;37m

The payload for conditional blocks can either be a then without an else, or both, you separate these with a pipe ``|``.

If
--

.. ansi-block::
    
    [1;31m{[1;33mif[1;34m([1;37mCONDITION[1;34m)[1;34m:[1;37mTHEN[1;35m|[1;37mELSE[1;31m}[1;37m

The simplest of conditional blocks, checks a singular condition.

Any/Or
------

.. ansi-block::

    [1;31m{[1;33many[1;34m([1;37mCONDITION[1;35m|[1;37mCONDITION[1;35m|[1;37mCONDITION[1;34m)[1;34m:[1;37mTHEN[1;35m|[1;37mELSE[1;31m}[1;37m

If you want to check if any condition out of whatever you provide are true, you can use an any block, just separate every condition with a ``|``.

All/And
-------

.. ansi-block::

    [1;31m{[1;33mand[1;34m([1;37mCONDITION[1;35m|[1;37mCONDITION[1;35m|[1;37mCONDITION[1;34m)[1;34m:[1;37mTHEN[1;35m|[1;37mELSE[1;31m}[1;37m

Nearly identical to the any block, this block just checks if every condition you provide is true.

Break/Shortcircuit
------------------

.. ansi-block::

    [1;31m{[1;33mbreak[1;34m([1;37mCONDITION[1;34m)[1;34m:[1;37mTHEN[1;31m}[1;37m

When used, if the condition given is true, the tags text output will only be whatever you put as the payload.

.. danger::

    This will not prevent command blocks from running or the embed from the embed builder from sending.
