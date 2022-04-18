Math
====

.. tagscript::

    {m:EQUATION}

    {math:9+10} -> 19
    {calc:365-5} -> 360
    {+:14/7} -> 2
    {m:12*10} -> 120

The math block also works as you'd expect it to, the block itself **only** takes a payload which will be calculated in the correct order of operations.

Basic Functions and Operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+------------------------------------+
| Function/Operator | Explanation                        |
+===================+====================================+
| x+y               | Addition                           |
+-------------------+------------------------------------+
| x-y               | Subtraction                        |
+-------------------+------------------------------------+
| x*y               | Multiplication                     |
+-------------------+------------------------------------+
| x/y               | Division                           |
+-------------------+------------------------------------+
| x%y               | Modulo                             |
+-------------------+------------------------------------+
| x^y               | Exponent                           |
+-------------------+------------------------------------+
| abs(x)            | Absolute value                     |
+-------------------+------------------------------------+
| round(x)          | Rounds to the nearest whole number |
+-------------------+------------------------------------+
| trunc(x)          | Truncation                         |
+-------------------+------------------------------------+

Advanced Functions, Operators and Vars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+------------------------------------------------------------+
| Function/Operator/Var | Explanation                                                |
+=======================+============================================================+
| sin(x)                | Sine (radians)                                             |
+-----------------------+------------------------------------------------------------+
| cos(x)                | Cosine (radians)                                           |
+-----------------------+------------------------------------------------------------+
| tan(x)                | Tangent (radians)                                          |
+-----------------------+------------------------------------------------------------+
| exp(x)                | Eulers number to the x power                               |
+-----------------------+------------------------------------------------------------+
| sgn()                 | Returns the sign of a number, 1 positive, -1 negative, 0 0 |
+-----------------------+------------------------------------------------------------+
| log(x)                | Logarithm                                                  |
+-----------------------+------------------------------------------------------------+
| ln(x)                 | Natural Logarithm                                          |
+-----------------------+------------------------------------------------------------+
| log2(x)               | Logarithm with base 2                                      |
+-----------------------+------------------------------------------------------------+
| pi/PI                 | Will be replaced with pi                                   |
+-----------------------+------------------------------------------------------------+
| e/E                   | Will be replaced with Euler's number                       |
+-----------------------+------------------------------------------------------------+

.. warning::

    When calculating long equations carl will occasionally hiccup and just output the entire equation, there's nothing you can do about this.

    `Try it for yourself <https://carl.gg/t/573444>`_

.. raw:: html

    <meta property="og:title" content="Math" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Block Reference">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Making the poor turtle do math" />
    <meta name="theme-color" content="#F62658">