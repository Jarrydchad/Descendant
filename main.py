import smtplib

from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = 'jarryd'

# Configuring Flask-Mail
SMTP_SERVER = "smtp.zoho.com"
SMTP_PORT = 587  # Use port 587 for TLS or 465 for SSL
SMTP_USERNAME = "admin@descendantinv.co.za"
SMTP_PASSWORD = "@Cj2022!"

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():

    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        if not name or not email or not message:
            flash('Please fill out all required fields.')
            return redirect('/')

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        status, response = server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # server.
        if status == 235:  # 235 is the status code for a successful login
            print("Successfully logged in")
        else:
            print(f"Login failed. Status code: {status}, Response: {response}")
            return 'MF255'

        # message = request.form['message']
        msg = Message('Automated Response: Booking Request Received', sender=SMTP_USERNAME, recipients=[email])
        msg.html = f"""
                   <html>
                   <body>
                       <table align="center" width="80%" cellspacing="0" cellpadding="20">
                           <tr>
                               <td align="center" bgcolor="#f2f2f2">
                                   <table width="100%" cellpadding="20">
                                       <tr>
                                           <td align="center" bgcolor="#ffffff">
                                               <h1>Thank you for your enquiry</h1>
                                               <p>Dear {name},</p>
                                               <p>Thank you for reaching out to Descendant Innovations. We have received your enquiry and appreciate your interest in our services.</p>
                                               <p>Our team is committed to providing you with the highest level of service, and we understand the importance of a prompt response. Rest assured that your enquiry is important to us, and we will get back to you as soon as possible.</p>
                                               <p>One of our team members will review your request and contact you shortly to discuss your needs in detail. Please keep an eye on your email and phone for further communication.</p>
                                               <p>If you have any urgent questions or require immediate assistance, please do not hesitate to contact us at 067 752 7059 / 073 256 8781 .</p>
                                               <p>We look forward to assisting you and providing you with the exceptional service you deserve.</p>
                                               <p>Sincerely,<br>The Descendant Innovations Team</p>
                                           </td>
                                       </tr>
                                   </table>
                               </td>
                           </tr>
                       </table>
                   </body>
                   </html>
                   """

        # Dummy response for demonstration
        server.sendmail(SMTP_USERNAME, [email], msg.as_string())

        msg = Message('Automated Response: Consultation Request Received', sender=SMTP_USERNAME,
                       recipients=['jarrydchad@gmail.com'])
        msg.html = f"""
                  <html>
                  <body>
                      <div class="container">
                          <h1>Automated Response: Consultation Request Received</h1>
                          <p>Client: {name}</p>
                          <p>Email: {email}</p>
                          <p>Cell: {phone}</p>
                          <p>Message: {message}</p>
\
                      </div>
                  </body>
                  </html>
                  """

        # mail.send(msg2)
        server.sendmail(SMTP_USERNAME,
                        ['jarrydchad@gmail.com'],
                        msg.as_string())


        return 'MF000'
    except Exception as e:
        print('Error:', str(e))  # Log the error for debugging
        return 'MF255'
        # response = {'status': 'error', 'message': str(e)}



    # print(server.user)
    # server.sendmail(SMTP_USERNAME, [email], msg.as_string())

    # response = {'status': 'success', 'message': 'Form submission successful!'}

    # return jsonify(response)

    # flash('Message sent successfully!')
    # return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
