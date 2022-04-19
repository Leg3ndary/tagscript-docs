_Leg3ndary#5759
===============

.. contents:: Table of Tags

Shell Cloud Command
-------------------

Working this out took a lot of time, however I'm proud to show the tagscript community the first tag that can save data through the bot, **you don't have to do any setting up.** (Other then importing of course)

You might recall **Raffael** made a tag where you would setup a role and then guess the number, you also might remember a user named **Squidtoon** made an api that did similar things however he removed his project from repl where it was hosted...

**What?**

**You can use this tag to do something similar to the cbsays tag where you can post a shell with text on it, you can also view other users posts or the latest post!**

**Why?**
This is just the general idea of using an api and python to interact through embed images, for those of you who don't know what an API is, its an "application program interface", you send a request to a site which then can give you something back, thats basically what I did. You send a request to a repl, the program will then save it to another further external cloud db known as mongodb (There are problems with saving data through repl which is why this part is needed).

**Usage:**

.. tagscript::

    ?shell add <Word>
    Your word must be less then or 10 characters
    ?shell show <Index>
    View already posted words, must be a number eg. view the 7th word added with the add command
    USE 0 OR LATEST TO VIEW LATEST POST
    ?shell cache
    Shows the Cache which you can use to view words with the show command

⚠️ **Warning.** ⚠️  

People are naturally stupid. In short people will be able to use words that shouldn't be used. For this reason I highly recommend this tag be marked nsfw.

Tag does not use any commands.

