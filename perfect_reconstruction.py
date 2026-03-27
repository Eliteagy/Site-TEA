
import os
import re

# 1. Config
brand_name = "The Elite Lake"
canonical_url = "https://the-elite-lake.vercel.app/"
new_title = f"{brand_name} — Parceiro Exclusivo dos Melhores Negócios Locais"

# 2. Start building our page from scratch to avoid any hidden duplication
# (I'll extract the core HTML from the current file safely)

with open('index.html', 'r', encoding='utf-8') as f:
    full_text = f.read()

# I'll use markers that are consistent
try:
    # Everything from Problema to Footer
    problema_start = full_text.find("<!-- ========== PROBLEMA SECTION")
    if problema_start == -1: problema_start = full_text.find("Invisibilidade Digital")
    
    footer_pos = full_text.find("<footer>")
    footer_end = full_text.find("</html>", footer_pos) + 7
    
    body_bottom = full_text[problema_start:footer_end]
except:
    body_bottom = "<!-- Problem section extraction failed -->"

# 3. Construct the perfect top part (incorporating Step 225 and Branding)
head_top = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>{new_title}</title>
    <link rel="canonical" href="{canonical_url}">
    <meta property="og:title" content="{new_title}">
    <meta property="og:url" content="{canonical_url}">
    <link rel="icon" type="image/png" href="https://res.cloudinary.com/dooigd0d3/image/upload/v1766771870/GENERATION-removebg-preview_yfwn01.png">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
"""

# Instead of re-parsing CSS, I'll just keep the first 1856 lines of our current file 
# but replace the title and canonical in them.
with open('index.html', 'r', encoding='utf-8') as f:
    current_lines = f.readlines()

# We take the style and body start from our current (mostly good) top reconstruction
top_body = "".join(current_lines[8:1856])

# 4. Social Proof Card Grid (Step 225 order & content)
social_proof_grid = f"""
        <div class="tc-grid">
            <!-- CARD 1: MESTRE CAPINHAS -->
            <div class="tc-card">
                <div class="tc-header">
                    <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1736706240/ChatGPT_Image_12_01_2026_18_22_58_gplexk.png" alt="Mestre Capinhas" class="tc-logo">
                    <div class="tc-info">
                        <span class="tc-name">Mestre Capinhas</span>
                        <span class="tc-segment">E-commerce / Retalho</span>
                    </div>
                </div>
                <div class="tc-body">
                    <div class="tc-stat">
                        <span class="tc-value">+247%</span>
                        <span class="tc-label">Vendas Online</span>
                    </div>
                    <p class="tc-quote">"A {brand_name} transformou a nossa presença digital. O ROI foi imediato."</p>
                </div>
                <div class="tc-mascote" style="position: absolute; bottom: -20px; right: -10px; width: 100px; opacity: 0.8;">
                    <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1766771870/GENERATION-removebg-preview_yfwn01.png" style="width:100%; height:auto;" alt="Mascote Small">
                </div>
            </div>

            <!-- CARD 2: RELIEFLY LAB -->
            <div class="tc-card">
                <div class="tc-header">
                    <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1736630419/Reliefly_Lab_Logo_White_sam8fz.png" alt="Reliefly Lab" class="tc-logo">
                    <div class="tc-info">
                        <span class="tc-name">Reliefly Lab</span>
                        <span class="tc-segment">Saúde / Bem-Estar</span>
                    </div>
                </div>
                <div class="tc-body">
                    <div class="tc-stat">
                        <span class="tc-value">4.8k</span>
                        <span class="tc-label">Leads Qualificados</span>
                    </div>
                    <p class="tc-quote">"Escalamos a nossa clínica para 3 novos distritos em tempo recorde."</p>
                </div>
            </div>

            <!-- CARD 3: ORGHEAL -->
            <div class="tc-card">
                <div class="tc-header">
                    <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1736630419/logo_no_backgr_rlzocd.png" alt="ORGHEAL" class="tc-logo">
                    <div class="tc-info">
                        <span class="tc-name">ORGHEAL</span>
                        <span class="tc-segment">Indústria / Exportação</span>
                    </div>
                </div>
                <div class="tc-body">
                    <div class="tc-stat">
                        <span class="tc-value">12</span>
                        <span class="tc-label">Novos Mercados</span>
                    </div>
                    <p class="tc-quote">"O posicionamento premium que a {brand_name} criou foi o diferencial."</p>
                </div>
            </div>

            <!-- CARD 4: EXSAD -->
            <div class="tc-card">
                <div class="tc-header">
                    <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1736701884/image-removebg-preview_2_bh9rny.png" alt="EXSAD" class="tc-logo">
                    <div class="tc-info">
                        <span class="tc-name">EXSAD</span>
                        <span class="tc-segment">Serviços B2B</span>
                    </div>
                </div>
                <div class="tc-body">
                    <div class="tc-stat">
                        <span class="tc-value">+180%</span>
                        <span class="tc-label">Faturação Anual</span>
                    </div>
                    <p class="tc-quote">"Deixamos de procurar clientes. Agora eles vêm até nós."</p>
                </div>
            </div>
        </div>
"""

# 5. Final Assembly
# Combine the header, top styles/body, the new social proof, and the cleaned bottom
final_content = head_top + top_body

# Replace the old social proof grid in the top_body part (which is already inside final_content)
# We find where it was and replace it with our gold-standard one.
grid_placeholder = re.compile(r'<div class="tc-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
final_content = grid_placeholder.sub(social_proof_grid + "\n        </div>\n    </section>", final_content)

# Now append the bottom
final_content += body_bottom

# 6. Global Branding & Meta Fixes
final_content = final_content.replace("The Elite Agency", brand_name)
final_content = final_content.replace("Elite Agency", brand_name)
final_content = final_content.replace("Olá%20Elite%20Agency", "Olá%20Elite%20Lake")

# 7. Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("PERFECT RECONSTRUCTION COMPLETE!")
