﻿define fourth_w = Character('Fourth Place Winner', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define manager = Character('Manager', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define environmentalist = Character('Environmentalist', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define office_l = Character('Office Lady', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define police_o = Character('Police Officer', color="#000",ctc="ctc_fixed",ctc_position="fixed")
define mother = Character("Boy's Mother", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define boy = Character("Little boy", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define cafe_owner = Character("Café Owner", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define schoolgirls = Character("Schoolgirls", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define pedestrian = Character("Pedestrian", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define teacher = Character("Teacher", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define neighbour = Character("Neighbour", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define clique = Character("Clique Leader", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define clique_girl = Character("Clique Girl", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define old_lady = Character("Old Lady", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define librarian = Character("Librarian", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define miki = Character("Miki", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define stranger = Character("Stranger", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define mamoru = Character("Mamoru", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define electrician = Character("Electrician", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define little_girl = Character("Little Girl", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define restaurant_owner = Character("Restaurant Owner", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define man = Character("Man", color="#000",ctc="ctc_fixed",ctc_position="fixed")
define hp_guy = Character("David Buki", color="#000",ctc="ctc_fixed",ctc_position="fixed")

#Burnout scenario (Stress high, happiness low)
label dead_burnout(character):
    play music sad_music fadein 2.0
    scene cafe with fade
    show yukari at left
    if character.name == "Mayumi":
        show mayumi_f sad_angry at right
    elif character.name == "Yuuko":
        show yuuko sad_angry  at right
    elif character.name == "Sumiko":
        show sumiko sad_angry  at right
    elif character.name == "Shunsuke":
        show shunsuke sad_angry at right
    with dissolve
    if character.name == "Mayumi":
        m "Yukari, we’ve been friends for a long time and I hate to do this to you, but I can’t keep working on [anime.name]. "
    elif character.name == "Yuuko":
        yuu "I have to talk to you… I’m really sorry, but… I’m leaving the team."
    elif character.name == "Sumiko":
        s "Agh, I can’t take this anymore! I’m tired of working on [anime.name]."
    elif character.name == "Shunsuke":
        ss "Yukari, I need to tell you something. After considering my options carefully, I’ve decided to leave the team."
    show yukari sad
    y "What? Why? Didn't all of us promise to work on this project until the very end?"
    if character.name == "Mayumi":
        m "If you really want to know, it’s because you’re stressing me out. I don’t enjoy working with you anymore!"
        m "I don’t think we can work together and still be friends… and I’d rather stay your friend, even if it means losing [anime.name]. I’m sorry, Yukari, but I have to leave the team." 
    elif character.name == "Yuuko":
        yuu "I know, but… Working on [anime.name] is making me depressed. If I stay, I’ll go crazy. I’m really sorry…"
    elif character.name == "Sumiko":
        s "Yeah, WE agreed to work on it—together, as a team! But you don’t care about anyone’s opinion except your own. I can’t stand it. Sorry it had to come to this, but I’m out."
    elif character.name == "Shunsuke":
        ss "We did promise, but I’m under too much pressure now. It’s not healthy. I hope you understand, Yukari. For my own sake, I have to leave."
    
    show yukari sad
    y "Wait, [character.name]! Come back!"
    "[character.name] has left your group..."
    "Yukari and the others try to continue on alone, but it’s no use. Without a complete team, [anime.name] is doomed to remain just a dream."
    $renpy.full_restart()
label dead_burnout_yukari:
    play music sad_music fadein 2.0
    scene studio with fade
    show yukari sad at left
    with dissolve
    y "This is too stressful for me... I guess making my own anime was never possible in the first place."
    y "Sigh... If only I was more competent..."
    "Yukari decides to give up on her dream and without a leader, [anime.name] is no more."
    $renpy.full_restart()

#ran out of funds
label dead_no_funds:
    play music sad_music fadein 2.0
    scene studio with fade
    show yukari at pos_left
    show sumiko at pos_right
    show yuuko at pos_outerright behind sumiko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    y "Everyone, we need to talk."
    "The seriousness of her tone makes the others look up from their work." 
    show mayumi worry
    m "Is something wrong?" 
    y "Yes." 
    "She takes a deep breath. They won't like hearing this, but she has no choice. They can't ignore the truth." 
    show yukari sad_angry
    y "We don't have enough funds to continue working on [anime.name]." 
    show sumiko sad_angry
    s "What?!" 
    show shunsuke sigh
    ss "I knew we were in a bad state, but I didn't know it was this bad." 
    y "I'm sorry. I wish it wasn't true." 
    show yuuko sad
    yuu "Then…" 
    show yukari sad
    y "The best thing to do is to end the project now." 
    show mayumi sad_angry
    m "W-wait… maybe we can raise some more funds, or…" 
    "She trails off when Yukari shakes her head." 
    y "I went over everything countless times. We can't raise enough money in the time we have. We'd just be delaying the inevitable." 
    s "What if we won the lottery? I'll go buy tickets!" 
    ss "That's a good way to lose money, not earn it." 
    y "I'm sorry, everyone. Rather than sink deeper into debt, we need to end it here. As the director of [anime.name], I'm disbanding the team." 
    show sumiko worry
    s "Nooooo!" 
    m "It doesn't have to be forever, does it?" 
    ss "That's right. In a few years, we can all get together and try again." 
    y "I hope so." 
    yuu "Don't worry, Yukari. When the time is right, we'll be there to work on [anime.name]." 
    s "Yeah!" 
    y "Thanks, everyone." 
    "Despite their reassuring words and the knowledge that they'll remain friends she can count on, Yukari can't help but feel depressed as they close up the studio for good."
    "Maybe someday, she'll be able to make her own anime… but for now, her dream is dead."
    $renpy.full_restart()
#job offering
label random_1:
    $rd_c = RandomCharacter(["m"])
    $company = getRandomCompany()
    scene studio_main with fade
    show yukari at left
    if rd_c.p == "yuu":
        show yuuko at right
    elif rd_c.p== "ss":
        show shunsuke at right
    elif rd_c.p == "s":
        show sumiko at right
    with dissolve

    rd_c.say "Yukari, there’s something I have to tell you."
    y "What is it, [rd_c.person]? You can tell me anything."
    rd_c.say " I’ve been scouted by [company]."
    if rd_c.p == "yuu":
        show yuuko sad
        rd_c.say "I visited their studio, and I really feel at home there… N-not that I don’t feel at home here, but…"
    elif rd_c.p == "s":
        rd_c.say "They need an artist and my style works perfectly with theirs."
    else:
        rd_c.say "[company] is well-established and offers excellent chances for career advancement."
    rd_c.say "I just wanted to let you know that I am considering the offer."
    show yukari worry
    y "(Thinking to herself) Oh no! We can’t finish [anime.name] if [rd_c.person] takes another job!"
    y "What should I do?"
    menu:
        "Assume [rd_c.person] will get over it":
            $rechoice_1_1(rd_c.stats)
        "Offer [rd_c.person] money from [anime.name] funds {space=15}{image=small_moneybag.png} [JOB_OFFER_FUNDS]":
            show yukari sad_angry
            y "I understand that [company] is a great company to work with, but won't you consider staying with us?"
            y " I can pay you some money for your work, if that'll change your mind?"
            if rd_c.p == "yuu" or rd_c.p == "s":
                if rd_c.p == "yuu":
                    show yuuko laugh_eyes_closed
                elif rd_c.p == "s":
                    show sumiko laugh_eyes_closed
                rd_c.say "That'll do, honestly it was mostly because of my parents nagging at me to find a real job to earn money, which has reached a tipping point because I currently don't earn any money."
            else:
                rd_c.say "Yes that just changed my mind. Having pocket money sounds great, considering that my parents wanted me to get a part time job to 'learn' how to survive in society."
                rd_c.say "With that sum of money, I'll be able to convince my parents that I'm learning life skills through this project."
            $rechoice_1_2()
    return

#Request for Raise in Salary/Allowance or Money
label random_2:
    scene cafe with fade
    $rd_c = RandomCharacter()
    show yukari worry at left
    if rd_c.p == "m":
        show mayumi_f sad at right
    elif rd_c.p == "s":
        show sumiko sad at right
    elif rd_c.p == "yuu":
        show yuuko sad at right
    else:
        show shunsuke sad at right
    with dissolve
    y "Hey [rd_c.person], is something wrong? You seem troubled today."
    if rd_c.p == "m":
        rd_c.say "Thanks, Yukari, I’m glad you noticed. I’m in a bit of financial trouble…"
        rd_c.say "My uncle had a stroke and our family can’t afford the healthcare costs."
        rd_c.say "Do you have any ideas on how I can get some money?"
    elif rd_c.p == "yuu":
        rd_c.say "O-oh, I didn’t think you’d notice…"
        rd_c.say "My grandfather is in the hospital and we’re struggling to pay for his treatment…"
        rd_c.say "I want to get money to help out, but I don’t know how…"
    elif rd_c.p == "s":
        rd_c.say "If I told you my secret plan for world domination was in jeopardy, would you believe me?"
        rd_c.say "Sorry. I’ve tried to joke to keep my spirits up, but it’s not working. See, my grandfather is undergoing expensive medical treatments, and I’m afraid we’ll run out of money."
        rd_c.say "Any ideas?"
    else:
        rd_c.say "I didn’t intend to trouble you with this, but if it’s that obvious, I suppose I should explain."
        rd_c.say "My cousin was in a bad car accident. She’s alive, but the medical bills are exorbitant."
        rd_c.say "If I’ve been distracted, it’s because I’m trying to think of a way to get the money to help her."
    y "Oh no! Thank you for telling me. Let me think…"
    menu:
        "Tell [rd_c.person] to approach their bank for loans":
            y "Have you tried getting a loan from your bank?"
            rd_c.say " Not yet…"
            y "I’ve heard that bank loans are pretty reasonable nowadays. Give it a try."
            rd_c.say "Okay…"
            $rechoice_2_1(rd_c.stats)
        "Give [rd_c.person] money from the project funds {space=15}{image=small_moneybag.png} [REQUEST_SALARY_FUNDS]":
            y "Here."
            rd_c.say "What? But this money is meant for [anime.name]!"
            y "Take it. You’re a friend and part of the team, so we should help you out. Besides, your family’s health is more important than an anime."
            rd_c.say "Thank you so much…"
            $rechoice_2_2()
    return

#Conflict during Team Meetings 
label random_3:
    $rd_c = RandomCharacter()
    scene studio_main with fade
    show mayumi at left
    if rd_c.p == "yuu":
        show yuuko at right
    elif rd_c.p == "s":
        show sumiko at right
    else:
        show shunsuke at right
    with dissolve
    m "Hey guys! Check out the new OST I wrote for [anime.name]!"
    "The team listens as Mayumi plays the OST for everyone to hear."
    if rd_c.p == "yuu":
        show yuuko worry
        rd_c.say "W-wait, the OST’s title… is this the leitmotif for the antagonist? But it doesn’t fit his style at all…"
    elif rd_c.p == "s":
        show sumiko sad_angry
        rd_c.say "It’s a little bland, isn’t it? Can’t you improve it? Maybe change the rhythm?"
    else:
        show shunsuke angry
        rd_c.say "No, no, no, this song’s tone doesn’t fit the scene at all!"
    show mayumi sad_angry
    m "Do you have to be so critical? I spent a long time working on it!"
    rd_c.say "You did ask for opinions."
    m "Yeah, but I didn’t think you’d say that…"
    rd_c.say "So you wanted me to lie?"
    m "I’d like to see you come up with a better OST!"
    show yukari at pos_left 
    show mayumi at pos_farleft
    with dissolve 
    y "Guys, please calm down!"
    menu:
        "Agree with [rd_c.person]":
            $rechoice_3_1(rd_c.stats)
            show yukari sad
            y "I'm sorry, Mayumi, but [rd_c.person] is right."
            show mayumi sad_angry
            m "W-what? But I…"
            rd_c.say "See?"
            y "You're a great composer, but this song needs work."
            m "Aw, okay…"
        "Agree with Mayumi":
            $rechoice_3_2()
            show yukari sad
            y "I'm sorry, [rd_c.person], but Mayumi is right."
            show mayumi happy
            m "Yes!"
            rd_c.say "Huh? But I was so sure…"
            m "Thanks, Yukari!"
            y " There's no need to thank me. The song is fine, and that's all there is to it.."
        "Try to distract them by changing the topic":
            show yukari happy
            y "Have you guys listened to the new song released by Love Live? It's selling like hotcakes right now and must be really good."
            if rechoice_3_3(rd_c.stats):
                m "I purchased their new album a few days ago. It's hard to describe how amazing they are, so I'll just let you guys listen to understand!"
                "Mayumi brings out her phone from her pocket and plays one of the tracks on the new album released by Love Live."
                "Everyone seems to be mesmerized by it."
                y "(thinking to self): That was close... Luckily I managed to distract them from their pointless argument."
            else:
                "Yukari's attempt to distract Mayumi and [rd_c.person] from their argument seems to be a futile attempt. She can feel that both of them are feeling grumpy "
    return

#Interview Request for Aspiring Anime Producers
label random_4:
    $rd_c = RandomCharacter()
    $company = getRandomCompany()
    scene studio_main with fade
    show yukari at left
    if rd_c.p == "yuu":
        show yuuko at right
    elif rd_c.p == "s":
        show sumiko at right
    elif rd_c.p == "m":
        show mayumi_f at right
    else:
        show shunsuke at right
    with dissolve
    y "Wow, [anime.name] is getting quite a lot of attention online!"
    y "[company] invited me to an interview for aspiring anime producers!"
    if rd_c.p == "yuu":
        show yuuko happy
    elif rd_c.p == "s":
        show sumiko happy
    elif rd_c.p == "m":
        show mayumi_f happy
    else:
        show shunsuke happy
    rd_c.say "Really? That's awesome! You should go!"
    rd_c.say "Think of the publicity this interview will bring. [company] is very well regarded in the anime industry."
    y "I don't know… The last interview conducted by [company] ruined an aspiring producer because the focus shifted from anime to his private life."
    menu:
        "Attend the interview":
            if rechoice_4_1():
                "Yukari attends the interview and manages to speak to the public fluently. She’s happy she decided to attend this interview which should give [anime.name] a nice boost in publicity."
            else:
                "Yukari attends the interview, but it’s just as nightmarish as the rumors claim."
                "Fortunately, she’s young enough that the interviewer couldn’t dig up too much dirt about her private life, but she’s still humiliated and more than happy to leave once it finally ends."
        "Do not attend the interview":
            $rechoice_4_2()
            y " I’m going to decline the offer."
            if rd_c.p == "yuu":
                show yuuko sad
            elif rd_c.p == "s":
                show sumiko sad
            elif rd_c.p == "m":
                show mayumi_f sad
            else:
                show shunsuke sad
            rd_c.say "What?"
            y "It looks good on the surface, but it’s way too risky."
            rd_c.say "Aw, I thought it was a good idea…"
        "Send [rd_c.person] to be interviewed instead":
            y "Why don’t you go?"
            if rd_c.p == "yuu":
                show yuuko worry
            elif rd_c.p == "s":
                show sumiko worry
            elif rd_c.p == "m":
                show mayumi_f worry
            else:
                show shunsuke worry
            rd_c.say "M-Me?"
            y "Yes, since you think it’s such a good idea."
            rd_c.say "Well, all right."
            $rechoice_4_3(rd_c.stats)
    return

# Receiving Anonymous Troll E-Mails 
label random_5:
    scene studio_main with fade
    show yukari at pos_left
    show mayumi sigh at pos_farleft behind yukari
    show sumiko sad at pos_middleright_half
    show shunsuke at Position(xalign = 1.05,yalign = 1.0) behind sumiko
    with fade
    m "What in the world is this? Have you guys checked the inbox recently?"
    s "Oh gross, not again! Who’s been sending all this ridiculous mail?"
    ss "Yukari, what do you make of this?"
    y "(Thinking to herself) These messages are pretty awful… How should I handle this?"
    $dice_number = renpy.random.randint(0,100)
    if dice_number <= choice_raise_funds_formula():
        show yukari happy
        show mayumi sad
        y " Come on, guys, don’t let some stupid emails get you down!"
        m "Did you read the things they said about us?"
        y "Yes, but I don’t care. This guy is clearly just a troll."
        m "You mean he’s waiting under a bridge to grab us when we cross?"
        s "Thank you in advance for my upcoming nightmares."
        y " I mean he’s trying to rile us. Don’t fall for it! We’re not going to let a bunch of spammy messages ruin our dream, are we? Of course not!"
        ss "Hah, the joke will be on him when [anime.name] is a hit."
        m "Yeah! Let’s get to work and show him what we’re capable of!"
        $rechoice_5_1_success()
    else:
        hide mayumi
        hide shunsuke
        hide sumiko
        show yukari sad at left
        show mayumi_f worry at right
        with dissolve
        "She can’t focus. Every time she tries to think of a solution, the discouraging comments from the email run through her mind."
        "What if they’re right? What if their team really is awful and [anime.name] is doomed to failure?"
        y "Ugh…"
        m "Yukari?"
        y "Leave me alone. I want to be by myself for a little bit…"
        "She can tell her attitude makes the others even more disheartened, but she’s too upset by the emails to care."
        $rechoice_5_1_failure()

    return
#A Suspicious Businessman Calls  
label random_6:
    $rd_c = RandomCharacter(["s","yuu"])
    scene studio_main with fade
    show yukari at left
    if rd_c.p == "m":
        show mayumi_f at right
    elif rd_c.p == "s":
        show sumiko at right
    with dissolve
    rd_c.say "Yes, I agree with you completely, sir, this advertising will help our project greatly!"
    rd_c.say "I’ll get back to you soon with the good news."
    "[rd_c.person] hangs up the phone."
    y "Who was that?"
    rd_c.say "An advertiser interested in working with us! He has a sure-success advertising program that can lift our publicity sky-high. It’s pretty expensive, but it’ll be worth it."
    y "Are you sure he can be trusted?"
    rd_c.say "Of course! He says he worked with many companies before!"
    y "I don’t know… it sounds kind of shady to me."
    menu:
        "Accept the advertising deal {space=15}{image=small_moneybag.png} [SUSPICIOUS_BUSINESSMAN_FUNDS]":
            #test this event later & emotes not done yet
            $rechoice_6_1()
            y "Well, let's give it a try."
            rd_c.say "Great!"
            "She calls the businessman back, and Yukari arranges payment for the advertising program. She and [rd_c.person] return to work."
            "An hour later, Shunsuke clears his throat."
            ss " I don't mean to interrupt, but I just read something important. There's a new scam going around."
            "Yukari has a sudden sinking feeling she won't like what he says."
            ss " This guy calls up small businesses and entrepreneurs and claims he's an advertiser who works with successful companies. Then he offers an advertising package to promote their business or project."
            ss "He uses dummy accounts to accept payment, so no one has tracked him down yet or gotten their money back."
            rd_c.say "Uh-oh…"
            ss "What's wrong? You and Yukari look like you're going to be sick. Oh no… Don't tell me you…"
            y "Damn… I can't believe I got scammed! I should have known it was too good to be true… "
        "Refuse the advertising deal":
            $rechoice_6_2()
            y "This isn’t a risk worth taking."
            if rd_c.p == "m":
                show mayumi_f sad_angry
            elif rd_c.p == "s":
                show sumiko sad_angry
            rd_c.say "But… but…"
            y "Eventually you’ll learn to judge when something sounds too good to be true."
            rd_c.say "I guess you’re right… I’m sorry."
            y "Don’t apologize! Anyone could be fooled by a conman."
            rd_c.say "Sure…"
    return

#Anime Convention During A Weekend 
label random_7:
    $rd_c = RandomCharacter()
    scene cafe with fade
    show yukari at left
    if rd_c.p == "s":
        show sumiko happy at right
    elif rd_c.p == "m":
        show mayumi_f happy at right
    elif rd_c.p == "ss":
        show shunsuke happy at right
    else:
        show yuuko happy at right
    with dissolve
    rd_c.say "Guess what, guys? I won VIP tickets to AnimeFest next week!"
    if rd_c.p == "s":
        show sumiko sad at right
    elif rd_c.p == "m":
        show mayumi_f sad at right
    elif rd_c.p == "ss":
        show shunsuke sad at right
    else:
        show yuuko sad at right
    rd_c.say "Oh no... there are only 4 tickets in this envelope."
    rd_c.say "That means one of us can’t go…"
    y "That's unfortunate that one of us will miss out on AnimeFest."
    y "But back to the main point, since we are VIPs, will we be able to interact with anime industry professionals?"
    if rd_c.p == "s":
        show sumiko at right
    elif rd_c.p == "m":
        show mayumi_f at right
    elif rd_c.p == "ss":
        show shunsuke at right
    else:
        show yuuko at right
    rd_c.say "Yes, that's an exclusive privilege for VIPs!"
    "Who should stay behind?"
    $rd_remaining_c = rd_c.remainingCharacters()
    $rd_stay_behind = False
    menu:
        "Tell Yuuko she won't be going" if "yuu" in rd_remaining_c:
            $rechoice_7_1(rd_c.stats)
            if rd_c.p == "s":
                hide sumiko
            elif rd_c.p == "m":
                hide mayumi_f
            elif rd_c.p == "ss":
                hide shunsuke
            show yuuko sad_angry at right with dissolve
            y  "Yuuko, I’d like you to stay here."
            yuu "Oh..."
            show yukari worry
            y "Don’t look so sad! It’s not anything against you. But since the character designs are pretty much completed, there’s not a lot of reason for you to go, right?"
            yuu "I understand…"
            y "Do you really?"
            yuu "Sure, I guess…"
        "Tell Sumiko she won't be going" if "s" in rd_remaining_c:
            $rechoice_7_1(rd_c.stats)
            if rd_c.p == "yuu":
                hide yuuko
            elif rd_c.p == "m":
                hide mayumi_f
            elif rd_c.p == "ss":
                hide shunsuke
            show sumiko worry at right with dissolve
            s "Whoa, whoa, why are you looking at me like that? You… no way, are you thinking I should stay behind?"
            y "Someone has to."
            s "Yeah, but why does “someone” have to be me?"
            y "Well, we have two artists. Yuuko can tell you what she learns from the professionals there. You wouldn’t argue that your sister should stay behind instead, would you?"
            s "Ugh, you sure know how to make a girl feel guilty."
        "Tell Shunsuke she won't be going" if "ss" in rd_remaining_c:
            $rechoice_7_1(rd_c.stats)
            if rd_c.p == "yuu":
                hide yuuko
            elif rd_c.p == "m":
                hide mayumi_f
            elif rd_c.p == "s":
                hide sumiko
            show shunsuke at right with dissolve
            y "Shunsuke, I think it’s best if you stay behind."
            ss "Why me?"
            y "How much can you really benefit from talking to industry professionals? Your writing style is your own, not theirs."
            ss "Yes, but—"
            y "Whereas the rest of us will benefit a lot more."
            ss "I could still—"
            y "Someone has to stay behind."
            ss "Oh, fine. I’ll do it for the team."
        "Tell Mayumi she won't be going" if "m" in rd_remaining_c:
            $rechoice_7_1(rd_c.stats)
            if rd_c.p == "yuu":
                hide yuuko
            elif rd_c.p == "s":
                hide sumiko
            elif rd_c.p == "ss":
                hide shunsuke
            y "Sorry, Mayumi, but would you mind staying behind?"
            show mayumi_f sigh at right with dissolve
            m "Aw, do I have to?"
            y "Only four of us can go, and I think the others need the experience more than you. Think of it as a compliment!"
            m "Sure… If you say so…"
        "Stay behind and let the rest go":
            $rechoice_7_2()
            hide shunsuke
            show mayumi_f at pos_outerright
            show yuuko at pos_right
            show sumiko at pos_middleright
            with dissolve
            y "You four go and have a good time. I’ll stay."
            show mayumi_f sigh
            m "Aw, Yukari, but—"
            y "No buts. I’ve made up my mind."
            show sumiko happy
            show yuuko happy
            s "See, that’s the sign of a good leader, everyone. Thanks, Yukari!"
            yuu "Yes, thank you."
            y "You better! I’m counting on you!"
            $rd_stay_behind = True    
    if rd_stay_behind:
        "Yukari stays at home during AnimeFest although she feels sad thinking of the others having fun without her. It’s balanced by the happiness she feels when she remembers their smiles and Sumiko calling her a good leader."
    else:
        "AnimeFest is both fun and informative, although Yukari can’t help but feel a little bad that she made one of the team members miss it all."
    return
# All-You-Can-Eat Ice-Cream 
label random_8:
    scene studio_main with fade
    show mayumi sigh at pos_farleft
    show yukari at pos_left
    show sumiko at right
    with dissolve
    "Mayumi sighs."
    m "Things haven’t been going so well lately…"
    s "I know, right? It's as if the whole world is conspiring against us."
    y "(thinking to herself) Hmm... We need to get our work done, but maybe I should take the team to the café for a treat?"
    menu:
        "Continue to work without a break at the café":
            $rechoice_8_1()
            "Yukari decides not to take a break."
            y "Come on, everyone, back to work. The sooner we make progress on [anime.name], the better we’ll all feel!"
            show mayumi
            m "I don’t know about that… but okay, I guess we should keep working…"
        "Announce the café break":
            y "Hey everyone, why don’t we take a break?"
            ss " Can we afford to?"
            y "We won’t get any work done if we’re unhappy. Let’s go to the café and relax for a little while. It’ll make us all feel better."
            m "She’s right. Let’s go!"
            scene cafe with fade
            show mayumi at pos_farleft
            show yukari at pos_left
            show sumiko at pos_right
            show yuuko at pos_outerright behind sumiko
            with dissolve
            yuu "I’ve never seen it so crowded here. What’s going on?"
            y "Let’s see… It looks like some sort of celebration."
            cafe_owner "That’s right! We’ve been open for a year now. To celebrate the anniversary, we’re having a special promotion: an ice cream buffet!"
            show sumiko happy
            s "Did you say ice cream BUFFET?"
            show mayumi happy
            m "All right! This is the best break we ever took!"
            "They spend more time at the café than Yukari expected, but a few hours of an ice cream buffet is enough to help the group forget their previous worries."
            $rechoice_8_2()
    return
#Street Musician Donation 
label random_9:
    scene street with fade
    show mayumi_f at right
    show yukari at left
    with dissolve
    "As guitar riffs fill the air, Mayumi stops to listen to the musician, eyes bright with excitement."
    show mayumi_f happy
    m "Wow, he’s pretty good!"
    show mayumi_f sad
    m "Oh no… he’s only gotten a few donations."
    y "Either this neighborhood doesn’t appreciate guitar music, or they don’t like supporting street performers."
    show mayumi_f happy
    m "But we do, right?"
    menu:
        "Continue walking home":
            show mayumi_f sigh
            "Mayumi’s face falls as Yukari keeps walking."
            y "Sorry, we have to worry about our own funds now. We can’t support random street performers."
            m "I see your point, but would a small donation really hurt?"
            show yukari sad_angry
            y "We can’t afford it."
            m "Okay…"
            "Despite her agreement, she looks back at the guitarist with an unhappy sigh as they walk away."
            $rechoice_9_1()
        "Donate some money":
            "Mayumi beams as Yukari approaches the guitarist."
            "The guitarist plays another song accordingly."
            show yukari happy
            y "Wow, that really is good."
            m "I can’t wait for work tomorrow. I have so many new ideas!"
            $rechoice_9_2()
    return

#Flowers for Charity
label random_10:
    scene street with fade
    show yukari at left with dissolve
    schoolgirls "Onee-sama! Would you be so kind as to buy our flowers?"
    schoolgirls "We're helping out the local cancer support organization!"
    y "What should I do? It is for charity… and I could pay for it personally."
    schoolgirls "We have many flowers, take your pick!"
    menu:
        "Buy the flowers":
            show yukari happy
            y "Sure, I’ll buy a flower."
            schoolgirls "Wow! Thank you very much!"
            "Yukari blushes, but smiles and hands them the money. They’re so happy, they can’t stop thanking her."
            schoolgirls "Thank you!"
            schoolgirls "Don’t mention it. Charities like these are very important. I’m just happy I could help out."
        "Politely refuse the girls":
            y "I’m sorry. I’m afraid I can’t help today."
            "She gives the girls a polite smile and continues on her way."
    return
        
#Shiny Object On The Ground 
label random_11:
    scene street with fade
    show yukari at left
    with dissolve
    show yukari worry
    y "Huh? What’s this?"
    "A shiny object in the crosswalk catches her eye and she wonders if it belongs to the nearby pedestrian who is crossing the road."
    y "I wonder if it belongs to him."
    menu:
        "Cross the road without paying heed to the object":
            $rechoice_11_1()
            show yukari
            "To her surprise, the other pedestrian doesn’t pick up the object, either."
            y "It looks like a pendant."
            "As she watches, a car speeds by and flattens the pendant. The pedestrian continues to walk, oblivious to what happened."
            show yukari sad
            y "Oh no! Well, either it wasn’t his, or it wasn’t worth much to him."
        "Attempt to pick up the object":
            $rechoice_11_2()
            "Yukari picks up what appears to be a pendant that dislodged from a necklace."
            "As she crosses the street, she pauses to pick up the object."
            y "It looks like a pendant, but there’s no chain. It must have fallen off."
            "She hurries back across the street, after the other pedestrian."
            y "Excuse me! Is this yours?"
            pedestrian "What? Oh! Yes, it is!"
            y "I found it in the crosswalk."
            pedestrian "The crosswalk?! I’m glad you found it before someone ran over it.  Thank you! Thank you so much!"
            y "Don’t mention it."
            "As she says goodbye to the pedestrian and heads home, her steps are a little lighter. It’s always a nice feeling to brighten someone’s day."
    return
#Homeroom Teacher Surprise Visit 
label random_12:
    #test later
    scene studio_main with fade
    teacher "Good afternoon, Yukari. How are you doing?"
    show yukari happy at left 
    with dissolve
    y "Oh my! This is unexpected. What brings you here?"
    teacher "I heard you started an anime studio, so I thought I’d stop by."
    "Yukari happily gives her former homeroom teacher a tour of the studio and introduces her to all of the team members. Everyone tells her a little bit about the anime and what they’re currently working on."
    teacher "I love the enthusiasm here. I’m so happy to see you’re doing well."
    y "Thank you, Sensei. I'm happy you took the time to visit!"
    $dice_number = renpy.random.randint(0,100)
    if dice_number <= choice_raise_funds_formula():
        $rechoice_12_1_success()
        teacher "Since you’re all working so hard, I’d like to give you something special."
        y "You don’t have to do that."
        teacher "I want to. This won’t take long."
        "She leaves the studio, and everyone gets back to work. Eventually she returns with a box filled with cookies for everyone."
        scene studio_main 
        show yukari at left
        with fade
        teacher "I hope you enjoy them."
        y "Sensei! Thank you!"
        teacher "In exchange, I expect to see a thrilling episode of [anime.name] on TV."
        y "You will!"
    else:
        $rechoice_12_1_failure()
        teacher "Any time. Goodbye, Yukari, and good luck!"
        y "Thank you!"
    return

#Where's my umbrella?
label random_13:
    scene studio_main with fade
    show yukari at left with dissolve
    y "Hmm, I can't help but feel I forgot something… Oh well, it’s probably my imagination."
    y "Oh no, where’s my umbrella?"
    "She suddenly remembers where she saw it last: on the table at home."
    menu:
        "Dash home as fast as possible to try and avoid the storm":
            scene street_rain with fade
            show yukari at left
            with dissolve
            play sound "music/sfx/rain.ogg" fadeout 1.0
            "With a sigh, Yukari breaks into a sprint. As she runs, the skies open up and rain pours down. She tries to run faster, but by the time she gets home, she’s completely soaked."
            "She tries to run faster, but by the time she gets home, she’s completely soaked."
            stop sound fadeout 1.0
            scene home with fade
            show yukari sad at left with dissolve
            y "F-freezing… n-need to warm up…"
            "She gets out of her wet clothes and dries off, but even once she dresses warmly and wraps a blanket around herself, she’s still chilled from being caught in the rain."
            y "Achoo! Oh no, don’t tell me I’m getting sick, too…"
            "Despite her hope, symptoms of a cold show themselves the next day. Miserable though she feels, she knows she’ll have to work on [anime.name] anyway."
            $rechoice_13_1()
        "Wait under a small shelter until the storm subsides":
            play sound "music/sfx/rain.ogg" fadeout 1.0
            scene street_rain with fade
            show yukari sad at left
            with dissolve
            "Yukari dashes to a nearby shelter just in time. A few drops of rain soon lead into a downpour."
            y "Oh great…"
            neighbour "Yukari, is that you?"
            "Out in the street, one of her neighbors stands beneath an umbrella. She waves for Yukari to join her."
            neighbour " I’m on my way home, too. Come on, there’s plenty of room under this umbrella!"
            show yukari happy
            y "Thank you!"
            "They hurry home together, and Yukari makes it into her house without getting too wet from the rain. She makes a mental note to thank her neighbor again the next time they meet."
            $rechoice_13_2()
            stop sound fadeout 1.0
    return
#Classmates Wish to Drop By
label random_14:
    scene studio_main with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    y "No way! The popular girls from my class want to visit our studio?"
    "Maybe we can get some ideas from them!"
    m "Are you sure that’s a good idea?"
    "I don’t remember them being very nice to you…"
    menu:
        "Invite the clique of girls to the studio":
            scene studio with fade
            show yukari at left with dissolve
            "A few hours later..."
            clique "Oh, Yukari, it’s so good to see you’re not doing too badly. I’ve been worried."
            show yukari worry
            y "Worried? Why?"
            clique "I remember how you were in high school. Someone like you might struggle to get by in the real world."
            show yukari
            y "Um… Well, anyway, this is the studio where we’ll be making [anime.name]!"
            clique_girl "I’m happy you found something to do with yourself, even if you couldn’t get a real job."
            y "This has nothing to do with getting a job."
            clique "Obviously, dear."
            y "No, I mean, this IS a job! Sort of."
            clique_girl "I envy you, Yukari."
            y "You do?"
            clique_girl "Yes, it must be nice to have time to play around at a pretend job. Unfortunately, I’m going to college."
            show sumiko_f angry at Position(xalign=0.3,yalign=1.0) with dissolve
            s "Okay, would you weirdos knock it off? We have work to do!"
            clique_girl "Don’t worry, we won’t keep you from your “work.”"
            "The girls giggle."
            clique "Yukari, dear, don’t be afraid to call on me. If you realize you can’t really make an anime, I’ll be happy to help you find a job within your capabilities."
            show yukari sad_angry
            "Yukari’s cheeks burn with embarrassment. She breathes a sigh of relief when the girls finally leave, but their comments disturb her for the rest of the day."
            $rechoice_14_1()
        "Turn them down":
            "Yukari refuses their offer. Like Mayumi said, they were never nice to her. It’s probably for the best that they don’t come."
            scene studio_main with fade
            "A few hours later..."
            show shunsuke at right
            show yukari at left
            with dissolve
            ss "Yukari, did you antagonize someone recently?"
            show yukari worry
            y "What do you mean?"
            ss "Some people started spamming anime forums with unpleasant comments about our studio. Come take a look."
            "She joins him at his computer. When she sees the names of the people spreading the rumors, her blood boils."
            show yukari angry
            y "The nerve of them! If I won’t let them visit the studio, they’ll drag us down, is that it?!"
            show shunsuke sigh
            ss "These girls clearly suffer from an inferiority complex. They can’t stand to see you succeed."
            y "We’ll show them. They can say as many nasty things as they like, but when [anime.name] comes out, everyone will see the truth!"
            $rechoice_14_2()
    return
# Won a prize on the radio!
label random_15:
    $rd_c = RandomCharacter()
    scene studio_main with fade
    show yukari at left
    if rd_c.p == "m":
        show mayumi_f at right
    elif rd_c.p == "yuu":
        show yuuko at right
    elif rd_c.p == "s":
        show sumiko at right
    else:
        show shunsuke at right
    with dissolve
    rd_c.say "[rd_c.person] takes off [rd_c.g] earpiece."
    rd_c.say "Yukari, do you mind if I step out for a minute?"
    rd_c.say "I need to make an important call."
    y "Sure, no problem."
    rd_c.say "[rd_c.person] steps out of the studio and returns after about five minutes."
    if rd_c.p == "m":
        show mayumi_f happy
    elif rd_c.p == "yuu":
        show yuuko happy
    elif rd_c.p == "s":
        show sumiko happy
    else:
        show shunsuke happy
    rd_c.say "Guess what? I just won {space=15}{image=small_moneybag.png} [WON_RADIO_FUNDS]"
    menu:
        "Ask how [rd_c.person] won the prize":
            show yukari happy
            y "How did you win{space=15}{image=small_moneybag.png} [WON_RADIO_FUNDS] from a phone call?"
            rd_c.say "Sometimes I listen to my favorite radio station while working."
            rd_c.say "It doesn't affect my work proficiency, I promise. Actually, it inspires me!"
            rd_c.say "Today, they had a prize ready for the eleventh person to call the station."
            menu:
                "Celebrate with [rd_c.person] and suggest sharing with the studio funds":
                   jump random_15_share
                "Tell off [rd_c.person] for listening to the radio during work.":
                    show yukari angry_mouth_closed
                    y "You shouldn’t be listening to the radio during work!"
                    if rd_c.p == "m":
                        show mayumi_f sigh
                    elif rd_c.p == "yuu":
                        show yuuko sigh
                    elif rd_c.p == "s":
                        show sumiko sigh
                    else:
                        show shunsuke sigh
                    rd_c.say "Like I just explained, it doesn’t cause any problems."
                    y "Still, it’s not right. I don’t want you to listen to the radio anymore when you’re at the studio, understand?"
                    rd_c.say "Fine. I’m sorry…"
        "Celebrate with [rd_c.person] and suggest sharing with the studio funds":
            jump random_15_share
    return
label random_15_share:
    y "That’s fantastic! Congratulations!"
    rd_c.say "Thank you!"
    y "Since that’s a fair amount of money, why don’t you add some of it to the studio’s funds?"
    rd_c.say "Sure, that’s fine, especially since I used studio time for this without asking permission. How much did you have in mind?"
    $radio_funds_25 = int(WON_RADIO_FUNDS * 0.25)
    $radio_funds_50 = int(WON_RADIO_FUNDS * 0.50)
    $radio_funds_75 = int(WON_RADIO_FUNDS * 0.75)
    menu:
        "25\% {space=15}{image=small_moneybag.png} [radio_funds_25]":
            $rechoice_15_1()
            rd_c.say "No problem!"
        "50\% {space=15}{image=small_moneybag.png} [radio_funds_50]":
            $rechoice_15_2(rd_c.stats)
            rd_c.say "A 50/50 split? I suppose that’s fair."
        "75\% {space=15}{image=small_moneybag.png} [radio_funds_75]":
            $rechoice_15_3(rd_c.stats)
            rd_c.say "That’s a little steep, isn’t it? If you insist…"
        "100\% {space=15}{image=small_moneybag.png} [WON_RADIO_FUNDS]":
            $rechoice_15_4(rd_c.stats)
            rd_c.say "So when you said “some,” you really meant “all”? You have the makings of a good tyrant, Yukari. Sheesh."
    return
#Wrong Food Delivery Address 
label random_16:
    scene studio_main with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    "The studio’s doorbell rings."
    m "I'll get it!"
    "She opens the door, speaks to the person outside for a moment, and then turns back to the group."
    show mayumi_f happy
    m "Wow, Yukari, you're so thoughtful!"
    m "Check it out, guys! There's fries, soda, and more!"
    y "(Thinking to herself) I didn’t order this… but everyone seems so happy. What should I do?"
    menu:
        "Pay for the delivery and make the team happy {space=15}{image=small_moneybag.png} [WRONG_FOOD_FUNDS]":
            y "(thinking to herself) I guess it can’t hurt. We didn’t make the mistake, after all."
            "She joins Mayumi at the door and pays the delivery person. The team splits the order up and everyone enjoys the food."
            y "(thinking to herself) No harm done, right?"
            scene studio_main with fade
            show yukari at left with dissolve
            "Later that day..."
            neighbour "Excuse me, did you take our food?"
            neighbour "Look at this e-receipt."
            neighbour "If you want to avoid trouble, you better pay up!"
            show yukari sad
            y "I’m sorry!"
            $rechoice_16_1()
        "Clarify to the delivery person that he's at the wrong address":
            show yukari sigh
            y "Sorry, but I’m afraid this isn’t ours. You must have gotten the address wrong."
            show mayumi_f sad
            m "B-but-..."
            y "Sorry guys. We have to be honest."
            m "Honesty doesn’t fill an empty stomach..."
            $rechoice_16_2()
    return
# Coffee or Tea?
label random_17:
    scene cafe with fade
    show yukari at left
    with dissolve
    y "Wow, there’s a promotion on the ground coffee!"
    y "And even though the matcha isn’t on sale, it’s still being sold at a good price."
    y " I’ve already spent a lot of this month’s pantry budget, though…"
    y "It's not every day that the café has such an amazing offer. I better pick one. Now if only I could remember if the others prefer coffee or tea…"
    menu:
        "Coffee":
            $rechoice_17_1()
            show sumiko sad at pos_right
            show shunsuke sad at pos_outerright
            show mayumi happy at Position(xalign=0.25,yalign=1.0) behind yukari
            show yuuko_f happy at Position(xalign=-0.15,yalign=1.0) behind yukari
            with dissolve
            m "Coffee! Coffee, coffee, coffee!"
            yuu "Thank you for thinking of us, Yukari."
            s "Aww, why did you have to get that?"
            ss "Were they all out of tea?"
        "Tea":
            $rechoice_17_2()
            show mayumi_f sad at Position(xalign=0.80,yalign=1.0)
            show yuuko sad at pos_outerright behind mayumi_f
            show shunsuke_f happy at Position(xalign=0.25,yalign=1.0) behind yukari
            show sumiko_f happy at Position(xalign=-0.15,yalign=1.0) behind yukari
            with dissolve
            ss "There’s nothing like a nice cup of tea."
            s "Woohoo! Thanks, Yukari!"
            m "Aw, you bought tea but no coffee…?"
            "Yuuko says nothing, but her shoulders slump and she sighs."
    show yukari worry
    y "Sorry! It’s really hard to please everyone."
    return
#Street Artist Sketch
label random_18:
    scene street with fade
    show yukari at left with dissolve
    y "This artwork is amazing! I really like these cherry blossoms."
    y "(thinking to self): It’s just a pity her art isn’t fitting for [anime.name]."
    old_lady "Why, thank you, young lady, I’m raising funds for an orphanage."
    show yukari happy
    y "I’m sure a lot of people will help out!"
    old_lady "I hope so. By the way, those keychains on your bag are very interesting."
    y "Oh, they’re from anime! I’m a big fan. I’m running my own anime studio, actually."
    old_lady "That’s wonderful. I wish you luck."
    y "Thanks! And I hope you earn a lot of money for the orphanage."
    old_lady "Before you leave, would you care to make a donation?"
    menu:
        "Donate":
            $rechoice_18_1()
            y "Here you go."
            old_lady "Thank you."
        "Walk away":
            $rechoice_18_2()
            return
    scene studio_main with fade
    show yukari at left
    show sumiko at pos_middleright
    show yuuko at pos_right
    with dissolve
    show sumiko happy
    "Later that day.."
    s "Oh wow, Yukari, look at what came in the mail!"
    s "It’s from Miss Eri. Who is she?"
    y "I have no idea."
    show yukari laugh_eyes_closed
    y " Wait a minute… This art matches my keychains!"
    y "No way! Could this be from the lady in the park?"
    show yuuko laugh_eyes_closed
    yuu " It’s beautiful… It’s given me a brilliant idea for [anime.name]!"
    return
#Overdue Library Book
label random_19:
    scene studio_main with fade
    show yukari at left with dissolve
    show yukari worry
    y "Okay, do I have everything? Antiseptic cream, tissues, manga, and… wait, what is this?"
    y "Oh my gosh, this book was due ages ago!"
    y "Why didn’t the librarian contact me? The fine must be insane by now."
    menu:
        "Return the book to the library on the way to work":
            $rechoice_19_1()
            scene street with fade
            show yukari at left with dissolve
            "On the way to work, Yukari stops by the library, but it’s closed. She reads the hours on the sign."
            y "Hmm, I’m a few minutes too early. Maybe I should come back during lunch."
            "She turns away from the library just in time to spot the librarian walking toward her."
            y "Perfect timing!"
            librarian "May I help you?"
            y "I’d like to return this book."
            "The librarian takes it from her and looks it over."
            librarian "Thank you for returning it. Don’t worry, there’s no fine."
            show yukari worry
            y "What? But it's been overdue for so long!"
            librarian "It's okay. We have a forgiveness policy if it’s the first time your book is overdue."
            show yukari laugh_eyes_closed
            y "Thank you so much!"
        "Choose to remain quiet since the librarian never said anything":
            scene home with fade
            show yukari at left with dissolve
            y "Hmm? What's in this letter?"
            show yukari sad
            y "No way! The library went through its records and noticed the missing book? The fine is so steep! I could buy a new copy cheaper than this."
            y "I guess there’s no running away this time…"
            $rechoice_19_2()
    return
#Newbie Voice Actor Looking for Work 
label random_20:
    scene black with fade
    "Yukari was browsing the web for potential partners who can do some voice acting at a bargain price."
    "She notices a thread set up by someone called Miki-chan who's a self-proclaimed up and rising seiyū who has all the equipment required."
    "Miki appears to be charging less than the market average as well. Even so, Miki hasn't been able to get any fair replies from members on the site as there's little trust for newbies and she works alone."
    "Yukari thinks she can afford to give Miki a chance and contacts her."
    scene recording_studio with fade
    show yukari at left with dissolve
    y "(thinking to self): Hmm, newbie or not, Miki might be a good voice actor for [anime.name], especially at her rates."
    show yukari happy
    y "This is an amazing studio!"
    miki "Yes. I mentioned it on the thread, but no one seemed to care."
    miki "Dad owns a successful advertising company and I'm free to use the equipment from time to time."
    y "Great. I brought a few scripts, so let’s hear what you can do."
    show yukari
    miki "Leave it to me! I’m confident in my skills!"
    "Miki enters the recording room, and Yukari sits down to listen."
    "Unfortunately, while confidence is good, it isn’t everything. Miki delivers her lines in monotone, with little emotion and even less variation. At last, it comes to an end."
    miki "Well? How did I do?"
    y "(thinking to self): Horribly, but it really would be nice to use this studio…"
    menu:
        "Truthfully inform Miki that she needs more practice":
            $rechoice_20_1()
            miki "Oh…"
            miki "You’re right. I understand. Thank you for being honest with me. I’ll practice harder than ever from now on!"
        "Lie to Miki that her voice acting is great, in order to make use of her studio":
            show yukari laugh_eyes_closed
            miki "Really? You liked my performance?"
            y "Yes, Miki, you're great!"
            miki "Are you sure?"
            y "(thinking to self): What’s this all about? It’s almost like she wants me to say no."
            miki "I’ll send you an email. Thank you for visiting."
            scene home_night with fade
            show yukari sad at left with dissolve
            y "What’s this? It’s not from Miki, but… from her father?"
            show yukari sad_angry
            y "Yikes! Looks like they know I lied to take advantage of the studio."
            $rechoice_20_2()
    return

#Suspicious Backpack
label random_21:
    scene street with fade
    show yukari worry at left
    y "What’s this? Someone left their bag lying in the alley."
    "The bag shakes."
    y "Did it just move? Must be my imagination."
    "As she starts to walk on, a loud cry comes from the bag."
    y "Agh! No way did I imagine that!"
    menu:
        "Peer into the bag":
            show yukari
            y "Phew. It's just a baby doll."
            y "What's this? There's a note inside as well."
            "The note reads; Haha! You got pranked on camera!"
            show yukari sigh
            y " Oh brother…."
            y "Irritated, she shakes her head and leaves the alley."
        "Call the authorities to inform them about the bag":
            show yukari angry_mouth_closed
            y "No way am I opening that."
            y "Who knows what could be in there?"
            "She calls the police and explains the situation to them, and then hurries on her way, still a little shaken from the strange incident."
    return
#New Menu - Food Tasting Session 
label random_22:
    scene studio_main with fade
    show yukari at left with dissolve
    y "This seems like a good time to announce the workshop I registered us for this afternoon."
    "Before she can speak, Sumiko stands up."
    show sumiko at right with dissolve
    s "Hey everyone, our family’s restaurant is switching to a new menu next week. I'd like you guys to preview the menu this afternoon once we finish our work!"
    s "You'll be the first people to enjoy the scrumptious new meals the master chef has planned for this season. What do you say?"
    y "(thinking to self): Oh no… it’s at the same time as the workshop!"
    menu:
        "Tell the team that there are already plans to attend the workshop":
            $rechoice_22_1()
            show yukari sad
            y "Sorry guys. I registered us for an important workshop this weekend, so we won’t be trying that new food until next week."
            show sumiko sigh
            s "No way! Why didn’t you say something sooner? By next week, it’ll be on the menu for everyone. There won’t be another chance like this until next season!"
            "Everyone groans in disappointment."
        "Scrap the workshop plan and join the food tasting session with everyone":
            $rechoice_22_2()
            show yukari happy
            y "Yeah, that sounds amazing. The food better be good!"
            s "Of course! I thought up some of the concepts myself!"
            y "Huh? Oh boy."
            jump random_22_eat
    return
label random_22_eat:
    #weekend stuff
    scene restaurant with fade
    show yukari at pos_left
    show yuuko at pos_right
    show sumiko at pos_outerright behind yuuko
    show shunsuke at pos_middleright
    show mayumi at pos_farleft behind yukari
    with dissolve
    show mayumi happy
    m "Wow, everything tastes amazing!"
    ss "Thank you for inviting us."
    y "This food is excellent!"
    y "(thinking to self): The workshop probably wasn’t too helpful anyway."
    return
#Bumped into popular Seiyū Mamoru-san!
label random_23:
    scene street with fade
    show mayumi at left with dissolve
    "Mayumi walks down the street, gaze fixed on her cell phone as she plays her current favorite game. Suddenly, she collides with someone. Her phone falls to the ground along with the man’s sunglasses."
    show mayumi sad
    m " I'm so sorry! Here are your glasses."
    stranger "Here's your phone, I hope it's all right."
    m "Thank you--wait a second, aren't you Mamoru-san?"
    "Her heart hammers and she can barely breathe. She literally ran into her favorite seiyū."
    menu:
        "Ask for an autograph and to take a picture first":
            show mayumi happy
            m "Mamoru-san! Can I have your autograph? How about a picture?"
            mamoru "Sorry, I'm in a hurry now."
            mamoru "Maybe next time!"
            "Mamoru puts on his shades and hurries away."
            show mayumi sad
            m "Aw, darn, he must be avoiding the paparazzi."
            $rechoice_23_1()
        "Return his sunglasses and ask if he's fine first":
            m "Here are your glasses. Are you all right?"
            mamoru "I’m fine. Thank you."
            "As he takes his sunglasses from her, Mayumi bounces on her heels, too excited for words."
            mamoru "I'm trying to avoid the paparazzi right now, but is there anything I can do for you before I go?"
            show mayumi laugh_eyes_closed
            m "Could I have your autograph? It'd mean a lot to me!"
            mamoru "Sure."
            "He pulls out a pen and signs Mayumi’s notebook."
            mamoru "See you around!"
            show mayumi happy
            m "Thank you, Mamoru-san! Thank you!"
            "Mamoru hurries off to avoid an approaching crowd, while Mayumi continues on her way with the precious autographed notebook clutched to her chest."
            $rechoice_23_2()
    return
#Unbelievably Hot Summer
label random_24:
    scene studio_main with fade
    show yukari at left
    show sumiko at right
    with dissolve
    s "It's so warm! Where's the AC controller?"
    y "Here."
    show sumiko worry
    s "Huh? It's already set to the lowest possible temperature!"
    s "Yukari, can we get this checked out? There must be something wrong with the AC unit!"
    show yukari sigh
    y "Calm down. You just returned from lunch after a long walk outside. You’re probably hot from that."
    s "C'mon, I'm not imagining this. Look at this bead of sweat that's forming!"
    y "Oh brother…"
    menu:
        "Call for an electrician to take a look":
            scene studio with fade
            show sumiko at right
            show yukari at left
            with dissolve
            "A few hours later, the electrician arrives..."
            electrician "Hmm, it looks like a valve is leaking."
            electrician "That must be why the air conditioner isn't cooling so well."
            electrician "It could've broken down completely at any time."
            show yukari happy
            y "Wow, good call, Sumiko. Thanks for noticing!"
            s "I’m just glad you believed me."
            $rechoice_24_1()
        "Tell Sumiko the AC isn't broken":
            scene studio with fade
            show yukari at left
            show sumiko at pos_outerright
            show shunsuke sad at pos_middleright_half
            with dissolve
            ss "I think our air conditioner just broke down."
            show yukari worry
            y "You can't be serious."
            show sumiko tsundere
            s "What? But Yukari, didn’t you call for a repairman last week?"
            y "I'll get one right away, sorry."
            show sumiko sad_angry
            s "Now we have to work in the studio without an air conditioner. Great."
            s "You should've listened to me last week…"
            $rechoice_24_2()
    return

#Arts Festival Performance
label random_25:
    scene studio_main with fade
    show mayumi at left with dissolve
    m "Ooh, what’s this? There's an art festival this week and Rosette is playing? Cool! I love that group."
    m "And there’s a special lucky draw for people who attend in pairs?"
    m "That’s it! I’m taking someone with me. Now I know I was talking to someone about Rosette. But who was it…?"
    menu:
        "Yukari":
            scene street with fade
            show mayumi at left
            show yukari_f at right
            with dissolve
            show mayumi happy
            m "Pretty lively, huh? I can't wait for Rosette to start playing!"
            y "Rosette? Haven't heard of them, but this is an amazing festival."
            m "Oh?"
            m "(thinking to self): Oops, guess I remembered wrong."
            m "Never mind. Let's just have fun."
            $rechoice_25_2()
        "Sumiko":
            scene street with fade
            show mayumi at left
            show sumiko at right
            with dissolve
            show mayumi happy
            m "Pretty lively, huh? I can't wait for Rosette to start playing!"
            s "Rosette? Haven't heard of them, but this is an amazing festival."
            m "Oh?"
            m "(thinking to self): Oops, guess I remembered wrong."
            m "Never mind. Let's just have fun."
            $rechoice_25_3()
        "Shunsuke":
            scene street with fade
            show mayumi at left
            show shunsuke at right
            with dissolve
            show mayumi happy
            m "Pretty lively, huh? I can't wait for Rosette to start playing!"
            ss "Rosette? Haven't heard of them, but this is an amazing festival."
            m "Oh?"
            m "(thinking to self): Oops, guess I remembered wrong."
            m "Never mind. Let's just have fun."
            $rechoice_25_4()
        "Yuuko":
            scene street with fade
            show mayumi at left
            show yuuko at right
            with dissolve
            show yuuko happy
            yuu "This is wonderful. I’m so happy you remembered I’m a fan of Rosette."
            yuu "Let's go enjoy the performance."
            show mayumi happy
            m "Hehe, of course I remembered!"
            m "Let's check out the lucky draw later."
            $rechoice_25_1()
    return
#Animation Studio Ex-Employee 
label random_26:
    scene street with fade
    show yukari at left with dissolve
    show yukari sigh
    y "That was a really long meeting…"
    "Worse, it was for nothing. She and the animation staff couldn’t agree on a price, and she left empty-handed."
    y "(thinking to self): Still, it’s an important company. Maybe we can work something out if I contact them later."
    stranger "Excuse me, did you just come from that studio?"
    y "Yes I did, why do you ask?"
    stranger "I used to work for that company. Let me give you a piece of advice: avoid them. The executives treat their staff poorly."
    show yukari worry
    stranger "Aside from being rude, they can rarely agree of anything, so work progresses very slowly."
    stranger "I'm sure they gave you their cards."
    y "Quite a few, yes."
    stranger "If I were you, I’d get rid of them. Let me discard them for you. I’ll feel better."
    menu:
        "Hand over the studio's name cards to the stranger":
            stranger "I'll enjoy ripping these to shreds."
            stranger "The assistant manager was especially rude to staff. The day I left the company was the happiest day of my life."
            show yukari
            y "Thanks for your advice."
            stranger "You're welcome."
        "Keep the name cards.":
            stranger "You're really going to keep them?"
            show yukari
            y "Yes. I might need to work with this company in the future."
            stranger "Are you out of your mind? Weren’t you listening to me?"
            y "I was but there might be a--"
            stranger " I pity anyone who works for you. If you’re an executive, your organization must be just as bad."
            show yukari sad_angry
            y "What? How could you say something so mean?!"
            "The former employee stomps away without another word."
    return
#Shunsuke shows a surprise video montage
label random_27:
    scene studio_main with fade
    show yukari at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at pos_middleright_half
    show sumiko at pos_outerright
    with dissolve
    ss "Hey guys, are you free to have a meal together this evening?"
    m "Yep!"
    s "Yuuko and I are also free."
    y "What's the occasion?"
    ss "I can’t tell you yet. It's a surprise."
    y "Let me check our work progress first."
    ss "C'mon, Yukari, surely you can spare one evening!"
    menu:
        "Hang out with the team at the restaurant this evening.":
            show yukari sigh
            y "Fine, fine! I’ll go, okay?"
            show yukari happy
            y "Let's have a good time tonight!"
            scene restaurant with fade
            show yukari at pos_left
            show yuuko at pos_right
            show sumiko at pos_outerright behind yuuko
            show shunsuke at pos_middleright
            show mayumi at pos_farleft behind yukari
            s "Okay, Shunsuke, what’s the big surprise?"
            ss "I've been secretly filming us at work for the past few weeks."
            show shunsuke laugh_eyes_closed
            ss "Allow me to present to you our journey from Week 1!"
            "He sets a laptop on the table and begins a video. It shows all of them working on various tasks for the production of [anime.name]."
            "Even from the short selection, it's easy to see them become more efficient and confident as time passes."
            show yukari happy
            y "Wow. We’ve come so far! It’s… hard to believe."
            show sumiko happy
            s "That was cool!"
            show yuuko laugh_eyes_closed
            yuu "Thank you for making that, Shunsuke."
            show mayumi happy
            m "Yeah, thanks!"
            $rechoice_27_1()
        "Skip the restaurant to work on getting more funds instead.":
            show yukari sad
            y "Sorry, but I can't make it."
            y "I'll be attending some events tonight that could help us raise additional funds."
            y "I hope you understand how important this is."
            ss "I understand… Let’s postpone the surprise until everyone is free."
            $rechoice_27_2()
    return
#Child's Birthday Celebration
label random_28:
    scene cafe with fade
    show sumiko_f at left
    show yuuko at right
    with dissolve
    little_girl "Onee-san would you like some cake?"
    s "What’s this? Are you sharing your birthday cake with us?"
    "The little girl nods."
    little_girl "Mommy says it’s good to share."
    show yuuko happy
    yuu "Aw, how cute."
    show sumiko_f happy
    s "We’d love to have some. And Happy Birthday!"
    show yuuko
    yuu "Did you make a birthday wish?"
    little_girl "I wished for everyone to be happy!"
    s "If Mayumi was here, I think she’d faint to hear a little kid say that."
    yuu "I think we should give her a birthday present."
    menu:
        "Yuuko gives the girl her newly-bought teddy bear keychain":
            little_girl "Thanks, Onee-san! I love teddy bears!"
            show yuuko laugh_eyes_closed
            yuu "You're so cute, I'd shower you with gifts if I had more."
            little_girl "Mommy and Daddy are calling, bye-bye!"
            $rechoice_28_1()
        "Sumiko gives the girl a set of animal stickers she got at a bazaar":
            little_girl "Thanks, Onee-san! I love animals!"
            s "Then we’re even, because I love cake! You better run along now. Your parents are calling."
            little_girl "Bye-bye!"
            $rechoice_28_2()
    return

#Decorate Restaurant (Not Y&S Restaurant) for Funds 
label random_29:
    scene studio_main with fade
    show yukari worry at pos_left
    show mayumi at pos_farleft behind yukari
    show shunsuke at right
    with dissolve
    y "Oh my gosh, we're almost broke!"
    y "All those Economics classes I took haven’t helped one bit."
    ss "Calm down. I know a place where we can make some extra cash."
    show yukari
    y "Really? Where?"
    ss "A local restaurant needs help putting up seasonal décor. If all of us work together, we can get quite a hefty sum."
    ss "The downside is we'll spend our entire afternoon and evening working without any rest."
    show yukari worry
    y "Afternoon AND evening? That might leave us too tired to work efficiently…"
    m "We need the money, so let’s do it anyway."
    y "But is it the right thing to do? We might get out of touch with our skills, too."
    show mayumi sigh
    m "Remember how hard it was to raise funds? An opportunity like this won’t come again."
    m "We should accept the offer before someone else snatches it!"
    menu:
        "Take up the décor job at the restaurant":
            $rechoice_29_1()
            scene cafe with fade
            show yukari at pos_left
            show yuuko at pos_outerright behind sumiko
            show shunsuke_f at pos_farleft
            show sumiko at pos_right 
            with dissolve
            show shunsuke_f laugh_eyes_closed
            ss "Let's get to work, guys! Fair pay for fair work."
            y "Sumiko, can you help me with the wallpaper?"
            s "Sure, let me get the right tools."
            yuu "Shunsuke, where's the paint?"
            ss "It's behind the counter. Be careful with the white. The lid is chipped."
            "For the rest of the day, they work under the restaurant owner’s guidance. By the time night falls, the job is complete."
            scene cafe with fade
            show yukari at left with dissolve
            restaurant_owner "Thanks for the work, kids. Here's your payment."
            show yukari happy
            y "This is even more than we agreed on!"
            y "That's very generous of you, thanks!"
            restaurant_owner "Seeing how hard you worked, I thought you guys deserved a bonus."
        "Pass on the opportunity":
            $rechoice_29_2()
            y "Thanks for your suggestion, Shunsuke, but I think we have to pass."
            y "If we take that much time to do something extra, it’ll affect the quality of our work on [anime.name]."
            show shunsuke sad
            ss "That's a fair point. I wanted you to weigh the options for yourself."
            ss "However, without any funds left to tap, we'll struggle much more as we proceed."
            show mayumi sad
            m "This is awful! I’ll have to borrow some money to finance our operations."
            m "Someone better break the news to Sumiko and Yuuko. They won’t be happy."
    return
#Funding Crisis 
label random_30:
    scene studio_main with fade
    show yukari at left with dissolve
    y "Wow, it says on this website that these consultants provide help on finance and legal matters, offer leadership courses, and more!"
    show yukari sigh
    y "Darn. Their service costs more than rent for this studio!"
    y "I wonder how much money we have…"
    "She checks the studio’s financial records and gasps in dismay."
    show yukari worry
    y "We've already spent that much?!"
    y "Not good. We need an emergency meeting, pronto."
    scene restaurant with fade
    show yukari at pos_left
    show yuuko at pos_right
    show sumiko at pos_outerright behind yuuko
    show shunsuke at pos_middleright
    show mayumi worry at pos_farleft behind yukari
    with dissolve
    m "Yukari, I get the impression you didn’t call us here for a fun meal."
    show yukari sigh
    show sumiko sad
    y "You’ve got that right. We have a huge problem."
    y "At the rate we're spending our money, we won't be able to stay afloat until production."
    s "What should we do? Making money isn’t easy."
    m "Aw, there are a lot of ways we can earn money."
    ss "Such as?"
    show mayumi worry
    m "Well… uh…"
    y "I already have a suggestion in mind."
    menu:
        "Everyone should chip in so we have more money to fall back on":
            show mayumi
            show sumiko
            show yukari 
            y "That's the best way for our studio to carry on in a financially stable manner."
            ss "You're asking a lot, but I'm with you all the way."
            s "Yeah. I want to see this project through to the end. Sparing some personal expenses is a sacrifice I’m willing to make."
            yuu "I agree."
            m "This might be our only chance to meet our deadline, so count me in."
            y "Thanks, everyone. We’ll definitely see [anime.name] come to fruition!"
            $rechoice_30_1()
        "Continue business-as-usual for the time being and be spontaneous":
            show yukari
            y "We're not exactly broke yet, so I think things will solve themselves if we’re frugal from now on."
            show shunsuke sigh
            ss "Are you sure this is a wise plan? Money doesn't grow on trees."
            y "It’ll be fine. Remember, I’ve already set some plans into motion to build more funds."
            show mayumi sad
            m "What are the odds of those plans succeeding?"
            y "Well, they're still underway, but our chances are better than a coin toss."
            show sumiko sad_angry
            s "A coin toss?! That's what we’re pinning our financial hopes on?"
            y "Relax, Sumiko. If anything happens, we’ll take care of it then."
            $rechoice_30_2()
    return

#Dance Challenge 
label random_31:
    scene street with fade
    show yukari at left with dissolve
    "I wonder what all the commotion is about?"
    "She squeezes through the crowd and reaches the arcade. They’re holding a “Dance Revolution” competition."
    y "Wow, those people warming up are really good."
    show yukari happy
    y "Wait a minute… Isn't that the ultra-rare Miku figurine?! And it’s only Fourth Prize?"
    y "Hmm, it looks like registration is still open…"
    show yukari worry
    "She hasn’t played in a long time, and she knows she doesn’t stand a chance against the major competitors. Fourth place, though, might be feasible."
    menu:
        "Register for the competition":
            "Yukari enters the competition."
            show yukari sigh
            y "Oh gosh, I haven't played this in forever!"
            y "What was I thinking?"
            y "Forget fourth place, I guess I'll have to settle for being the comic relief."
            $rechoice_31_1()
        "Cheer on the competitors":
            show yukari happy
            "It’s been too long since she played. Yukari stays with the crowd and cheers." 
            "The contestants are all fantastic. When the competition ends, she claps for the winners."
            fourth_w "Thanks for cheering me on. It really boosted my confidence!"
            fourth_w "To be honest, I don't really want this figurine I won. I'd like you to have it."
            show yukari laugh_eyes_closed
            y "No way! Really? Thank you so much!"
            y "Wow, I wasn't even cheering for him in particular…"
            $rechoice_31_2()
    return

#Free Breakfast Samples! 
label random_32:
    scene street with fade
    show sumiko_f laugh_eyes_closed at pos_left
    show yuuko_f at pos_farleft
    with dissolve
    s "Wow, do you smell that?"
    yuu "What is it? It's amazing…"
    manager "Hello!"
    "Sumiko and Yuuko stop. The sign behind the man announces the grand opening of a new café, and the delicious smells waft from inside the building."
    manager "We're holding a special promotion to celebrate our grand opening."
    manager "Would you like to try a sample from our breakfast menu?"
    s "Yes, please! These look mouth-watering!"
    show yuuko_f happy
    yuu "Mm, they're really delicious too!"
    manager "Come on inside. There's plenty more on the menu."
    "The two girls exchange glances. After all, they’re on their way to the studio."
    menu:
        "Head into the cafe":
            scene cafe
            show sumiko_f at left
            show yuuko at right
            with dissolve
            "A little relaxation won’t hurt. They follow the manager into the café."
            show yuuko happy
            yuu "It’s beautiful in here."
            show sumiko_f happy
            s " Look at how many things are listed on the menu!"
            manager "Let me serve you today's breakfast special."
            s "Thank you!"
            "Two hours later…"
            show yuuko
            s "That was the best breakfast I've had in a long while!"
            "Yuuko nods, and then looks at the clock on the wall."
            show yuuko worry
            yuu "We're going to be so late… I hope Yukari isn’t angry."
            show sumiko_f
            s "We’ll just tell her about the café. A tip about great food like this should make up for anything!"
            $rechoice_32_1()

        "Continue to work":
            scene studio
            show yukari happy at left
            show sumiko at pos_middleright_half
            show yuuko at pos_farright
            with dissolve
            y "Hey, you guys are here early!"
            yuu "Good morning."
            y "Since you're here, can you help me tidy up the studio?"
            "Sumiko glances at Yuuko and leans close so she can whisper."
            show sumiko sad_angry
            s "We should’ve gone for that breakfast…"
            show yuuko sad
            "Yuuko gives her sister a sad nod, but it’s too late now. They trudge forward to help Yukari clean."
            $rechoice_32_2()
    return
# Accessories at 50% Off!
label random_33:
    scene street with fade
    show mayumi at left
    with dissolve
    "After lunch, Mayumi walks back toward the studio when a sign makes her freeze. “Clearance Sale”?"
    show mayumi sigh
    "No way! ABC store is closing down?"
    "Everything’s half-price or cheaper…"
    "She looks at the jewelry on display. She’s had her eye on it for quite some time, but it was always too expensive before."
    show mayumi
    "True, her lunch break isn’t long enough for a shopping spree, but…"
    "A chance like this will probably never come again."
    menu:
        "Go in and browse":
            "She can’t let an opportunity like this go to waste. Mayumi rushes inside."
            show mayumi laugh_eyes_closed
            m "Look at that necklace! And those bangles! Wow!"
            m "One basket won’t be enough!"
            "One hour later…"
            "As she leaves the store, she checks the time."
            show mayumi worry
            m "Oh no! I'm super late!"
            "Clinging tightly to her purchases, Mayumi runs down the street."
            scene studio
            show mayumi at left
            show yukari_f at pos_right
            show yuuko at pos_outerright behind yukari_f
            with dissolve
            y "Where have you been, Mayumi? We were all waiting for you."
            m "Um… Well…"
            show yukari_f worry
            yuu "What's in all those bags you’re carrying?"
            show mayumi sad
            m "Eheheh…"
            "She sets down the bags and tries to look innocent."
            y " Oh Mayumi…"
            $rechoice_33_1()
        "Return to the office":
            scene studio
            show mayumi at left
            show yukari_f at right
            with dissolve
            "Mayumi reluctantly returns back to the office."
            y "Hey, did you see ABC store is going out of business?"
            y "They’re having an epic sale!"
            show yukari_f happy
            y " I got this bangle for just $5!"
            m "Aw, I should have gone in…"
            $rechoice_33_2()
    return
#Ideal Office Fragrance 
label random_34:
    scene studio with fade
    show yukari at left with dissolve
    y "ABC store is having a discount on scents this week!"
    y "Hmm… our studio doesn’t really have that “fresh” smell anymore. We could use a nice air freshener. What kind, though?"
    y "Grapefruit's obviously the best choice, but I wonder if the others will think so…"
    "She racks her brain, but although she’s sure the topic of favorite scents has come up at least with Mayumi, she can’t remember what any of her team members like."
    y "Oh well. I'm paying, so nobody should have a problem with what I pick."
    menu:
        "Tropical Grapefruit air freshener":
            show yukari happy
            "Ahhh… Grapefruit's so refreshing! No one has complained, so I’m glad I picked it."
            $rechoice_34_1()
        "Ocean Breeze air freshener":
            show shunsuke at right
            hide yukari
            show mayumi at left
            with dissolve
            ss "Hmm, the office smells pretty good today."
            m "You noticed, too? I thought it was just me! Feels like I'm on the beach."
            "The two of them smile as they head to their desks. Mayumi is even more upbeat than usual and Shunsuke seems more relaxed. The air freshener is a hit!"
            $rechoice_34_2()
        "Classic Rosemary air freshener":
            hide yukari
            show yuuko_f at left
            show sumiko at right
            with dissolve
            s "Hmm?"
            s "This scent, it’s so…"
            yuu "Familiar."
            s "It makes me feel at peace."
            yuu "Kind of reminds me of a garden we used to play in. Do you remember?"
            "The sisters reminisce as they sit at their desks, but it doesn’t take away from their work. Instead, both seem more at ease and inspired."
            "A fresher atmosphere in the studio is just what they needed."
            $rechoice_34_3()
    return
#How to Catch a Thief?  
label random_35:
    scene street with fade
    show shunsuke_f at left with dissolve
    "Shunsuke is deep in thought as he walks to the meeting with the advertising company. He doesn’t even notice the stranger near him on the street until the man bumps into him."
    show shunsuke_f angry
    ss "Watch where you're goi-"
    "The stranger rushes past without a word."
    ss "Huh. Someone’s in a hurry…"
    office_l "Help! That man stole my purse!"
    show shunsuke_f sad_angry
    ss "Wait a second, where's my phone?!"
    menu:
        "Chase the thief":
            show shunsuke_f angry
            ss "No way am I letting him get away like that!"
            "Shunsuke dashes after the thief. Although the man is fast, Shunsuke is faster. The distance between them shrinks, and finally he tackles him to the ground."
            ss "You're not getting away!"
            "He pins the man until the woman gets in touch with the authorities. Once the thief has been taken into custody and the stolen items returned, the woman smiles at Shunsuke."
            office_l "Thank you so much! The police would never have gotten here in time!"
            show shunsuke_f happy
            ss "Thank you, Miss. I'm glad to have been of service."
            ss "I have to go for a meeting now. Thanks again!"
            $rechoice_35_1()
        "Ask the lady to call the police":
            office_l "Is this the police? We've just been robbed!"
            ss "Yes, right along ABC Street."
            police_o "We'll send the nearest patrol to your location."
            ss "My phone has information saved on it that I planned to use at the meeting…"
            ss "How can I go to the meeting if I don’t have my phone?"
            "One hour later…"
            police_o " I'm sorry. We have yet to apprehend the culprit. Please give us your contact details, and we will inform you as soon as we make progress."
            show shunsuke_f sad
            ss "No way!"
            "He looks at the clock."
            ss "Not only do I not have my phone, but I’m going to be late for the meeting."
            office_l "Oh no… my purse…"
            ss "This will be hard to explain to Yukari…"
            $rechoice_35_2()
    return
#Playful Child  
label random_36:
    scene cafe with fade
    show yukari at left
    show mayumi_f at right
    with dissolve
    y "So I was thinking we can improve the studio’s atmosphere if we--"
    "A little boy suddenly pops up beside them. He climbs into the seat next to Mayumi."
    m "Hi there. Where did you come from?"
    show yukari tsundere
    y "Ugh, not now. We have important things to discuss. Hey kid, shoo! Go bother your mommy."
    show mayumi_f sigh
    m "Come on, Yukari, have a heart. I know you’re stressed out--"
    y "And this kid isn’t helping."
    menu:
        "Get the child to leave":
            show yukari sigh
            y "We're having an important talk."
            y "Boy, go and find your parents!"
            "The little boy was stunned by her raising her voice and hurried away. In the process, he slipped on the just-mopped floor and burst into tears."
            show mayumi_f sad
            m "Yukari, that wasn’t nice."
            y "I didn’t know he’d fall. Besides, he’s not our problem. So as I was saying, I think--"
            "The boy continues to cry, and then a woman enters the café. She looks frantic."
            "Uwahh! Mommy!"
            mother "Takumi! There you are!"
            mother " I've been looking for you for so long! Are you all right? What happened?"
            show yukari sad
            m "Oh no, he was lost?"
            "Aw man, now I feel bad..."
            $rechoice_36_1()
        "Entertain the child":
            show mayumi_f happy
            m "Here here, Onee-san will play with you!"
            show yukari
            y "Yukari rolls her eyes, but doesn’t object. The little boy rushes to Mayumi and plays with the frills on her shirt."
            y "Seems like you're a natural with kids."
            m "I like kids. I often babysit my neighbors’ children."
            "Just then, the door to the café opens, and a woman enters. She looks frantic."
            mother "Takumi?"
            "She spots them and hurries over to their table."
            mother "Oh, thank you two so much for taking care of Takumi!"
            mother "I've been looking all over for him."
            mother "Say thank you to the nice ladies."
            boy "Thank you Onee-san!"
            show mayumi_f laugh_eyes_closed
            m "Aw, isn't he cute?"
            show yukari happy
            y "Yukari rolls her eyes again, but smiles. She’s glad she didn’t chase the kid away after all."
            $rechoice_36_2()
    return

label random_37:
    scene street with fade
    show mayumi at left
    show headphone_guy at right
    with dissolve
    "Mayumi hurries down the street on her way home when faint music catches her attention."
    m "(thinking to self): His music is so loud I can hear it through his headphones! Something about it sounds familiar…"
    "With a jolt of surprise, she realizes it sounds familiar because she composed it herself in the studio. It’s the theme song for [anime.name]!"
    m "E-excuse me, that song you’re listening to…"
    show headphone_guy shocked
    hp_guy "Hmm?"
    "He lowers the volume of his music and gives her an inquisitive look."
    m "The song you were listening to just now—"
    show headphone_guy happy
    hp_guy "Oh, that? It’s the theme song for an upcoming anime called [anime.name]! They released it as part of a promotion, and I’ve been listening to it ever since."
    show mayumi happy
    m "You like it a lot, then?"
    hp_guy "Yeah, it’s great! Here, let me get the website link for you so you can download it, too."
    "Mayumi hesitates. Of course she doesn’t need to download the song. She has the original copy. But she’s embarrassed at the thought of admitting it. This is the first time she’s really had to deal with a… fan."
    menu:
        "Pretend to not be involved":
            "David Buki copies down the URL onto a piece of paper and hands it to her."
            hp_guy "Here you go."
            m "Um, thanks… I really should be going now!"
            "She dashes away before he can ask any questions."
            
        "Tell him the truth":
            m "Actually… I’m the composer for [anime.name]."
            $dice_number = renpy.random.randint(0,100)
            if dice_number <= choice_raise_funds_formula():
                $rechoice_37_1()
                hp_guy "Really? Cool! I’m so happy to meet you! Your music is fantastic."
                show mayumi laugh_eyes_closed
                m "Thanks!"
                hp_guy "If the rest of the soundtrack is half as good as this, I can’t wait to hear it!"
                m "You really think it’s that good?"
                hp_guy "Definitely. I’m going to tell all of my friends to check out [anime.name]."
                m "Wow! Thanks!"
                "They talk a little longer about music, and then Mayumi continues on her way, feeling like she’s on top of the world."
            else:
                $rechoice_37_2()
                show headphone_guy sad
                hp_guy "Sure you are. And I’m the director of Yu Yu Hakusho."
                show mayumi sad
                m "No, I mean it!"
                hp_guy "Come on, don’t joke about something like that. This is a great song, and you shouldn’t steal credit for yourself."
                m "But I… Never mind."
                m "She runs past him down the street, crestfallen that he didn’t believe her."
    return

