from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)

# Ensure the 'diary_entries' folder exists
if not os.path.exists("diary_entries"):
    os.makedirs("diary_entries")

@app.route("/", methods=["GET"])
def diary_form():
    return render_template("index.html")  # Load HTML from 'templates/index.html'

@app.route("/save", methods=["POST"])
def save_diary():
    # Get form data
    schedule = request.form.get("schedule")
    wake_up_time = request.form.get("wakeUpTime")
    verse = request.form.get("verse")
    quote = request.form.get("quote")
    reflections = request.form.get("reflections")
    aspects = request.form.get("aspects")
    special_reflections = request.form.get("specialReflections")
    chanting = request.form.get("chanting")
    reading = request.form.get("reading")
    art = request.form.get("art")

    # Generate Markdown content
    current_date = datetime.now().strftime("%Y-%m-%d")
    markdown_content = f"""
# Daily Diary - {current_date}

## Morning 🌅
- **Today's Schedule:** {schedule}
- **Wake-Up Time:** {wake_up_time}
- **Verse Memorized:** {verse}
- **Quote of the Day:** {quote}

## Evening 🌇
- **Reflections on the Day:** {reflections}
- **Key Aspects of the Day:** {aspects}
- **Special Reflections to Remember:** {special_reflections}

## Sadhana 🕉️
- **Chanting:** {chanting}
- **Reading:** {reading}
- **A.R.T (Reflective Thought):** {art}
"""

    # Save to a Markdown file in 'diary_entries' folder
    filename = f"diary_entries/diary_{current_date}.md"
    with open(filename, "w") as file:
        file.write(markdown_content)

    return f"<h1>Diary Saved Successfully!</h1><p>Your diary has been saved as '{filename}'.</p>"

if __name__ == "__main__":
    app.run(debug=True, port=8080)  # You can change the port if needed
