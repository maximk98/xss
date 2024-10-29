import html
xss = "<script type = 'text/javascript'> alert('This XXS!!!'); </script>"
print(html.escape(xss))
