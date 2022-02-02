Default Variables
=================

Defualt variables are variables that every tag will have defined.

Unix
----

.. code:: CSS
    
    {unix}


Returns the current unix time

Often used in conjunction with strf and timedelta blocks

.. note::

    To use this outside of tags, add this to the top of your code ``{=(unix):{strf:%s}}``

.. warning::
    
    This is exclusive to tags.

Uses
----

.. code:: CSS
    
    {uses}


Returns how many times your tag was used

.. warning::
    
    This is exclusive to tags.

.. warning::

    This increments even if the tag fails to output/work, the only way to reset this is to delete and re-import the tag.

Mention
-------

.. code:: CSS

    {mention}

Mentions the user who used the tag

.. note::
    
    This is the same as ``{user(mention)}``

Args/Message
------------

.. important::
    
    This is probably the most used and important block in tagscript, it's what allows you to access what users put after an invocation.

    In addition you will often need to parse this block, so it would be wise to check out :ref:`parsing-label`.

.. code:: CSS
    
    {args}
    {message}

What is after a tag invocation:

.. code:: CSS

    ?foo bar baz

    {args} will output bar baz

.. note::
    If used in a tag, this block will also contain the trigger invocation.

Digit Shorthands
~~~~~~~~~~~~~~~~

.. code:: CSS

    {1}
    {2}
    {3} etc.

The main difference between args and message is how message has digit shorthands.

.. code:: CSS

    {args(1)} is equivalent to {1}
    {args(2)} is equvalent to {2}

However digit shorthands are based upon the message variable, meaning if you change it, by redefining it, digit shorthands will now be based on that instead.

.. note::

    If you don't understand digit shorthands, don't worry! They aren't really used and it's much more common to see people use ``{args(1)}``!