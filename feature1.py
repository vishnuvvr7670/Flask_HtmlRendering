from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/send_html')
def send_html():
    return render_template('send_html.html',name='Vishnu',age=23,gender='Male')

@FAI.route('/properties')
def properties():
    return render_template('proparties.html')

if __name__ == '__main__':
    FAI.run(debug=True)