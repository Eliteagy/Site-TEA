
import os

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# 1. Load CSS
css_parts = [
    read_file('new_style_1.css'),
    read_file('new_style_2.css'),
    read_file('new_style_3.css'),
    read_file('new_style_4.css')
]
all_css = "\n".join(css_parts)

# 2. Load Top HTML
top_html = read_file('new_html_top.html')

# 3. Define Testimonial Cards (tc-card)
tc_cards_html = """
            <div class="tc-card">
                <div class="tc-top">
                    <div class="tc-logo">
                        <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1766771945/Reliefly_Lab_Logo_White_sam8fz.png" alt="RelieflyLab Logo">
                    </div>
                    <div class="tc-id">
                        <span class="tc-name">RelieflyLab</span>
                        <span class="tc-niche">E-commerce Wellness</span>
                        <span class="tc-badge gold">Projeto: €25k</span>
                    </div>
                </div>
                <div class="tc-divider"></div>
                <p class="tc-text">Investimento total <strong>€18.000</strong> ao longo de 12 meses. Infraestrutura completa de e-commerce que hoje gera <strong>vendas diárias consistentes</strong>.</p>
                <div class="tc-footer">
                    <div class="tc-stat">
                        <span class="tc-stat-val">12x</span>
                        <span class="tc-stat-label">ROI</span>
                    </div>
                </div>
            </div>

            <div class="tc-card">
                <div class="tc-top">
                    <div class="tc-logo">
                        <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1766771926/logo_no_backgr_rlzocd.png" alt="ORGHEAL Logo">
                    </div>
                    <div class="tc-id">
                        <span class="tc-name">ORGHEAL</span>
                        <span class="tc-niche">Produtos Naturais</span>
                        <span class="tc-badge gold">Projeto: €12.5k</span>
                    </div>
                </div>
                <div class="tc-divider"></div>
                <p class="tc-text">Investimento <strong>€12.500</strong> em website, funis e campanhas. Sistema que converte <strong>7% dos visitantes em clientes</strong> pagantes.</p>
                <div class="tc-footer">
                    <div class="tc-stat">
                        <span class="tc-stat-val">7%</span>
                        <span class="tc-stat-label">Conversão</span>
                    </div>
                </div>
            </div>

            <div class="tc-card">
                <div class="tc-top">
                    <div class="tc-logo">
                        <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1768919919/ChatGPT_Image_12_01_2026_18_22_58_gplexk.png" alt="Mestre Capinhas Logo">
                    </div>
                    <div class="tc-id">
                        <span class="tc-name">Mestre Capinhas</span>
                        <span class="tc-niche">Loja Local Porto</span>
                        <span class="tc-badge gold">Mensal: €1.25k</span>
                    </div>
                </div>
                <div class="tc-divider"></div>
                <p class="tc-text">Investimento <strong>€1.250/mês</strong>. De invisível na cidade a <strong>30+ clientes novos no 1º mês</strong>. Agenda com 3 semanas de antecedência.</p>
                <div class="tc-footer">
                    <div class="tc-stat">
                        <span class="tc-stat-val">6x</span>
                        <span class="tc-stat-label">ROI Mensal</span>
                    </div>
                </div>
            </div>

            <div class="tc-card">
                <div class="tc-top">
                    <div class="tc-logo">
                        <img src="https://res.cloudinary.com/dooigd0d3/image/upload/v1768920238/image-removebg-preview_2_bh9rny.png" alt="EXSAD Logo">
                    </div>
                    <div class="tc-id">
                        <span class="tc-name">EXSAD</span>
                        <span class="tc-niche">Serviços B2B</span>
                        <span class="tc-badge green">TRIAL GRATUITO</span>
                    </div>
                </div>
                <div class="tc-divider"></div>
                <p class="tc-text">Começaram <strong>gratuitamente</strong> para testar a nossa metodologia. Resultado: <strong>+1M pessoas alcançadas</strong> organicamente e leads qualificados diários sem investimento.</p>
                <div class="tc-footer">
                    <div class="tc-stat">
                        <span class="tc-stat-val">100%</span>
                        <span class="tc-stat-label">Prova</span>
                    </div>
                </div>
            </div>
"""

social_proof_end = """
        </div>
    </div>
</section>
"""

# 4. Extract bottom from current index.html
full_html = read_file('index.html')
# We want to find the LAST occurrence of "PROBLEMA SECTION" to avoid any duplicates I might have created
# Actually, the original one was around line 1860.
marker = "<!-- ========== PROBLEMA SECTION ========== -->"
pos = full_html.find(marker)
if pos == -1:
    # Fallback to a different marker if needed
    marker = "<!-- ========== PROBLEMA ========== -->"
    pos = full_html.find(marker)

if pos != -1:
    bottom_content = full_html[pos:]
else:
    print("Error: Could not find Problema marker")
    bottom_content = ""

# 5. Build Head
head_start = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>The Elite Agency — Parceiro Exclusivo dos Melhores Negócios Locais</title>
    <link rel="icon" type="image/png" href="https://res.cloudinary.com/dooigd0d3/image/upload/v1766771870/GENERATION-removebg-preview_yfwn01.png">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
"""

head_end = """
    </style>
</head>
<body>
"""

# 6. Assemble Final
final_content = head_start + all_css + head_end + top_html + tc_cards_html + social_proof_end + bottom_content

# 7. Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("index.html reconstructed successfully!")
