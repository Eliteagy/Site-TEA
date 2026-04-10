
import os
import re

print("Starting ULTIMATE MERGE...")

# 1. Load the Mascot Base64
with open('mascot_base64.txt', 'r', encoding='utf-8') as f:
    mascot_b64 = f.read().strip()

# 2. Extract sections from new_html_top.html (Sticky CTA + Hero + Social Proof Intro)
with open('new_html_top.html', 'r', encoding='utf-8') as f:
    top_content = f.read()

# 3. Extract sections from parceiro-comercial.html (8 Pillars, Timeline, Comparison Table)
with open('parceiro-comercial.html', 'r', encoding='utf-8') as f:
    p_content = f.read()

def extract_section(text, start_marker, end_marker):
    start = text.find(start_marker)
    if start == -1: return ""
    end = text.find(end_marker, start)
    if end == -1: return text[start:]
    return text[start:end]

# 8 Pillars (Features Grid)
pillars_section = extract_section(p_content, "<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->", "<!-- ========== SECTION 5: QUALIFICAÇÃO ========== -->")
# Timeline (Como Funciona)
timeline_section = extract_section(p_content, "<!-- ========== SECTION 3: COMO FUNCIONA (TIMELINE) ========== -->", "<!-- ========== SECTION 4: O QUE ESTÁ INCLUÍDO ========== -->")
# Comparison Table
comparison_section = extract_section(p_content, "<!-- ========== SECTION 6: PACKS / NÍVEIS DE SERVIÇO ========== -->", "<!-- ========== SECTION 7: GARANTIAS ========== -->")

# 4. Load the base index.html (the one restored from index_test.html)
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# 5. PERFORM REPLACEMENTS

# A. Header & Hero: Replace everything from body start to after social proof intro
# Actually, I'll just take the top part of index.html and replace from <body... onwards
body_start = index_content.find("<body")
if body_start != -1:
    head = index_content[:body_start]
    # We find where the "Problem" section starts in the original index.html
    problem_section_start = index_content.find("<!-- ========== PROBLEMA SECTION")
    if problem_section_start == -1: problem_section_start = index_content.find("O Teu Negócio Tem Potencial. Mas Está Invisível Online.")
    
    footer_part = index_content[problem_section_start:]
    
    # Assembly
    final_html = head + top_content + "\n" + footer_part
else:
    final_html = index_content # Fallback

# B. Insert Pillars, Timeline, Comparison
# We'll insert them after the Ecosystem section or replace it
ecosystem_marker = "<!-- ========== ECOSYSTEM SECTION"
ecosystem_pos = final_html.find(ecosystem_marker)
if ecosystem_pos != -1:
    # Find the next section start to replace the ecosystem
    next_section_pos = final_html.find("<!-- ==========", ecosystem_pos + 10)
    if next_section_pos != -1:
        # Replace Ecosystem with Pillars + Timeline
        final_html = final_html[:ecosystem_pos] + pillars_section + "\n" + timeline_section + "\n" + final_html[next_section_pos:]

# C. Insert Comparison Table before FAQ
faq_marker = "<!-- ========== FAQ SECTION"
faq_pos = final_html.find(faq_marker)
if faq_pos != -1:
    final_html = final_html[:faq_pos] + comparison_section + "\n" + final_html[faq_pos:]

# D. Insert Mascot into the first card
if "MASCOT_BASE64_PLACEHOLDER" in final_html:
    final_html = final_html.replace("MASCOT_BASE64_PLACEHOLDER", mascot_b64)
elif "tc-mascote" in final_html:
    # If the mascot div exists but is empty or has a placeholder, replace it
    final_html = re.sub(r'<img src="[^"]*" alt="Mascote">', f'<img src="data:image/png;base64,{mascot_b64}" alt="Mascote">', final_html)

# E. Global Branding Fix
final_html = final_html.replace("The Elite Lake", "The Elite Agency")
final_html = final_html.replace("Elite Lake", "Elite Agency")
final_html = final_html.replace("Olá%20Elite%20Lake", "Olá%20Elite%20Agency")

# F. Write Output
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("ULTIMATE MERGE COMPLETE! Mascot integrated, branding fixed, and all sections consolidated.")
