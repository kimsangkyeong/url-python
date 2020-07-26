from urllib.request import urlopen
import bs4

#url = "https://www.naver.com"
#html = urlopen(url)

#html_str = html.read()
# print(html_str)

# ex1
html_str = "<html><div>hello</div></html>"
print("ex1 : ", html_str)
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find("div"))

# ex2
html_str = """
<html>
  <body>
    <ul>
      <li>hello</li>
      <li>bye</li>
      <li>welcome</li>
    </ul>
  </body>
</html>
"""
print("ex2 : ", html_str)
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

print(bs_obj.find("ul"))

# ex3
print("ex3 : ", html_str)
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul")
li = ul.find("li")
print(li, "....", "li.text:", li.text)

# ex4
print("ex4 : ", html_str)
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul")
li = ul.findAll("li")
print(li)

#ex5
html_str = """
<html>
  <body>
    <ul class="greet">
      <li>hello</li>
      <li>bye</li>
      <li>welcome</li>
    </ul>
    <ul class="reply">
      <li>ok</li>
      <li>no</li>
      <li>sure</li>
    </ul>
  </body>
</html>
"""
print("ex5 : ", html_str)
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul", {"class":"reply"})
print(ul)