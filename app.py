from __future__ import annotations

import base64
import html
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent

NAME = "Ycia Debby Hebraica R. Magnanao"
INITIALS = "YM"
COURSE = "BS Computer Science"
SCHOOL = "CIT-U"
SECTION = "F2" 
EMAIL = "yciadhmagnanao@gmail.com" 
CITY = "Lapu-Lapu City, Cebu" 

HELLO = "A Computer Science student, student leader, and creative problem-solver passionate about software development and community involvement."
STORY = {
    "BACKGROUND": [
        "I am a Computer Science student from Marigondon, Lapu-Lapu City, Cebu. I’m tech-savvy, detail-oriented, and quick to learn new systems.",
        "I enjoy leading academic and creative projects through organized task management, collaboration, and thoughtful problem-solving.",
    ],
    "EDUCATION": [
        "I began studying BS Computer Science at CIT-U in 2024. My studies let me explore technology, programming, and the way digital tools solve practical problems.",
        "Replace this paragraph with more details about your school journey, your favorite subjects, and the lessons you've learned.",
    ],
    "INTERESTS": [
        "I’m interested in combining software, research, design, and leadership to create work that matters.",
        "Replace this paragraph with your own hobbies, creative interests, and experiences outside the classroom.",
    ],
}
MILESTONES = [
    ("2019", "Won in publishing & research"),
    ("2021", "Placed in robotics"),
    ("2024", "Started BS Computer Science"),
    ("Now", "Student leader at CIT-U"),
]
SKILLS = [
    {"skill": "Programming & Web", "rating": 48, "area": "Technical"},
    {"skill": "UI / UX & Graphic Design", "rating": 88, "area": "Creative"},
    {"skill": "Research Writing", "rating": 86, "area": "Academic"},
    {"skill": "Leadership & Communication", "rating": 92, "area": "Leadership"},
]
TOOLBOX = [
    {"tool": "Java · C++ · C", "purpose": "Core programming", "experience": "Beginner"},
    {"tool": "Python · HTML · CSS", "purpose": "Web and programming fundamentals", "experience": "Foundational"},
    {"tool": "Research & documentation", "purpose": "Academic investigations", "experience": "Developing"},
    {"tool": "Design tools (edit to specify)", "purpose": "Graphics and visual communication", "experience": "Developing"},
]
PROJECTS = [
    {
        "id": "tuklas", "number": "01", "category": "Research", "eyebrow": "ROBOTICS RESEARCH",
        "title": "TUKLAS", "description": "A robotics and intelligent machine research project developed for the Regional Science and Technology Fair.",
        "tags": ["Research", "Robotics"], "role": "Co-author", "outcome": "2nd Place · Regional",
        "tools": "[List the actual robotics and research tools used]", "color": "sage",
    },
    {
        "id": "investigation", "number": "02", "category": "Research", "eyebrow": "SCIENTIFIC RESEARCH",
        "title": "Science Investigation", "description": "A school-level investigatory project shaped through structured inquiry, documentation, and clear presentation.",
        "tags": ["Research", "Data"], "role": "Student Researcher", "outcome": "2nd Place · School",
        "tools": "[List the actual research and data tools used]", "color": "linen",
    },
    {
        "id": "pasundayag", "number": "03", "category": "Creative", "eyebrow": "CREATIVE DIRECTION",
        "title": "Pasundayag", "description": "A film-poster concept that combined visual storytelling, layout, and creative direction for Pasundayag.",
        "tags": ["Graphic Design", "Publishing"], "role": "Poster Designer", "outcome": "1st Place · Film Poster",
        "tools": "[List the actual design tools used]", "color": "mist",
    },
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def portrait_data() -> str:
    photo = ROOT / "assets" / "profile.jpg"
    return base64.b64encode(photo.read_bytes()).decode("ascii") if photo.exists() else ""


def skills_markup(items: list[dict]) -> str:
    if not items:
        return '<p class="empty-message">No skills in this category yet.</p>'
    return '<div class="skill-grid">' + ''.join(
        '<div class="skill-item">'
        f'<div class="skill-top"><h3>{esc(s["skill"])}</h3><span>{s["rating"]}%</span></div>'
        f'<div class="skill-track"><div class="skill-fill" style="width:{int(s["rating"])}%"></div></div>'
        f'<div class="skill-category">{esc(s["area"])}</div>'
        '</div>' for s in items
    ) + '</div>'


def projects_markup(items: list[dict]) -> str:
    if not items:
        return '<p class="empty-message">There are no projects in this category.</p>'
    result = ['<div class="project-grid">']
    for p in items:
        tags = ''.join(f'<span class="tag">{esc(t)}</span>' for t in p["tags"])
        result.append(
            f'<article class="project-card {esc(p["color"])}">'
            f'<div class="project-no">{esc(p["number"])}</div>'
            '<div class="project-middle">'
            f'<div class="micro-label">{esc(p["eyebrow"])}</div>'
            f'<h3>{esc(p["title"])}</h3>'
            f'<p>{esc(p["description"])}</p>'
            f'<div class="tags">{tags}</div>'
            '</div>'
            '<div class="project-bottom">'
            f'<div><small>MY ROLE</small><b>{esc(p["role"])}</b></div>'
            f'<div><small>OUTCOME</small><b>{esc(p["outcome"])}</b></div>'
            f'<a class="round-arrow" href="#detail-{esc(p["id"])}" '
            f'aria-label="View {esc(p["title"])} details">↗</a>'
            '</div></article>'
        )
    result.append('</div>')
    return ''.join(result)


st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "CSIT 349 · Applied AI — Autobiography and Portfolio"},
)
st.markdown(f"<style>{(ROOT / 'styles.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
if "feedback_count" not in st.session_state:
    st.session_state.feedback_count = 0
if "milestone_cursor" not in st.session_state:
    st.session_state.milestone_cursor = -1

with st.sidebar:
    st.markdown(
        '<div class="side-shell">'
        f'<div class="side-logo">{esc(INITIALS)}<span>.</span></div>'
        '<nav class="side-nav" aria-label="Section navigation">'
        '<a href="#home">HOME</a>'
        '<a href="#story">STORY</a>'
        '<a href="#skills">SKILLS</a>'
        '<a href="#work">WORK</a>'
        '<a href="#contact">CONTACT</a>'
        '</nav>'
        '<div class="side-status"><span class="status-dot"></span>'
        '<div><b>Available</b><small>for new ideas</small></div></div>'
        '</div>', unsafe_allow_html=True,
    )

# Mobile fallback navigation. Sidebar is hidden on small screens.
st.markdown(
    '<nav class="mobile-nav"><span class="mobile-logo">YM<span>.</span></span>'
    '<a href="#home">Home</a><a href="#story">Story</a>'
    '<a href="#skills">Skills</a><a href="#work">Work</a>'
    '<a href="#contact">Contact</a></nav>', unsafe_allow_html=True
)

with st.container(key="home_section"):
    st.markdown(
        '<span id="home" class="scroll-anchor"></span>'
        '<div class="site-topbar"><span>CSIT 349 · APPLIED AI</span>'
        '<a href="#contact">LET’S CONNECT</a></div>', unsafe_allow_html=True,
    )
    hero_copy, hero_photo = st.columns([1.22, 0.95], gap="large", vertical_alignment="center")
    with hero_copy:
        st.markdown(
            '<div class="hero-copy">'
            f'<p class="overline">HELLO, I’M {esc(NAME.upper())}</p>'
            '<h1>I build with<br>logic<br><em>and<br>creativity.</em></h1>'
            f'<p class="hero-summary">{esc(HELLO)}</p>'
            '<div class="hero-actions"><a class="primary-link" href="#work">Explore my work <span>→</span></a>'
            '<a class="text-link" href="#story">Read my story</a></div>'
            '</div>', unsafe_allow_html=True,
        )
    with hero_photo:
        image_b64 = portrait_data()
        photo_html = (f'<img src="data:image/jpeg;base64,{image_b64}" alt="Portrait supplied with the design reference">'
                      if image_b64 else '<div class="photo-placeholder">ADD YOUR PROFILE PHOTO</div>')
        st.markdown(
            '<div class="portrait-wrap">'
            '<div class="portrait-frame">'
            + photo_html +
            '<div class="portrait-caption"><span>CURRENTLY STUDYING</span>'
            f'<strong>{esc(COURSE)} at<br>{esc(SCHOOL)}</strong></div></div>'
            '<div class="portrait-badge"><strong>BSCS</strong><small>CIT–U STUDENT</small></div>'
            '</div>', unsafe_allow_html=True,
        )
    st.markdown(
        '<div class="hero-stats">'
        '<div><small>FEATURED</small><strong>03 selected projects</strong></div>'
        '<div><small>LEARNING</small><strong>Software & design</strong></div>'
        f'<div><small>BASED IN</small><strong>{esc(CITY)}</strong></div>'
        '</div>', unsafe_allow_html=True,
    )

with st.container(key="story_section"):
    st.markdown('<span id="story" class="scroll-anchor"></span>', unsafe_allow_html=True)
    story_left, story_right = st.columns([0.82, 1.18], gap="large")
    with story_left:
        st.markdown(
            '<div class="story-title"><p class="overline">01 · MY STORY</p>'
            '<h2>Curious by<br>nature,<br>grounded<br>by<br>purpose.</h2></div>',
            unsafe_allow_html=True,
        )
    with story_right:
        background_tab, education_tab, interests_tab = st.tabs(["BACKGROUND", "EDUCATION", "INTERESTS"])
        for title, tab in [("BACKGROUND", background_tab), ("EDUCATION", education_tab), ("INTERESTS", interests_tab)]:
            with tab:
                st.markdown(
                    '<div class="story-paragraphs">' + ''.join(f'<p>{esc(s)}</p>' for s in STORY[title]) + '</div>',
                    unsafe_allow_html=True,
                )
        st.markdown(
            '<div class="timeline">' + ''.join(
                f'<div><strong>{esc(year)}</strong><span>{esc(detail)}</span></div>'
                for year, detail in MILESTONES
            ) + '</div>', unsafe_allow_html=True,
        )

with st.container(key="skills_section"):
    st.markdown('<span id="skills" class="scroll-anchor"></span>', unsafe_allow_html=True)
    heading, select_area = st.columns([1.65, 0.7], gap="large", vertical_alignment="bottom")
    with heading:
        st.markdown('<p class="overline">02 · CAPABILITIES</p><h2 class="section-title">Skills I’m<br>growing.</h2>', unsafe_allow_html=True)
    with select_area:
        chosen_area = st.selectbox("SHOW SKILLS", ["All", "Technical", "Creative", "Academic", "Leadership"], label_visibility="visible")
    shown_skills = SKILLS if chosen_area == "All" else [s for s in SKILLS if s["area"] == chosen_area]
    st.markdown(skills_markup(shown_skills), unsafe_allow_html=True)


    st.markdown('<div class="toolbox-divider"></div>', unsafe_allow_html=True)

    toolbox_left, toolbox_right = st.columns(
        [3, 1],
        vertical_alignment="center"
    )

    with toolbox_left:
        st.markdown(
            '<div class="toolbox-heading"><h3>Toolbox</h3></div>',
            unsafe_allow_html=True
        )

    with toolbox_right:
        show_experience = st.checkbox(
            "Show experience",
            value=True
        )
    st.markdown(
        '<div class="tool-table"><div class="tool-table-head">'
        '<span>TOOL</span><span>USED FOR</span><span>EXPERIENCE</span></div>'
        + ''.join(
            '<div class="tool-row">'
            f'<strong>{esc(t["tool"])}</strong><span>{esc(t["purpose"])}</span>'
            f'<span>{esc(t["experience"]) if show_experience else "—"}</span></div>'
            for t in TOOLBOX
        ) + '</div>', unsafe_allow_html=True,
    )

    with st.expander("EXPLORE MY SKILLS · interactive data & reflections"):
        st.caption("All ratings are the self-assessments shown in your reference design. Edit them to your real values.")
        min_rating = st.slider("Minimum self-rating to display", min_value=0, max_value=100, value=0, step=5)
        areas = st.multiselect("Areas I'm exploring", ["Technical", "Creative", "Academic", "Leadership"], default=["Technical", "Creative", "Academic", "Leadership"])
        chart_view = st.radio("How would you like to see the ratings?", ["Chart", "Table"], horizontal=True)
        ratings = pd.DataFrame(SKILLS)
        ratings = ratings[(ratings["rating"] >= min_rating) & ratings["area"].isin(areas)]
        if ratings.empty:
            st.info("No ratings match this selection. Adjust the filters above.")
        elif chart_view == "Chart":
            st.bar_chart(ratings.set_index("skill")["rating"], color="#8B9B80", horizontal=True)
        else:
            st.table(ratings.rename(columns={"skill": "Skill", "rating": "Self-rating (%)", "area": "Area"}))
        metric1, metric2 = st.columns(2)
        metric1.metric("Skills in profile", len(SKILLS))
        metric2.metric("Shown in explorer", len(ratings))
        if st.button("Show me a milestone", key="milestone_button"):
            st.session_state.milestone_cursor = (st.session_state.milestone_cursor + 1) % len(MILESTONES)
        if st.session_state.milestone_cursor >= 0:
            yr, item = MILESTONES[st.session_state.milestone_cursor]
            st.info(f"{yr} · {item}")

with st.container(key="work_section"):
    st.markdown('<span id="work" class="scroll-anchor"></span>', unsafe_allow_html=True)
    work_title, work_filter = st.columns([1.65, 0.7], gap="large", vertical_alignment="bottom")
    with work_title:
        st.markdown('<p class="overline">03 · SELECTED WORK</p><h2 class="section-title">A few things<br>I’ve made.</h2>', unsafe_allow_html=True)
    with work_filter:
        focus = st.selectbox("PROJECT FOCUS", ["All projects", "Research", "Creative"], label_visibility="visible")
    filtered_projects = PROJECTS if focus == "All projects" else [p for p in PROJECTS if p["category"] == focus]
    st.markdown(projects_markup(filtered_projects), unsafe_allow_html=True)
    with st.expander("MORE ABOUT THESE PROJECTS · roles, tools & outcomes"):
        for p in filtered_projects:
            st.markdown(f'<span id="detail-{esc(p["id"])}"></span><h4>{esc(p["title"])}</h4>', unsafe_allow_html=True)
            st.write(p["description"])
            st.write(f"**My role:** {p['role']}  ·  **Outcome:** {p['outcome']}")
            st.write(f"**Tools:** {p['tools']}")
            st.divider()

with st.container(key="contact_section"):
    st.markdown('<span id="contact" class="scroll-anchor"></span>', unsafe_allow_html=True)
    contact_copy, contact_form = st.columns([0.85, 1.15], gap="large")
    with contact_copy:
        st.markdown(
            '<div class="contact-copy"><p class="overline">04 · SAY HELLO</p>'
            '<h2 class="section-title">Have an<br>idea?<br><em>Let’s talk.</em></h2>'
            '<p class="contact-lede">I’m open to learning opportunities, meaningful collaborations, and projects where technology and creativity come together.</p>'
            f'<a class="email-link" href="mailto:{esc(EMAIL)}">{esc(EMAIL)}</a>'
            f'<p class="contact-details">{esc(CITY)}<br>Section: {esc(SECTION)}</p></div>',
            unsafe_allow_html=True,
        )
    with contact_form:
        with st.form("portfolio_contact", clear_on_submit=True):
            name_col, email_col = st.columns(2)
            with name_col:
                visitor_name = st.text_input("YOUR NAME", placeholder="Jane Smith")
            with email_col:
                visitor_email = st.text_input("EMAIL ADDRESS", placeholder="jane@example.com")
            topic = st.selectbox("I’D LIKE TO TALK ABOUT", ["A project idea", "A collaboration", "A learning opportunity", "Just saying hello"])
            visitor_message = st.text_area("YOUR MESSAGE", placeholder="Tell me a little about what you have in mind…", height=170)
            sent = st.form_submit_button("Send message    →")
        if sent:
            if not visitor_name.strip() or not visitor_email.strip() or not visitor_message.strip():
                st.warning("Please enter your name, email address, and a message.")
            elif "@" not in visitor_email or "." not in visitor_email.rsplit("@", 1)[-1]:
                st.warning("Please enter a valid email address.")
            else:
                st.session_state.feedback_count += 1
                st.success(f"Thanks, {visitor_name}! Your message was received in this demo session.")
                st.info("This is a school-demo form. It does not send email or save messages to a server.")
                st.download_button(
                    "Download your message",
                    data=f"From: {visitor_name}\nEmail: {visitor_email}\nTopic: {topic}\n\n{visitor_message}\n",
                    file_name="my_portfolio_message.txt",
                    mime="text/plain",
                    key=f"save_message_{st.session_state.feedback_count}",
                )
    portfolio_summary = (
        f"{NAME}\n{COURSE} · {SCHOOL}\nSection: {SECTION}\n\n"
        f"ABOUT ME\n{HELLO}\n\nMY STORY\n"
        + '\n'.join(f"{key}: {' '.join(paragraphs)}" for key, paragraphs in STORY.items())
        + "\n\nSKILLS\n" + '\n'.join(f"{s['skill']} — {s['rating']}%" for s in SKILLS)
        + "\n\nPROJECTS\n" + '\n'.join(
            f"{p['title']}: {p['description']} | Role: {p['role']} | Tools: {p['tools']} | Outcome: {p['outcome']}"
            for p in PROJECTS
        )
    )
    st.download_button("↓ Download portfolio summary", portfolio_summary, "portfolio_summary.txt", "text/plain", key="download_portfolio")

st.markdown(
    f'<footer class="site-footer"><b>{esc(NAME)}</b>'
    '<span>CSIT 349 · APPLIED AI</span>'
    '<small>DESIGNED WITH CURIOSITY · 2026</small></footer>', unsafe_allow_html=True,
)


st.html("""
<script>
(function () {
    const sections = ["home", "story", "skills", "work", "contact"];

    function updateActiveSection() {
        let currentSection = "home";
        const threshold = window.innerHeight * 0.35;

        sections.forEach(function (id) {
            const section = document.getElementById(id);

            if (section &&
                section.getBoundingClientRect().top <= threshold) {
                currentSection = id;
            }
        });

        document.querySelectorAll(".side-nav a").forEach(function (link) {
            const active = link.getAttribute("href") === "#" + currentSection;

            link.classList.toggle("active", active);

            if (active) {
                link.setAttribute("aria-current", "location");
            } else {
                link.removeAttribute("aria-current");
            }
        });
    }

    if (window.portfolioScrollHandler) {
        window.removeEventListener(
            "scroll", window.portfolioScrollHandler, true
        );
        window.removeEventListener(
            "resize", window.portfolioScrollHandler
        );
    }

    window.portfolioScrollHandler = updateActiveSection;

    window.addEventListener(
        "scroll", updateActiveSection, true
    );
    window.addEventListener(
        "resize", updateActiveSection
    );

    updateActiveSection();
})();
</script>
""", unsafe_allow_javascript=True)

