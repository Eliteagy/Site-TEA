
import os
import re

print("Starting ULTIMATE RECONSTRUCTION...")

def get_file(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Load modules
p_html = get_file('parceiro-comercial.html')
top_html = get_file('new_html_top.html')
base_html = get_file('index_test.html')
mascot_b64 = get_file('mascot_base64.txt').strip()

# 1. Extract Head & Styles
head_start = p_html.find('<head>')
head_end = p_html.find('</head>')
if head_start == -1 or head_end == -1:
    # Use base_html as fallback
    head_start = base_html.find('<head>')
    head_end = base_html.find('</head>')
    final_head = base_html[head_start:head_end+7].replace('The Elite Lake', 'The Elite Agency')
else:
    final_head = p_html[head_start:head_end+7].replace('The Elite Lake', 'The Elite Agency')

# Ensure stars.css is linked
if "stars.css" not in final_head:
    final_head = final_head.replace("</head>", '    <link rel="stylesheet" href="assets/css/stars.css">\n</head>')

# 2. Extract Sections
def extract_section(text, start_marker, end_marker):
    start = text.find(start_marker)
    if start == -1: return ""
    end = text.find(end_marker, start)
    if end == -1: return text[start:]
    return text[start:end]

pillars = extract_section(p_html, '<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->', '<!-- ========== SECTION 5: QUALIFICAÇÃO ========== -->')
timeline = extract_section(p_html, '<!-- ========== SECTION 3: COMO FUNCIONA (TIMELINE) ========== -->', '<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->')
comparison = extract_section(p_html, '<!-- ========== SECTION 6: PACKS / NÍVEIS DE SERVIÇO ========== -->', '<!-- ========== SECTION 7: GARANTIAS ========== -->')
faq_footer = extract_section(base_html, '<!-- ========== FAQ SECTION', '</html>')

# 3. Assemble Body
# We'll use top_html as the core body start
body_content = '<body>\n<div class="starry-background" id="starryBg"></div>\n'
body_content += top_html + '\n'
body_content += pillars + '\n' + timeline + '\n' + comparison + '\n'
body_content += faq_footer

# 4. Final Processing & Branding
full_html = '<!DOCTYPE html>\n<html lang="pt">\n' + final_head + '\n' + body_content

# Mascot Integration
if mascot_b64:
    # Look for Mestre Capinhas and insert mascot
    full_html = re.sub(r'(Mestre Capinhas.*?Vendas Online.*?</div>)', r'\1\n<div class="tc-mascote" style="position: absolute; bottom: -20px; right: -10px; width: 100px; opacity: 0.8;"><img src="data:image/png;base64,' + mascot_b64 + r'" style="width:100%;" alt="Mascote"></div>', full_html, flags=re.DOTALL)

# Branding Fix
full_html = full_html.replace('The Elite Lake', 'The Elite Agency')
full_html = full_html.replace('Elite Lake', 'Elite Agency')
full_html = full_html.replace('Olá%20Elite%20Lake', 'Olá%20Elite%20Agency')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("ULTIMATE RECONSTRUCTION COMPLETE! The site is back.")
