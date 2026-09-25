"""Styling constants for the digital twin Gradio app.

Soft & rounded theme, tested against Gradio 4.44 and Gradio 5.x.

Key layout rules (why the previous version scaled badly):
- Gradio puts the class `chatbot` on the *markdown text inside every message*,
  not on the chat panel. Styling `.chatbot` therefore resized every message.
  The chat panel is now targeted with `.block:has(.bubble-wrap)` instead.
- Bubbles are styled on exactly one element (`.flex-wrap > .message`) and sized
  against a full-width row, so short messages like "Hi" no longer collapse.
- No global `min-width: 0` — it let flex items shrink to a few pixels wide.
"""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
/* =====================================================================
   1. Design tokens
   ===================================================================== */
:root {
  --twin-gold: #ecad0a;
  --twin-gold-hover: #ffc320;
  --twin-blue: #209dd7;
  --twin-purple: #753991;

  /* Neutrals — dark (default) */
  --twin-bg: #0d0d10;
  --twin-surface: #16161b;
  --twin-surface-2: #1e1e25;
  --twin-border: #2a2a32;
  --twin-border-strong: #3a3a44;
  --twin-text: #ececef;
  --twin-muted: #8c8c95;
  --twin-user-bg: rgba(32, 157, 215, 0.20);
  --twin-user-text: #e3f3fb;

  /* Chat panel height — change this one value to resize the conversation area */
  --twin-chat-height: 800px;

  --twin-radius-xl: 20px;
  --twin-radius-lg: 18px;
  --twin-radius-md: 12px;
  --twin-radius-sm: 8px;
  --twin-radius-tail: 6px;

  --twin-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.35);
  --twin-shadow-md: 0 8px 24px rgba(0, 0, 0, 0.35);
  --twin-ring: 0 0 0 3px rgba(236, 173, 10, 0.25);

  --twin-font: 'Inter', ui-sans-serif, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --twin-mono: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
}

/* Light mode: Gradio adds `.dark` to <body> when dark; absence = light. */
body:not(.dark) {
  --twin-bg: #f6f6f8;
  --twin-surface: #ffffff;
  --twin-surface-2: #f3f3f6;
  --twin-border: #e4e4ea;
  --twin-border-strong: #c4c4cc;
  --twin-text: #1a1a20;
  --twin-muted: #6a6a72;
  --twin-user-bg: #e3f2fb;
  --twin-user-text: #0d3a52;
  --twin-shadow-sm: 0 1px 2px rgba(16, 16, 24, 0.06);
  --twin-shadow-md: 0 1px 2px rgba(16, 16, 24, 0.04), 0 8px 24px rgba(16, 16, 24, 0.06);
}

/* Neutralise Gradio theme fills so no grey bands appear around blocks */
.gradio-container {
  --block-background-fill: transparent;
  --block-border-width: 0px;
  --block-shadow: none;
  --block-padding: 0px;
  --panel-background-fill: transparent;
  --background-fill-secondary: transparent;
  --border-color-primary: var(--twin-border);
  --body-text-color: var(--twin-text);
}

footer, .built-with, .show-api, .api-docs { display: none !important; }
html, body, gradio-app { background: var(--twin-bg) !important; }

/* =====================================================================
   2. Page layout
   ===================================================================== */
.gradio-container {
  background: var(--twin-bg) !important;
  color: var(--twin-text) !important;
  font-family: var(--twin-font) !important;
  width: 100% !important;
  max-width: 820px !important;
  margin: 0 auto !important;
  padding: 36px 24px 40px !important;
}
.gradio-container .main,
.gradio-container main,
.gradio-container .contain,
.gradio-container > .main > .wrap {
  width: 100% !important;
  max-width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}

.gradio-container .block,
.gradio-container .form,
.gradio-container .gr-group,
.gradio-container .gr-group .styler {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}
.gradio-container .gr-group,
.gradio-container .gr-group .styler,
.gradio-container .gr-group .block.padded { padding: 0 !important; }

/* Let the composer's focus ring show instead of being clipped at the edges */
.gradio-container .gr-group,
.gradio-container .gr-group .styler,
.gradio-container .gr-group .block,
.gradio-container .gr-group .form { overflow: visible !important; }

/* Components Gradio has hidden must not leave empty bordered strips */
.gradio-container .hidden { display: none !important; }

/* =====================================================================
   3. Header
   ===================================================================== */
