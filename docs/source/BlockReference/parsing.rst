Parsing 
=======

Parsing is an extremely important part of tagscript, and there are a few ways in which you can parse text.

.. note::

    Parsing can be done with basically anything, though you shouldn't try to parse datetimes using methods below, that's what strf blocks are for ADD LINK HERE.

Variable Parsing
----------------

.. tagscript::

    {=(test_var):Carl-bot is the best bot! His favorite food is subway!}

    {test_var} -> Calling the variable
    {Variable Name(Elements):Delimiter}

    {test_var(1)} -> Calling the first "word" (Basically setting the delimiter to a space)
    The above would return Carl-bot

    {test_var(1):!} -> Calling the first part of the variable up to the first "!"
    The above would return Carl-bot is the best bot

One big function of variables is the ability to parse them, you can specify any number of elements and can also change the delimiter.

.. note::

    This also works with {args} and {message}.

Elements
~~~~~~~~

.. tagscript::

    {=(test_var):Carl-bot is the best bot! His favorite food is subway!}

    {test_var(ELEMENT)}

    {test_var(4)} -> Calling the fourth element
    The above would return best

    {test_var(0)} {test_var(-2)} -> Calling the last element and the third last element.
    The above would return subway! food

    {test_var(+3)} | {test_var(7+)} -> Calling everything up to the third element and everything from the seventh onward
    The above would return Carl-bot is the | favorite food is subway!

Elements are how you control how many elements you return.

Delimiters
~~~~~~~~~~

.. tagscript::

    {=(test_var):Carl-bot is the best bot! His favorite food is subway!}

    {test_var(ELEMENT):DELIMITER}

    {test_var(2):!} -> Calling the second argument when test_var is split by ! instead of spaces
    The above would return His favorite food is subway!

When a delimiter isn't specified, tagscript automatically assumes you mean a space, or basically ``{args(5)}`` is the same as ``{args(5): }``.

Delimiters on their own don't do anything, you need to specify an element for this to change anything.

.. note::

    This is most often used to get certain parts of variables, an example being a urls domain name.

    Knowing that urls are formatted like so: ``https://readthedocs.org/dashboard/`` We can first parse everything after the ``//`` and then everything before the first ``/``.

    .. tagscript::

        {=(url):https://readthedocs.org/dashboard/}
        {=(url):{url(2)://}}
        {=(url):{url(1):/}}
        {url}

.. warn::

    Just to reiterate ``{test_var:DELIMITER}`` won't do anything

List & Cycle
------------

.. tagscript::

    {list(INDEX):elem,elem2,elem3,elem4}
    {list(INDEX):elem~elem2~elem3~elem4}

    {cycle(INDEX):elem,elem2,elem3,elem4}
    {cycle(INDEX):elem~elem2~elem3~elem4}

List blocks will return the element at whatever index you specify. If you specify an index that's out of bounds, the block will return nothing.

Cycle blocks will work the same, however when specifying an index that's out of bounds, the block will *cycle* back.

When separating elements you may use ``,`` or ``~``, however if you have both, the tilde will take precedence.

Index
~~~~~

.. tagscript::
    
    {list(-1):elem~elem2~elem3~elem4} -> elem4
    {list(1):elem~elem2~elem3~elem4} -> elem2

    {cycle(5):elem~elem2~elem3~elem4} -> elem2
    {cycle(-6):elem~elem2~elem3~elem4} -> elem3

You may parse this similarily to regular parsing, however you may only parse one element at a time.

You also may use negative numbers to go backward.

.. attention::

    Indexes start at 0, meaning the first element will have index 0, the second, 1 etc. etc.

Index
-----

.. tagscript::

    {index(ELEMENT):elem~elem2~elem3~elem4}

Index is quite straightforward, it will simply index the element and return its position.

Element
~~~~~~~

.. tagscript::

    {index(elem2):elem~elem2~elem3~elem4} -> 1

    {index(elem5):elem~elem2~elem3~elem4} -> -1

Note that this block will always return the first found instance regardless of how many times it's found in the string, in addition if the element isn't found, the block will return -1.

.. attention::

    Indexes start at 0, meaning the first element will have index 0, the second, 1 etc. etc.

Membership Testing (In & Contains)
----------------------------------

.. tagscript::
    
    {in(STRING):TEXT}

    {contains(ELEMENT):LIST}

These blocks test if a list or piece of text has a string or element in it.

In is the more powerful of the two, it will check if the string is in the text regardless of where it is while contains must have spaces around the given text.

This will return a bool value of true or false.

.. tagscript::

    {in(cool):Carl-bot is cool!} -> true
    {contains(cool):Carl-bot is cool!} -> false

    {in(efg):abcdefghijklmnop} -> true
    {contains(efg):abcdefghijklmnop} -> false
    
    {in(Carl):Carl bot} -> true
    {in(carl):Carl bot} -> true
    {contains(Carl):Carl bot} -> true
    {contains(carl):Carl bot} -> false

.. attention::

    Everything in tagscript is case-sensitive, this includes contains and in blocks, you can use the lower or upper block to null this though.

.. raw:: html

    <meta property="og:title" content="Tagscript Unofficial Docs" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="By _Leg3ndary#5759">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="The unofficial but better docs for Carl-bots Tagscript, not affiliated with Botlabs or Carl-bot" />
    <meta name="theme-color" content="#9C20BC">