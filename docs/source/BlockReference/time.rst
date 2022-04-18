Time
====

STRF
----

.. tagscript:: 

    {strf(OPTIONAL DATETIME OR UNIX):STRF FORMAT CODE}
    
    December 31st 1999 was a {strf(1999-12-31 23.59.59):%A} -> December 31st 1999 was a Friday
    The current time is {strf:%-I:%M %p} -> The current time is followed by whatever the current 12h clock is for UTC, eg 2:19 AM
    Your account was created on {strf({user(created_at)}: %x} -> Your account was created on 2015/12/24 (For Carl)

When dealing with time we often want it to be outputted in different ways, strf does exactly that.

You can either supply a datetime or unix value, if none are supplied, the engine assumes you want the current time.

.. note::

    For a full list of STRF codes, check `here <https://strftime.org>`_

.. note::

    Some useful codes
    
    .. tagscript::

        %Y-%m-%d %H:%M:%S & the short version %F %T are the DateTime format in strf codes, which can be useful for timedelta blocks.
        
        {strf:%FT%T}.000Z is the strf code for the ISO 8601 format, which is used when setting the timestamp in an embed's JSON. Useful if you're creating embeds manually.

Timedelta
---------

.. tagscript::

    {td(OPTIONAL DATETIME OR UNIX):DATETIME}

    {td:2020-01-01 00.00.00} as of 2019-11-25 would output 1 month, 5 days and 21 hours, or the time until Midnight New Years Day

    {td({m:trunc({unix}-3600)}):{strf:%Y-%m-%d %H.%M.%S}} -> 1 hour because we're just subtracting 3600 seconds or 1 hour from the current time.

Timedelta blocks will output a readable time until said datetime will be reached.

.. raw:: html

    <meta property="og:title" content="Time" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Block Reference">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Anything that deals with time" />
    <meta name="theme-color" content="#F62658">