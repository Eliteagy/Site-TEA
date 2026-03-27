
import re

# 1. Configuration
brand_name = "The Elite Lake"
canonical_url = "https://the-elite-lake.vercel.app/"
whatsapp_link = "https://wa.me/351924132341?text=Ol%C3%A1%20Elite%20Lake%2C%0A%0AQuero%20marcar%20uma%20chamada%20estrat%C3%A9gica"

# 2. Read the current (messy) index.html
with open('index.html', 'r', encoding='utf-8') as f:
    full_content = f.read()

def extract_section(content, marker_start, marker_end_next):
    """Extracts content between two markers."""
    try:
        # We look for the marker and take until the next major marker starts
        start_pos = content.find(marker_start)
        if start_pos == -1: return ""
        
        # Find the next section start to know where to stop
        end_pos = content.find(marker_end_next, start_pos + len(marker_start))
        if end_pos == -1:
            # If no next marker, take a reasonable amount or find </body>
            end_pos = content.find("</section>", start_pos) + 10
            if end_pos < 10: end_pos = content.find("</body>", start_pos)
            
        return content[start_pos:end_pos]
    except:
        return ""

# 3. Extract core sections
# We'll use the markers we found
problema = extract_section(full_content, "<!-- ========== PROBLEMA SECTION", "<!-- ========== AGITAÇÃO")
agitacao = extract_section(full_content, "<!-- ========== AGITAÇÃO", "<!-- ========== SISTEMA")
sistema = extract_section(full_content, "<!-- ========== SISTEMA", "<!-- ========== OFFER")
offer = extract_section(full_content, "<!-- ========== OFFER", "<section class=\"partners")
partners = extract_section(full_content, "<section class=\"partners", "<section class=\"commercial-partnership")
partnership = extract_section(full_content, "<section class=\"commercial-partnership", "<section class=\"credibility")
credibility = extract_section(full_content, "<section class=\"credibility", "<section class=\"faq")
faq = extract_section(full_content, "<section class=\"faq", "<section class=\"cta-final")
cta_final = extract_section(full_content, "<section class=\"cta-final", "<footer>")
footer = extract_section(full_content, "<footer>", "</html>") + "</html>"

# 4. Assemble the NEW index.html
# Use the user's Step 225 Head/Top as base (I'll reconstruct it based on what I have)

# Head & Styles
head_top = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>{brand_name} — Parceiro Exclusivo dos Melhores Negócios Locais</title>
    <link rel="canonical" href="{canonical_url}">
    <meta property="og:title" content="{brand_name} — Parceiro Exclusivo dos Melhores Negócios Locais">
    <meta property="og:url" content="{canonical_url}">
    <link rel="icon" type="image/png" href="https://res.cloudinary.com/dooigd0d3/image/upload/v1766771870/GENERATION-removebg-preview_yfwn01.png">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
"""

# Extract the <style> and <body> start from the current file's first valid page
# (We'll take lines 9 to 1856 of our current file as they are correct)
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
styles_and_top_body = "".join(lines[8:1856]) # lines 9 to 1856 approx

# 5. Combine everything
new_index = head_top + styles_and_top_body + problema + agitacao + sistema + offer + partners + partnership + credibility + faq + cta_final + footer

# 6. Apply global branding replacements to the new assembly
new_index = new_index.replace("The Elite Agency", brand_name)
new_index = new_index.replace("wa.me/351924132341?text=Ol%C3%A1%20Elite%20Agency", f"wa.me/351924132341?text=Ol%C3%A1%20Elite%20Lake")

# 7. Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

print("Surgical reconstruction complete!")
