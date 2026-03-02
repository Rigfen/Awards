import streamlit as st

st.set_page_config(page_title="Air & Space Achievement Medal Builder", layout="wide")

MAX_POINTS = 32

general_checks = [
    ("Correct character length", 2),
    ("No more than 3 grammar errors", 2),
    ("Correct font formatting", 2),
    ("Correct tense used", 2),
    ("Name & pronouns correct", 2),
    ("Number usage correct", 2),
    ("Acronyms correct", 2),
    ("No absolutes/unquantifiable claims", 2),
]

sections = [
    ("Heading", 2),
    ("Opening Sentence", 2),
    ("Accomplishment 1", 2),
    ("Accomplishment 2", 2),
    ("Accomplishment 3", 2),
    ("Closing Sentence", 2),
    ("Feedback Form Completed", 2),
]

st.title("Air & Space Achievement Medal Builder")

# -------------------------
# COMPLIANCE SECTION
# -------------------------
st.header("Compliance")

compliance_checks = []
for label, pts in general_checks:
    checked = st.checkbox(f"{label} (+{pts})")
    compliance_checks.append((checked, pts))

st.divider()

# -------------------------
# SECTION INPUTS
# -------------------------
st.header("Citation Sections")

section_text = {}
section_checks = []

for name, pts in sections:
    st.subheader(name)

    text = st.text_area(
        f"Enter {name}",
        height=120,
        key=f"text_{name}"
    )
    section_text[name] = text

    meets = st.checkbox(f"{name} meets requirement (+{pts})", key=f"check_{name}")
    section_checks.append((meets, pts))

    st.divider()

# -------------------------
# SCORE CALCULATION
# -------------------------
score = 0

for checked, pts in compliance_checks:
    if checked:
        score += pts

for checked, pts in section_checks:
    if checked:
        score += pts

st.header(f"Total Score: {score} / {MAX_POINTS}")

# -------------------------
# COMPILE CITATION
# -------------------------
st.divider()
st.header("Final Citation")

if st.button("Compile Citation"):
    compiled = ""

    for name, _ in sections:
        text = section_text[name].strip()
        if text:
            compiled += text + "\n\n"

    st.session_state["compiled"] = compiled

if "compiled" in st.session_state:
    st.text_area("Compiled Output", st.session_state["compiled"], height=300)
    st.write(f"Character Count: {len(st.session_state['compiled'])}")
