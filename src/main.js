import 'reveal.js/dist/reveal.css'
import 'reveal.js/dist/theme/black.css' // Base theme
import './style.css' // Our overrides

import Reveal from 'reveal.js'
import RevealNotes from 'reveal.js/plugin/notes/notes'
import RevealMarkdown from 'reveal.js/plugin/markdown/markdown'
import RevealHighlight from 'reveal.js/plugin/highlight/highlight'

// Initialize Reveal.js
const deck = new Reveal({
  hash: true,
  slideNumber: true,
  transition: 'slide', // none/fade/slide/convex/concave/zoom
  backgroundTransition: 'fade',
  plugins: [RevealMarkdown, RevealHighlight, RevealNotes],
  controls: true,
  progress: true,
  center: true,
  width: 1280,
  height: 720,
  margin: 0.1,
});

deck.initialize();

// Custom Interaction Scripts
window.highlightDecision = function (element) {
  // Remove active class from all
  document.querySelectorAll('.decision-card').forEach(card => {
    card.style.background = 'var(--card-bg)';
    card.style.transform = 'scale(1)';
  });

  // Add active state to clicked
  element.style.background = 'rgba(61, 220, 132, 0.2)';
  element.style.transform = 'scale(1.1)';
}
