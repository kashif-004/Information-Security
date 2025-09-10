sample_dict = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"new york",

}

new_dict={}

keys_to_extract = {"name","salary"}

for keys in sample_dict:
    if keys in keys_to_extract:
        new_dict[keys] = sample_dict[keys]

print(new_dict)