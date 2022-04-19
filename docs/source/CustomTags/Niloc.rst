Niloc#0421
==========

.. contents:: Table of Tags

Dictionary Tag With Image or Link Output
----------------------------------------

**What:**

A tag that gives the user a definition of a word

**How:**

This tag takes the user input and sends it to an API or application programming interface that I built using node.js and express. Once there it takes the word imputed and sends it to another API to get the definition, part of speech, etc.. Then using that info it either creates an image or a website with link previews depending on what is selected in the tag to output to the user. The website is using html meta tags to generate the preview but also is generating more info found on the actual website

**Why:**

I have seen other dictionary tags here on #show-off but they all require you to click a link and go to your browser in order to see the definition and other info. I wanted to make something that gave the user what they needed without ever having to leave discord.

**Links:**

`Image of Tag <https://i.imgur.com/eSeTGyN.png>`_

`Image of Error Msgs <https://i.imgur.com/Nsigb9N.png>`_

`Image of Website <https://i.imgur.com/IhGH61h.png>`_

**How to Customize:**

To change if the tag uses an image or link preview all you have to do is change the ``displayType`` variable to "image" or "link". This is also explained in the tag comments

I would also like to mention this whole idea is possible and inspired by the stuff that **_Leg3ndary#5759** did in his shell tag and other post here about saving data with tagscript 


.. dropdown:: Source Code

    .. tagscript::

        {=(COMMENT):--This tag can either  use a image or a link preview to display the definition --}
        {=(COMMENT):-- to change this just change the below displayType variable to "image" or "link" --}
        {=(displayType):link}

        {=(COMMENT):--Don't touch anything from now on, unless you know what you're doing --}
        {=():}
        {{if({displayType}==link):blacklist(https://define-tag.niloc3.repl.co/l?word={1}&time={unix}):{server(id)}}}
    
.. link-button:: https://carl.gg/t/1217391
    :type: url
    :text: Tag Import
    :classes: btn-outline-primary btn-block

.. raw:: html

    <meta property="og:title" content="Niloc#0421's Tags" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:site_name" content="Custom Tags">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Find Niloc#0421's tags here!" />
    <meta name="theme-color" content="#2980B9">