import os



HTML_FILE_NAME = 'shige_addons_v2.html'

STR_PAGE_TITLE = "Shige addons"
STR_TITLE_TEXT = "🎮Shige's  addo-ns (for Patrons)"

STR_TOP_TEXT = """\
Hi I’m Anki geek and developer Shigeඞ! So far I’ve developed 150+ add-ons (fixed, customized, created). If you support my volunteer development on Patreon you’ll get access to exclusive add-ons. ($5/Month. Not related to the official Anki)
"""




def generate_image_html(url, label):
    if url:
        return f'<img src="{url}" alt="{label}">'
    else:
        return '<div class="no-image">No Image</div>'


def generate_html_content(addon_contents):
    items_html = ""
    for index, addon_content in enumerate(addon_contents):
        html_addon_content = generate_image_html(
                                addon_content["url"],
                                addon_content["label"]
                                )
        items_html += f'''
        <div class="item-card">
            <div class="item-image-container">
                {html_addon_content}
            </div>
            <h3 class="item-label">{addon_content["label"]}</h3>
            <p class="item-description">{addon_content["description"]}</p>
            <a href="{addon_content["link"]}" target="_blank" class="item-link">View Details</a>
        </div>
        '''

    HTML_CONTENT = f"""
    <!DOCTYPE html>
    <html>
    <meta http-equiv="Permissions-Policy" content="interest-cohort=()">
    <head>
        <title>{STR_PAGE_TITLE}</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Arial', sans-serif;
                background-color: #222222;
                color: #ffffff;
                padding: 20px;
            }}

            .header {{
                text-align: center;
                margin-bottom: 40px;
            }}

            .header h1 {{
                font-size: 32px;
                margin-bottom: 10px;
            }}

            .header p {{
                font-size: 14px;
                color: #aaaaaa;
            }}

            .items-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 20px;
                max-width: 1400px;
                margin: 0 auto;
            }}

            .item-card {{
                background-color: #333333;
                border: 1px solid #444444;
                border-radius: 10px;
                overflow: hidden;
                transition: transform 0.2s, box-shadow 0.2s;
                display: flex;
                flex-direction: column;
            }}

            .item-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
            }}

            .item-image-container {{
                width: 100%;
                height: 200px;
                background-color: #1a1a1a;
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: hidden;
            }}

            .item-image-container img {{
                width: 100%;
                height: 100%;
                object-fit: contain;
                background-color: #1a1a1a;
            }}

            .no-image {{
                color: #666666;
                font-size: 14px;
            }}

            .item-label {{
                font-size: 18px;
                font-weight: bold;
                padding: 15px 15px 8px 15px;
                color: #1e90ff;
            }}

            .item-description {{
                font-size: 13px;
                color: #cccccc;
                padding: 0 15px 12px 15px;
                flex-grow: 1;
            }}

            .item-link {{
                display: inline-block;
                margin: 0 15px 15px 15px;
                padding: 8px 15px;
                background-color: #1e90ff;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 12px;
                font-weight: bold;
                text-align: center;
                transition: background-color 0.2s;
            }}

            .item-link:hover {{
                background-color: #1478d2;
                cursor: pointer;
            }}

            ::-webkit-scrollbar {{
                width: 16px;
            }}

            ::-webkit-scrollbar-track {{
                background-color: #333333;
            }}

            ::-webkit-scrollbar-thumb {{
                background-color: rgba(255, 255, 255, 0.3);
                border-radius: 10px;
                border: 3px solid transparent;
                background-clip: content-box;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h3>{STR_TITLE_TEXT}</h3>
            <p>{STR_TOP_TEXT}</p>
        </div>

        <div class="items-grid">
            {items_html}
        </div>
    </body>
    </html>
    """

    return HTML_CONTENT

