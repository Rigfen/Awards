import streamlit as st

st.set_page_config(page_title="AF Form 1206 Award Builder", layout="wide")

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

st.title("AF Form 1206 Award Builder")

# =====================================================
# PERFORMANCE STATEMENT GUIDANCE
# =====================================================
with st.expander("Performance Statements Guidance (AF Form 1206)", expanded=False):

    st.subheader("Purpose")
    st.write("""
Performance Statements are the Air Force narrative-style method used on AF Form 1206 
to clearly communicate an Airman’s performance.
""")

    st.subheader("Two Core Principles")

    st.markdown("""
**Standalone**
- Each statement must stand on its own.
- Must include:
  - an **action**
  - and at least one:
    - impact
    - result/outcome

**Readability**
- Use plain language.
- Avoid uncommon acronyms.
- Only use approved Air Force acronyms.
""")

    st.subheader("Administration & Format")

    st.markdown("""
- AF Form 1206 is the standard award nomination form.
- White space on the right margin is expected.
- Award authority sets maximum length.
- Nominations may not exceed one full AF Form 1206 page.
- Bullets are **not authorized**.
- Future forms may include character limits.
""")

    st.subheader("Writing Tips")
    st.markdown("""
✔ Be specific and measurable  
✔ Include results and mission impact  
✔ Quantify whenever possible  
✔ Avoid vague claims  
✔ Focus on mission contribution  
""")

    st.subheader("Example Performance Statements")

    st.info("""
Capt Snuffy led a survey team of 33 MCA to establish an XAB supporting a PACAF ACE exercise across 4 countries and 7 allies, culminating in 153 sorties and 334 training events. She also championed a merger of maintenance and operations; results saved 360 maintenance workhours weekly and increased sortie generation by 10%.
""")

    st.info("""
TSgt Snuffy led 4 instructors through Mission Ready Airmen course validation, generating 153 changes, eliminating 32 classroom hours, and improving training for 70 students annually. Additionally, he facilitated a $15M facility renovation ensuring on-time course delivery for 8 programs across 11 AFSCs.
""")

# =====================================================
# COMPLIANCE CHECKS
# =====================================================
st.header("Compliance")

compliance_checks = []
for label, pts in general_checks:
    checked = st.checkbox(f"{label} (+{pts})")
    compliance_checks.append((checked, pts))

st.divider()

# =====================================================
# CITATION SECTIONS
# =====================================================
st.header("1206 Builder")

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

# =====================================================
# SCORE
# =====================================================
score = 0

for checked, pts in compliance_checks:
    if checked:
        score += pts

for checked, pts in section_checks:
    if checked:
        score += pts

st.header(f"Total Score: {score} / {MAX_POINTS}")

# =====================================================
# COMPILE CITATION
# =====================================================
st.divider()
st.header("Final Citation")

if st.button("Compile Citation"):
    compiled = ""

    for name, _ in sections:
        text = section_text[name].strip()
        if text:
            compiled += text + "\n\n"

    st.session_state["compiled"] = compiled

# =====================================================
# AF FORM 1206 – NOMINATION HEADER
# =====================================================

st.markdown("## NOMINATION FOR AWARD")

# Row 1
col1, col2, col3 = st.columns([2, 2, 2])
award = col1.text_input("AWARD")
category = col2.text_input("CATEGORY (If Applicable)")
award_period = col3.text_input("AWARD PERIOD")

# Row 2
col4, col5 = st.columns([3, 2])
nominee_name = col4.text_input("RANK/NAME OF NOMINEE (First, Middle Initial, Last)")
majcom = col5.text_input("MAJCOM, FLDCOM, FOA OR DRU (ALL CAPS)")

# Row 3
col6, col7 = st.columns([2, 2])
dafsc = col6.text_input("DAFSC/DUTY TITLE")
nominee_phone = col7.text_input("NOMINEE'S TELEPHONE (DSN & Commercial)(You dont need a area code)")

# Row 4
unit_address = st.text_input(
    "UNIT/OFFICE SYMBOL/STREET ADDRESS/BASE/STATE/ZIP CODE(Simple address. No th in 48th)"
)

# Row 5
commander_info = st.text_input(
    "RANK/NAME OF UNIT COMMANDER (First, Middle Initial, Last) / COMMANDER'S TELEPHONE (DSN & Commercial)"
)

st.divider()

if "compiled" in st.session_state:
    st.text_area("Compiled Output", st.session_state["compiled"], height=300)
    st.write(f"Character Count: {len(st.session_state['compiled'])}")
