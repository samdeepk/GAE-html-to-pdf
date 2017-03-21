
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import StringIO
from flask import Flask, send_file

from xhtml2pdf import pisa


app = Flask(__name__)


@app.route('/pdf/')
def hello_pdf():
    pisa.showLogging()

    packet = StringIO.StringIO()

    sourcehtml = u"""<!DOCTYPE html>
    <html>
    <head>
        <title>Annual Examinations</title>
    </head>
    <body style="font-family: times; font-size: 15px;">
    <div style="font-size: 13px;text-align: right;"> Centre&#58;</div><br/>
     <table style="width: 100%;">
        <tr>
            <td rowspan="4" style=" border:1px solid black; width:150px;"></td>
            <td style="text-align: center; font-family: Times, serif; font-size: 17px; font-weight: bold; width:800px;">POTTI SREERAMULU TELUGU UNIVERSITY</td>
            <td rowspan="4" style="width:100px;"></td>
        </tr>
        <tr>
            <td style="text-align: center;font-size: 14px; width:700px;">Public Gardens, Hyderabad - 500 004 Andhra Pradesh, India</td>
        </tr>
        <tr>
            <td style="text-align: center; font-size: 14px; width:700px;">Ph &#58; 040 - 2323 4490 Fax &#58; 040 - 2323 6045 e-mail &#58; itc@teluguuniversity.ac.in</td>
        </tr>
        <tr>
            <td style="text-align: center; font-size: 17px; font-weight: bold; width:700px;">CERTIFICATE COURSE IN TELUGU (Four Years)</td>
        </tr>
        <tr>
            <td></td>
            <td style="text-align: center; font-size: 15px; width:700px;">        
                <div style=" font-size: 15px; text-align: center;margin-top: 10px;"><b>(SILICONANDHRA - MANABADI)</b><br/></span><span style=" font-size: 15px;"> 2015 - 2016 Annual Examinations</span>
            </td>
            <td></td>
        </tr>
    </table>

<br/>
    <table style="">
        <tr style="margin-bottom:1px;">
            <td style="width:60%; color: grey; font-size: 15px;" align="left">APPLICATION FORM NO.    Not Applicable</td>
            <td style="width:35%; padding-left:8px; border:1px solid black; padding-top:3px;">Hall Ticket No.</td>
            <td style="width:5%;"></td>
        </tr>
        <tr style="margin-top:1px; font-size: 15px;">
            <td style="width:65%;"></td>
            <td style="width:35%; padding-top:3px; text-align:center">(To be filled by the Office)</td>
            <td style="width:5%;"></td>
        </tr>
    </table>

    <table style="margin-top: 5px; width:100%;">
        <tr>
            <td style=" font-size: 15px; width: 140px;">ManaBadi Location&#58;</td>
            <td style="width: 30%;"><hr/></td>
        </tr>
        <tr>
            <td></td>
            <td style="text-align: center; font-size: 15px;">(City, STATE)</td>
        </tr>
    </table>
    <br/>
    <div style="font-size: 15px;">Name of the Association: <b>SiliconAndhra ManaBadi</b></div>
    <div style="font-size: 15px;">Name of the Course (circle one): Prakasam (Jr.Certificate) <b>OR</b> Prabhasam (Sr.Certificate)   </div>
    
    <table style="width: 100%; font-size: 13px;">
        <tr>
            <td style="width: 50%; border: 1px solid black; border-collapse: collapse; padding-top: 3px; padding-left: 3px;">SUBJECT&#58; <b>TELUGU</b></td>
            <td style="width: 50%; border: 1px solid black; border-collapse: collapse; padding-top: 3px; padding-left: 3px;">BATCH&#58;  <b>Not Applicable</b></td>
        </tr>
    </table>

    <table style="width: 90%; margin-top: 28px;">
        <tr>
            <td style="width: 40%;font-size: 15px;"></td>
            <td style="color: grey;font-size: 15px;">Examination Fee</td>
            <td style="color: grey;font-size: 15px;">&#58;</td>
            <td style="color: grey;font-size: 15px; text-align: center;">Not Applicable</td>
        </tr>
        <tr>
            <td style="width: 40%;font-size: 15px;"></td>
            <td style="color: grey;font-size: 15px;">Late Fee</td>
            <td style="color: grey;font-size: 15px;">&#58;</td>
            <td style="color: grey;font-size: 15px; text-align: center;">Not Applicable</td>
        </tr>
        <tr>
            <td style="width: 40%;font-size: 15px;"></td>
            <td style="color: grey;font-size: 15px;">Total</td>
            <td style="color: grey;font-size: 15px;">&#58;</td>
            <td style="color: grey; text-align: center;font-size: 15px;">Not Applicable</td>
        </tr>
    </table>

    <br/><br/>

    <table style="width: 100%;">
        <tr style="color: grey;">
            <td style="width: 60px;font-size: 13px;">D.D. No.</td>
            <td style="width: 60px; font-size: 13px;"><hr/></td>
            <td style="width: 50px;font-size: 13px; padding-left:15px;">Date&#58;</td>
            <td style="width: 120px;font-size: 13px; padding-left:15px;"><hr/></td>
            <td style="width: 30px;font-size: 13px;">Rs.</td>
            <td style="width: 120px;font-size: 13px;"><hr/></td>
            <td style="width: 120px;font-size: 13px;">Name of the Bank</td>
            <td style="width: 100px;font-size: 13px;"><hr/></td>
        </tr>
    </table>

    <br/>
    <table style="font-size: 14px; width:100%">
        <tr>
            <td rowspan="11" style="width: 23%;height: 1px; border:1px solid black; font-size: 12px; padding: 1%; margin-top: 2px; margin-left: 5px; margin-right: 0px;">
            Passport size photo of the Candidate to be attested by the Secretary &#47;Head of the Institution concerned with seal of the Office affixed over it.
            <td style="width:5%"></td>
            <td style=" font-size: 15px; line-height: 30px;" ><b>NOTE&#58;</b></td>
        </tr>
        <tr>
            <td style="width:5%"></td>
            <td style="width:60%">1.&#32;&#32;The Candidate should apply separately for each course for each year.</td>
        </tr>
        <tr>
            <td style="width:5%"></td>
            <td style="width:60%">2.&#32;&#32;Candidate&#39;s recent Passport size photo should be affixed.</td>
        </tr>
        <tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr>
    </table>

<br/><br/>
    <div style="margin:6px;font-size: 15px;">1.   Name of the Candidate in full (in block letters):
            <div style="font-size: 12px; margin-left:8px;">(According to the registration) <b>(Last name, First Name. Middle Name)</b></div>
    </div>
    <div style="margin:6px; font-size: 15px;">2.   Father&#39;s Name <b>(Last Name, First Name)&#58;</b></div>
    <table style="width: 100%; margin:8px;">
        <tr>
            <td style="width: 20px;font-size: 15px;">3.</td>
            <td style="width: 265px; font-size: 15px;">Details of the Papers to be appeared:</td>
            <td style="width: 70px; font-size: 15px;"></td>
            <td style="width: 120px; font-size: 15px;">Subject&#58; N&#47;A</td>
            <td style="width: 120px; font-size: 15px;">Year&#58; <b>2015-16</b></td>
            <td style="width: 120px; font-size: 15px;">Department</td>
        </tr>
    </table>
    <table style="color: grey; width: 100%; margin:0px 0px 0px 10px;">
        <tr>
            <td style="width: 25%; font-size: 15px;">1. Paper-I</td>
            <td style="width: 25%; font-size: 15px;">2. Paper-II</td>
            <td style="width: 33%; font-size: 15px;">3. Paper-III(Viva-Voce)</td>
        </tr>
    </table>
    <table style="width: 100%;margin: 8px;">
        <tr style="height: 30px;">
            <td style="font-size: 15px;">4. Father&#39;s Email id&#58;</td>
            <td style="font-size: 15px;">Mother&#39;s Email id&#58;</td>
        </tr>
        <tr style="height: 30px;">
            <td style="font-size: 15px;">5. Fathers&#39;s Cell Ph&#35;&#58;</td>
            <td style="font-size: 15px;">Mother&#39;s Cell Ph&#35;&#58;</td>
        </tr>
    </table>
    <div style="margin:8px;font-size: 15px;">6.  Did the student appear for Junior Course Exam&#63; Yes or No (circle one)</div>
    <div style="margin:8px;font-size: 15px;">7.   Details of the Examinations Passed (for marks, refer to the portal)</div>
    <table style="width: 100%;border-collapse: collapse; padding-top: 3px; padding-left: 3px;">
        <tr style="height: 50px;">
            <th style="text-align: center;font-size: 15px;width: 25%;border: 1px solid black;">Name of the <br/> Examination</th>
            <th style="text-align: center;font-size: 15px; width: 25%;border: 1px solid black;">Name of the University &#47; Institution</th>
            <th style="text-align: center;font-size: 15px; width: 10%;border: 1px solid black;">Year of Pass</th>
            <th style="text-align: center;font-size: 15px; width: 35%;border: 1px solid black;">Pass details (Marks&#47; 100)&#58;Final aggregate score</th>
        </tr>
        <tr>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">Pravesam</td>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">SiliconAndhra ManaBadi</td>
            <td style="width: 10%;border: 1px solid black;font-size: 15px;"></td>
            <td style="width: 35%;border: 1px solid black;font-size: 15px;font-size: 15px;"></td>
        </tr>
        <tr>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">Prasunam</td>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">SiliconAndhra ManaBadi</td>
            <td style="width: 10%;border: 1px solid black;font-size: 15px;"></td>
            <td style="width: 35%;border: 1px solid black;font-size: 15px;"></td>
        </tr>
        <tr>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">Prakasam(Jr. Certificate)</td>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">SiliconAndhra ManaBadi</td>
            <td style="width: 10%;border: 1px solid black;font-size: 15px;"></td>
            <td style="width: 35%;border: 1px solid black;font-size: 15px;"></td>
        </tr>
        <tr>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">Pramodam </td>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">SiliconAndhra ManaBadi</td>
            <td style="width: 10%;border: 1px solid black;font-size: 15px;"></td>
            <td style="width: 35%;border: 1px solid black;font-size: 15px;"></td>
        </tr>
        <tr>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">Prabhasam (Sr. Certificate)</td>
            <td style="width: 25%;border: 1px solid black;font-size: 15px;">SiliconAndhra ManaBadi</td>
            <td style="width: 10%;border: 1px solid black;font-size: 15px;"></td>
            <td style="width: 35%;border: 1px solid black;font-size: 15px;"></td>
        </tr>
    </table>

    <div style="margin:8px;font-size: 15px; color:gray;">8.   Whether you have debarred/rusticated in            : NOT APPLICABLEEarlier public examinations, if so, furnish the details</div>
    <div style="margin:8px;font-size: 15px; color:gray;">9.   Whether you are appearing for any other Examination   : NOT APPLICABLE</div>
    <div style="padding-left:12px; font-size: 15px; color:gray;">Of the University / Other Universities along with this,<br/>If so, what examinations</div>
    <div style="margin:8px;font-size: 15px; color:gray;">10.   Permanent Address: Not Applicable</div>
    <br/><br/>
        <div style=" font-size: 15px; text-align: center; margin: 11px 0px 0px 5px;"><b><u>DECLARATION OF THE CANDIDATE</u></b></div>
        <div style="text-align:center">I do hereby declare that the above particulars furnished by me are true and correct to the best of my knowledge. </div>
                <br/>
        <div>Place &#58;</div>
        <br/>
        <table>
            <tr>
                <td style="width:65%">Date &#58;</td>
                <td style="width:35%"><i>Signature of the Student</i></td>
            </tr>
        </table>
        <br/><br/><br/>
        <div style=" font-size: 15px; text-align: center; margin: 11px 0px 0px 5px;"><b><u>CERTIFICATE BY THE HEAD OF THE DEPARTMENT/PRINCIPAL</u></b></div>
        <div>This is to certify that the above candidate is a regular student of this Institution during the year 
        2015  -  2016. His/her character is good and the facts mentioned by him/her in the application form have been verified 
        and found to be correct. He/She has appeared/not appeared before for this Examination in the year 201______ from this 
        Institution with Roll No. _______________.
        </div>
<br/><br/><br/>
        <table>
            <tr>
                <td style="width:65%">Dated &#58;___________20</td>
                <td style="width:35%"><i>Signature of the Institution</i></td>
            </tr>
            <tr>
                <td style="width:65%"></td>
                <td style="width:35%"><i> (with Office Seal)</i></td>
            </tr>
        </table>
    </body>
</html>"""
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
