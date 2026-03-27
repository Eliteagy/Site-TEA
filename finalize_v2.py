
import os
import re

# 1. Config
brand_name = "The Elite Lake"
canonical_url = "https://the-elite-lake.vercel.app/"

# 2. Read the current file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Fix the Social Proof Card Order
# cards (Mestre Capinhas, RelieflyLab, ORGHEAL, EXSAD)
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
                <!-- MASCOTE AQUI (Placeholder for now) -->
                <div class="tc-mascote">
                    <div style="background: rgba(255,255,255,0.1); width: 100px; height: 100px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 10px; color: white;">Lake Mascot</div>
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

# Replace the grid in the content
grid_regex = re.compile(r'<div class="tc-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
content = grid_regex.sub(social_proof_grid + "\n        </div>\n    </section>", content)

# 4. Global Branding Replacements (Case-insensitive where possible)
content = content.replace("The Elite Agency", brand_name)
content = content.replace("Elite Agency", brand_name) # Catch remaining "Elite Agency" mentions

# 5. Fix Sticky CTA Badge text (if it was "The Elite Agency")
content = content.replace("<span class=\"ea-text\">A <strong>The Elite Lake</strong>", f"<span class=\"ea-text\">A <strong>{brand_name}</strong>")

# 6. Final write
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final cleanup v2 complete!")