.gradio-container h1 {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  color: var(--twin-text) !important;
  font-size: 28px !important;
  font-weight: 700 !important;
  letter-spacing: -0.025em !important;
  margin: 0 0 4px !important;
  padding: 0 !important;
  border: 0 !important;
}
.gradio-container h1::before {
  content: "";
  flex: none;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--twin-gold), var(--twin-purple));
  box-shadow: 0 0 0 4px rgba(236, 173, 10, 0.15);
}
.gradio-container h1 + p { color: var(--twin-muted) !important; margin: 0 !important; }

/* =====================================================================
   4. Chat panel (the block that contains the conversation)
   ===================================================================== */
.gradio-container .block:has(.bubble-wrap) {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-xl) !important;
  box-shadow: var(--twin-shadow-md) !important;
  overflow: hidden !important;
  padding: 0 !important;
  /* Overrides Gradio's inline height (400px in Gradio 5, 200px in Gradio 4).
     On short screens it shrinks so the message box always stays visible. */
  height: min(var(--twin-chat-height), calc(100vh - 220px)) !important;
  min-height: 360px !important;
}

/* Hide the "Chatbot" label chip */
.gradio-container .block:has(.bubble-wrap) [data-testid="block-label"] { display: none !important; }

/* Scrolling area. Top padding leaves room for the clear (trash) button so it
   never sits on a message. */
.gradio-container .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  padding: 44px 20px 16px !important;
}
.gradio-container .message-wrap {
  display: flex !important;
  flex-direction: column !important;
  gap: 14px !important;
  padding: 0 !important;
  margin: 0 !important;
  background: transparent !important;
}
.gradio-container .bubble-wrap .placeholder,
.gradio-container .bubble-wrap .placeholder * { color: var(--twin-muted) !important; }

/* =====================================================================
   5. Messages
   Structure (both versions): .message-row > .flex-wrap > .message (bubble) > inner
   ===================================================================== */
.gradio-container .message-row {
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  animation: twin-in 0.18s ease-out both;
}
.gradio-container .message-row > .flex-wrap {
  display: flex !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}
.gradio-container .message-row.user-row > .flex-wrap { justify-content: flex-end !important; }
.gradio-container .message-row.bot-row  > .flex-wrap { justify-content: flex-start !important; }

@keyframes twin-in {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: none; }
}

/* --- The bubble: one element only --- */
.gradio-container .message-row > .flex-wrap > .message {
  display: block !important;
  flex: 0 1 auto !important;
  width: auto !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 10px 16px !important;
  border: 0 !important;
  border-radius: var(--twin-radius-lg) !important;
  box-shadow: none !important;
  font-family: var(--twin-font) !important;
  font-size: 15px !important;
  line-height: 1.6 !important;
  text-align: left !important;
  overflow-wrap: anywhere;
}
.gradio-container .message-row.user-row > .flex-wrap > .message {
  max-width: 75% !important;
  background: var(--twin-user-bg) !important;
  color: var(--twin-user-text) !important;
  border-bottom-right-radius: var(--twin-radius-tail) !important;
}
.gradio-container .message-row.bot-row > .flex-wrap > .message {
  max-width: 85% !important;
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-border) !important;
  border-bottom-left-radius: var(--twin-radius-tail) !important;
  box-shadow: inset 3px 0 0 var(--twin-purple) !important;
  padding: 12px 18px 12px 20px !important;
}

/* --- Everything inside the bubble is plain: no extra boxes or padding --- */
.gradio-container .message-row > .flex-wrap > .message * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.gradio-container .message-row > .flex-wrap > .message :is(.message, button, [data-testid], .message-content, .md, .prose) {
  display: block !important;
  width: auto !important;
  max-width: 100% !important;
  min-height: 0 !important;
  height: auto !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  border-radius: 0 !important;
  font: inherit !important;
  letter-spacing: normal !important;
  text-transform: none !important;
  text-align: left !important;
  cursor: text !important;
  user-select: text !important;
}

