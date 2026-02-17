import re

# Read the file
with open('module1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove platform logos from headers (Android, iOS, Flutter, React Native, KMP)
content = re.sub(
    r'          <img src="https://upload\.wikimedia\.org/wikipedia/commons/d/d7/Android_robot\.svg"[^>]+>\r?\n',
    '',
    content
)
content = re.sub(
    r'          <img src="https://upload\.wikimedia\.org/wikipedia/commons/f/fa/Apple_logo_black\.svg"[^>]+>\r?\n',
    '',
    content
)
content = re.sub(
    r'          <img src="https://storage\.googleapis\.com/cms-storage-bucket/0dbfcc7a59cd1cf16282\.png"[^>]+>\r?\n',
    '',
    content
)
content = re.sub(
    r'          <img src="https://upload\.wikimedia\.org/wikipedia/commons/a/a7/React-icon\.svg"[^>]+>\r?\n',
    '',
    content
)
content = re.sub(
    r'          <img src="https://upload\.wikimedia\.org/wikipedia/commons/7/74/Kotlin_Icon\.png"[^>]+>\r?\n',
    '',
    content
)

# 2. Remove fire emoji demand ratings
content = re.sub(r'            <div class="demand-rating">.*?</div>\r?\n', '', content, flags=re.DOTALL)

# 3. Remove wrapper divs that are now empty in header
content = re.sub(
    r'          <div>\r?\n            <h2>([^<]+)</h2>\r?\n          </div>',
    r'          <h2>\1</h2>',
    content
)

# 4. Remove emoji icons from section titles
content = content.replace('🏢 ', '')
content = content.replace('💰 ', '')

# 5. Remove ALL company logo img tags (this is the critical part)
# Remove img tags within company-item-compact divs
content = re.sub(r'<img[^>]*class="company-logo-tiny[^"]*"[^>]*>\s*', '', content)

# 6. Remove emoji prefixes from company items
content = content.replace('💳 ', '')
content = content.replace('💰 ', '')
content = content.replace('🏦 ', '')
content = content.replace('🌍 ', '')
content = content.replace('🚀 ', '')
content = content.replace('🏢 ', '')

# Write back
with open('module1.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("✓ All icons and logos removed successfully!")
