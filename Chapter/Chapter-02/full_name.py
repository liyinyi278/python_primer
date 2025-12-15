first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print(favorite_language.rstrip())

nostarch_url = 'https://nostarch.com/'
simple_url = nostarch_url.removeprefix('https://') 
print(simple_url)

message = 'One of Python\'s strengths is its diverse community.'
print(message)