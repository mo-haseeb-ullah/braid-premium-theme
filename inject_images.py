import os
import re

sections_dir = r'D:\Etsy_Shopify_Themes\My_First_Theme\sections'

for filename in os.listdir(sections_dir):
    if filename.startswith('braid-') and filename.endswith('.liquid'):
        filepath = os.path.join(sections_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace empty placeholder tags with hardcoded assets
        updated_content = re.sub(
            r'\{\{\s*''[^'']+''\s*\|\s*placeholder_svg_tag[^}]*\}\}',
            r'<img src="{{ ''braid-image-1.jpg'' | asset_url }}" style="width:100%;height:100%;object-fit:cover;">',
            content
        )
        
        if content != updated_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f'Updated {filename}')
