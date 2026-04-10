
import os
import re

print("Starting FINAL RECOVERY MERGE...")

# 1. Load Mascot
with open('mascot_base64.txt', 'r', encoding='utf-8') as f:
    mascot_b64 = f.read().strip()

# 2. Load Modules
with open('new_html_top.html', 'r', encoding='utf-8') as f:
    top_html = f.read()

with open('parceiro-comercial.html', 'r', encoding='utf-8') as f:
    p_html = f.read()

with open('index_test.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

def get_section(content, start_marker, end_marker):
    start = content.find(start_marker)
    if start == -1: return ""
    end = content.find(end_marker, start)
    if end == -1: return content[start:]
    return content[start:end]

# Extract Advanced Sections from parceiro-comercial
pillars_8 = get_section(p_html, "<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->", "<!-- ========== SECTION 5: QUALIFICAÇÃO ========== -->")
timeline = get_section(p_html, "<!-- ========== SECTION 3: COMO FUNCIONA (TIMELINE) ========== -->", "<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->")
comparison = get_section(p_html, "<!-- ========== SECTION 6: PACKS / NÍVEIS DE SERVIÇO ========== -->", "<!-- ========== SECTION 7: GARANTIAS ========== -->")

# Extract Styles (We need ALL styles merged)
style_start = base_html.find("<style>")
style_end = base_html.find("</style>")
base_styles = base_html[style_start:style_end+8]

# 3. Assemble the Ultimate Page
# Standard Head
head_end = base_html.find("</head>")
final_head = base_html[:head_end].replace("The Elite Lake", "The Elite Agency")
# Add link to stars.css if not there
if "stars.css" not in final_head:
    final_head = final_head.replace("</head>", '    <link rel="stylesheet" href="assets/css/stars.css">\n</head>')
else:
    final_head = final_head + "</head>"

# Body
final_body = '<body style="background: #000000;">\n<div class="starry-background" id="starryBg"></div>\n'
final_body += top_html # Hero + Social Proof + CTA

# Insert 8 Pillars and Timeline after Social Proof
problem_start = base_html.find("<!-- ========== PROBLEMA SECTION")
if problem_start == -1: problem_start = base_html.find("O Teu Negócio Tem Potencial")

# Transition from Top to Middle
final_body += pillars_8 + "\n" + timeline + "\n"

# Add the middle sections (Problem, Ecosystem - we'll keep the new pillars instead of old ecosystem)
middle_part = base_html[problem_start:]
# Remove the old ecosystem from middle_part if it exists
eco_start = middle_part.find("<!-- ========== ECOSYSTEM SECTION")
eco_end = middle_part.find("<!-- ==========", eco_start + 10)
if eco_start != -1 and eco_end != -1:
    middle_part = middle_part[:eco_start] + middle_part[eco_end:]

# Insert Comparison Table before FAQ
faq_start = middle_part.find("<!-- ========== FAQ SECTION")
if faq_start != -1:
    middle_part = middle_part[:faq_start] + comparison + "\n" + middle_part[faq_start:]

final_body += middle_part

# Add scripts
if "stars.js" not in final_body:
    final_body = final_body.replace("</body>", '<script src="assets/js/stars.js"></script>\n</body>')

# 4. Final Processing
full_html = final_head + final_body

# Mascot fix (Force it into Mestre Capinhas card if found)
if mascot_b64:
    # Look for Mestre Capinhas card and insert Mascot div before card end
    card_pattern = re.compile(r'(Mestre Capinhas.*?Vendas Online.*?</div>)', re.DOTALL)
    full_html = card_pattern.sub(r'\1\n<div class="tc-mascote" style="position: absolute; bottom: -20px; right: -10px; width: 100px; opacity: 0.8;"><img src="data:image/png;base64,' + mascot_b64 + r'" style="width:100%;" alt="Mascote"></div>', full_html)

# Global Branding
full_html = full_html.replace("The Elite Lake", "The Elite Agency")
full_html = full_html.replace("Elite Lake", "Elite Agency")
full_html = full_html.replace("Olá%20Elite%20Lake", "Olá%20Elite%20Agency")

# 5. Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("RECOVERY COMPLETE. Ultimate index.html generated with all modules and Branding.")
