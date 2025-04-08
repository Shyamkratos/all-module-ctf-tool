from flask import Flask, request, render_template_string
import sys, io

app = Flask(__name__)

HTML = """
<h2>CTF Python Runner</h2>
<form method="post">
    <textarea name="code" rows="15" cols="80">{{code}}</textarea><br>
    <input type="submit" value="Run Code">
</form>
<pre>{{output}}</pre>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    code = ""
    if request.method == "POST":
        code = request.form["code"]
        buffer = io.StringIO()
        sys.stdout = buffer
        try:
            exec(code)
        except Exception as e:
            print("Error:", e)
        sys.stdout = sys.__stdout__
        output = buffer.getvalue()
    return render_template_string(HTML, output=output, code=code)

if __name__ == "__main__":
    import os  port = int(os.environ.get("PORT", 5000)) app.run(host="0.0.0.0", port=port)
