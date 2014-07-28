from collections import defaultdict

output = open("output.css", "w")
result = defaultdict(set)
no_boder = "{border-radius: 0px !important;-webkit-border-radius: 0px !important;-moz-border-radius: 0px !important;}"
output.write("*" + no_boder)
target_css_attributes_dict = {
                              #   "border-radius": no_boder,
                              # "border-top": no_boder,
                              # "border-bottom": no_boder,
                              "box-shadow": "{box-shadow:none !important}",
                              "-webkit-linear-gradient" : "{background-image: none !important}"
                              }

with open("github.css", "r") as f:
    for line in f:
        line = line.rstrip()
        if line.endswith("{") and not line.startswith(" ")\
                             and not line.startswith("::")\
                             and not line.startswith("@"):
            target_list = line[:-1].split(",")
        elif line.endswith("}"):
            target_list = []
        else:
            for attribute in target_css_attributes_dict:
                if attribute in line:
                    result[attribute] |= set(target_list)

for key in result:
    string = ",".join(result[key]) + target_css_attributes_dict[key]
    output.write(string)

output.close()