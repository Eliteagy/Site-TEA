
import os
import re

print("Starting RECONSTRUCTION V3 (Bulletproof)...")

def get_file(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Load source files
p_html = get_file('parceiro-comercial.html')
top_html = get_file('new_html_top.html')
base_html = get_file('index_test.html')
mascot_b64 = get_file('mascot_base64.txt').strip()

# Helper to extract content between markers
def extract_section(text, start_marker, end_marker):
    start = text.find(start_marker)
    if start == -1: return ""
    end = text.find(end_marker, start)
    if end == -1: return text[start:]
    return text[start:end]

# 1. HEAD & STYLES (from parceiro-comercial for maximum feature coverage)
head_part = extract_section(p_html, '<head>', '</head>')
if not head_part:
    head_part = extract_section(base_html, '<head>', '</head>')

# Ensure stars.css and stars.js are referenced
head_part = head_part.replace('</head>', '    <link rel="stylesheet" href="assets/css/stars.css">\n</head>')

# 2. BODY CONSTRUCTION
# Start with the starry background
body_start = '<body style="background: #000000; color: #ffffff; margin: 0; padding: 0;">\n<div class="starry-background" id="starryBg"></div>\n'

# A. Header & Hero (extracted from new_html_top.html, skipping any <html>/<body> tags)
hero_section = top_html
# Clean up top_html if it has tags
hero_section = re.sub(r'<!DOCTYPE.*?>', '', hero_section, flags=re.IGNORECASE | re.DOTALL)
hero_section = re.sub(r'<html.*?>', '', hero_section, flags=re.IGNORECASE | re.DOTALL)
hero_section = re.sub(r'<head.*?</head>', '', hero_section, flags=re.IGNORECASE | re.DOTALL)
hero_section = re.sub(r'<body.*?>', '', hero_section, flags=re.IGNORECASE | re.DOTALL)
hero_section = re.sub(r'</body>', '', hero_section, flags=re.IGNORECASE)
hero_section = re.sub(r'</html>', '', hero_section, flags=re.IGNORECASE)

# B. Advanced Sections (from parceiro-comercial)
pillars = extract_section(p_html, '<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->', '<!-- ========== SECTION 5: QUALIFICAÇÃO ========== -->')
timeline = extract_section(p_html, '<!-- ========== SECTION 3: COMO FUNCIONA (TIMELINE) ========== -->', '<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->')
comparison = extract_section(p_html, '<!-- ========== SECTION 6: PACKS / NÍVEIS DE SERVIÇO ========== -->', '<!-- ========== SECTION 7: GARANTIAS ========== -->')

# C. Problem & Ecosystem (from base_html, if needed, but pillars might replace ecosystem)
problem = extract_section(base_html, '<!-- ========== PROBLEMA SECTION', '<!-- ========== ECOSYSTEM SECTION')

# D. Footer & FAQ (from base_html)
faq_footer = extract_section(base_html, '<!-- ========== FAQ SECTION', '</html>')
# Clean up faq_footer to only keep content before </html>
if '</html>' in faq_footer:
    faq_footer = faq_footer[:faq_footer.find('</html>')]

# 3. ASSEMBLE
final_body = body_start + hero_section + "\n" + problem + "\n" + pillars + "\n" + timeline + "\n" + comparison + "\n" + faq_footer + "\n"
final_body += '<script src="assets/js/stars.js"></script>\n</body>\n</html>'

# 4. FINAL POLISH
full_html = '<!DOCTYPE html>\n<html lang="pt">\n' + head_part + '\n' + final_body

# Mascot Branding in first card
if mascot_b64:
    # Try to insert into Mestre Capinhas card
    full_html = re.sub(r'(Mestre Capinhas.*?Vendas Online.*?</div>)', r'\1\n<div class="tc-mascote" style="position: absolute; bottom: -20px; right: -10px; width: 100px; opacity: 0.8;"><img src="data:image/png;base64,' + mascot_b64 + r'" style="width:100%;" alt="Mascote"></div>', full_html, flags=re.DOTALL)

# Global Branding Fix
full_html = full_html.replace('The Elite Lake', 'The Elite Agency')
full_html = full_html.replace('Elite Lake', 'Elite Agency')
full_html = full_html.replace('Olá%20Elite%20Lake', 'Olá%20Elite%20Agency')

# Fix Giant Icons: Inject small CSS fix into head
css_fix = """
<style>
    .warning-icon { width: 28px !important; height: 28px !important; min-width: 28px; }
    .warning-icon svg { width: 16px !important; height: 16px !important; }
    .tc-logo { width: 60px !important; height: 60px !important; object-fit: contain; }
    .tc-mascote img { max-width: 100px; }
    body { overflow-x: hidden; width: 100vw; }
    .container { max-width: 1400px !important; width: 100% !important; margin: 0 auto !important; }
</style>
"""
full_html = full_html.replace('</head>', css_fix + '</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("RECONSTRUCTION V3 COMPLETE! The site is restored and fixed.")
