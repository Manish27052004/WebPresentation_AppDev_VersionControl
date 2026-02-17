import re

# Read the file
with open('module1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove ONLY company logo img tags (the small logos before company names)
# This targets img tags with class="company-logo-tiny"
content = re.sub(r'<img[^>]*class="company-logo-tiny[^"]*"[^>]*>\s*', '', content)

# Write back
with open('module1.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("✓ Company logos removed from Top Companies sections!")
print("  Platform logos, fire emojis, and section icons kept intact.")
