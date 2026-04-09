# Copyright (C) Shigeyuki <http://patreon.com/Shigeyuki>
# License: GNU AGPL version 3 or later <http://www.gnu.org/licenses/agpl.html>

import os
import json

HTML_FILE_NAME = 'shige_addons_v2.html'

STR_PAGE_TITLE = "Shige addons"
STR_TITLE_TEXT = "🎮Shige's addo-ns (for Patrons)"

STR_TOP_TEXT = """\
Hi I’m Anki geek and developer Shigeඞ! So far I’ve developed 150+ Anki add-ons (fixed, customized, created). If you support my volunteer development on Patreon you’ll get access to exclusive add-ons. ($5/month. Not related to the official Anki)
"""


def make_html_content(addon_contents):
    items_html = ""
    for item in addon_contents:
        item:dict

        item_date = item.get("date", "")
        item_url = item.get("url", "")
        item_label = item.get("label", "")
        item_link = item.get("link", "")
        item_description = item.get("description", "")

        if item_url:
            html_addon_content =  f'<img src="{item_url}" alt="{item_label}">'
        else:
            html_addon_content =  '<div class="no-image">No Image</div>'

        items_html += f"""
        <div class="item-card">
            <div class="item-image-container">
                {html_addon_content}
            </div>
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


