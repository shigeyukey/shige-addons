# Copyright (C) Shigeyuki <http://patreon.com/Shigeyuki>
# License: GNU AGPL version 3 or later <http://www.gnu.org/licenses/agpl.html>

import os
import json
import base64

HTML_FILE_NAME = 'shige_addons_v2.html'

STR_PAGE_TITLE = "Shige addons"

STR_TOP_TITLE_TEXT = "💖Looking for Supporters!"

STR_TOP_TEXT = """\
Hi I’m Shigeඞ a developer and bookworm who loves Anki! I’ve been active since 2023 and have developed 150+ add-ons so far (fixed, customized, created). I'm looking for supporters on Patreon to develop many more powerful and useful add-ons in the future! If you become a patron you’ll get access to all my patron exclusive add-ons for gamifying learning. (Not related to the official Anki)
"""

STR_PATREON_LINK = (
                f'<a href="https://www.patreon.com/Shigeyuki" '
                f'target="_blank" '
                f'style="color: #1e90ff;" '
                f'>'
                )

STR_SUB_TITLE_TEXT = (
                    f"🎮Shige's addo-ns "
                    f"{STR_PATREON_LINK}"
                    f"(Patreon $5/month)"
                    f"</a>"
                    )

STR_SUB_TEXT = """\
If you become a $5/month Patron you can download all of these Patron exclusive add-ons:
"""


BASE_DIR = os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__))
                )


def get_image_as_base64(image_path:str):
    try:

        full_path = os.path.join(
                                BASE_DIR,
                                image_path.lstrip('/'))

        print(full_path)
        if os.path.exists(full_path):
            with open(full_path, 'rb') as img_file:
                encoded = base64.b64encode(
                            img_file.read()).decode('utf-8')
                ext = os.path.splitext(full_path)[1].lower()
                mime_type = {
                    'jpg': 'image/jpeg',
                    'jpeg': 'image/jpeg',
                    'png': 'image/png',
                    'webp': 'image/webp'
                    }.get(ext[1:], 'image/png')
                return f"data:{mime_type};base64,{encoded}"

    except Exception as e:
        print(f"Error: {image_path} - {e}")

    return None



def make_html_content(addon_contents):
    items_html = ""

    for item in addon_contents:
        item:dict

        item_date = item.get("date", "")
        item_url = item.get("url", "")
        item_label = item.get("label", "")
        item_link = item.get("link", "")
        item_description = item.get("description", "")

        date_html = ""
        if item_date:
            date_html = f'<p class="image-date">{item_date}</p>'

        if item_url:
            base64_image = get_image_as_base64(item_url)
            if base64_image:
                html_addon_content = (
                    f'<img src="{base64_image}" alt="{item_label}">'
                    )
            else:
                html_addon_content = (
                    f'<div class="no-image">Image Load Failed</div>'
                )
        else:
            html_addon_content = (
                f'<div class="no-image">No Image</div>'
                )


        items_html += f"""
        <div class="item-card">
            <div class="item-image-container">
                {html_addon_content}
            </div>
            {date_html}
            <h3 class="item-label">{item_label}</h3>
            <p class="item-description">{item_description}</p>
            <a href="{item_link}" target="_blank" class="item-link">View Details</a>
        </div>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html>
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
                margin-bottom: 10px;
            }}

            .header h1 {{
                font-size: 32px;
                margin-bottom: 10px;
            }}

            .header p {{
                font-size: 12px;
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

            .image-date {{
                font-size: 12px;
                color: #aaaaaa;
                padding: 5px 10px;
                margin: 0;
                text-align: right;
            }}

            .no-image {{
                color: #666666;
                font-size: 14px;
            }}

            .item-label {{
                font-size: 18px;
                font-weight: bold;
                padding: 2px 5px 8px 15px;
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
            <h4>{STR_TOP_TITLE_TEXT}</h4>
            <p>{STR_TOP_TEXT}</p>
            <h4>{STR_SUB_TITLE_TEXT}</h4>
            <p>{STR_SUB_TEXT}</p>
        </div>

        <div class="items-grid">
            {items_html}
        </div>
    </body>
    </html>
    """

    return html_content

# https://shigeyukey.github.io/shige-addons-wiki/patrons_q_and_a.html"

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'addon_contents.json')

with open(json_path, 'r', encoding='utf-8') as f:
    addon_contents = json.load(f)

html_content = make_html_content(addon_contents)

file_path = f'G:/among anki/_00_Github/Shige-Addons/shige-addons/HTML/{HTML_FILE_NAME}'

os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

"""
    {
        "url": "/addons_media/🟩.webp",
        "label": "addon: 🟩",
        "description": "🟩",
        "link": "https://shigeyukey.github.io/shige-addons-wiki/🟩",
        "date":"Last update: 🟩"
    },
"""

