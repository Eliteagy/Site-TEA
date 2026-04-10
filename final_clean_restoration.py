
import os
import re

print("Starting FINAL CLEAN RESTORATION...")

def get_file(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Load parts
p_html = get_file('parceiro-comercial.html')
top_html = get_file('new_html_top.html')
base_html = get_file('index_test.html')
with open('mascot_base64.txt', 'r', encoding='utf-8') as f:
    mascot_b64 = f.read().strip()

# 1. Extract the COMPLETE Head/Styles from parceiro-comercial
head_part = re.search(r'<head>(.*?)</head>', p_html, re.DOTALL).group(1)
# Fix Title
head_part = re.sub(r'<title>.*?</title>', '<title>The Elite Agency — Construímos Impérios Locais</title>', head_part)

# 2. Extract specific sections from parceiro-comercial
def extract_section(text, start_marker, end_marker):
    start = text.find(start_marker)
    if start == -1: return ""
    end = text.find(end_marker, start)
    if end == -1: return text[start:]
    return text[start:end]

pillars = extract_section(p_html, '<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->', '<!-- ========== SECTION 5: QUALIFICAÇÃO ========== -->')
timeline = extract_section(p_html, '<!-- ========== SECTION 3: COMO FUNCIONA (TIMELINE) ========== -->', '<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->')
comparison = extract_section(p_html, '<!-- ========== SECTION 6: PACKS / NÍVEIS DE SERVIÇO ========== -->', '<!-- ========== SECTION 7: GARANTIAS ========== -->')

# 3. Extract the Hero & Social Proof from top_html
# We only want the content inside the body-like area of top_html
hero_content = top_html
# Clean up any full-page tags that might be in top_html
hero_content = re.sub(r'<!DOCTYPE.*?>', '', hero_content, flags=re.IGNORECASE|re.DOTALL)
hero_content = re.sub(r'<html.*?>', '', hero_content, flags=re.IGNORECASE|re.DOTALL)
hero_content = re.sub(r'<head.*?>.*?</head>', '', hero_content, flags=re.IGNORECASE|re.DOTALL)
hero_content = re.sub(r'<body.*?>', '', hero_content, flags=re.IGNORECASE|re.DOTALL)
hero_content = re.sub(r'</body>', '', hero_content, flags=re.IGNORECASE)
hero_content = re.sub(r'</html>', '', hero_content, flags=re.IGNORECASE)

# 4. Extract FAQ & Footer from base_html
faq_footer = extract_section(base_html, '<!-- ========== FAQ SECTION', '</html>')
if '</html>' in faq_footer: faq_footer = faq_footer[:faq_footer.find('</html>')]

# 5. ASSEMBLE
final_html = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    {head_part}
    <link rel="stylesheet" href="assets/css/stars.css">
    <style>
        /* CSS FIXES FOR HORRIBLE LAYOUT */
        body {{ background: #000000 !important; margin: 0; padding: 0; min-height: 100vh; width: 100%; }}
        .starry-background {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; }}
        .container {{ max-width: 1400px !important; width: 100% !important; margin: 0 auto !important; padding: 0 20px !important; }}
        .hero {{ padding: 120px 0 60px !important; width: 100% !important; }}
        
        /* Fix Giant Icons */
        .warning-icon {{ width: 28px !important; height: 28px !important; min-width: 28px; display: inline-flex; align-items: center; justify-content: center; }}
        .warning-icon svg {{ width: 100% !important; height: 100% !important; }}
        svg {{ max-width: 100%; height: auto; }}
        
        /* Fix Layout Squeezing */
        section {{ width: 100% !important; position: relative; }}
        .hero-grid {{ display: grid; grid-template-columns: 1.2fr 1fr; gap: 60px; width: 100%; }}
        
        /* Mascot */
        .tc-mascote img {{ max-width: 120px; filter: drop-shadow(0 0 20px rgba(251,191,36,0.3)); }}
    </style>
</head>
<body>
    <div class="starry-background" id="starryBg"></div>
    
    {hero_content}
    
    {pillars}
    {timeline}
    {comparison}
    
    {faq_footer}
    
    <script src="assets/js/stars.js"></script>
</body>
</html>"""

# Mascot Insertion
if mascot_b64:
    final_html = re.sub(r'(Mestre Capinhas.*?Vendas Online.*?</div>)', r'\1\n<div class="tc-mascote" style="position: absolute; bottom: -24px; right: -16px; z-index: 10;"><img src="data:image/png;base64,' + mascot_b64 + r'" alt="Mascote"></div>', final_html, flags=re.DOTALL)

# Global Branding
final_html = final_html.replace('The Elite Lake', 'The Elite Agency')
final_html = final_html.replace('Elite Lake', 'Elite Agency')
final_html = final_html.replace('Olá%20Elite%20Lake', 'Olá%20Elite%20Agency')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("FINAL CLEAN RESTORATION COMPLETE! index.html is now perfect.")
