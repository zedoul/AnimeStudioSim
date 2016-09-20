﻿label start:
    #initialize the class objects at runtime here instead of python init so object will be saved
    $anime = Anime("Macross Delta")
    $anime.funds = 20
    $anime.plot = 2.5
    # $anime.storyboard = 3
    # $anime.character_development = 0.5
    # $anime.character_design = 1.5
    # $anime.background = 2.5
    # $anime.animation = 3.5
    # $anime.ost = 2
    # $anime.op_ed = 1
    # $anime.voice_acting = 0.5
    #stats for characters
    $yukari_stats = Stats("Yukari")
    $mayumi_stats = Stats("Mayumi")
    $sumiko_stats = Stats("Sumiko")
    $yuuko_stats = Stats("Yuuko")
    $shunsuke_stats = Stats("Shunsuke")
    #some placeholder values
    $yukari_stats.proficiency = renpy.random.randint(1,10)
    $yuuko_stats.proficiency = renpy.random.randint(1,10)
    $sumiko_stats.proficiency = renpy.random.randint(1,10)
    $mayumi_stats.proficiency = renpy.random.randint(1,10)
    $shunsuke_stats.proficiency = renpy.random.randint(1,10)
    #15 stars is the max number of stars we have, * 100 to convert it to percentage
    $anime.story_progress = int((anime.plot + anime.storyboard + anime.character_development) / 15.0 * 100.0)
    $anime.art_progress = int((anime.character_design + anime.background + anime.animation) / 15.0 * 100.0)
    $anime.music_progress = int((anime.op_ed + anime.ost + anime.voice_acting) / 15.0 * 100.0)
    #jump game_start
    jump week_6_6

init python:
    import datetime
    GREEN_COLOR = "{color=#1E824C}"
    RED_COLOR = "{color=#C0392B}"
    MINUS_SIGN = "{font=fonts/Delius-Regular.ttf}{size=+15}- {/size}{/font}"
    POSITIVE_SIGN = "{font=fonts/Delius-Regular.ttf}{size=+15}+ {/size}{/font}"
    CLOSE_COLOR_TAG = "{/color}"

init: 
    $_game_menu_screen = "navigation"
    $upgrade_proficiency_value = 0.5
    $upgrade_proficiency_cost = 2
    python:
        #A list of allowed stats to be modified during the game
        anime_stats = ["plot","character_development","storyboard",
                        "character_design","background","animation",
                        "voice_acting","op_ed","ost",
                        "quality_check","marketing","funds"]
        char_stats = ["stress","proficiency","happiness","management"]

        yukari_tasks = [Tasks("Raise Funds","Raise some money for [anime.name].",funds=1,stress=1,proficiency=-2,character_development = 2)
                        ,Tasks("Networking","Mingle around with people in the anime industry.",marketing=1)
                        ,Tasks("Read Books","Read books for knowledge.",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=-1)]

        yuuko_tasks = [Tasks("Sketch Character","Sketch some character designs.",character_design=1)
                        ,Tasks("Doodle","Doodle on a piece of paper.",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=1)]

        sumiko_tasks = [Tasks("Sketch Background","Sketch some backgrounds.",background=1)
                        ,Tasks("Doodle","Doodle on a piece of paper.",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=1)]

        mayumi_tasks = [Tasks("Compose Music","Compose OST for [anime.name].",ost=1)
                        ,Tasks("Practice","Get inspiration from other artists.",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=1)]

        shunsuke_tasks = [Tasks("Writing","Work on the scenario for [anime.name].",storyboard = 1)
                        ,Tasks("Practice","Hone your writing skills",proficiency=0.5)
                        ,Tasks("Relax","Spend the day taking it easy.",happiness=1,stress=1)]

    #game variables
    $current_week = 1
    # Day limits, 0 = Mon, 5 = Sat
    # current_date e.g '8/30'
    $days_array = ["Mon","Tues","Wed","Thurs","Fri","Sat"]
    $current_day = 0
    $current_date = datetime.date(2016,3,20)
    $game_casual = False
    $task_ready = False
    $side_nav_interaction = True
    $show_floating_buttons = True
    $upgrade_tooltip_color = "#2ecc71"
    $initial_week = True

    #upgrade screen
    $upgrade_tooltip_default = "Send your team for training! This will increase their Proficiency stats."
    $upgrade_tooltip_complete = "Success!"
    $upgrade_tooltip = ""
    $upgrade_selection_count = 0
    $yukari_upgrade = Outsource.NOT_SELECTED
    $yuuko_upgrade = Outsource.NOT_SELECTED
    $sumiko_upgrade = Outsource.NOT_SELECTED
    $mayumi_upgrade = Outsource.NOT_SELECTED
    $shunsuke_upgrade = Outsource.NOT_SELECTED
    #task screen

    #outsource screen

    $outsource_tooltip = ""
    $outsource = Outsource()
    $outsource.selection_count = 0
    $outsource.cost = 1
    $outsource.value = 1
    #boolean to know whether they are selected
    $yukari_task_selected = False
    $yuuko_task_selected = False
    $sumiko_task_selected = False
    $mayumi_task_selected = False
    $shunsuke_task_selected = False
    #random names
    $random_company = ["Wadaka","Sokono","Kirodo","Matsura","Enshu","Nosata"
                        ,"Zekoy","Inoshi","Pokomi","Takiza","Kibono","Koiga","Vozobi"
                        ,"Asozo","Noyoko","Kibachi","Tamaza","Kirodo","Shinu","Pokomi","Koiga"]
    #animation director
    $random_names = ["Hayate","Haruto","Kaito","Nobu","Yuuto","Yoshiro","Takeshi","Souta"]
    $random_va_female = ["Shina","Kaoru","Kagami","Yoshike","Shizue","Akemi"]
    $random_va_male = ["Ryuichi","Motoki","Naizen","Naosuke","Seinosuke","Akihisa"]
    $anim_studio_dir = getRandomName()
    $anim_studio_expensive = getRandomCompany() + " Studios"
    $anim_studio_cheap = getRandomCompany() + " Studio"
    $anim_studio = "Default Studios"
    $va_choice = "Talent Agency"
    #va_letter
    #va defaults to harem
    $va_a = "Bradley"
    $va_b = getRandomFemaleName()
    $va_c = getRandomFemaleName()
    $va_studio = getRandomCompany() + " Studio"
    $investor_marketing = True
    #positions for images
    $pos_farleft = Position(xalign = -0.045,yalign = 1.0)
    $pos_left = Position(xalign = 0.18,yalign = 1.0)
    $pos_middle = Position(xalign = 0.5,yalign = 1.0)
    $pos_middleright = Position(xalign = 0.65,yalign = 1.0)
    $pos_middleright_half = Position(xalign = 0.75,yalign = 1.0)
    $pos_farright = Position(xalign = 1.0,yalign = 1.0)
    $pos_right = Position(xalign = 0.92,yalign = 1.0)
    $pos_outerright = Position(xalign = 1.1,yalign = 1.0)
    $pos_textbox_right = Position(xalign = 0.85,yalign=1.0)
    

