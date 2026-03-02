import streamlit as st

# MUST be first Streamlit command
st.set_page_config(page_title="AF Form 1206 Award Builder", layout="wide")

# =====================================================
# AF FORM 1206 – NOMINATION HEADER
# =====================================================

st.markdown("## NOMINATION FOR AWARD")

# Row 1
col1, col2, col3 = st.columns(3)
award = col1.text_input("AWARD")
category = col2.text_input("CATEGORY (If Applicable)")
award_period = col3.text_input("AWARD PERIOD")

# Row 2
col4, col5 = st.columns([3, 2])
nominee_name = col4.text_input("RANK/NAME OF NOMINEE (First, Middle Initial, Last)")
majcom = col5.text_input("MAJCOM, FLDCOM, FOA OR DRU (ALL CAPS)")

# Row 3
col6, col7 = st.columns(2)
dafsc = col6.text_input("DAFSC/DUTY TITLE")
nominee_phone = col7.text_input("NOMINEE'S TELEPHONE (DSN & Commercial)")

# Row 4
unit_address = st.text_input(
    "UNIT/OFFICE SYMBOL/STREET ADDRESS/BASE/STATE/ZIP CODE"
)

# Row 5 (Commander Info)
col8, col9 = st.columns(2)
commander_name = col8.text_input(
    "RANK/NAME OF UNIT COMMANDER (First, Middle Initial, Last)"
)
commander_phone = col9.text_input(
    "COMMANDER'S TELEPHONE (DSN & Commercial)"
)

st.divider()

# =====================================================
# COMMANDER'S BLOCK (replaces Block 6)
# =====================================================
st.subheader("COMMANDER'S BLOCK")

commander_block = st.text_area(
    "Commander’s Comments / Endorsement",
    height=150
)

st.divider()

# =====================================================
# SCORING + BUILDER SETTINGS
# =====================================================

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

with st.expander("Performance Statements Guidance (AF Form 1206)"):

    st.subheader("Purpose")
    st.write("""
Performance Statements communicate an Airman’s performance clearly and concisely.
""")

    st.subheader("Core Principles")

    st.markdown("""
**Standalone**
- Include action + impact/result

**Readability**
- Use plain language
- Avoid uncommon acronyms
""")

    st.subheader("Writing Tips")

    st.markdown("""
✔ Be measurable  
✔ Show mission impact  
✔ Quantify results  
✔ Avoid vague claims  
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
# CITATION BUILDER
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
