

def print_name():
    print("Brett Bryant")


def test_dict():
    print("-------- Dictionary---------")

    me = {
        "first": "Brett",
        "last": "Bryant",
        "age": 35,
        "hobbies": [],
        "address": {
            "street": "evergreen",
            "city": "springfield"
        }
    }

    print(me["first"] + " " + me["last"])

    address = me["address"]
    print(address["street"] + " " + address["city"])


print_name()
test_dict()
