from flask import Flask, request, jsonify, render_template
from jinja2 import Template
import os

app = Flask(__name__)

# Load the template file
def load_template():
    with open('template.yml', 'r') as file:
        return file.read()

@app.route('/')
def index():
    return render_template('config.html')

@app.route('/generate-script', methods=['POST'])
def generate_script():
    user_input = request.json  # Get the JSON data from the request
    
    # Load the YAML template
    template_content = load_template()
    
    # Render the template with the user data
    template = Template(template_content)
    final_script = template.render(user_input)
    
    # Respond with the generated script
    return jsonify({"generated_script": final_script})

if __name__ == '__main__':
    app.run(debug=True)
