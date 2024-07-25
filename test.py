from flask import Flask, render_template, request, send_from_directory
from datetime import date, datetime
from dateutil import parser
from main import main
from flask_wtf import FlaskForm
from flask import redirect, url_for


app = Flask(__name__)
self = main()
placeholder = main.placeholder
file_name = ""


# ------------Display index----------------
@app.route('/')
def index():
    return render_template('index.html')

# ----------Fetch Data-------------
@app.route('/submit-form', methods=['GET','POST'])
def submit_form():
  global placeholder
  placeholder = {
    "contract_date": request.form.get('contract-date'),
    "address": request.form.get('address'),
    "auth_per": request.form.get('auth-per'),
    "designation": request.form.get('designation'),
    "eff_date": request.form.get('eff-date'),
    "client_company": request.form.get('client-company'),
    "client_address": request.form.get('client-address'),
    "client_name": request.form.get('client-name'),
    "client_designation": request.form.get('client-designation'),
    "gender": request.form.get('gender')
  }

  main.get_input(self, placeholder)
  file_name = f"NDA_{placeholder['client_company']}.docx"
  
  return redirect(url_for("download_file", file_name=file_name))


# -----------Download-----------
@app.route('/download/<file_name>', methods=['GET', 'POST'])
def download_file(file_name):
  global placeholder
  file_name = f"NDA_{placeholder['client_company']}.pdf"
  filepath = "Updated"
  return send_from_directory(filepath, file_name, as_attachment=True)


if __name__ == '__main__':
  app.run(debug=True)
