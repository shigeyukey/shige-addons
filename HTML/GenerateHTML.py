import os



HTML_FILE_NAME = 'ShigeAddons.html'
# HTML_FILE_NAME = 'ShigeAddons_test.html'





def generate_html_content(buttons):
    button_html = ""
    for i, button in enumerate(buttons):
        button_html += f'<button id="button-{i}"\
            onclick="changeImage(\
                \'{button["url"]}\',\
                \'{button["description"]}\',\
                    \'{button["link"]}\',\
                        \'{button["label"]}\',\
                    {i})">{button["label"]}</button>\n'

    js_code = """
    window.onload = function() {
        var images = [];
    """
    for i, button in enumerate(buttons):
        js_code += f"""
        images[{i}] = new Image();
        images[{i}].src = "{button['url']}";
    """
    js_code += f"""
        changeImage("{buttons[0]['url']}", "{buttons[0]['description']}", "{buttons[0]['link']}", "{buttons[0]['label']}", 0);

    }};
    """




    HTML_CONTENT = f"""
    <!DOCTYPE html>
    <html>
    <meta http-equiv="Permissions-Policy" content="interest-cohort=()">
    <head>
        <title>Embedded Image</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Arial', sans-serif;
            }}
            .wrapper {{
                display: block;
                height: 100%;
            }}
            .container {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100%;
            }}
            a {{
                display: block;
                max-width: 100%;
                max-height: 80%;
            }}

            a:hover {{
                cursor: pointer;
            }}
            .image-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                height: 255px;
                position: relative;
            }}
            .image-container .side-container {{
                width: 24px;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .image-container .center-container {{
                width: 400px;
                height: 255px;
                position: relative;
                border: 1px solid #000;
                box-sizing: border-box;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            img {{
                width: 100%;
                height: auto;
                display: none;
            }}
            .button-container {{
                margin-top: 10px;
            }}
            button {{
                margin: 2px;
                padding: 5px 10px;
                font-size: 12px;
            }}
            #loading {{
                font-size: 20px;
                color: gray;
                width: 100%;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                top: 0;
                left: 0;
            }}
            #shigeAddons {{
            font-size: 16px;
            color: gray;
            }}
            
            #description {{
                margin-top: 10px;
                font-size: 12px;
            }}
            #label {{
                margin-top: 10px;
                font-size: 16px;
            }}
            .selected-button {{
                background-color: #007BFF;
                color: white;
            }}
            .arrow {{
                cursor: pointer;
                font-size: 24px;
            }}
        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="container">
                <div id="shigeAddons">Add-ons created, fixed, and customized by Shigeyuki.</div>
                <div class="image-container">
                    <div class="side-container">
                        <span class="arrow left-arrow" onclick="prevImage()">&#9664;</span>
                    </div>
                    <div class="center-container">
                        <div id="loading">No image</div>
                        <img id="image" src="{buttons[0]['url']}" onload="hideLoading()">
                    </div>
                    <div class="side-container">
                        <span class="arrow right-arrow" onclick="nextImage()">&#9654;</span>
                    </div>
                </div>
            <a id="description-link" href="{buttons[0]['link']}" target="_blank">
                    <div id="label">{buttons[0]['label']}</div>
                </a>
                    <div id="description">{buttons[0]['description']}</div>
                <div class="button-container">
                    {button_html}
                </div>
            </div>
        </div>
        <script>

            function hideLoading() {{
                document.getElementById('loading').style.display = 'none';
                document.getElementById('image').style.display = 'block';
            }}

            var currentSelectedButton = 0;

            function changeImage(newSrc, description, link, label, buttonIndex) {{
                document.getElementById('image').style.display = 'none';

                document.getElementById('loading').style.display = 'flex';
                document.getElementById('image').src = newSrc;
                document.getElementById('description').innerText = description;
                document.getElementById('label').innerText = label;
                document.getElementById('description-link').href = link;
                document.getElementById('button-' + currentSelectedButton).classList.remove('selected-button');
                document.getElementById('button-' + buttonIndex).classList.add('selected-button');
                currentSelectedButton = buttonIndex;
            }}

            function prevImage() {{
                var newIndex = (currentSelectedButton - 1 + {len(buttons)}) % {len(buttons)};
                var button = document.getElementById('button-' + newIndex);
                button.click();
            }}

            function nextImage() {{
                var newIndex = (currentSelectedButton + 1) % {len(buttons)};
                var button = document.getElementById('button-' + newIndex);
                button.click();
            }}

            document.getElementById('description-link').addEventListener('click', function() {{
                console.log('Description link clicked');
            }});

            {js_code}

        </script>
    </body>
    </html>
    """

    return HTML_CONTENT

