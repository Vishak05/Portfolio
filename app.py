from flask import Flask, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title = 'Home')

# Route for Projects
@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

# Route for Education
@app.route('/education')
def education():
    return render_template('education.html', title="Education")

# Route for Certifications
@app.route('/certifications')
def certifications():
    return render_template('certifications.html', title="Certifications")

# Route for Skills
@app.route('/skills')
def skills():
    return render_template('skills.html', title="Skills")

@app.route('/contact' , methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', title="Contact")
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_email(name, email, message)
        return redirect(url_for('home'))
    
def send_email(name, email, message):
    sender_email = email
    reciver_email = "vishaksenthilkumar@gmail.com"
    password = 'password'

    subject = 'Contact Form'
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, reciver_email, body)
        server.quit()
        print("Email sent successfully")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)

