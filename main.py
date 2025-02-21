import os
import json
from flask import Flask, request, render_template, send_from_directory
from datetime import datetime
from Utils.md2html import convert_md_to_html
from Utils.json2md import generate_markdown
app = Flask(__name__)

THEME = "dark"

# Ensure the 'diary_entries' folder exists
if not os.path.exists("diary_entries"):
    os.makedirs("diary_entries")

# Ensure the 'data.json' file exists
data_file_path = "diary_entries/data.json"
if not os.path.exists(data_file_path):
    with open(data_file_path, "w") as file:
        json.dump({}, file)

@app.route("/", methods=["GET"])
def diary_form():
       # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Read the existing data
    with open(data_file_path, "r") as file:
        data = json.load(file)
    
    # Check if there is an entry for the current date
    entry = data.get(current_date, None)
    
    return render_template("index.html", entry=entry)

@app.route("/save", methods=["POST"])
def save_diary():
    # Get form data
    times = request.form.getlist("time[]")
    tasks = request.form.getlist("task[]")
    wake_up_time = request.form.get("wakeUpTime")
    verse = request.form.get("verse")
    quote = request.form.get("quote")
    reflections = request.form.get("reflections")
    chanting = request.form.get("chanting")

# Update the data.json file
    # Create a dictionary for the new entry
    new_entry = {
        "schedule": [{"time": t, "task": task} for t, task in zip(times, tasks)],
        "wakeUpTime": wake_up_time,
        "verse": verse,
        "quote": quote,
        "reflections": reflections,
        "chanting": chanting
    }
    # Read the existing data
    with open(data_file_path, "r") as file:
        data = json.load(file)
    # Append the new entry with the current date as the key
    date_key = datetime.now().strftime("%Y-%m-%d")
    data[date_key] = new_entry
    # Save the updated data back to the file
    with open(data_file_path, "w") as file:
        json.dump(data, file, indent=4)
    return f"<h1>Diary Saved Successfully!</h1><p>Your diary has been saved as 'diary_{date_key}'.</p>"

@app.route("/entries", methods=["GET"])
def list_entries():
    # List all Markdown files in the 'diary_entries' directory
    # get the key of the json file
    with open(data_file_path, "r") as file:
        data = json.load(file)
    keys = list(data.keys())
    entries = [f"diary_{key}" for key in keys]
    return render_template("entries.html", entries=entries)

@app.route("/entries/<filename>", methods=["GET"])
def view_entry(filename):
    # Convert Markdown to HTML
    md_content = generate_markdown(data_file_path, filename[6:16])
    html_content = convert_md_to_html(md_content, theme= THEME)  # Change theme to "dark" if needed 
    return html_content

if __name__ == "__main__":
    app.run(debug=True, port=8080)
