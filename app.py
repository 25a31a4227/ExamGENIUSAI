import streamlit as st
from PyPDF2 import PdfReader

# Page configuration
st.set_page_config(
    page_title="ExamGenius AI",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 EXAMGENIUS AI")
st.subheader("From Syllabus & Past Papers to Personalized Exam Preparation")

st.write(
    "Upload your syllabus and past question papers to generate "
    "an intelligent practice paper."
)

# --------------------------------------------------
# STEP 1: UPLOAD SYLLABUS
# --------------------------------------------------

st.header("📚 Step 1: Upload Syllabus")

syllabus_file = st.file_uploader(
    "Upload your syllabus PDF",
    type=["pdf"]
)

syllabus_text = ""
topics = []

if syllabus_file:

    reader = PdfReader(syllabus_file)

    for page in reader.pages:
        text = page.extract_text()

        if text:
            syllabus_text += text + "\n"

    st.success("✅ Syllabus uploaded successfully!")

    with st.expander("📄 View Extracted Syllabus"):
        st.write(syllabus_text)

# --------------------------------------------------
# STEP 2: EXTRACT TOPICS
# --------------------------------------------------

st.header("🤖 Step 2: Extract Topics")

if syllabus_file:

    lines = syllabus_text.split("\n")

    for line in lines:
        line = line.strip()

        if len(line) > 5:
            topics.append(line)

    topics = topics[:15]

    st.success("✅ Topics extracted successfully!")

    for i, topic in enumerate(topics, 1):
        st.write(f"**{i}.** {topic}")

else:
    st.info("Please upload your syllabus first.")

# --------------------------------------------------
# STEP 3: PAST QUESTION PAPERS
# --------------------------------------------------

st.header("📑 Step 3: Past Question Papers")

past_papers = st.file_uploader(
    "Upload previous year question papers (optional)",
    type=["pdf"],
    accept_multiple_files=True
)

past_text = ""

if past_papers:

    st.header("🔍 Step 4: Analyze Past Papers")

    for paper in past_papers:

        reader = PdfReader(paper)

        for page in reader.pages:
            text = page.extract_text()

            if text:
                past_text += text + "\n"

    st.success("✅ Past papers analyzed!")

    with st.expander("📄 View Extracted Past-Paper Content"):
        st.write(past_text[:5000])

else:
    st.info(
        "No past papers uploaded. You can continue using syllabus-based preparation."
    )

# --------------------------------------------------
# STEP 5: EXAM INTELLIGENCE
# --------------------------------------------------

st.header("📊 EXAM INTELLIGENCE")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Topics Detected",
        len(topics)
    )

with col2:
    st.metric(
        "Past Papers",
        len(past_papers) if past_papers else 0
    )

with col3:
    st.metric(
        "Preparation Mode",
        "AI"
    )

# --------------------------------------------------
# STEP 6: PREPARATION MODE
# --------------------------------------------------

st.header("🎯 Step 5: Choose Preparation Mode")

mode = st.selectbox(
    "Select your preparation mode",
    [
        "Quick Revision",
        "Full Mock Test",
        "Hard Practice",
        "Complete Syllabus Practice",
        "Topic Practice"
    ]
)

st.write(f"Selected Mode: **{mode}**")

# --------------------------------------------------
# STEP 7: QUESTION SETTINGS
# --------------------------------------------------

st.header("📝 Step 6: Question Settings")

number_of_questions = st.slider(
    "Number of Practice Questions",
    min_value=5,
    max_value=20,
    value=10
)

difficulty = st.selectbox(
    "Difficulty Level",
    [
        "Easy",
        "Medium",
        "Hard",
        "Mixed"
    ]
)

# --------------------------------------------------
# STEP 8: GENERATE PRACTICE PAPER
# --------------------------------------------------

st.header("🚀 Step 7: Generate Practice Paper")

if st.button("✨ Generate Practice Paper"):

    if not syllabus_file:
        st.warning("⚠️ Please upload your syllabus first.")

    else:

        st.success("🎉 Practice Paper Generated!")

        st.write(f"### 📄 {mode}")
        st.write(f"**Difficulty:** {difficulty}")
        st.write(f"**Number of Questions:** {number_of_questions}")

        st.divider()

        # Generate sample questions based on detected topics
        if topics:

            for i in range(number_of_questions):

                topic = topics[i % len(topics)]

                st.write(
                    f"**Question {i + 1}:** Explain the important concepts "
                    f"related to **{topic}**."
                )

        else:

            for i in range(number_of_questions):

                st.write(
                    f"**Question {i + 1}:** Write an answer based on "
                    "the uploaded syllabus."
                )

        st.divider()

        st.success(
            "✅ Your personalized practice paper is ready!"
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "ExamGenius AI – From Syllabus & Past Papers to Personalized Exam Preparation"
)