# ﾎﾞﾀﾝの情報をﾘｽﾄとして定義
# buttons = [
#     {"url": "https://github.com/shigeyukey/my_addons/blob/main/media_files/DinoTimer%20%E2%80%90%202024-07-23.gif?raw=true",
#         "description": "Raising Dinosaurs with Pomodoro Study",
#         "label": "🦖DinoTimer",
#         "link": "https://www.patreon.com/posts/how-to-use-with-108767216?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link"},

#     {"url": "https://github.com/shigeyukey/my_addons/blob/main/media_files/New_Card_Farm_for_patreon.gif?raw=true",
#         "description": "You can grow crops and flowers with the new cards you have learned",
#         "label": "🌱NewCardFarm 1",
#         "link": "https://www.patreon.com/posts/how-to-use-new-0-105040125?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link"},

#     {"url": "https://github.com/shigeyukey/my_addons/blob/main/media_files/Add-ons_AnkiWeb_media/merged_resize.gif?raw=true",
#         "description": "You can grow crops and flowers with the new cards you have learned",
#         "label": "🌱NewCardFarm 2",
#         "link": "https://www.patreon.com/posts/how-to-use-new-2-109485931?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link"},

#     {"url": "https://github.com/shigeyukey/my_addons/blob/main/media_files/output_08.gif?raw=true",
#         "description": "Multiple mini games",
#         "label": "⚔️AnkiArcade",
#         "link": "https://github.com/shigeyukey/AnkiArcade/wiki"},

#     {"url": "https://github.com/shigeyukey/my_addons/blob/main/media_files/AnkiCoins_faster.gif?raw=true",
#         "description": "Kill streak extension",
#         "label": "🎖️AnkiCoins",
#         "link": "https://www.patreon.com/posts/how-to-use-anki-99615150?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link"},

# ]

# buttons = [
#     {
#     "url": "🟢",
#     "label": "🟢",
#     "description": "🟢",
#     "link": "🟢"},
# ]


"""
(Patron)
(Free)
(Free, Fork)
(Free, Original)


"""

