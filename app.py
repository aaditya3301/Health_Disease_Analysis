from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'heart-disease-analysis-secret-key'

# =====================================================
# TABLEAU EMBED URLS - REPLACE THESE WITH YOUR OWN
# =====================================================
TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/YourWorkbookName/Dashboard"
TABLEAU_STORY_URL = "https://public.tableau.com/views/YourWorkbookName/Story"
# =====================================================


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', tableau_url=TABLEAU_DASHBOARD_URL)


@app.route('/story')
def story():
    return render_template('story.html', tableau_url=TABLEAU_STORY_URL)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if name and email and message:
            flash('Thank you for your message! We will get back to you soon.', 'success')
        else:
            flash('Please fill in all fields.', 'error')
        return redirect(url_for('contact'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