.. dropdown:: Source Code

    .. tagscript::

        {=(Comment): Tag by _Leg3ndary :D Nothing should be edited in this tag... other then the variables below...}

        {embed(color):{user(color)}}
        {=(prefix):?}
        {=(command_name):shell}

        {=(Comment): Don't touch anything below}

        {=():}

        {=(len_args):{index(■):{args} ■}}
        {=(type):{lower:{args(1)}}}

        {=({type}):/error}
        {=(dev/show):dev/show}
        {=(cache):dev/cache}
        {=(show):show/{if(latest=={lower:{2}}):0|{args(2)}}/{unix}}
        {=(add):add/{if(=={2}):Blank|{args(2)}}/{unix}}

        {{if(/error=={{type}}):embed(title):Error}}
        {{if(/error=={{type}}):embed(description):Subcommand {if(=={args(1)}):__`Blank`__|`{lower:{args(1)}}`} not found...
        Available options are:
        ```asciidoc
        = {prefix}{command_name} add <Word> =
        [ Your word must be less then or 10 characters ]
        = {prefix}{command_name} show <Index> =
        [ View already posted words, must be a number eg. view the 7th word added with the add command ]
        [ USE 0 OR LATEST TO VIEW LATEST POST THIS MIGHT NOT WORK THOUGH ]
        = {prefix}{command_name} cache =
        [ Shows the Cache which you can use to view words with the show command ]
        ```}}

        {{if(dev/cache=={{type}}):embed(title):Cache}}
        {{if(dev/cache=={{type}}):embed(description):This link shows the cache which will be formatted like so:
        ```
        {"1":"Carl-bot","2":"Hello"}
        ```
        [__`Cache`__](https://leg3ndarytagscript.tenshibot.repl.co/dev/cache)}}

        {=(endpoint):{if(/error!={{type}}):{{type}}}}

        {=(api_endpoint):https://leg3ndarytagscript.tenshibot.repl.co/{endpoint}}

.. link-button:: https://carl.gg/t/856897
    :type: url
    :text: Tag Import
    :classes: btn-outline-primary btn-block

Suspicion Command
-----------------

Check for alts using a system of checks with each being given their own weight, in addition see other info about the user to manually determine if a user is "sus".

.. tagscript::

    {=(ud.seconds.points):3} {=(README):Users account age is under 24 hours old, usually an alt MAKE THIS THE BIGGEST NUMBER}
    {=(ud.minutes.points):2} {=(README):Users account age is 1-30 days old, could be an alt would recommend keeping an eye on the user}
    {=(ud.hours.points):1} {=(README):Users account age is 1-12 months old, again could be an alt but not likely}
    {=(ud.days.points):0} {=(README):Users account age is 1+ years old, most likely not an alt but could be one}
    {=(ujd.seconds.points):2} {=(README):Users account age in server is under 24 hours old, new memberMAKE THIS THE BIGGEST NUMBER}
    {=(ujd.minutes.points):1} {=(README):Users account age in server is 1-30 days old, not a new member but not really an old member}
    {=(ujd.hours.points):0} {=(README):Users account age in server is 1-12 months old, would be considered seasoned or at least an old member}
    {=(ujd.days.points):0} {=(README):Users account age in the server is 1+ years old, old member}
    {=(ua.default.points):3} {=(README):Is the users avatar a default one? Most alts don't change pfps which is a dead giveaway}
    {=(ua.nitro.points):-1} {=(README):Does the user have a .gif avatar? Not many people have nitro for an alt(s) Negative number here because user has nitro}
    {=(un.points):1} {=(README): Has the user changed his/her nickname? Alts don't usually change their nickname, Disable this with "0" if needed}

.. dropdown:: Source Code

    .. tagscript::

        {=(COMMENT): Change the prefix and the recommended action taken if needed}
        {=(tag.prefix):?}
        {=(preset.punishment):warn}
        {=(preset.reason):Please don't use alts as they are against our rules.}


        {=(COMMENT): None of these should be changed unless you know what your doing and even then not really needed basically finds the basic vars you need and sets a var with all the default variable avatars}
        {=(user.days):{td:{target(created_at)}}}
        {=(user.join.days):{td:{target(joined_at)}}}
        {=(default.avatars):https://cdn.discordapp.com/embed/avatars/0.png https://cdn.discordapp.com/embed/avatars/1.png https://cdn.discordapp.com/embed/avatars/2.png https://cdn.discordapp.com/embed/avatars/3.png https://cdn.discordapp.com/embed/avatars/4.png}

        {=(Comment): This is a limiter to prevent the embed from breaking change it to increase the number of roles seen-or decrease it}
        {=(limiter):15} 
        {=(user.roleids.sub):{target(roleids)}}
        {=(user.roleids.stuff):{index(abc):{target(roleids)} abc}}
        {=(user.roleids.stuff):{if({user.roleids.stuff}>{limiter}):{replace({user.roleids.sub(+{m:trunc({user.roleids.stuff}-{limiter})})},):{target(roleids)}|{target(roleids)}}}}
        {=(user.roleids.ping):<@&{replace( ,> <@&):{user.roleids.stuff}>}}
        {=(user.roleids.ping):{if({user.roleids.ping}==<@&>):None|{replace(<@&>,):{user.roleids.ping}}}}
        {=(user.roleids.list):{target(roleids)}}

        {=(COMMENT):Sets the sus.score to 0 so that it can calculate the later values in this command}
        {=(sus.score):0} 

        {=(COMMENT): THIS IS THE POINTS SYSTEM, IT IS ESSENTIAL YOU READ AND UNDERSTAND THIS}
        {=(COMMENT): This determines what level suspicion the user has, the bigger the number the more suspicion 0 means nothing and it won't affect the final variable itself, use that to disable parts of the command, you can have values with negatives to make the suspicion score smaller (will make the final score less sus) more is explained about it beside the var itself}
        {=(ud.seconds.points):3} {=(README):Users account age is under 24 hours old, usually an alt MAKE THIS THE BIGGEST NUMBER}
        {=(ud.minutes.points):2} {=(README):Users account age is 1-30 days old, could be an alt would recommend keeping an eye on the user}
        {=(ud.hours.points):1} {=(README):Users account age is 1-12 months old, again could be an alt but not likely}
        {=(ud.days.points):0} {=(README):Users account age is 1+ years old, most likely not an alt but could be one}
        {=(ujd.seconds.points):2} {=(README):Users account age in server is under 24 hours old, new memberMAKE THIS THE BIGGEST NUMBER}
        {=(ujd.minutes.points):1} {=(README):Users account age in server is 1-30 days old, not a new member but not really an old member}
        {=(ujd.hours.points):0} {=(README):Users account age in server is 1-12 months old, would be considered seasoned or at least an old member}
        {=(ujd.days.points):0} {=(README):Users account age in the server is 1+ years old, old member}
        {=(ua.default.points):3} {=(README):Is the users avatar a default one? Most alts don't change pfps which is a dead giveaway}
        {=(ua.nitro.points):-1} {=(README):Does the user have a .gif avatar? Not many people have nitro for an alt(s) Negative number here because user has nitro}
        {=(un.points):1} {=(README): Has the user changed his/her nickname? Alts don't usually change their nickname, Disable this with "0" if needed}

        {=(COMMENT):Checking and determining how old the account is and then adding sus points based on it}
        {=(sus.score):{if({in(seconds ago):{user.days}}==true):{m:{sus.score}+{ud.seconds.points}}|{sus.score}}}
        {=(sus.score):{if({in(minutes ago):{user.days}}==true):{m:{sus.score}+{ud.minutes.points}}|{sus.score}}}
        {=(sus.score):{if({in(hours ago):{user.days}}==true):{m:{sus.score}+{ud.hours.points}}|{sus.score}}}
        {=(sus.score):{if({in(days ago):{user.days}}==true):{m:{sus.score}+{ud.days.points}}|{sus.score}}}

        {=(COMMENT):Same as above except its checking account age in the server or how long he/she has been in the server}
        {=(sus.score):{if({in(seconds ago):{user.join.days}}==true):{m:{sus.score}+{ujd.seconds.points}}|{sus.score}}}
        {=(sus.score):{if({in(minutes ago):{user.join.days}}==true):{m:{sus.score}+{ujd.minutes.points}}|{sus.score}}}
        {=(sus.score):{if({in(hours ago):{user.join.days}}==true):{m:{sus.score}+{ujd.hours.points}}|{sus.score}}}
        {=(sus.score):{if({in(days ago):{user.join.days}}==true):{m:{sus.score}+{ujd.days.points}}|{sus.score}}}

        {=(COMMENT): Checking if the user has a nitro pfp or if its just a regular default pfp in addition we'll check the discriminator as if it has a 1111 or 0001 or something like that we know they probably changed it and has nitro}
        {=(sus.score):{if({in({target(avatar)}):{default.avatars}}==true):{m:{sus.score}+{ua.default.points}}|{sus.score}}}
        {=(sus.score):{if({in(.gif):{target(avatar)}}==true):{m:{sus.score}+{ua.nitro.points}}|{sus.score}}}
        {=(COMMENT): This list below is what we'll be checking... Edit as you please it will also check if we've determined he/she already has nitro so we don't double it up}
        {=(sus.discrim):0001 0002 0003 0004 0005 0006 0007 0008 0009 1111 2222 3333 4444 5555 6666 7777 8888 9999 2020 2021 1000 2000 3000 4000 5000 6000 7000 8000 9000}
        {=(sus.score):{and({contains({replace({user(name)}#,):{user(proper)}}):{sus.discrim}}==true|{in(.gif):{target(avatar)}}==false):{m:{sus.score}+{ua.nitro.points}}|{sus.score}}}

        {=(COMMENT):Has the user changed his or her name since joining? Again you can disable this if you want by changing un.points to 0}
        {=(sus.score):{if({target}=={target(name)}):{m:{sus.score}+{un.points}}|{sus.score}}}

        {=(COMMENT):Checking how many roles the user has, had a problem if the user had 1 or 0 roles would output 0 no matter what so the bottom block checks if its 1 or 0 and changes the above value to the correct one}
        {=(user.roleids.number):{index($$$):{{target(roleids)}} $$$}}
        {=(user.roleids.number):{if({user.roleids.list(1)}=={user.roleids.list(2)}):{if({user.roleids.list(1)}==):0|1}|{user.roleids.number}}}

        {=(COMMENT):Taking all the scores checking if there negative and then adding if they aren't This determines the final percentage and embed color which is why you must follow the points system correctly ^ find above}
        {=(total.score):{m:{if({m:sgn({ud.seconds.points})}==-1):0|{ud.seconds.points}}+{if({m:sgn({ujd.seconds.points})}==-1):0|{ujd.seconds.points}}+{if({m:sgn({ua.default.points})}==-1):0|{ua.default.points}}+{if({m:sgn({ua.nitro.points})}==-1):0|{ua.nitro.points}}+{if({m:sgn({un.points})}==-1):0|{un.points}}}}

        {=(COMMENT):Finally determining the percentage since truncate can't cut of to a certain decimal it multiplies by 10000 then truncates and divides by 100 which gives it the decimal, this could be in one block but I've left it to multiple so you can edit/better understand it}
        {=(sus.score):{m:{sus.score}/{total.score}}}
        {=(sus.score):{if({target(proper)}=={server(owner)}):0.00|{sus.score}}} {=(README): Just checking if the person is the owner}
        {=(sus.score):{m:{sus.score}*10000}}
        {=(sus.score):{m:trunc({sus.score})}}
        {=(sus.score):{m:{sus.score}/100}}

        {=(COMMENT):Embed color, don't touch if you don't know how it works, if you want to have just one color change the bottom block with the hex you want}
        {=(embed.color):{if({sus.score}<=20.001):7ED321|{if({sus.score}<=40.001):BBDD1F|{if({sus.score}<=60.001):F8E71C|{if({sus.score}<=80.001):E4751C|D0021B}}}}}
        {embed(color):#{embed.color}}

        {=(COMMENT):The final punishment if recommended}
        {=(preset.punishment.final):{if({sus.score}>=90.001):Most likely an alt, command to {preset.punishment}: ```
        {tag.prefix}{preset.punishment} {target(id)} {preset.reason}
        ```|}}
    
.. link-button:: https://carl.gg/t/715929
    :type: url
    :text: Tag Import
    :classes: btn-outline-primary btn-block

.. raw:: html

    <meta property="og:title" content="_Leg3ndary#5759's Tags" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:site_name" content="Custom Tags">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Find _Leg3ndary#5759's tags here!" />
    <meta name="theme-color" content="#2980B9">