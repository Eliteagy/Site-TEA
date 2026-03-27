
import os

def update_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    old_block = """            <div class="eco-sys-wrap">
                <div class="eco-sys-label">PANTHEON GROWTH ECOSYSTEM</div>
                <div class="eco-sys-top">
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">WEB DESIGN</div>
                        <div class="eco-sys-desc">Landing Pages de Alta Conversão</div>
                        <div class="eco-sys-sub">UX/UI focada em Autoridade</div>
                    </div>
                    <div class="eco-sys-arrow">→</div>
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">FUNNELS</div>
                        <div class="eco-sys-desc">Sistemas de Vendas Automáticos</div>
                        <div class="eco-sys-sub">Arquitetura Estratégica</div>
                    </div>
                    <div class="eco-sys-arrow">→</div>
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">PAID ADS</div>
                        <div class="eco-sys-desc">Aceleração de Tráfego</div>
                        <div class="eco-sys-sub">Meta, Google & LinkedIn</div>
                    </div>
                    <div class="eco-sys-arrow">→</div>
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">AUTOMATION</div>
                        <div class="eco-sys-desc">Operação Scalable</div>
                        <div class="eco-sys-sub">CRM & Workflow Optimization</div>
                    </div>
                    <div class="eco-sys-arrow">→</div>
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">AI AGENTS</div>
                        <div class="eco-sys-desc">Inteligência Operacional</div>
                        <div class="eco-sys-sub">Chatbots & Process Mapping</div>
                    </div>
                </div>
                <div class="eco-sys-bottom">
                    <div class="eco-sys-bottom-label">DATA & ANALYTICS LAYER</div>
                    <div class="eco-sys-bottom-text">One system where everything amplifies everything.</div>
                </div>
            </div>"""

    new_block = """            <div class="eco-sys-wrap">
                <div class="eco-sys-label">ELITE GROWTH ECOSYSTEM</div>
                <div class="eco-sys-top">
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">DIGITAL PRESENCE</div>
                        <div class="eco-sys-desc">High-End Brand Interfaces</div>
                        <div class="eco-sys-sub">UX/UI focused on Authority</div>
                    </div>
                    <div class="eco-sys-arrow">→</div>
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">CONVERSION SYSTEMS</div>
                        <div class="eco-sys-desc">Automated Sales Funnels</div>
                        <div class="eco-sys-sub">Strategic Conversion Architecture</div>
                    </div>
                    <div class="eco-sys-arrow">→</div>
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">SCALE INFRASTRUCTURE</div>
                        <div class="eco-sys-desc">Precision Paid Advertising</div>
                        <div class="eco-sys-sub">Meta, Google & LinkedIn Scaling</div>
                    </div>
                    <div class="eco-sys-arrow">→</div>
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">OPERATIONAL LEVERAGE</div>
                        <div class="eco-sys-desc">Scalable Workflows</div>
                        <div class="eco-sys-sub">CRM & Process Optimization</div>
                    </div>
                    <div class="eco-sys-arrow">→</div>
                    <div class="eco-sys-card">
                        <div class="eco-sys-title">AI-DRIVEN GROWTH</div>
                        <div class="eco-sys-desc">Operational Intelligence</div>
                        <div class="eco-sys-sub">Advanced AI Agents & Automation</div>
                    </div>
                </div>
                <div class="eco-sys-bottom">
                    <div class="eco-sys-bottom-label">INTELLIGENCE & ANALYTICS LAYER</div>
                    <div class="eco-sys-bottom-text">One unified system where every component amplifies the next.</div>
                </div>
            </div>"""

    # Try replacement with stripping whitespace to be safe
    # We'll use a more robust way to find the block
    if old_block in content:
        new_content = content.replace(old_block, new_block)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {filename}")
    else:
        # Fallback: find by label
        print(f"Exact block match failed for {filename}. Searching by markers...")
        start_marker = '<div class="eco-sys-wrap">'
        end_marker = 'One system where everything amplifies everything.'
        
        start_pos = content.find(start_marker)
        if start_pos != -1:
            end_pos = content.find(end_marker, start_pos) + len(end_marker)
            # Find the next 2 closing divs after end_marker
            end_pos = content.find('</div>', end_pos) + 6
            end_pos = content.find('</div>', end_pos) + 6
            
            new_content = content[:start_pos] + new_block + content[end_pos:]
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated {filename} via marker search.")
        else:
            print(f"Start marker NOT found in {filename}")

update_file('index_test.html')
update_file('index.html')