/* --- Typography --- */
.gradio-container .message-row .message p {
  font-size: 15px !important;
  line-height: 1.6 !important;
  margin: 0 0 10px !important;
}
.gradio-container .message-row .message p:last-child { margin-bottom: 0 !important; }
.gradio-container .message-row .message :is(.md, .prose) > :first-child { margin-top: 0 !important; }
.gradio-container .message-row .message :is(.md, .prose) > :last-child  { margin-bottom: 0 !important; }
.gradio-container .message-row .message :is(ul, ol) {
  margin: 4px 0 10px !important;
  padding-left: 1.3em !important;
}
.gradio-container .message-row .message li {
  margin: 4px 0 !important;
  padding-left: 2px !important;
  font-size: 15px !important;
  line-height: 1.55 !important;
}
.gradio-container .message-row .message li::marker { color: var(--twin-muted); }
.gradio-container .message-row .message strong { font-weight: 600 !important; }
.gradio-container .message-row .message :is(code, pre) {
  font-family: var(--twin-mono) !important;
  font-size: 13px !important;
  background: rgba(127, 127, 127, 0.14) !important;
  border-radius: 6px !important;
}
.gradio-container .message-row .message code { padding: 1px 5px !important; }
.gradio-container .message-row .message pre { padding: 10px 12px !important; overflow-x: auto !important; }
.gradio-container .message-row .message pre code { padding: 0 !important; background: transparent !important; }
.gradio-container .message-row.bot-row .message a {
  color: var(--twin-blue) !important;
  text-decoration: underline;
  text-underline-offset: 2px;
}

/* =====================================================================
   6. Icon buttons: retry / undo / copy under replies, clear at the top
   ===================================================================== */
.gradio-container .message-buttons,
.gradio-container .message-buttons .icon-button-wrapper {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  padding: 0 !important;
  margin: 0 !important;
  gap: 2px !important;
}
.gradio-container .message-buttons { margin-top: -6px !important; }

.gradio-container .icon-button {
  width: 30px !important;
  height: 30px !important;
  min-height: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  border-radius: var(--twin-radius-sm) !important;
  background: transparent !important;
  color: var(--twin-muted) !important;
  box-shadow: none !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: background 0.15s ease, color 0.15s ease;
}
.gradio-container .icon-button:hover {
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
}
.gradio-container .icon-button-wrapper { border: 0 !important; box-shadow: none !important; }
.gradio-container .icon-button-wrapper > * { border: 0 !important; }
.gradio-container .icon-button-wrapper::before,
.gradio-container .icon-button-wrapper > *::before { display: none !important; }  /* dividers */

/* Clear (trash) button — top-right corner, inside the panel's top padding */
.gradio-container .icon-button-wrapper.top-panel {
  top: 8px !important;
  right: 10px !important;
  background: transparent !important;
  padding: 0 !important;
  z-index: 5 !important;
}

/* Scroll-to-latest button — small round chip, bottom-right */
.gradio-container .scroll-down-button-container {
  left: auto !important;
  right: 14px !important;
  bottom: 14px !important;
  transform: none !important;
  z-index: 5 !important;
}
.gradio-container .scroll-down-button-container button {
  width: 34px !important;
  height: 34px !important;
  min-height: 0 !important;
  padding: 0 !important;
  border-radius: 50% !important;
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  box-shadow: var(--twin-shadow-md) !important;
}

/* =====================================================================
   7. Composer — message box + send button in one rounded pill
   ===================================================================== */

/* Gradio 5: textarea and send button share .input-container */
.gradio-container .input-container {
  display: flex !important;
  align-items: flex-end !important;
  gap: 8px !important;
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 26px !important;
  padding: 6px 6px 6px 18px !important;
  box-shadow: var(--twin-shadow-md) !important;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}
.gradio-container .input-container:focus-within {
  border-color: var(--twin-gold) !important;
  box-shadow: var(--twin-ring), var(--twin-shadow-md) !important;
}

/* Gradio 4: textarea block and Submit button are siblings in a row */
.gradio-container .gr-group:has(textarea):not(:has(.input-container)) > .styler > div:not(.hidden):has(> .block textarea) {
  display: flex !important;
  align-items: flex-end !important;
  gap: 8px !important;
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 26px !important;
  padding: 6px 6px 6px 18px !important;
  box-shadow: var(--twin-shadow-md) !important;
}
.gradio-container .gr-group:has(textarea):not(:has(.input-container)) > .styler > div:not(.hidden):has(> .block textarea):focus-within {
  border-color: var(--twin-gold) !important;
  box-shadow: var(--twin-ring), var(--twin-shadow-md) !important;
}

