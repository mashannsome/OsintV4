from jinja2 import Template

def save(data):
    html = Template(open("reports/index.html").read()).render(data=data)
    open("reports/report.html","w").write(html)
