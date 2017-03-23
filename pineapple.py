#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import StringIO
from flask import Flask, send_file

from xhtml2pdf import pisa


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/pdf/')
def hello_pdf():
    pisa.showLogging()

    packet = StringIO.StringIO()

    sourcehtml = u"""<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body style="width: 100%; font-family: Times, serif;">

<!-- <style>
    .collapes_row1{
        padding-top:-20px;
    }
    .collapes_row2{
        padding-top:-10px;
    }
    .collapes_row3{
        display:none;
    }
</style> -->

<table style="width: 100%;">
    <tr>
        <td rowspan="4" style=" width:20%;"><img height="240px" width="240px" src="./image01.png"></td>
        <td style="text-align: center; font-family: Times, serif; font-size: 17px; font-weight: bold; width:60%;">POTTI SREERAMULU TELUGU UNIVERSITY</td>
        <td rowspan="4" style="width:20%;"><img height="220px" width="240px" src="./image03.png"></td>
    </tr>
    <tr>
        <td style="text-align: center; font-size: 17px; width:60%">M.V.K.R. INTERNATIONAL TELUGU CENTRE</td>
     </tr>
    <tr>
        <td style="text-align: center;font-size: 14px; width:60%">Public Gardens, Hyderabad - 500 004 Andhra Pradesh, India</td>
    </tr>
    <tr>
        <td style="text-align: center; font-size: 14px; width:60%">Ph &#58; 040 - 2323 4490 Fax &#58; 040 - 2323 6045 e-mail &#58; itc@teluguuniversity.ac.in</td>
    </tr>    
</table>

<div style="text-align: center; font-size: 17px; font-weight: bold; width:100%">CERTIFICATE COURSE IN TELUGU (Four Years) - 2015  - 2016</div>
<div style="text-align: center; font-size: 17px; font-weight: bold; width:60%">(SILICONANDHRA - MANABADI)</div>

 <hr>
    <div style="font-size: 15px; font-weight: bold;">Sr. No.&#58;</div>
    <div style="text-align: center; font-size: 28px; font-weight: bold;">Student Registration Application Form</div>
    <br/>
    <table style="width: 100%; font-size: 14px;">
        <tr>
            <td style="width: 4%;">1.</td>
            <td style="width: 42%;"></td>
            <td style="width: 48%;">&#58; Silicon Andhra ManaBadi</td>
        </tr>
        <tr>
            <td style="width: 4%; "></td>
            <td style="width: 42%;" class="collapes_row1">Name of the Institution & Address</td>
            <td style="width: 48%; ">7912 August Lane, Cupertino CA 95014, USA</td>
        </tr>
    </table>
    <br/><br/>
    <table style="width: 100%; font-size: 14px;">
        <tr>
            <td style="width: 5%;">2.</td>
            <td style="width: 37%;"></td>
            <td style="width: 10%; ">&#58; STATE&#58;</td>
            <td style="width: 25%; border-bottom: 1px solid black; ">{{state}}</td>
            <td style="width: 20%;"></td>
        </tr>
    </table>
    <table style="width: 100%; font-size: 14px;">
        <tr style="padding-top:3px;">
            <td style="width: 5%;"></td>
            <td style="width: 40%;" class="collapes_row1">Name of the Country & State</td>
            <td style="width: 11%;">COUNTRY&#58;</td>
            <td style="width: 25%; border-bottom: 1px solid black; ">{{country}}</td>
            <td style="width: 24%;"></td>
        </tr>
    </table>

    <br/>
    <table style="width: 100%; font-size: 14px;">
        <tr>
            <td style="width: 5%; ">3.</td>
            <td style="width: 45%; "></td>
            <td style="width: 50%; "></td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 45%;" class="collapes_row1">Affiliation details</td>
            <td style="width: 50%;">{{&#58;N/A}}</td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 45%;" class="collapes_row1">(Mention affiliation number and year)</td>
        </tr>
    </table>

    <table style="width: 100%; font-size: 14px; margin-top:12px;">
        <tr>
            <td style="width: 5%;">4.</td>
            <td style="width: 40%;"></td>
            <td style="width: 1%;">&#58;{{last_name}}{{first_name}}{{middle_name}}</td>
            <td style="width: 54%;  border-bottom: 1px solid black; "></td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 40%;" class="collapes_row1">Name of the Candidate in Full</td>
            <td style="width: 1%;"></td>
            <td style="width: 54%; padding-top:3px;" class="collapes_row1">(Last Name, First Name and Middle Name)</td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 40%;" class="collapes_row1">(CAPITAL LETTERS)</td>
            <td style="width: 1%;"></td>
            <td style="width: 54%;"></td>
        </tr>
    </table>

    <table style="width: 100%; font-size: 14px; margin-top:12px;">
        <tr>
            <td style="width: 5%;">5.</td>
            <td style="width: 40%;"></td>
            <td style="width: 1%;">&#58;</td>
            <td style="width: 53%; border-bottom: 1px solid black; ">{{father_lastname}}{{father_firstname}}</td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 40%;" class="collapes_row1">Father&#39;s  Husband&#39;s Name</td>
            <td style="width: 1%;"></td>
            <td style="width: 53%; padding-top:3px;">(Last Name, First Name)</td>
        </tr>
    </table>

    <table style="width: 100%; font-size: 14px; margin-top:12px;">
        <tr>
            <td style="width: 5%; ">6.</td>
            <td style="width: 40%; "> </td>
            <td style="width: 20%; border-bottom: 1px solid black;"> &#58; {{date_birth}}</td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 40%; " class="collapes_row2">Candidate&#39;s Date of Birth & Age </td>
            <td style="width: 20%;"></td>
        </tr>
    </table>

    <table style="width: 100%; font-size: 14px; margin-top:12px;">
        <tr>
            <td style="width: 5%; ">7.</td>
            <td style="width: 40%; "></td>
            <td style="width: 48%; "></td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 40%; " class="collapes_row2">Affiliation details</td>
            <td style="width: 48%; " class="collapes_row2">&#58;{{N/A}}</td>
        </tr>
    </table>

    <table style="width: 100%; font-size: 14px; margin-top:15px; padding-top:3px;">
        <tr>
            <td style="width: 5%;">8.</td>
            <td style="width: 40%;"></td>
            <td style="width: 8%;">&#58;Address&#58;</td>
            <td style="width: 47%; border-bottom: 1px solid black;"> {{address}}</td>
        </tr>
        <tr>
            <td style="width: 5%;"></td>
            <td style="width: 41%;" class="collapes_row1">Current Address  Email</td>
            <td style="width: 8%;"></td>
            <td style="width: 46%; border-bottom: 1px solid black;">{{address}}</td>
        </tr>
        <tr>
            <td style="width: 5%;"></td>
            <td style="width: 41%;"></td>
            <td style="width: 8%;">Email&#58;</td>
            <td style="width: 46%; border-bottom: 1px solid black;">{{email}}</td>
        </tr>
        <tr>
            <td style="width: 5%;"></td>
            <td style="width: 41%;"></td>
            <td style="width: 8%;">Phone&#58;</td>
            <td style="width: 46%; border-bottom: 1px solid black;">{{phone}}</td>
        </tr>
    </table>

    <table style="width: 100%; font-size: 14px; margin-top:20px;">
        <tr>
            <td style="width: 5%; ">9.</td>
            <td style="width: 41%; "></td>
            <td style="width: 48%; ">&#58;{{N/A}}</td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 41%; " class="collapes_row2">Mother tongue </td>
            <td style="width: 48%; "></td>
        </tr>
    </table>
<br>
    <table style="width: 100%; font-size: 14px;">
        <tr>
            <td style="width: 5%; ">10.</td>
            <td style="width: 41%; "></td>
            <td style="width: 48%; ">&#58;{{N/A}}</td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 41%; " class="collapes_row2">Nationality</td>
            <td style="width: 48%; "></td>
        </tr>
    </table>

    <br/><br/>
    <table style="width: 100%; font-size: 14px;">
        <tr>
            <td style="width: 5%; ">11.</td>
            <td style="width: 41%; "></td>
            <td style="width: 48%; ">&#58;{{N/A}}</td>
        </tr>
        <tr>
            <td style="width: 5%; "></td>
            <td style="width: 41%; " class="collapes_row2">Please tick (&#10004;) the appropriate column</td>
            <td style="width: 48%; "></td>
        </tr>
    </table>
    <table style="width: 60%; font-size: 14px;">
        <tr>
            <td style="width: 5%;"></td>
            <td style="width: 10%; color:white">1</td>
            <td style="width: 10%; text-align:center; border:1px solid black; width:20px; height:8px"></td>
            <td style="width: 10%; "></td>
            <td style="width: 10%; text-align:center; border:1px solid black; width:20px; height:8px"</td>
            <td style="width: 10%; "></td>
            <td style="width: 10%; text-align:center; border:1px solid black; width:20px; height:8px"></td>
            <td style="width: 10%; "></td>
            <td style="width: 10%; text-align:center; border:1px solid black; width:20px; height:8px"></td>
        </tr>
        <tr>
            <td style="width: 5%;"></td>
            <td style="width: 10%; text-align:center;" class="collapes_row2">Male</td>
            <td style="width: 10%; text-align:center; width:20px; height:8px"></td>
            <td style="width: 10%; text-align:center;" class="collapes_row2">Female</td>
            <td style="width: 10%; text-align:center; width:20px; height:8px"</td>
            <td style="width: 10%; text-align:center;" class="collapes_row2">Married</td>
            <td style="width: 10%; text-align:center; width:20px; height:8px"></td>
            <td style="width: 10%; text-align:center;" class="collapes_row2">Unmarried</td>
            <td style="width: 10%; text-align:center; width:20px; height:8px"></td>
        </tr>
    </table>
    <table style="width: 60%; font-size: 14px;">
        <tr>
            <td style="width: 5%;"></td>
            <td style="width: 15%; color:white">1</td>
            <td style="width: 10%; text-align:center; border:1px solid black; width:20px; height:8px"></td>
            <td style="width: 10%; "></td>
            <td style="width: 10%; text-align:center; border:1px solid black; width:20px; height:8px"</td>
            <td style="width: 10%; "></td>
            <td style="width: 10%; text-align:center; border:1px solid black; width:20px; height:8px"></td>
        </tr>
        <tr>
            <td style="width: 5%;"></td>
            <td style="width: 15%; text-align:center;" class="collapes_row2">Phy. Handicapped</td>
            <td style="width: 10%; text-align:center; width:20px; height:8px"></td>
            <td style="width: 10%; text-align:center;" class="collapes_row2">Urban</td>
            <td style="width: 10%; text-align:center; width:20px; height:8px"</td>
            <td style="width: 10%; text-align:center;" class="collapes_row2">Rural</td>
            <td style="width: 10%; text-align:center; width:20px; height:8px"></td>
        </tr>
    </table>
<br/><br/>
    <table style="width: 100%; font-size: 14px;">
        <tr>
            <td style="width: 5%;">12.</td>
            <td style="width: 40%;"></td>
            <td style="width: 55%;">&#58;</td>
        </tr>
        <tr>
            <td style="width: 5%;"></td>
            <td style="width: 50%;" class="collapes_row2">Educational Qualifications</td>
            <td></td>
        </tr>
    </table>

    <table style=" width:50%; font-size: 14px; padding-top:2px;">
        <tr style=" ">
            <td rowspan="6" style="border: 1px solid transparent; width:5%;"></td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center;">Name Of <br/> the Course</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Name of the <br/> University</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Month & Year <br/> of Pass</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Second <br/> Language</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Optional Subjects</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Percentage <br/> of Marks <br/>(Out of 100)</td>
        </tr>
        <tr style="">
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Pravesam</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">SiliconAndhra ManaBadi</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
        </tr>
        <tr style=" ">
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Prasunam</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">SiliconAndhra ManaBadi</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
        </tr>
        <tr style="  ">
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Prakasam</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">SiliconAndhra ManaBadi</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
        </tr>
        <tr style=" ">
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Pramodam</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">SiliconAndhra ManaBadi</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
        </tr>
        <tr style="">
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">Prabhasam</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">SiliconAndhra ManaBadi</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center">N/A</td>
            <td style=" border: 1px solid black; border-collapse: collapse; text-align: center"></td>
        </tr>
    </table>
<br/><br/>
    <div style="font-size: 15px;">I hereby declare that the above particulars are true to the best of my knowledge and belief. In case of any defect 
    or false information found in the above particulars, of a later date, the University can take disciplinary action against
    me. I solemnly pledge to follow the rules and regulations stipulated by the University from time to time.</div>

<br/><br/>
    <table style="font-size: 17px; width:100%;">
        <tr>
            <td style="width:7%"></td>
            <td style="width:63%;">:</td>
            <td style="width:30%">{{sign}}</td>
        </tr>
        <tr>
            <td style="width:7%">Date</td>
            <td style="width:63%;">: {{date}}</td>
            <td style="width:30%">Signature of the Student</td>
        </tr>
    </table>
<br/>
<br/>
<br/><br/><br class="collapes_row3"/><br class="collapes_row3"/>
    <table style="font-size: 17px;">
        <tr>
            <td style="margin-left:50px;">{{}}</td>
            <td style="text-align:center">{{director_sign}}}</td>
        </tr>
        <tr>
            <td>Signature of the Institution </td>
            <td style="text-align:center">Director</td>
        </tr>
        <tr>
            <td style="margin-left:50px;">With Seal   </td>
            <td style="text-align:center">M.V.K.R. International Telugu Centre</td>
        </tr>
        <tr>
            <td></td>
            <td style="text-align:center">P.S. Telugu University</td>
        </tr>
    </table>
<br/>
<br/>
<br/><br/><br class="collapes_row3" /><br class="collapes_row3"/><br class="collapes_row3"/><br class="collapes_row3"/><br class="collapes_row3"/><br class="collapes_row3"/><br class="collapes_row3"/>

<div style="text-align:center; font-size: 21px;"><b>Rules & Regulations</b></div>
<ol style="font-size: 16px;">
    <li><br class="collapes_row3"/>Incomplete applications will be summarily rejected.</li>
    <li><br class="collapes_row3"/>Any false information furnished by the candidate and or if the information 
    furnished not in accordance with the rules and regulations, stipulate therein the admission is liable for cancellation.<l/i>
    <li><br class="collapes_row3"/> The following shall be enclosed with the application
        <br/>Affix latest passport size photograph, in the specified place and enclose an extra photograph for office use.
        <br/>b)<br class="collapes_row3"/>A set of Xerox copies of S.S.C. Marks Statement or your Education Qualifications.
    </li>
    <li>The application, duly filled-in, along with the necessary enclosures, should be sent to the 
    <b>Director I/c, M.V.K.R. International Telugu Centre, Potti Sreeramulu Telugu University, Public Gardens, Hyderabad - 500 004 </b>
    through your Institution Secretary or Academic Secretary</li>
</ol>
<br/><br class="collapes_row3"/><br class="collapes_row3"/><br class="collapes_row3"/>
<div style="text-align:center; font-size: 21px;">- - o - - </div>
</body>
</html>"""
    pisa.CreatePDF(sourcehtml.encode('utf-8'),
        dest=packet, encoding = 'utf-8', debug=True)

    packet.seek(0)
    return send_file(packet, attachment_filename="willi.pdf", as_attachment=False)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
