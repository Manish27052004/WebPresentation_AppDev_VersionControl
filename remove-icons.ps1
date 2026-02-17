# PowerShell script to remove icons from career slides
$file = "module1.html"
$content = Get-Content $file -Raw -Encoding UTF8

# Remove career logos (Android, iOS, Flutter, React Native, KMP logos)
$content = $content -replace '          <img src="https://upload\.wikimedia\.org/wikipedia/commons/d/d7/Android_robot\.svg"[^>]+>\r?\n', ''
$content = $content -replace '          <img src="https://upload\.wikimedia\.org/wikipedia/commons/f/fa/Apple_logo_black\.svg"[^>]+>\r?\n', ''
$content = $content -replace '          <img src="https://storage\.googleapis\.com/cms-storage-bucket/0dbfcc7a59cd1cf16282\.png"[^>]+>\r?\n', ''
$content = $content -replace '          <img src="https://upload\.wikimedia\.org/wikipedia/commons/a/a7/React-icon\.svg"[^>]+>\r?\n', ''  
$content = $content -replace '          <img src="https://upload\.wikimedia\.org/wikipedia/commons/7/74/Kotlin_Icon\.png"[^>]+>\r?\n', ''

# Remove fire emoji demand ratings
$content = $content -replace '            <div class="demand-rating">.*?</div>\r?\n', ''

# Remove emoji icons from section titles  
$content = $content -replace ' ', ''
$content = $content -replace ' ', ''

# Remove company logos - remove entire img tags within company items
$content = $content -replace '<img[^>]*class="company-logo-tiny"[^>]*>\s*', ''

# Remove standalone emoji company items (, , , , , )
$content = $content -replace '<div class="company-item-compact"> ', '<div class="company-item-compact">'
$content = $content -replace '<div class="company-item-compact"> ', '<div class="company-item-compact">'  
$content = $content -replace '<div class="company-item-compact"> ', '<div class="company-item-compact">'
$content = $content -replace '<div class="company-item-compact"> ', '<div class="company-item-compact">'
$content = $content -replace '<div class="company-item-compact"> ', '<div class="company-item-compact">'
$content = $content -replace '<div class="company-item-compact"> ', '<div class="company-item-compact">'

$content | Out-File $file -Encoding UTF8 -NoNewline
Write-Host "Successfully removed all icons and emojis from career slides"
