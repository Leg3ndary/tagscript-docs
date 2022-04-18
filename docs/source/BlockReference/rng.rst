Random Number Generators
========================

Random
------

.. tagscript::

    {random(OPTIONAL SEED):List,of,elements}
    {rand(OPTIONAL SEED):List~of~elements}
    {#(OPTIONAL SEED):4|Weighted,2|list,of,3|elements}

Random blocks just pick a random choice out of a list you provide, you can also provide optional seeds and weight elements to prevent repetition.

Optional Seeding
~~~~~~~~~~~~~~~~

Seed values are completely optional, however when you use a certain seed value with the same list of elements, the same element will always be chosen.

You can think of this to almost be a key that works almost like a cycle block.

Weighting
~~~~~~~~~

.. tagscript::

    {#:4|Carl,2|bot} == {#:Carl,Carl,Carl,Carl,bot,bot}

    {#:4|Lose,Win}

Weighting is just a simple way to add more elements without typing as much, keep in mind you don't need to provide weighting for every value, the last example shows an example of having a 1 in 5 chance of winning.

Range
~~~~~

.. tagscript::

    {range(OPTIONAL SEED):LOWER-HIGHER}
    {rangef(OPTIONAL SEED):LOWER-HIGHER}

    {range:1-100}
    {rangef:0-1}

Range blocks generate random numbers between the 2 numbers given (inclusive) while rangef blocks generate random numbers with a single decimal (also inclusive).

Seeds may also be provided and work exactly the same as random blocks.

5050 Blocks
~~~~~~~~~~~

.. tagscript::

    {5050:OPTION}
    {50:OPTION}
    {?:OPTION}

Has a 5050 chance of choosing said option, or nothing at all.

.. raw:: html

    <meta property="og:title" content="Random Number Generators" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Block Reference">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Randomness" />
    <meta name="theme-color" content="#F62658">