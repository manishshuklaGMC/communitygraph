from flask import Flask, render_template, url_for

application = Flask(__name__)


@application.route('/')
def hello_world():
    return render_template('%s.html' % 'index')


if __name__ == '__main__':
    application.run()
    #application.run(host='0.0.0.0', port=80)