addon_contents = [


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/refs/heads/main/addons_media/thumbnails04/00_animation.webp",
    "label": "Patreon only addons",
    "description": "Support my work on Patreon ($5/month) for access to Patrons-only add-ons!",
    # "link": "https://shigeyukey.github.io/shige-addons-wiki/patrons_q_and_a.html"
    "link": "https://www.patreon.com/Shigeyuki"
    },


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon(01).webp",
    "label": "addon: 🌱New Cards Farm 2",
    "description": "(Patron) You can grow crops and flowers with the new cards you have learned.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/new-card-farm/new-card-farm-02.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_Medley.webp",
    "label": "⚔️AnkiArcade Medley",
    "description": "(Patron) multiple mini games, progress bar, pomodoro timer, and more.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/Home.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_chunk_progressbar.webp",
    "label": "⌛️Chunk Progressbar",
    "description": "(Patron) Progress bars for chunking Anki cards.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/progress-bar-for-anki.html"},


    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/refs/heads/main/addons_media/thumbnails04/AnkiArcadev1.8.5.webp",
    "label": "⚔️AnkiArcade v1.8.5 update info",
    "description": "(Patron) multiple mini games, progress bar, pomodoro timer, and more.",
    "link": "https://youtu.be/DVr3pEDn3EM"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/refs/heads/main/addons_media/thumbnails04/LeadarboardPlus.webp",
    "label": "🎖️Anki Leaderboard Plus",
    "description": "(Patreon) Real time sync of the Anki Leaderbord during review",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/Anki-Leaderboard-Plus.html"},



    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnail_Resident_Anki.webp",
    "label": "🧟Resident Anki",
    "description": "(Patron) Shooting Game with Mini Zombies.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/06-resident-anki.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon-dinotimer.webp",
    "label": "🦖Dinotimer",
    "description": "(Patron) DinoTimer - Raising Dinosaurs with Pomodoro Study.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/dino-timer.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_pomotimer.webp",
    "label": "🍅Pomotimer",
    "description": "(Patron) Circular progress bar with transparent background.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/pomotimer.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_new_cards_farm.webp",
    "label": "🌱New Cards Farm",
    "description": "(Patron) You can grow crops and flowers with the new cards you have learned.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/new-card-farm/new-card-farm-01.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/new_card_heatmap.webp",
    "label": "📅New Card Heatmap",
    "description": "(Patron) Show calendar and streaks of New cards learned, like the review heatmap.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/new-card-heatmap.html"},

    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/EaseScouter_thumbnail.webp",
    "label": "👓️EaseScouter",
    "description": "(Patron) Visual feedback on Ease, Answer and Interval with multilingual text. ",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/easescouter.html"},

    {
    "url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/thumbnails02/Animated_coins_02.webp",
    "label": "🎖️Animation coins",
    "description": "(Patron) You can add animated coins to the Anki killstreaks.",
    "link": "https://shigeyukey.github.io/shige-addons-wiki/additional-animation-coins.html"},


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


    # {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/_thumbnail_terminator.webp",
    # "label": "🤖AnkiTerminator SR-800",
    # "description": "(Patron) Cute mascot character for Ankis reviews.",
    # "link": "https://shigeyukey.github.io/shige-addons-wiki/AnkiArcade/themes/09-ankiterminator-sr-800.html"},

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


    {"url": "https://raw.githubusercontent.com/shigeyukey/shige-addons/main/addons_media/patreon_simple_fix.webp",
    "label": "🔧Fix broken add-ons",
    "description": "(Contact) You can send me repair requests for broken add-ons.(Free)",
    "link": "https://www.patreon.com/posts/free-simple-fix-99149368"},

    ]

# HTML ｺﾝﾃﾝﾂを生成
HTML_CONTENT = generate_html_content(addon_contents)

# 指定されたﾊﾟｽ
file_path = f'G:/among anki/_00_Github/Shige-Addons/shige-addons/HTML/{HTML_FILE_NAME}'

os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(HTML_CONTENT)