from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store projects
projects = []

# Home page - list of projects
@app.route('/')
def index():
    return render_template('index.html', projects=projects)

# Add a new project
@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        projects.append({'name': name, 'description': description})
        return redirect(url_for('index'))
    return render_template('add_project.html')

# Edit a project
@app.route('/edit_project/<int:index>', methods=['GET', 'POST'])
def edit_project(index):
    if request.method == 'POST':
        projects[index]['name'] = request.form['name']
        projects[index]['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('edit_project.html', project=projects[index])

# Delete a project
@app.route('/delete_project/<int:index>')
def delete_project(index):
    del projects[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
