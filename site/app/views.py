# views.py

from app import app

from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
  organizations = [
                    {'name':'Select an Organization and Press Start', 'address': '-'},
                    {'name':'New Wave Nigeria', 'address': '43k9DZs9WDe5FNei1C4zUo4A5LBNQ3wLain8UcQzv522JpVrPEodDnvcmrmYRAixhyJVdEdp6NEQmXgbRbpf8a2r2hAjCQs'},
                  ]

  if request.method == 'GET':
    return render_template("index.html", organizations=organizations, address='', status='NOT MINING', button_name='Start')
  elif request.method == 'POST':
    choice_org_list = organizations
    addr = ''

    org_response = request.form.get('org_select')
    org = str(org_response)

    if org == 'Select an Organization and Press Start':
      return render_template("index.html", organizations=organizations, address='', status='NOT MINING', button_name='Start')

    for orgs in organizations:
      if orgs['name'] == org:
        addr = orgs['address']
        # Keep selection at top of list
        organizations.remove(orgs)
        organizations.insert(0, orgs)
        break

    return render_template("index.html", organizations=organizations, address=addr, status='MINING - Keep this page open', button_name='Switch Organization')

# TODO: Cummulative fund bar, contact info, license
