Switches
========

Switches are basically a way you can change a variable to something you've set before based on keywords.

.. danger::

    If you have **anything** that looks relatively similar to this, you're doing it wrong. Keep reading for more info on why

    .. tagscript::

        {=(test_var):{if(keyword=={args}):something}}
        {=(test_var):{if(keyword2=={args}):Tagscript|{test_var}}}
        {=(test_var):{if(keyword3=={args}):Tagscript|{test_var}}}
        {=(test_var):{if(keyword4=={args}):Tagscript|{test_var}}}

.. dropdown:: Raffael's Explanation (Original)

    **How to use variables to make a switch statement/membership test check**

    Let's say you want a tag that outputs a URL pretaining to one of the 16 Myers-Briggs Personality Type Indicators, depending on which personality type the user input. And if what the user inputted isn't one of those 16 types, show an error message. You could write a logical check for each one, like: 
    
    .. tagscript::
        
        {if({1}==ENFJ):url|{if({1}==ISTP):url2|etc etc}}

    but that can be messy to type out, and confusing to troubleshoot. Instead, let's use variables to check if the input matches one of them. First let's capitalize the first element of the input. 
    
    .. tagscript::
        
        {=(u1):{upper:{1}}}

    Next we'll assign our error message to a variable named the contents of the {u1} variable.

    .. tagscript::
         
        {=({u1}):Your input did not match one of the 16 Myers-Briggs Personality Types.}

    Now we'll define our personality type variables. I'll set the base of the url to a variable to save space: 
    
    .. tagscript::

        {=(url):https://www.verywellmind.com/}
        {=(ENFJ):{url}enfj-extraverted-intuitive-feeling-judging-2795979}
        {=(ENFP):{url}enfp-an-overview-of-the-champion-personality-type-2795980}
        {=(ENTJ):{url}entj-personality-type-2795981}
        {=(ENTP):{url}the-entp-personality-type-and-characteristics-2795982}
        {=(ESFJ):{url}esfj-extraverted-sensing-feeling-judging-2795983}
        {=(ESFP):{url}esfp-extraverted-sensing-feeling-perceiving-2795984}
        {=(ESTJ):{url}estj-extraverted-sensing-thinking-judging-2795985}
        {=(ESTP):{url}estp-extraverted-sensing-thinking-perceiving-2795986}
        {=(INFJ):{url}infj-introverted-intuitive-feeling-judging-2795978}
        {=(INFP):{url}infp-a-profile-of-the-idealist-personality-type-2795987}
        {=(INTJ):{url}intj-introverted-intuitive-thinking-judging-2795988}
        {=(INTP):{url}intp-introverted-intuitive-thinking-perceiving-2795989}
        {=(ISFJ):{url}isfj-introverted-sensing-feeling-judging-2795990}
        {=(ISFP):{url}isfp-introverted-sensing-feeling-perceiving-2795991}
        {=(ISTJ):{url}istj-introversion-sensing-thinking-judgment-2795992}
        {=(ISTP):{url}istp-introverted-sensing-thinking-perceiving-2795993}

    At the end, we'll call the contents of {u1} itself as a variable by putting brackets around it.

    .. tagscript::

        {{u1}}

    This variable will either contain our error message since we previously assigned the error message to the variable with the name of {u1}, or that variable will have been overwritten by one of the 16 variables containing the URLs about the Myers-Briggs Personality types if {u1} was one of those types, and calling the variable will output the relevant link. No length checking or logical if statements needed. 
    
    .. link-button:: https://carl.gg/t/246445
        :type: url
        :text: Want to try it out?
        :classes: btn-outline-primary btn-block

.. dropdown:: Asty's Explanation

    **Switch Method Made Easy**

    Return a conditional response/content depending on the user's argument (words typed along with the custom command).

    Prompt Example: We want to display a if the first argument is xyz, b when it's carl, or otherwise a default response.

    Input:

    ``!mytag xyz``

    Expected Output:

    ``a``

    Here is how to do it without using a single if/conditional block, and only variables assignments and calls.

    .. tagscript::

        {=(l1):{lower:{1}}}

        {=(r.{l1}):default response}
        {=(r.xyz):a}
        {=(r.carl):b}

        {r.{l1}}

    The first line simply sets the first argument (``{1}`` is a short alias for ``{args(1)}``) as lowercase, so it doesn't matter if the user typed ``XYZ`` or ``xYz`` or ``xyz``, it will still consider it as ``xyz``.

    Then, I created variables with ``r.`` as their name prefix just so I'm sure the rest of the name won't conflict with blocks that already exist in TagScript.

    The principle of the switch method (which is explained thoroughly but in a more complex way in the pinned messages in this channel) is to basically have a variable that returns content based on the user arguments.

    ``r.{l1}`` here creates a default response for when the argument specified doesn't meet any other below it. For example, if the user types ``xyz`` as the first argument, the ``r.{l1}`` variable will be overwritten with the content of ``r.xyz``, effectively returning a in our case instead of the default response, because it exists.

    In our case, when neither ``xyz`` or ``carl`` was specified as the first argument, then it will send the default response.

    And then the last line is what actually calls the response to display it to the user.

    You could store it in a variable you'd name something like ``response`` or ``output``, if you wanted to call it somewhere else, in your embed's description field for example. 

.. raw:: html

    <meta property="og:title" content="Blanks" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:url" content="https://tagscript-docs.readthedocs.io/en/latest/index.html" />
    <meta property="og:site_name" content="Advanced Concepts">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="How to use blanks" />
    <meta name="theme-color" content="#AA22FF">
