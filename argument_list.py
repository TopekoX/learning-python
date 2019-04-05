# gunanya untuk memasukan property bisa lebih dari satu dengan perintah **

def create_html(tag, text, **attribute):
    html = f"<{tag}"

    for key, value in attribute.items():
        html  = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html

html = create_html("p","Hello Python", style="paragraf")
print(html)
html = create_html("a", "ini link", href="www.google.com", style="link")
print(html)