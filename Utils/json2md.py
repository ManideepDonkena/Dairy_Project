# takes the json file and gets the date and the content of the diary entry 
import markdown
import os
import json
from  datetime import datetime
from Utils.md2html import convert_md_to_html


def get_diary_entry(date: str, data_file_path: str) -> dict:
    with open(data_file_path, "r") as file:
        data = json.load(file)
    return data.get(date, {})
def generate_markdown(json_path, date):
    # form json path to get the diary entry of the date
    diary_entry = get_diary_entry(date, json_path)
    # check if the diary entry is empty
    if not diary_entry:
        return None
    # get the schedule from the diary entry
    schedule = diary_entry.get("schedule", [])
    # get table form of the schedule
    schedule_table = "| Time | Task |\n|------|------|\n"
    for item in schedule:
        schedule_table += f"| {item['time']} | {item['task']} |\n"
    wake_up_time = diary_entry.get("wakeUpTime", "")
    verse = diary_entry.get("verse", "")
    quote = diary_entry.get("quote", "")
    reflections = diary_entry.get("reflections", "")
    chanting = diary_entry.get("chanting", "")


    # generate the markdown content
    current_date = date
    markdown_content = f"""
# 📔 Daily Diary - {current_date}

---

## 🌅 Morning Reflections

### ⏰ Schedule & Activities

{schedule_table}

### 🔔 Morning Details
- Wake-Up Time: `{wake_up_time}`
- Verse Memorized:
  > {verse}
- Quote of the Day:
  > {quote}

---

## 🌇 Evening Reflections

### 💭 Day's Overview
- **Reflections:**
  {reflections}

### 🕉️ Spiritual Practice
- **Chanting Progress:**
  {chanting}

---

*Last Updated: {datetime.now().strftime("%I:%M %p")}*
"""
    return markdown_content

if __name__ == "__main__":
    json_path = "../data.json"
    date = "2025-02-20"
    markdown_content = generate_markdown(json_path, date)
    if markdown_content:
        print(markdown_content)
        html_content = convert_md_to_html(markdown_content)
        # save the html content to a file
        with open(f"diary.html", "w") as file:
            file.write(html_content)
        print(html_content)
    else:
        print(f"No diary entry found for the date: {date}")