/* Textarea inside either composer: invisible, just text */
.gradio-container :is(.input-container, .gr-group) textarea {
  flex: 1 1 auto !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  outline: none !important;
  padding: 10px 0 !important;
  min-height: 40px !important;
  resize: none !important;
  color: var(--twin-text) !important;
  font-family: var(--twin-font) !important;
  font-size: 15px !important;
  line-height: 1.5 !important;
}
.gradio-container textarea::placeholder { color: var(--twin-muted) !important; }

/* Send button (G5 .submit-button, G4 primary "Submit") — round gold */
.gradio-container .input-container .submit-button,
.gradio-container .gr-group:has(textarea) button.primary {
  flex: none !important;
  width: 40px !important;
  height: 40px !important;
  min-width: 40px !important;
  max-width: 40px !important;
  min-height: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  border-radius: 50% !important;
  background: var(--twin-gold) !important;
  color: #111111 !important;
  box-shadow: none !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 0 !important;                /* hides the word "Submit" in Gradio 4 */
  transition: background 0.15s ease, transform 0.1s ease;
}
.gradio-container .gr-group:has(textarea) button.primary::after {   /* arrow for Gradio 4 */
  content: "\\2191";
  font-size: 18px;
  font-weight: 700;
  line-height: 1;
}
.gradio-container .input-container .submit-button:hover,
.gradio-container .gr-group:has(textarea) button.primary:hover { background: var(--twin-gold-hover) !important; }
.gradio-container .input-container .submit-button:active,
.gradio-container .gr-group:has(textarea) button.primary:active { transform: scale(0.94); }
.gradio-container .input-container .submit-button svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 !important;
  color: #111111 !important;
}
.gradio-container .input-container .stop-button,
.gradio-container .gr-group:has(textarea) button.stop {
  flex: none !important;
  width: 40px !important;
  height: 40px !important;
  min-height: 0 !important;
  padding: 0 !important;
  border-radius: 50% !important;
  background: var(--twin-surface-2) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
}

/* =====================================================================
   8. Other buttons (e.g. "Fake API", Gradio 4 Retry / Undo / Clear)
   ===================================================================== */
.gradio-container button.secondary:not(.icon-button) {
  width: auto !important;
  flex: 0 0 auto !important;
  align-self: center !important;
  margin: 0 auto !important;
  min-height: 34px !important;
  padding: 0 16px !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 999px !important;
  background: var(--twin-surface) !important;
  color: var(--twin-muted) !important;
  box-shadow: var(--twin-shadow-sm) !important;
  font-family: var(--twin-font) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  letter-spacing: normal !important;
  text-transform: none !important;
  transition: border-color 0.15s ease, color 0.15s ease;
}
.gradio-container button.secondary:not(.icon-button):hover {
  border-color: var(--twin-gold) !important;
  color: var(--twin-text) !important;
}

/* =====================================================================
   9. Example prompts
   ===================================================================== */
.gradio-container :is(.gallery-item, .examples button, [data-testid="examples"] button, .example) {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 999px !important;
  color: var(--twin-text) !important;
  box-shadow: var(--twin-shadow-sm) !important;
  font-family: var(--twin-font) !important;
  font-size: 13.5px !important;
  padding: 6px 14px !important;
  transition: border-color 0.15s ease, color 0.15s ease;
}
.gradio-container :is(.gallery-item, .examples button, [data-testid="examples"] button, .example):hover {
  border-color: var(--twin-blue) !important;
  color: var(--twin-blue) !important;
}

/* =====================================================================
   10. Scrollbar, selection, motion
   ===================================================================== */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: var(--twin-border-strong);
  border-radius: 999px;
  border: 2px solid transparent;
  background-clip: padding-box;
}
* { scrollbar-width: thin; scrollbar-color: var(--twin-border-strong) transparent; }
::selection { background: var(--twin-gold); color: #111111; }

@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}

/* =====================================================================
   11. Mobile
   ===================================================================== */
@media (max-width: 640px) {
  .gradio-container { padding: 20px 12px 28px !important; }
  .gradio-container h1 { font-size: 23px !important; }
  .gradio-container .bubble-wrap { padding: 44px 12px 12px !important; }
  .gradio-container .block:has(.bubble-wrap) { height: 70vh !important; }
  .gradio-container .message-row.user-row > .flex-wrap > .message { max-width: 85% !important; }
  .gradio-container .message-row.bot-row  > .flex-wrap > .message { max-width: 100% !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""