buttons = [


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_Medley.webp",
    "label": "⚔️AnkiArcade Medley",
    "description": "(Patron) multiple mini games, progress bar, pomodoro timer, and more.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/Home.html"},


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon(01).webp",
    "label": "🌱New Cards Farm 2",
    "description": "(Patron) You can grow crops and flowers with the new cards you have learned.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/new-card-farm/new-card-farm-02.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_new_cards_farm.webp",
    "label": "🌱New Cards Farm",
    "description": "(Patron) You can grow crops and flowers with the new cards you have learned.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/new-card-farm/new-card-farm-01.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/new_card_heatmap.webp",
    "label": "📅New Card Heatmap",
    "description": "(Patron) Show calendar and streaks of New cards learned, like the review heatmap.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/new-card-heatmap.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon-dinotimer.webp",
    "label": "🦖Dinotimer",
    "description": "(Patron) DinoTimer - Raising Dinosaurs with Pomodoro Study.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/dino-timer.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_pomotimer.webp",
    "label": "🍅Pomotimer",
    "description": "(Patron) Circular progress bar with transparent background.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/pomotimer.html"},



    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnail_AnkiKnights%20and%20Dragons.webp",
    "label": "⚔️AnkiKnights and Dragons",
    "description": "(Patron) The knights fight many monsters.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/01-anki-knights--doragons.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnail_little_Ankimare.webp",
    "label": "💎Little Ankimare",
    "description": "(Patron) The hooded protagonist explores a mysterious cave in search of gemstones.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/02-little-ankimares.html"},


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnail_study_with_Zombie.webp",
    "label": "🧟Study with Zombie",
    "description": "(Patron) Improved version of Doomanki, zombie emerges.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/05-study-with-zombie.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnail_Resident_Anki.webp",
    "label": "🧟Resident Anki",
    "description": "(Patron) Shooting Game with Mini Zombies.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/06-resident-anki.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/Doomanki.webp",
    "label": "🔫Doomanki",
    "description": "(Patron) Anki addon like FPS game. When you answer, gun animations, gunshot sounds, explosions.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/doomanki.html"},


    # {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_Mozartanki.webp",
    # "label": "🎵Mozartanki",
    # "description": "🟢",
    # "link": "🟢"},


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_meowknight.webp",
    "label": "🐱Meowknight",
    "description": "(Patron) Cat knight fighting theme.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/13-meowknight.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_cats.webp",
    "label": "🐱Cat Gathering in Anki",
    "description": "(Patron) Cats walking and running around.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/07-%EF%B8%8Fcat-gathering-in-anki.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/top_toolbar_icons.webp",
    "label": "🎨Top toolbar icons",
    "description": "(Patron) Decks Add-Browse-Stats-Sync",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/top-toolbar-icons.html"},


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_mozartanki.webp",
    "label": "🎵Mozartanki",
    "description": "(Patron) MIDI music player with 328 classical music tracks.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/11-mozartanki.html"},


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnail_CatGirlandSushi.webp",
    "label": "🐱Cat Girl and Sushi",
    "description": "(Patron) Cute CatGirl eats a lot of Sushi.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/03-catgirl--sushi.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_redwitch_darkwitch.webp",
    "label": "🧙Redwitch Darkwitch",
    "description": "(Patron) Wizard transforms",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/14-redwitch.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/just_do_it_timer.webp",
    "label": "🔥Just Do Anki timer",
    "description": "(Patron) Pomodoro timer with voice and animation that shouts JustDoIt when the time is up.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/just-anki-timer.html"},


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_terminator.webp",
    "label": "🤖AnkiTerminator SR-800",
    "description": "(Patron) Cute mascot character for Ankis reviews.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/09-ankiterminator-sr-800.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_v-ankipad.webp",
    "label": "🎮Virtual Ankipad",
    "description": "(Patron) Review screens will show answer buttons like the gamepad.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/10-virtual-ankipad.html"},

    # {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/banner_virtual_ankipad.webp",
    # "label": "🎮Virtual Ankipad",
    # "description": "🟢",
    # "link": "🟢"},

    # {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_ankiarcade5.webp",
    # "label": "⚔️Ankiarcade5",
    # "description": "🟢",
    # "link": "🟢"},


    # {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnail_AnkiArcade.webp",
    # "label": "⚔️AnkiArcade",
    # "description": "🟢",
    # "link": "🟢"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_ambient.webp",
    "label": "⭐Ambient",
    "description": "(Patron) Ambient sounds such as bonfires and rainfall are played instead of music.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/04-ambiebt-music.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_zenmode.webp",
    "label": "🧘‍♀Zenmode",
    "description": "(Patron) Turns off all animation, progress bar, and music.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/08-%EF%B8%8Fzen-mode.html"},

    # FREE add-ons

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/Anki_Leader_bord.webp",
    "label": "🏆Anki Leaderboard",
    "description": "(Free, Custom) Compete with friends to boost motivation",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/anki-leaderboard.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/anki_kill_streaks.webp",
    "label": "🎖️Anki Killstreaks",
    "description": "(Free, Fixed) Reward Medals for Correct Answers",
    "link": "https://ankiweb.net/shared/info/1562475180"},#🟢

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/Animated_coins.webp",
    "label": "🎖️Animation coins",
    "description": "(Patron) You can add animated coins to the Anki killstreaks.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/additional-animation-coins.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/progress_bar.webp",
    "label": "⌛️Progress bar",
    "description": "(Free, Custom) Visualize reviewed cards and remaining",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/progress-bar.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_progress_bar_for_Anki_how_to_use.webp",
    "label": "⌛️Progress Bar for Anki",
    "description": "(Patron) Progress bars for chunking Anki cards.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/progress-bar-for-anki.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/pokemanki.webp",
    "label": "🎮️Pokemanki Gold",
    "description": "(Free, Custom) Raising Pokemon with Anki.",
    "link": "https://ankiweb.net/shared/info/1677779223"},#🟢

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/AnkiTerminator_Thumbnail.webp",
    "label": "🤖AnkiTerminator-AI",
    "description": "(Free, Original) ChatGPT Sidebar for Review, GoogleBard, BingChat",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiTerminator/anki_terminator_00.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/NoDistractionsFullScreen.webp",
    "label": "🖥️No Distractions Full Screen",
    "description": "(Free, Fixed) Hides all the distractions such as menu bars, etc., there are cool answer buttons.",
    "link": "https://ankiweb.net/shared/info/1370336700"},#🟢

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/AlwaysOnTop.webp",
    "label": "🔝Always On Top",
    "description": "(Free, Fixed) permanently keep Anki as top",
    "link": "https://ankiweb.net/shared/info/1045980020"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/zoom24.webp",
    "label": "🔍️Zoom for Anki24",
    "description": "(Free, Custom) Keep zoom level after reboot",
    "link": "https://ankiweb.net/shared/info/1923741581"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/AnkiRedesign.webp",
    "label": "🎨Anki Redesign",
    "description": "(Free, Fixed) Make Anki Cool Design",
    "link": "https://ankiweb.net/shared/info/1959668791"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/break_timer.webp",
    "label": "☕Break Timer",
    "description": "(Free, Original) After 10 cards, take a 3 minute break",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/break-timer.html"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/todayAgainCount.webp",
    "label": "🎮Today Again Count",
    "description": "(Free, Original) Display todays Again count in menu bar for each card",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/today-again-count.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnail_ankiRestart.webp",
    "label": "🔂AnkiRestart",
    "description": "(Free, Original) just adds a reboot button to the menu bar.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/ankirestart.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/tidyankibear.webp",
    "label": "🐻Tidyankibear",
    "description": "(Free, Original) Select and hide Anki menu bar items.",
    "link": "https://ankiweb.net/shared/info/906950015"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/Rearrange_home_addons.webp",
    "label": "📌Rearrange home addons",
    "description": "(Free, Original) Rearrange the add-ons displayed on Ankis home screen.",
    "link": "https://ankiweb.net/shared/info/1797615099"},


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/EaseScouter_thumbnail.webp",
    "label": "👓️EaseScouter",
    "description": "(Patron) Visual feedback on Ease, Answer and Interval with multilingual text. ",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/easescouter.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/An_Ki_Oh_thumbnail.webp",
    "label": "🃏An-ki-oh!",
    "description": "(Patron) Anki card templates like a monster card game.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/an-ki-oh.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/Bulk_Image_Downloader.webp",
    "label": "🦾Bulk Image Downloader",
    "description": "(Free, Original) Add images to many cards at once, and quickly add images to cards during reviews.",
    "link": "https://ankiweb.net/shared/info/8280891"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/Editor_Auto_Show.webp",
    "label": "📝Editor auto show",
    "description": "(Free, Original) Editor auto show or hide during review",
    "link": "https://ankiweb.net/shared/info/1715279230"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/DiscordSidebar.webp",
    "label": "📱Anki Discord Sidebar",
    "description": "(Free, Original) Chat room within Anki",
    "link": "https://ankiweb.net/shared/info/33855257"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/AutoHighlight.webp",
    "label": "🖌️Auto Highlight Cloze in Browser",
    "description": "(Free, Custom) auto Highlight Cloze of selected card in Browser.",
    "link": "https://ankiweb.net/shared/info/210078606"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/GraphView.webp",
    "label": "📊Graph View",
    "description": "(Free, Fixed) Link notes and visualize connections ",
    "link": "https://ankiweb.net/shared/info/1068714931"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/PreviewSlideshow.webp",
    "label": "⏩Preview Slideshow",
    "description": "(Free, Fixed) Make Anki preview window as slideshow.",
    "link": "https://ankiweb.net/shared/info/1621302762"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/RandomSprite.webp",
    "label": "👾Random Sprites",
    "description": "(Free, Fixed) Find new random image on cards",
    "link": "https://ankiweb.net/shared/info/1956685960"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/AnkiIPA.webp",
    "label": "🔊Anki IPA",
    "description": "(Free, Fixed) Add phonetic symbols",
    "link": "https://ankiweb.net/shared/info/391848360"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/AnkiOCR.webp",
    "label": "📸Anki OCR",
    "description": "(Free, Fixed) Generate OCR text from images.",
    "link": "https://ankiweb.net/shared/info/546383173"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/PasteOCR.webp",
    "label": "📸PasteOCR",
    "description": "(Free, Fixed) Paste image as text.",
    "link": "https://ankiweb.net/shared/info/1808435406"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/BrowserExternalEditor.webp",
    "label": "📝Browser external editor",
    "description": "(Free, Fixed) open separate window",
    "link": "https://ankiweb.net/shared/info/1284875472"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/AnkiConnectDowngrader.webp",
    "label": "🔙Anki Connect Downgrader",
    "description": "(Free, Fixed) for downgrading Anki Connect.",
    "link": "https://ankiweb.net/shared/info/1485099361"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/AnkiPet.webp",
    "label": "🐤AnkiPet",
    "description": "(Free, Fixed) gamify your learning by caring for a pet ",
    "link": "https://ankiweb.net/shared/info/2026040256"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/AnniesCatEmporium.webp",
    "label": "🐈️Annies Cat Emporium",
    "description": "(Free, Fixed) For every UWorld block completed, the plug-in will give the user one cat.",
    "link": "https://ankiweb.net/shared/info/741979554"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/AnswerFeedback.webp",
    "label": "🎮️Answer feedback",
    "description": "(Free, Custom) Answer feedback, same as Ankimote.",
    "link": "https://ankiweb.net/shared/info/724185003"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/Beeline.webp",
    "label": "🐝BeeLine",
    "description": "(Free, Fixed) Color gradients for better Reading Focus",
    "link": "https://ankiweb.net/shared/info/122706731"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/CopyNotes.webp",
    "label": "📋Copy notes",
    "description": "(Free, Fixed) Allow to copy notes selected in the browser. ",
    "link": "https://ankiweb.net/shared/info/800604861"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/googleDictionary.webp",
    "label": "🌍️Google Dictionary",
    "description": "(Free, Fixed) add Google Dictionary results to vocabulary entries",
    "link": "https://ankiweb.net/shared/info/1947506677"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/AddNotesID.webp",
    "label": "🆔Add note ID",
    "description": "(Free, Fixed) adds a uuid to an empty field Note ID when opening edit note window.",
    "link": "https://ankiweb.net/shared/info/8897764"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/MultiDeckInporter.webp",
    "label": "📥Multi Deck Importer",
    "description": "(Free, Fixed) to import multiple decks at a time.",
    "link": "https://ankiweb.net/shared/info/1563006742"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/LeechToolKit.webp",
    "label": "🩸Leech Toolkit ",
    "description": "(Free, Fixed) Advanced leech tag management",
    "link": "https://ankiweb.net/shared/info/1633380637"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/Dict2Anki.webp",
    "label": "🐼Dict2Anki",
    "description": "(Free, Fixed) for native Chinese speakers",
    "link": "https://ankiweb.net/shared/info/1019143216"},



    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/NoSpaceDash.webp",
    "label": "🏃🏻No Space Dash",
    "description": "(Free, Fixed) Prevents answer for 1.5 seconds",
    "link": "https://ankiweb.net/shared/info/1573867049"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/RemoveTooltip.webp",
    "label": "👻Remove tooltip for Answer buttons",
    "description": "(Free, Custom) to remove tooltips for buttons like Shortcut key",
    "link": "https://ankiweb.net/shared/info/1845966780"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/RenderedBrowser.webp",
    "label": "🔍Rendered Browser",
    "description": "(Free, Fixed) Show multiple cards at once ",
    "link": "https://ankiweb.net/shared/info/648503413"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/reset%20card%20scheduring.webp",
    "label": "🗑️Reset Card Scheduling",
    "description": "(Free, Fixed) handling accidentally imported scheduling data from other users.",
    "link": "https://ankiweb.net/shared/info/83793850"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/ReviewHighlighter.webp",
    "label": "🖍️Review Highlighter",
    "description": "(Free, Original) Auto highlight card text in order",
    "link": "https://ankiweb.net/shared/info/452681944"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/SimpleTimer.webp",
    "label": "⏰️Simple Timer and Stopwatch",
    "description": "(Free, Fixed) Built-in Clock, Timer and Stopwatch ",
    "link": "https://ankiweb.net/shared/info/2041168053"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/Syllabus.webp",
    "label": "📊Syllabus",
    "description": "(Free, Fixed) Anki Statistics and Export by Tag and Deck",
    "link": "https://ankiweb.net/shared/info/1403834620"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/SyncToObsidian.webp",
    "label": "🪨Sync to Obsidian",
    "description": "(Free, Fixed) helps sync selected Anki note to your Obsidian vault.",
    "link": "https://ankiweb.net/shared/info/1979329733"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/TagStatistics.webp",
    "label": "📊Tag Statistics",
    "description": "(Free, Fixed) adds a dialog to Anki that displays some statistics about your tags.",
    "link": "https://ankiweb.net/shared/info/1269070743"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/TemplatesImportAndExport.webp",
    "label": "📤Templates Import and Export",
    "description": "(Free, Fixed) A tool for Anki user to import export CSS and card templates of all note types.",
    "link": "https://ankiweb.net/shared/info/2032572419"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/MathDelimitersReplacer.webp",
    "label": "🧮Math Delimiters Replacer",
    "description": "(Free, Fixed) for LaTex MathJax",
    "link": "https://ankiweb.net/shared/info/401047458"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/TriggerAndActions.webp",
    "label": "⛓️Trigger and actions",
    "description": "(Free, Fixed) Change card based on another ",
    "link": "https://ankiweb.net/shared/info/119880939"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/AddMediaEasy.webp",
    "label": "🖼️Add media easy",
    "description": "(Free, Fixed) to speed up the routine process of adding media files.",
    "link": "https://ankiweb.net/shared/info/1920408989"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/AutoEaseFactor.webp",
    "label": "📊Auto Ease Factor",
    "description": "(Free, Fixed) Dynamically adjusts ease factor on cards automatically after each rep",
    "link": "https://ankiweb.net/shared/info/179120908"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/HistoryRecorder.webp",
    "label": "💾History Recorder",
    "description": "(Free, Fixed) word cloud and statistics ",
    "link": "https://ankiweb.net/shared/info/510715849"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/ScrollinReviewer.webp",
    "label": "🖱️Scroll in reviewer",
    "description": "(Free, Fixed) Scroll in reviewer with vi vim-like keys j and k ",
    "link": "https://ankiweb.net/shared/info/1241205467"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails03/ReadableAddonsFolder.webp",
    "label": "📂Readable Addons Folder",
    "description": "(Free, Custom)  containing symlinks with the name of the add-on to the add-on folder.",
    "link": "https://ankiweb.net/shared/info/158759867"},


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_simple_fix.webp",
    "label": "🔧Fix broken add-ons",
    "description": "(Contact) You can send me repair requests for broken add-ons.(Free)",
    "link": "https://www.patreon.com/posts/free-simple-fix-99149368"},


    ]


#     {
#     "url": "🟢",
#     "label": "🟢",
#     "description": "🟢",
#     "link": "🟢"},


# HTMLｺﾝﾃﾝﾂを生成
HTML_CONTENT = generate_html_content(buttons)



# 指定されたﾊﾟｽ
file_path = f'G:/among anki/_00_Github/Shige-Addons/shige-addons/HTML/{HTML_FILE_NAME}'

os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(HTML_CONTENT)
