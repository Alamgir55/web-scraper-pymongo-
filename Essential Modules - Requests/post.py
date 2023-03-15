import requests

my_data = {"name": "Nick", "email": "nick99@gmail.com"}

r = requests.post(
    "https://tryphp.w3schools.com/showphp.php?filename=demo_form_get", data=my_data)

f = open("myfile.html", "w+")
f.write(r.text)
