from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'heart-disease-analysis-secret-key'


def build_gallery(items):
    return [
        {
            'src': url_for('static', filename=item['path']),
            'title': item['title'],
            'description': item['description'],
        }
        for item in items
    ]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/dashboard')
def dashboard():
    dashboard_slides = build_gallery([
        {
            'path': 'images/dashboard/Screenshot 2026-04-17 092804.png',
            'title': 'Dashboard Overview',
            'description': 'Main dashboard layout with summary charts and filters.',
        },
        {
            'path': 'images/dashboard/Screenshot 2026-04-17 092811.png',
            'title': 'Visualization Detail',
            'description': 'Detailed chart view showing the key heart disease patterns.',
        },
        {
            'path': 'images/dashboard/Screenshot 2026-04-17 092820.png',
            'title': 'Final Dashboard View',
            'description': 'Full dashboard screenshot for the final presentation slide.',
        },
    ])
    return render_template('dashboard.html', slides=dashboard_slides)


@app.route('/story')
def story():
    story_slides = build_gallery([
        {
            'path': 'images/story/Screenshot 2026-04-17 092903.png',
            'title': 'Story Scene 1',
            'description': 'Gender suffering from heart disease.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 092912.png',
            'title': 'Story Scene 2',
            'description': 'Effect of physical activity on heart disease.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 092918.png',
            'title': 'Story Scene 3',
            'description': 'Diabetes affecting heart disease.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 092924.png',
            'title': 'Story Scene 4',
            'description': 'Impact of smoking and alcohol on stroke.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 092930.png',
            'title': 'Story Scene 5',
            'description': 'Ethnicity-wise heart disease count.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 092939.png',
            'title': 'Story Scene 6',
            'description': 'People suffering from diabetes by age category.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 092949.png',
            'title': 'Story Scene 7',
            'description': 'Further analysis of heart disease indicators.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 092955.png',
            'title': 'Story Scene 8',
            'description': 'Additional story scene from the Tableau presentation.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 093003.png',
            'title': 'Story Scene 9',
            'description': 'Continuation of the story walkthrough.',
        },
        {
            'path': 'images/story/Screenshot 2026-04-17 093011.png',
            'title': 'Story Scene 10',
            'description': 'Final story screenshot for the presentation.',
        },
    ])
    return render_template('story.html', slides=story_slides)


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
