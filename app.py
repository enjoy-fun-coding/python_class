from flask import Flask, request, render_template, jsonify
import info
app = Flask(__name__)

RECAPTCHA_SECRET_KEY = info.SECRETE_KEY

@app.route('/', methods=['GET'])
def hello():
    return render_template('captcha.html')

@app.route('/test', methods=['POST'])
def test():
    token = request.form.get('g-recaptcha-response')
    verification_response = request.post('https://www.google.com/recaptcha/api/siteverify',
                                         data={
                                             'secret' : RECAPTCHA_SECRET_KEY,
                                             'response' : token
                                         } )
    result = verification_response.json()

    if result.get('success'):
        return jsonify({'message': 'Success!'}) , 200
    else:
        return jsonify({'msg' : 'Failed reCaptcha verfication.'}), 400
if __name__ == '__main__':
    app.run(debug=True)
