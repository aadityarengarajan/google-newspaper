from datetime import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup
import random

def news(q):
    prehtml='''
<html>
<head>
    <link href='https://fonts.googleapis.com/css?family=Playfair+Display:400,700,900,400italic,700italic,900italic|Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="styles/newspaper.css">
    <title>Newspaper Style Design Experiment</title>
    <meta name="viewport" content="width=device-width">
    <style>
        body{
            font-family: 'Droid Serif', serif;
            font-size: 14px;
            color: #2f2f2f;
            background-color: #f9f7f1;
        }
        header{
            font-family: 'Playfair Display', serif;
            font-weight: 900;
            font-size: 80px;
            text-transform: uppercase;
            display: inline-block;
            line-height: 72px;
            margin-bottom: 20px;

        }
        p{
            margin-top: 0;
            margin-bottom: 20px;
        }
        .head{
            text-align: center;
            position: relative;


        }

        .headerobjectswrapper{
        }

        .subhead{
            text-transform: uppercase;
            border-bottom: 2px solid #2f2f2f;
            border-top: 2px solid #2f2f2f;
            padding: 12px 0 12px 0;

        }
        .weatherforcastbox{
            position: relative;
            width: 12%;
            left: 10px;
            border: 3px double #2f2f2f;
            padding: 10px 15px 10px 15px;
            line-height: 20px;
            display: inline-block;
            margin: 0 50px 20px -360px;
        }
        .content{
            font-size: 0;
            line-height: 0;
            word-spacing: -.31em;
            display: inline-block;
            margin: 30px 2% 0 2%;


        }
        .collumns{

        }

        .collumn{
            font-size: 14px;
            line-height: 20px;
            width: 17.5%;
            display: inline-block;
            padding: 0 1% 0 1%;
            vertical-align: top;
            margin-bottom: 50px;
            transition: all .7s;
        }
        .collumn + .collumn { 
          border-left: 1px solid #2f2f2f;
        }
        .collumn .headline{
            text-align: center;
            line-height: normal;
            font-family: 'Playfair Display', serif;
            display: block;
            margin: 0 auto;


        }
        .collumn .headline.hl1{
            font-weight: 700;
            font-size: 30px;
            text-transform: uppercase;
            padding: 10px 0 10px 0;

        }

        .collumn .headline.hl2{
            font-weight: 400;
            font-style: italic;
            font-size: 24px;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }

        .collumn .headline.hl2:before{
            border-top: 1px solid #2f2f2f;
            content: '';
            width: 100px;
            height: 7px;
            display: block;
            margin: 0 auto;
        }
        .collumn .headline.hl2:after{
            border-bottom: 1px solid #2f2f2f;
            content: '';
            width: 100px;
            height: 13px;
            display: block;
            margin: 0 auto;

        }

        .collumn .headline.hl3{
            font-weight: 400;
            font-style: italic;
            font-size: 36px;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }
        .collumn .headline.hl4{
            font-weight: 700;
            font-size: 12px;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }
        .collumn .headline.hl4:before{
            border-top: 1px solid #2f2f2f;
            content: '';
            width: 100px;
            height: 7px;
            display: block;
            margin: 0 auto;
        }
        .collumn .headline.hl4:after{
            border-bottom: 1px solid #2f2f2f;
            content: '';
            width: 100px;
            height: 10px;
            display: block;
            margin: 0 auto;

        }

        .collumn .headline.hl5{
            font-weight: 400;
            font-size: 42px;
            text-transform: uppercase;
            font-style: italic;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }
        .collumn .headline.hl6{
            font-weight: 400;
            font-size: 18px;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }
        .collumn .headline.hl6:before{
            border-top: 1px solid #2f2f2f;
            content: '';
            width: 100px;
            height: 7px;
            display: block;
            margin: 0 auto;
        }
        .collumn .headline.hl6:after{
            border-bottom: 1px solid #2f2f2f;
            content: '';
            width: 100px;
            height: 10px;
            display: block;
            margin: 0 auto;

        }
        .collumn .headline.hl7{
            font-weight: 700;
            font-size: 12px;
            box-sizing: border-box;
            display: block;
            padding: 10px 0 10px 0;
        }
        .collumn .headline.hl8{
            font-weight: 700;
            font-size: 12px;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }
        .collumn .headline.hl9{
            font-weight: 700;
            font-size: 12px;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }
        .collumn .headline.hl10{
            font-weight: 700;
            font-size: 12px;
            box-sizing: border-box;
            padding: 10px 0 10px 0;
        }
        .collumn .citation{
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            line-height: 44px;
            /*font-style: italic;*/
            text-align: center;
            font-weight: 400;
            display: block;
            margin: 40px 0 40px 0;
            font-feature-settings: "liga", "dlig";

        }
        .collumn .citation:before{
            border-top: 1px solid #2f2f2f;
            content: '';
            width: 100px;
            height: 16px;
            display: block;
            margin: 0 auto;
        }
        .collumn .citation:after{
            border-bottom: 1px solid #2f2f2f;
            content: '';
            width: 100px;
            height: 16px;
            display: block;
            margin: 0 auto;
        }
        .collumn .figure {
              margin: 0 0 20px;
        }
        .collumn .figcaption{
            font-style: italic;
            font-size: 12px;
        }
        .media {
            -webkit-filter: sepia(80%) contrast(1) opacity(0.8);
            filter: sepia(80%) grayscale(1) contrast(1) opacity(0.8);
            mix-blend-mode: multiply;
            width: 100%;
        }
        /*________________________________________________________________________________________________________________________________*/
        /*MEDIAQUERIES*/
        @media only all and (max-width: 1300px) {
            .weatherforcastbox{
                display: none;
            }

        }
        @media only all and (max-width: 1200px) {
            .collumn{
                width: 31%;
            }

        }
            @media only all and (max-width: 900px) {
            .collumn{
                width: 47%;
            }

        }
        @media only all and (max-width: 600px) {
            .collumn{
                width: 100%;
            }
            .collumn + .collumn {
                        border-left: none;
                border-bottom: 1px solid #2f2f2f;
            }
            header{
                max-width: 320px;
                font-size: 60px;
                line-height: 54px;
                overflow: hidden;
            }

        }
    </style>
</head>'''+f'''
<body>
<div class="head">
    <div class="headerobjectswrapper">
        <header>{q} NEWS</header>
    </div>

    <div class="subhead">TOP HEADLINES - {datetime.now().strftime('%d/%m/%Y')}</div>
</div>
<div class="content">
    <div class="collumns">
'''
    if q=='':
        url="https://news.google.co.in/"
    else:
        url=f"https://news.google.com/search?q={q}&hl=en-IN&gl=IN&ceid=IN%3Aen"
    code=requests.get(url)
    soup=BeautifulSoup(code.text,'html5lib')
    htmllines=[prehtml]
    for title in soup.find_all('span',class_="xBbh9"):
        a=f'''<div class="collumn">
            <div class="head"><span class="headline hl{random.randint(1,4)}">{title}</span></div>
        </div>'''
        htmllines.append((a.replace('hl4','hl2')).replace('hl1','hl3'))
    posthtml='''    </div>
</div>

</body>
</html>'''
    htmllines.append(posthtml)
    newshtml=open('news.html','w')
    newshtml.writelines(htmllines)
    newshtml.close()
    webbrowser.open_new_tab('news.html')
