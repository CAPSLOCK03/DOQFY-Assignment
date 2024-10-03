from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

snippets={}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/share',methods=['POST'])
def snippet_share():

    text_snippet = request.form['snippet']
    
    snippet_id = str(uuid.uuid4())

    snippets[snippet_id]=text_snippet

    return redirect(url_for('snippet_view',snippet_id=snippet_id))

@app.route('/view/<snippet_id>')
def snippet_view(snippet_id):

    snippet = snippets.get(snippet_id)

    return render_template('snippet_view.html', snippet=snippet) if snippet else 'Snippet not found.'

if __name__ == '__main__':
    app.run(debug=True)