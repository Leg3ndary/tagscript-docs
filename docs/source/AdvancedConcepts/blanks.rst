Blanks
======

Blanks are how we conditionally run blocks, this is due to tagscript running all blocks first, and not checking wether they should actually be run (Conditional Statements).

.. danger::

    Probably the hardest concept you'll ever have to learn in tagscript, most people give up here.

If you think you can explain blanks feel free to add a dropdown with your explanation on it.

.. dropdown:: Asty' (With GIF)

    **What is that {=():} variable that you put in your code?**
    
    .. tagscript::

        {=():}
        {=(execution):{if({args}!=):c:echo Hello!}}
        {{execution}}

    In the simple example code above, if there is an argument, it will call the content of the execution variable, and because it has double brackets, it actually executes the command block.
    
    If there is no argument, the else of the conditional if block that's in execution would return nothing, but when we call it with double brackets, it would output ``{}`` as plain text and we don't want that.
    
    So to avoid that, we create a variable with no name and no content, that is being called when an else is blank.

    **Most common usage (please use this instead of the above!)**

    .. tagscript::

        {=():}
        {{if(boolean expression here):c:command here}}
        Such as
        {=():}
        {{if(!={1}):c:echo Yay, you typed words: {args}}}
    
    The above example runs the echo command block only if there was at least an argument (if the first argument is not empty, rather).
    
    Reminder: ``The {=():}`` (blank variable) is there because otherwise when the condition evaluates to false, the line below it would return ``{}`` as plain text and would be outputted to the user, which we want to avoid.

    .. image:: images/blankexample.gif
        :width: 800
        :alt: Not Loaded

.. dropdown:: _Leg3ndary

    **What Are Blanks**

    Tagscript is largely different from any other programming languages...

    When you have any block that will send or alter its behaviour for example command blocks

    .. tagscript::
        
        eg {c:role add blah blah blah}

    Normally you would do something like this
    
    .. tagscript::

        {if(condition):{c:role add blah blah blah}}
    
    This will not work the c role will always add the role

    **It will run no matter what**, no matter where you put it in the code, even if you put it in an ``if`` statement or in a ``variable`` it will still run. **TAGSCRIPT DOES NOT CARE**

    So how do we stop this?

    First we remove the brackets making it work

    .. tagscript::
        {if(condition):{c:role add blah blah blah}}
        {if(condition):c:role add blah blah blah}

    Notice now if we run it it will literally output ``c:role add blah blah blah`` but don't worry thats what we want!

    Now all we have to do is actually allow carl to run it so we move it outside!

    .. tagscript::

        {if(condition):c:role add blah blah blah}
        {{if(condition):c:role add blah blah blah}}

    Now the command block will actually run because after outputting ``c:role add blah blah blah`` carl will add the brackets making it ``{c:role add blah blah blah}``
    
    Now all you have to do is add a ``{=():}``, this will make it so when the condition fails instead of saying {} it will just say nothing.

    Lets do one more example, I want to dm the command if no arguments are present:
    
    Normally a person would do this:

    .. tagscript::

        {if(=={args}):{dm}}

    But now knowing what we have to do lets fix this!

    .. tagscript::

        {if(=={args}):{dm}}
        {if(=={args}):dm} first we remove the brackets!
        {{if(=={args}):dm}} now we add them aroudn the outside
    
    Finally we add a ``{=():}`` before it and we're done!

    This can be used for many blocks like: ``dm, redirect, require, blacklist, whitelist, del, silence, override`` basically anything that will affect the overall block itself just replace ``c:role add blah blah blah` with whatever block you want!``

.. dropdown:: Asty's Second Explanation

    **Deeper explanation about how to make any command/behavior block conditional using the Blank Variable** ``{=():}``

    If you were to do ``{if(this==that):{c:echo {args}}}``, then the command block would execute no matter what, because you put the entire block and it's a behavior block, and will ignore the fact it is inside of an if block.

    Note: All action/behavior blocks like react(u), delete, silence, override, require/blacklist, dm, embed etc. will execute no matter where they are, if you are not using the blank workaround.

    The way to make command blocks conditional is to have the if block return our command block's content as text, and then this text when returned would be evaluated as an actual block thanks to the { and } around the if block.
    When the condition evaluates to false, then the condition returns no text, so the entire block returns {}. This is where the blank variable {=():} comes in handy, as it would get called in that case and would return nothing. That's the workaround to allow you to execute a command block or any behavior block conditionally.

    Essentially, we are doing {if(this==that):c:echo {args}}, which, when true is returned from the boolean equation (the check in the if block), returns the text c:echo {args}.
    And now for it to actually become a block it should execute when the condition is met, we wrap all of that between { and }. When the if block returns false, since no text would be returned, then with the extra brackets around it would become {}, which, if you have a blank variable above it {=():}, would actually call this variable that has no name and no content, effectively doing nothing.

    Becomes:
    {=():}
    {{if(this==that):c:echo {args}}}

    Replace the condition with yours and the command you're willing to execute in the snippet above. Don't copy-paste it without understanding what it does.
    You only need 1 {=():} in your code!

.. raw:: html

    <meta property="og:title" content="Blanks" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Advanced Concepts">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="How to use blanks" />
    <meta name="theme-color" content="#AA22FF">