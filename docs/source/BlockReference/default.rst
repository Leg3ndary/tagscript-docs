Default Variables
=================

Defualt variables are variables that every tag will have defined.

Unix
----

.. ansi-block::
    
    [1;31m{[1;32munix[1;31m}[1;37m

Returns the current unix time

Often used in conjunction with strf and timedelta blocks

.. note::

    To use this outside of tags, add this to the top of your code ``{=(unix):{strf:%s}}``

.. warning::
    
    This is exclusive to tags.

Uses
----

.. ansi-block::
    
    [1;31m{[1;32muses[1;31m}[1;37m

Returns how many times your tag was used

.. warning::
    
    This is exclusive to tags.

.. warning::

    This increments even if the tag fails to output/work, the only way to reset this is to delete and re-import the tag.

Mention
-------

.. ansi-block::

    [1;31m{[1;32mmention[1;31m}[1;37m

Mentions the user who used the tag

.. note::
    
    This is the same as ``{user(mention)}``

Args/Message
------------

.. important::
    
    This is probably the most used and important block in tagscript, it's what allows you to access what users put after an invocation.

    In addition you will often need to parse this block, so it would be wise to check out :ref:`parsing-label`.

.. ansi-block::
    
    [1;31m{[1;32margs[1;31m}[1;37m
    [1;31m{[1;32mmessage[1;31m}[1;37m

What is after a tag invocation:

.. ansi-block::

    ?foo bar baz

    [1;31m{[1;32margs[1;31m}[1;37m will output bar baz


.. note::
    If used in a tag, this block will also contain the trigger invocation.

Digit Shorthands
~~~~~~~~~~~~~~~~

.. ansi-block::

    [1;31m{[1;37m1[1;31m}[1;37m
    [1;31m{[1;37m2[1;31m}[1;37m
    [1;31m{[1;37m3[1;31m}[1;37m etc.

The main difference between args and message is how message has digit shorthands.

.. ansi-block::

    [1;31m{[1;32margs[1;34m([1;37m1[1;34m)[1;31m}[1;37m is equivalent to [1;31m{[1;37m1[1;31m}[1;37m
    [1;31m{[1;32margs[1;34m([1;37m2[1;34m)[1;31m}[1;37m is equvalent to [1;31m{[1;37m2[1;31m}[1;37m

However digit shorthands are based upon the message variable, meaning if you change it, by redefining it, digit shorthands will now be based on that instead.

.. note::

    If you don't understand digit shorthands, don't worry! They aren't really used and it's much more common to see people use ``{args(1)}``!