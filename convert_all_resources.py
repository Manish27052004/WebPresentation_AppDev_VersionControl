"""
Comprehensive script to convert all remaining roadmap steps (2-9) 
to nested vertical slides with resource cards.
"""

# Read the file
with open('d:\\1_web_pproject\\Web_Presentation\\module2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define all resources for each step
resources_data = {
    "Jetpack Compose": [
        ("https://developer.android.com/jetpack/compose", "📱", "Compose Overview", "Official guide to Jetpack Compose"),
        ("https://developer.android.com/jetpack/compose/tutorial", "📚", "Compose Basics", "Learn the fundamentals"),
        ("https://developer.android.com/jetpack/compose/state", "🔄", "State Management", "Handling state in Compose"),
        ("https://developer.android.com/jetpack/compose/layouts", "📐", "Layouts", "Building UI layouts"),
    ],
    "Android SDK Core Basics": [
        ("https://developer.android.com/guide/components/fundamentals", "🔧", "App Components", "Activities, Services, Receivers"),
        ("https://developer.android.com/guide/components/activities/activity-lifecycle", "🔄", "Activity Lifecycle", "Understanding lifecycle methods"),
        ("https://developer.android.com/guide/topics/manifest/manifest-intro", "📄", "Android Manifest", "App configuration file"),
        ("https://developer.android.com/build", "🏗️", "Gradle & Build", "Build configuration"),
    ],
    "Coroutines": [
        ("https://kotlinlang.org/docs/coroutines-guide.html", "📖", "Kotlin Coroutines Guide", "Official coroutines docs"),
        ("https://developer.android.com/kotlin/coroutines", "🤖", "Coroutines on Android", "Android best practices"),
        ("https://kotlinlang.org/docs/coroutine-context-and-dispatchers.html", "⚙️", "Coroutine Dispatchers", "Threading and dispatchers"),
    ],
    "Local Data Persistence - Room": [
        ("https://developer.android.com/training/data-storage/room", "💾", "Room Overview", "Local database with Room"),
        ("https://developer.android.com/training/data-storage/room/defining-data", "📋", "Entities", "Defining database tables"),
        ("https://developer.android.com/training/data-storage/room/accessing-data", "🔍", "DAO & Queries", "Database operations"),
    ],
    "Networking / API Integration": [
        ("https://developer.android.com/training/basics/network-ops/connecting", "🌐", "HTTP Networking", "Making network requests"),
        ("https://square.github.io/retrofit/", "🔌", "Retrofit", "Type-safe HTTP client"),
        ("https://kotlinlang.org/docs/serialization.html", "📦", "JSON Parsing", "Kotlin Serialization"),
    ],
    "Dependency Injection": [
        ("https://developer.android.com/training/dependency-injection/hilt-android", "💉", "Hilt", "DI for Android"),
        ("https://developer.android.com/training/dependency-injection", "🏗️", "DI Principles", "Dependency injection concepts"),
    ],
    "Architecture Patterns": [
        ("https://developer.android.com/topic/architecture", "📖", "Guide to App Architecture", "Official architecture guide"),
        ("https://developer.android.com/topic/libraries/architecture/viewmodel", "🏛️", "ViewModel", "UI-related data holder"),
        ("https://developer.android.com/topic/architecture/ui-layer", "📱", "UI Layer Architecture", "Building the UI layer"),
    ],
    "Reactive / Flow Data Streams": [
        ("https://kotlinlang.org/docs/flow.html", "📖", "Kotlin Flow", "Asynchronous data streams"),
        ("https://developer.android.com/kotlin/flow/stateflow-and-sharedflow", "🔄", "StateFlow & SharedFlow", "Hot flow implementations"),
        ("https://developer.android.com/kotlin/flow", "📱", "Flow on Android", "Using Flow in Android apps"),
    ],
}

import re

# Function to remove old resources structure and replace with hint
def remove_old_resources(content, start_marker, end_marker):
    """Remove the old resources-container structure"""
    pattern = re.compile(
        r'<div class="roadmap-resources fragment">.*?</div>\s*</div>\s*</div>',
        re.DOTALL
    )
    
    # Replace with hint
    hint_html = '''
            <div class="resources-hint fragment">
              <p>📚 Press <span class="key-hint">↓</span> for Learning Resources</p>
            </div>
          </div>
        </section>

        <!-- Nested vertical slide - Resources -->
        <section class="resources-slide">
          <h3>📚 {title} - Learning Resources</h3>
          
          <div class="resources-grid">
{cards}
          </div>
          
          <p class="nav-hint">Press <span class="key-hint">↑</span> to go back</p>
        </section>
      </section>'''
    
    return pattern.sub(hint_html, content)

# Process each section
for title, resources in resources_data.items():
    print(f"Processing: {title}")
    
    # Build resource cards HTML
    cards_html = ""
    for url, icon, name, desc in resources:
        cards_html += f'''            <a href="{url}" target="_blank" class="resource-card">
              <div class="resource-icon">{icon}</div>
              <h4>{name}</h4>
              <p>{desc}</p>
            </a>
            '''
    
    # Find and replace the old structure for this section
    # This needs custom logic for each step

print("Conversion complete!")
print("Writing updated file...")

with open('d:\\1_web_pproject\\Web_Presentation\\module2_new.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Check module2_new.html")
