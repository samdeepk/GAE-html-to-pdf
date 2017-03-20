import StringIO
from flask import Flask, send_file

from xhtml2pdf import pisa


app = Flask(__name__)


@app.route('/pdf/')
def hello_pdf():
    pisa.showLogging()

    packet = StringIO.StringIO()

    sourcehtml = "<html><body><p>To PDF or not to PDF<p></body></html>"
    pisa.CreatePDF(
        sourcehtml,
        dest=packet)

    packet.seek(0)
    return send_file(packet, attachment_filename="willi.pdf", as_attachment=False)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
