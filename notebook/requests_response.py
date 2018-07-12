import requests

url = 'https://example.com/'

response = requests.get(url)

print(response)
# <Response [200]>

print(type(response))
# <class 'requests.models.Response'>

print(response.url)
# https://example.com/

print(response.status_code)
# 200

print(response.headers)
# {'Content-Encoding': 'gzip', 'Accept-Ranges': 'bytes', 'Cache-Control': 'max-age=604800', 'Content-Type': 'text/html', 'Date': 'Thu, 12 Jul 2018 11:58:54 GMT', 'Etag': '"1541025663"', 'Expires': 'Thu, 19 Jul 2018 11:58:54 GMT', 'Last-Modified': 'Fri, 09 Aug 2013 23:54:35 GMT', 'Server': 'ECS (oxr/8313)', 'Vary': 'Accept-Encoding', 'X-Cache': 'HIT', 'Content-Length': '606'}

print(type(response.headers))
# <class 'requests.structures.CaseInsensitiveDict'>

print(response.headers['Content-Type'])
# text/html

print(response.headers['content-type'])
# text/html

print(response.headers['cOntEnt-typE'])
# text/html

# print(response.headers['xxxxx'])
# KeyError: 'xxxxx'

print(response.headers.get('xxxxx'))
# None

print(response.encoding)
# ISO-8859-1

print(response.text)
# <!doctype html>
# <html>
# <head>
#     <title>Example Domain</title>
# 
#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
#         
#     }
#     div {
#         width: 600px;
#         margin: 5em auto;
#         padding: 50px;
#         background-color: #fff;
#         border-radius: 1em;
#     }
#     a:link, a:visited {
#         color: #38488f;
#         text-decoration: none;
#     }
#     @media (max-width: 700px) {
#         body {
#             background-color: #fff;
#         }
#         div {
#             width: auto;
#             margin: 0 auto;
#             border-radius: 0;
#             padding: 1em;
#         }
#     }
#     </style>    
# </head>
# 
# <body>
# <div>
#     <h1>Example Domain</h1>
#     <p>This domain is established to be used for illustrative examples in documents. You may use this
#     domain in examples without prior coordination or asking for permission.</p>
#     <p><a href="http://www.iana.org/domains/example">More information...</a></p>
# </div>
# </body>
# </html>
# 

print(type(response.text))
# <class 'str'>

print(response.content)
# b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 50px;\n        background-color: #fff;\n        border-radius: 1em;\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        body {\n            background-color: #fff;\n        }\n        div {\n            width: auto;\n            margin: 0 auto;\n            border-radius: 0;\n            padding: 1em;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is established to be used for illustrative examples in documents. You may use this\n    domain in examples without prior coordination or asking for permission.</p>\n    <p><a href="http://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'

print(type(response.content))
# <class 'bytes'>

print(response.content.decode(response.encoding) == response.text)
# True
