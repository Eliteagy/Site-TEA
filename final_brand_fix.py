
import re

# 1. Config
brand_name = "The Elite Lake"

# 2. Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Global Case-Insensitive Brand Replace
# We target "Elite Agency" but avoid breaking class names if possible
# Actually, the user wants the branding visible to the user to be "The Elite Lake".
content = re.sub(r'(?i)Elite\s+Agency', brand_name, content)
content = content.replace("Olá%20Elite%20Lake", "Olá%20Elite%20Lake") # Just in case

# 4. Canonical URL (Ensure it's correct)
content = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://the-elite-lake.vercel.app/">', content)

# 5. Fix Card Order
# I'll extract each card as a block and then reassemble the tc-grid.

def extract_card(content, name):
    pattern = rf'<div class="tc-card">.*?<span class="tc-name">{name}</span>.*?</div>\s*</div>\s*</div>'
    # Actually, the structure is <div class="tc-card"> ... card content ... </div>
    # But let's look for the start and end of the card block carefully.
    
    # Simple search: find the card that contains the name
    # We find the <div class="tc-card"> that precedes the name.
    match = re.search(rf'(<div class="tc-card">.*?<span class="tc-name">{name}</span>.*?</div>\s*</div>)', content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

card_mestre = extract_card(content, "Mestre Capinhas")
card_reliefly = extract_card(content, "RelieflyLab")
card_orgheal = extract_card(content, "ORGHEAL")
card_exsad = extract_card(content, "EXSAD")

if card_mestre and card_reliefly and card_orgheal and card_exsad:
    new_grid = f"""
        <div class="tc-grid">
            {card_mestre}
            {card_reliefly}
            {card_orgheal}
            {card_exsad}
        </div>
"""
    # Replace the old grid
    grid_regex = re.compile(r'<div class="tc-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
    content = grid_regex.sub(new_grid + "\n        </div>\n    </section>", content)
else:
    print(f"Card extraction failed: M:{bool(card_mestre)} R:{bool(card_reliefly)} O:{bool(card_orgheal)} E:{bool(card_exsad)}")

# 6. Final Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final brand and card fix complete!")
