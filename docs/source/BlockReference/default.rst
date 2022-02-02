Default Variables
=================

Defualt variables are variables that every tag will have defined.

Unix
----

Returns the current unix time

Often used in conjunction with strf and timedelta blocks

.. code:: css
    
    {unix}

.. warning::
    
    This is exclusive to tags.

.. note::

    To use this outside of tags, add this to the top of your code ``{=(unix):{strf:%s}}``

Uses
----

Returns how many times your tag was used

.. code:: css
    
    {uses}

.. warning::
    
    This is exclusive to tags.

.. warning::

    This increments even if the tag fails to output/work, the only way to reset this is too delete and re-import the tag

Mention
-------

Mentions the user who used the tag

.. code:: css

    {mention}

.. note::
    
    This is the same as ``{user(mention)}``

Args/Message

.. important::
    
    This is probably the most used and important block in tagscript, it's what allows you to access what users put after an invocation.

    In addition you will often need to parse these, so it would be wise to check out :docs:`parsing`.

.. code:: css
    
    {args}
    {message}

What is after a tag invocation:

.. code:: css

    ?foo bar baz

    {args} will output bar baz

.. note::
    If used in a tag, this block will also contain the trigger invocation.

Digit Shorthands
~~~~~~~~~~~~~~~~

.. code:: css

    {1}
    {2}
    {3} etc.

The main difference between args and message is how message has digit shorthands.

.. code:: css

    {args(1)} is equivalent too {1}
    {args(2)} is equvalent too {2}

However digit shorthands are based upon the message variable, meaning if you change it, by redefining it, digit shorthands will now be based on that instead.

.. note::

    If you don't understand digit shorthands, don't worry! They aren't really used and it's much more common to see people use ``{args(1)}``!