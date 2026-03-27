import re
import os

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Read the CSS parts
styles = []
for i in range(1, 5):
    with open(f"new_style_{i}.css", "r", encoding="utf-8") as f:
        styles.append(f.read())

new_css = "\n".join(styles)

# Read the new top HTML
with open("new_html_top.html", "r", encoding="utf-8") as f:
    new_html_top = f.read()

# Replace the style block
# We find <style> and </style>
style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
text = style_pattern.sub(f'<style>\n{new_css}\n    </style>', text, count=1)

# Now, replace the body content from <!-- ========== STICKY CTA to <div class="testimonials-horizontal">
body_pattern = re.compile(r'<!-- ========== STICKY CTA.*?<div class="testimonials-horizontal">', re.DOTALL)

# Since the prompt truncated at the first tc-card, let's inject our custom tc-cards
cards_html = """
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

# The chunk to replace is up to the testimonials-horizontal start.
# So we need to insert new_html_top + cards_html + end of testimonials-horizontal div.
end_cards_pattern = re.compile(r'<!-- ========== STICKY CTA.*?<div class="testimonials-horizontal">.*?</section>', re.DOTALL)

replacement = new_html_top + cards_html + """
        </div>
    </div>
</section>
"""

text = end_cards_pattern.sub(replacement.replace('\\', '\\\\'), text, count=1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updates applied to index.html successfully.")
