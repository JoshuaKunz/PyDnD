class HTML:
    htmlStr = ""
    QUOTE = "\""

    def start_html():
        HTML.htmlStr += """
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Document</title>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>

</head>"""

    def end_html():
        HTML.htmlStr += "</html>"

    def text(text):
        HTML.htmlStr += text

    def body(close=False):
        if close:
            HTML.htmlStr += "</body>"
            return
        HTML.htmlStr += "<body>"

    def div(cls="", id="", close=False):
        if close:
            HTML.htmlStr += "</div>"
            return
        cls = "class=" + HTML.QUOTE + cls + HTML.QUOTE
        id = "id=" + HTML.QUOTE + id + HTML.QUOTE
        HTML.htmlStr += '<div {} {}>'.format(cls, id)

    def head(close=False):
        if close:
            HTML.htmlStr += "</head>"
            return
        HTML.htmlStr += "<head>"

    def p(cls="", close=False):
        if close:
            HTML.htmlStr += "</p>"
        else:
            HTML.htmlStr += "<p class=\"{}\">".format(cls)

    def h1(close=False):
        if close:
            HTML.htmlStr += "</h1>"
        else:
            HTML.htmlStr += "<h1>"

    def h4(cls="", text=""):
        HTML.htmlStr += "<h4 class=\"{}\">{}</hr>".format(cls,text)
        
    def table(cls="", close=False):
        if close:
            HTML.htmlStr += "</table>"
        else:
            HTML.htmlStr += "<table class=\"{}\">".format(cls)
    
    def thead(cls="", close=False):
        if close:
            HTML.htmlStr += "</thead>"
        else: 
            HTML.htmlStr += "<thead class=\"{}\">".format(cls)
    
    def tr(cls="", close=False):
        if close:
            HTML.htmlStr += "</tr>"
        else:
            HTML.htmlStr += "<tr class=\"{}\">".format(cls)

    def th(cls="", scope="", text="", header_font=False):
        if not header_font:
            HTML.htmlStr += "<th class=\"{}\" scope=\"{}\">{}</th>".format(cls, scope, text)
        else:
            HTML.htmlStr += "<th class=\"{}\" scope=\"{}\"><h4>{}</th>".format(cls, scope, text)
    def tbody(cls="", close=False):
        if close:
            HTML.htmlStr += "</tbody>"
        else:
            HTML.htmlStr += "<tbody class=\"{}\">".format(cls)

    def td(cls="", text=""):
        HTML.htmlStr += "<td class=\"{}\">{}</td>".format(cls, text)