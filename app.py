from flask import Flask, render_template, request

app = Flask(__name__)

# Career data
careers = [
    {
        "name": "BioAI Researcher 🧬🤖",
        "description": "Combine biology and artificial intelligence to discover new drugs, analyze genomes, and improve healthcare using machine learning.",
        "skills": [
            "Biology & Life Sciences",
            "Python Programming",
            "Machine Learning",
            "Data Analysis"
        ],
        "resources": [
            "https://www.youtube.com/embed/PD-Kx2stUgU?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/SSzSOeGP87I?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/dde5II6xaWI?autoplay=1&enablejsapi=1&start=0&controls=1"
        ],
        "motivation": "✨ Shape the future of medicine with the power of AI."
    },
    {
        "name": "Natural Language Processing (NLP) Specialist 🗣️💡",
        "description": "Work on AI that understands human language—chatbots, translators, voice assistants, and text analysis.",
        "skills": [
            "Linguistics / Languages",
            "Python Programming",
            "Deep Learning (Transformers)",
            "Text & Speech Processing"
        ],
        "resources": [
            "https://www.youtube.com/embed/CMrHM8a3hqw?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/M7SWr5xObkA?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/Jzw2iw-2CMM?autoplay=1&enablejsapi=1&start=0&controls=1"
        ],
        "motivation": "✨ Give machines the gift of human language."
    },
    {
        "name": "Data Scientist 📊🔍",
        "description": "Turn raw data into insights using math, statistics, and AI. Data Scientists help businesses and researchers make smart decisions.",
        "skills": [
            "Mathematics & Statistics",
            "Python / R",
            "SQL & Databases",
            "Machine Learning"
        ],
        "resources": [
            "https://www.youtube.com/embed/dAkZTYgPBsw?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/7eh4d6sabA0?autoplay=1&enablejsapi=1&start=0&controls=1"
        ],
        "motivation": "✨ Turn data into discoveries that change the world."
    },
    {
        "name": "AI Engineer ⚙️🤖",
        "description": "Build and deploy real-world AI systems—recommendation engines, apps, and tools that people use every day.",
        "skills": [
            "Programming (Python, Java, or C++)",
            "Deep Learning Frameworks (TensorFlow, PyTorch)",
            "APIs & Web Development",
            "Problem-Solving"
        ],
        "resources": [
            "https://www.youtube.com/embed/FkqINm-l3q0?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/hKVNdNAIvD4?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/FQtlM5tiDlY?autoplay=1&enablejsapi=1&start=0&controls=1"
        ],
        "motivation": "✨ Be the builder who brings AI ideas to life."
    },
    {
        "name": "Computer Vision Specialist 👁️📷",
        "description": "Teach AI to see the world through images and videos—self-driving cars, medical imaging, and facial recognition.",
        "skills": [
            "Physics / Imaging",
            "Mathematics",
            "Python",
            "Convolutional Neural Networks (CNNs)"
        ],
        "resources": [
            "https://www.youtube.com/embed/Tu11SMJGGIA?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.learnopencv.com/computer-vision-in-30-days/"
        ],
        "motivation": "✨ Give AI the eyes to understand our world."
    },
    {
        "name": "Generative AI Artist (AI + Creativity) 🎨✨",
        "description": "Use AI to create art, music, and designs. Combine creativity with machine learning to explore new forms of expression.",
        "skills": [
            "Arts / Design Thinking",
            "Creativity & Innovation",
            "Python (basic for AI tools)",
            "Generative Models (GANs, Diffusion Models)"
        ],
        "resources": [
            "https://www.youtube.com/embed/gtzNUq7OnFQ?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/MYFOVROLK1A?autoplay=1&enablejsapi=1&start=0&controls=1",
            "https://www.youtube.com/embed/VA2L5iHRQRI?autoplay=1&enablejsapi=1&start=0&controls=1"
        ],
        "motivation": "✨ Unleash your creativity with the power of AI."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    name = request.form.get("name")
    grade = request.form.get("grade")
    subject = request.form.get("subject")
    coding = request.form.get("coding")
    thinking = request.form.get("thinking")

    # Career recommendation logic (customize as you wish!)
    if subject == "Biology":
        career = careers[0]
    elif subject == "Languages":
        career = careers[1]
    elif subject == "Math" and coding == "Yes":
        career = careers[2]
    elif subject == "Math" and coding == "No":
        career = careers[4]
    elif subject == "Arts":
        career = careers[5]
    elif subject == "Physics":
        career = careers[4]
    else:
        career = careers[3]

    return render_template(
        "results.html",
        name=name,
        career_name=career["name"],
        description=career["description"],
        skills=career["skills"],
        resources=career["resources"],
        motivation=career["motivation"]
    )

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
