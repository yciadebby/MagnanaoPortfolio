# Figma-inspired Streamlit Autobiography & Portfolio

A single-page, scrollable **CSIT 349 · Applied AI** portfolio recreated from the six screenshots provided in the conversation. It uses **real Streamlit components** rather than a static mockup.

## Run locally

Open this folder in VS Code and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Folder contents

```
Streamlit_Figma_Portfolio/
├── app.py                    # All sections + interactive components
├── styles.css                # Figma-inspired styling and responsive layout
├── assets/
│   └── profile.jpg           # Cropped from the screenshot you supplied
├── .streamlit/
│   └── config.toml           # Streamlit theme
├── requirements.txt
└── README.md
```

## How the design corresponds to your screenshots

- **Dark fixed-looking left navigation**: native Streamlit sidebar with vertical HOME / STORY / SKILLS / WORK / CONTACT links.
- **Cream home / hero**: large serif headline, muted green italic text, split portrait, overlap BSCS badge, and bottom info strip.
- **Dark story section**: underlined native Streamlit tabs for background, education, and interests, plus a 4-part milestone timeline.
- **Cream skills section**: four olive progress bars, category dropdown, toolbox, native checkbox.
- **Warm-gray work section**: three tall, differently colored project cards, category dropdown, role and outcome details, and an expandable detailed list.
- **Off-white contact section**: elegant inputs, project-topic selector, message text area, and a functioning Streamlit form that confirms submission locally.
- **Dark footer** and responsive layout for narrower screens.

## Complete the assignment before submitting

1. Change `SECTION = "[YOUR SECTION]"` to your actual section; verify program and name.
2. Verify that all **milestones, achievements, skills, percentages, project descriptions and awards** reflect *your real experiences*. Some content is based on the screenshot, which is a design reference.
3. Add the **actual tools used** to each project under `PROJECTS` (they are deliberately left as placeholders where screenshots did not specify them).
4. Replace placeholder educational and hobbies paragraphs with **your own autobiography**, as required by your teacher.
5. Replace `EMAIL` only if you are comfortable publishing a contact address. The public website should not display your home address or personal phone number.
6. Replace `assets/profile.jpg` with a high-resolution photo you have permission to share; its existing crop was extracted from your screenshot.
7. Revisit the extra widgets under **Explore my skills**. The chart, table, slider, multiselect, radio, metric, button, session state, tabs, download button, columns, sidebar, checkbox, and form meet the component variety in the PDF.

## Form note

This is a **demo contact form**, not an email service. When submitted, it validates its inputs, displays a success message, and lets the visitor download their own message. It does not deliver messages to your inbox. Do not add a plain API key to the repository.

## Streamlit Community Cloud (+10 bonus)

Push these files to a public GitHub repo, visit [share.streamlit.io](https://share.streamlit.io), choose that repository and `app.py`, then deploy. Ensure the app displays correctly from an incognito window and put the public `.streamlit.app` URL in your submission. Do not upload `.venv`, secrets, or `.env`.

## Notes on design fidelity

Streamlit's DOM and native components are not identical to Figma Make/React. The page recreates the main typography, color scheme, vertical navigation, section flow, spacing, and layouts with CSS. Widget appearance can vary slightly across Streamlit releases. The portrait is a cropped preview, not the source-quality photograph.
