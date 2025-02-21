import markdown

def convert_md_file_to_html(md_filepath, theme="light"):
        # Read the Markdown file
    with open(md_filepath, "r") as md_file:
        md_content = md_file.read()
    return convert_md_to_html(md_content, theme)

def convert_md_to_html(md_content, theme="light"):
    # Define CSS for light and dark themes
    CSS_LIGHT = """
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f9;
            margin: 20px;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #5cb85c;
            text-align: center;
        }
        h2 {
            color: #333;
            margin-top: 20px;
            border-bottom: 2px solid #5cb85c;
            padding-bottom: 5px;
        }
        ul {
            list-style-type: square;
            margin-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        strong {
            color: #5cb85c;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 18px;
            text-align: left;
        }
        table th, table td {
            padding: 12px 15px;
            border: 1px solid #ddd;
        }
        table th {
            background-color: #5cb85c;
        }
        table tr:hover {
            background-color: #92cf92;
        }
    </style>
    """

    CSS_DARK = """
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #333;
            color: #f4f4f4;
            margin: 20px;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #5cb85c;
            text-align: center;
        }
        h2 {
            color: #f4f4f4;
            margin-top: 20px;
            border-bottom: 2px solid #5cb85c;
            padding-bottom: 5px;
        }
        ul {
            list-style-type: square;
            margin-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        strong {
            color: #5cb85c;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 18px;
            text-align: left;
        }
        table th, table td {
            padding: 12px 15px;
            border: 1px solid #555;
        }
        table th {
            background-color: #444;
        }
        table tr:nth-child(even) {
            background-color: #555;
        }
        table tr:hover {
            background-color: #666;
        }
    </style>
    """
    # Select the appropriate CSS
    CSS = CSS_LIGHT if theme == "light" else CSS_DARK

    # Convert Markdown to HTML with multiple extensions
    html_content = markdown.markdown(md_content, extensions=['extra', 'tables', 'fenced_code', 'toc', 'sane_lists', 'footnotes'])

    # Combine CSS and HTML
    full_html = f"{CSS}<body>{html_content}</body>"

    return full_html

# Example usage
if __name__ == "__main__":
    html_output = convert_md_to_html("../diary_entries/diary_2025-02-20.md", theme="light")
    with open("diary.html", "w") as html_file:
        html_file.write(html_output)
    print("Markdown has been converted to HTML successfully!")