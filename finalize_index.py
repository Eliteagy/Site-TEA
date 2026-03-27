
import os
import re

# 1. Load the Mascot Base64 (Placeholder for now, but I'll use a shell command to fill it)
# Actually, I'll just write the full HTML for the Social Proof grid here.

brand_name = "The Elite Lake"
canonical_url = "https://the-elite-lake.vercel.app/"

social_proof_grid = f"""
        <div class="tc-grid">
            <!-- CARD 1: MESTRE CAPINHAS (Com Mascote) -->
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
                <!-- MASCOTE AQUI -->
                <div class="tc-mascote">
                    <img src="MASCOT_BASE64_PLACEHOLDER" alt="Mascote">
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
                        <span class="tc-label">Leeds Qualificados</span>
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

# Now assemble index.html
with open('reconstructed_top.html', 'r', encoding='utf-8') as f:
    top = f.read()

# We need the bottom sections from index.html (the clean ones)
with open('index.html', 'r', encoding='utf-8') as f:
    current = f.read()

# The clean reconstruction from before was actually okay except for the duplication at the bottom.
# I'll just take the sections from surgical_reconstruction.py results.

# Combine
final_index = top.replace("<!-- Entire Body Start, Sticky CTA, Hero, Social Proof from Step 225 -->", social_proof_grid)
# (In reality, I need the Hero/Sticky CTA too. I'll just update index.html directly)

# SCRIPT TO UPDATE index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the social proof grid specifically
grid_pattern = re.compile(r'<div class="tc-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
content = grid_pattern.sub(social_proof_grid + "\n        </div>\n    </section>", content)

# Update branding
content = content.replace("The Elite Agency", brand_name)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final assembly complete (mascot placeholder)! Use powershell to swap the base64.")
