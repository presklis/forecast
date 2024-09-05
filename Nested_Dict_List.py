import json

try:
    with open('network.json', 'r') as file:
    network = json.load(file)
except FileNotFoundError:
    network = {}
except json.JSONDecodeError:
    network = {}

network = {
"Region_A": {
"altens": {
"Van_Fill": {
"1": 12.1,
"2": 12.2
},
"Site_Shared": {
"1": 0.09,
"2": 0.08
}
},
"killingworth": {
"Van_Fill": {
"1": 12.1,
"2": 12.2
},
"Site_Shared": {
"1": 0.09,
"2": 0.08
}
}
}
}

def show_van_fill(network_dictionery, site_name):
    output = ""
    for region in network_dictionery:
        output += f"\n{region.title()}\n"
        for site in network_dictionery[region]:
            if site == site_name:
                output += f"{site.title()}\n"
                if "Van_Fill" in network_dictionery[region][site]:
                    output += "Van Fill\n"
                    for week, value in network_dictionery[region][site]["Van_Fill"].items():
                        output += f"WK{week}: {value}\n"
                        return output

def main():
    branch = pyscript.interpreter.globals.get('branch')
    output = show_van_fill(network, branch)
    document.getElementById('output').innerText = output
