Raffael#1372
============

.. contents:: Table of Tags

Original AFK COMMAND
--------------------

Made an "afk" tag. When it's set to ``on`` it will inform anyone that mentions you that you are afk. Setting it to ``off`` will turn it off. If you type a message after ``on`` it will be set as your away message, but if you leave it blank the tag will use the default away message. 

.. dropdown:: Source Code

    .. tagscript::

        {=(L1):{lower:{1}}}
        {=(A2+):{replace(|, - ):{args(2+)}}}
        {=(error):You must follow the `afk` command with either `on` or `off`.}
        {=(on):add}
        {=(off):del}
        {=(template):c:ar {{L1}} {user(id)}>{if({L1}==on): {if({list(0):{join(,):{A2+}}}!=):{A2+}|{replace(|, - ):{user}} is afk right now, send them a PM or wait for them to return.}}}
        {=(sel):{if({contains({L1}):on off}==false):error|{template}}}
        {override}{{sel}}
            
.. link-button:: https://carl.gg/t/41176
    :type: url
    :text: Tag Import
    :classes: btn-outline-primary btn-block

Back 4 Blood Card Lookup
------------------------

A Back 4 Blood card lookup command. Will display the card that best matches the provided search term alphabetically. Displays an error message if the provided search term does not match a card's name or a substring of that name.

For when you can't recall the specifics of a card, or want to discuss it within a Discord server without having to type out the card's description or stats.

I will attempt to keep the card images updated as future patches occur. These card images are current as of 2021-10-16.

This custom command is not affiliated with or endorsed by Back 4 Blood, Warner Bros. and it's divisions, or Turtle Rock Studios. I do not own these images, I am using them under the constraints of Fair Use as established in the Copyright Act of 1976, for nonprofit educational purposes.

The image below shows the command invocation for example purposes. This invocation will be deleted upon execution in the linked version of this tag. 

.. dropdown:: Source Code

    .. tagscript::

        {delete}
        {=(comment):This custom command is not affiliated with or endorsed by Back 4 Blood, Warner Bros. and it's divisions, or Turtle Rock Studios. I do not own these images, I am using them under the constraints of Fair Use as established in the Copyright Act of 1976, for nonprofit educational purposes.}
        {=(cardnames):Cadmin_reload Cadrenaline_fueled Cammo_belt Bammo_drop Cammo_for_all Cammo_mule Cammo_pouch Cammo_scavenger Cammo_stash Camped_up Cantibiotic_ointment Cavenge_the_fallen Cbatter_up Cbattle_lust Cbelt_clip Cberserker Cbody_armor Cbodyguard Cbomb_squad Cbounty_hunter Cbox_o'_bags Cbravado Cbrazen Cbreakout Cbroadside Cbuckshot_bruiser Ccanned_goods Ccharitable_soul Cchemical_courage Ccocky Ccold_brew_coffee Ccombat_knife Ccombat_medic Ccombat_training Ccompound_interest Cconfident_killer Ccontrolled_movement Ccopper_scavenger Ccross_trainers Cdash Cdefensive_maneuver Cdemolitions_expert Pdoc Cdouble_grenade_pouch Cdown_in_front! Cdurable Bdusty's_customs_assault_rifle Bdusty's_customs_handgun Bdusty's_customs_lmg Bdusty's_customs_shotgun Bdusty's_customs_smg Bdusty's_customs_sniper_rifle Cemt_bag Cenergy_bar Cenergy_drink Pevangelo Cexperienced_emt Bextra_padding Cface_your_fears Cfanny_pack Cfield_surgeon Cfire_in_the_hole! Cfit_as_a_fiddle Cfleet_of_foot Cfresh_bandage Cfront_sight_focus Cglass_cannon Cgrenade_pouch Cgrenade_training Cgroup_therapy Cguns_out Chazard_pay Bhazard_suit Cheadband_magnifier Cheavy_attack Cheavy_hitter Bhell_can_wait Chellfire Pheng Chi_vis_sights Chighwayman Bhired_gun Phoffman Pholly Chunker_down Chydration_pack Chyper-focused Cignore_the_pain Cimprovised_explosives Cin_the_zone Cinspiring_sacrifice Pjim Pkarlee Ckiller's_instinct Cknowledge_is_power Clarge_caliber_rounds Clife_insurance Cline_'em_up Clucky_pennies Cmad_dash Cmag_carrier Cmag_coupler Cmagician's_apprentice Cmandatory_pt Cmarathon_runner Cmarked_for_death Cmean_drunk Cmeatgrinder Cmedical_expert Cmedical_professional Cmeth_head Cmiraculous_recovery Pmom Cmoney_grubbers Cmotorcycle_helmet Cmotorcycle_jacket Cmugger Cmultitool Cnatural_sprinter Cneeds_of_the_many Cnumb Coffensive_scavenger Colympic_sprinter Con_your_mark Coptics_enthusiast Cover-protective Coverwatch Cpadded_suit Cpatient_hunter Cpep_in_your_step Cpep_talk Cpinata Cpoultice Cpower_reload Cpower_strike Cpower_swap Cpumped_up Cpyro Cquick_kill Creckless Creckless_strategy Creload_drills Crhythmic_breathing Cridden_slayer Crolling_thunder Crousing_speech Crun_and_gun Crun_like_hell Csadist Csadistic Csaferoom_recovery Cscar_tissue Cscattergun_skills Cscrewdriver Csecond_chance Cshare_the_wealth Psharice Cshell_carrier Cshooting_gloves Cshoulder_bag Cshredder Csilver_bullets Bslippery_when_wet Cslugger Csmelling_salts Cspeed_demon Cspiky_bits Csteady_aim Cstealthy_passage Cstimulants Cstock_pouch Csunder Csuperior_cardio Csupport_scavenger Csurplus_pouches Ctactical_vest Ctool_belts Ctrigger_control Ctrue_grit Ctunnel_vision Ctwo_is_one_and_one_is_none Burgent_care Cutility_belt Cutility_scavenger Cvanguard Cvitamins Pwalker Cweapon_scavenger Cweaponsmith Cwell_fed Cwell_rested Cwidemouth_magwell Bwindfall Cwooden_armor Cwounded_animal }
        {=(searchterm):{replace( ,_):{lower:{args}}}}
        {if({in({searchterm}):{cardnames}}==true):https://raw.githubusercontent.com/Raffael7777/B4B-Card-Images/main/{replace(P,Cleaner%20Cards/):{replace(B,Burn%20Cards/):{replace(C,Campaign%20Cards/):{cardnames({index({searchterm}):{replace({searchterm},. {searchterm} .):{cardnames}}})}}}}.png|`{replace(_, ):{searchterm}}` does not appear to match a card name or part of a card name. Double check your input and spelling and try again.}
            
.. link-button:: https://carl.gg/t/1111395
    :type: url
    :text: Tag Import
    :classes: btn-outline-primary btn-block

.. raw:: html

    <meta property="og:title" content="Raffael#1372's Tags" />
    <meta property="og:type" content="Site Content" />
    <meta property="og:site_name" content="Custom Tags">
    <meta property="og:image" content="https://i.imgur.com/AcQAnss.png" />
    <meta property="og:description" content="Find Raffael#1372's tags here!" />
    <meta name="theme-color" content="#2980B9">