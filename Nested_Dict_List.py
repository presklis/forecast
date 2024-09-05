# nested dictionaries with lists

# online_profile = {
#     "name" : "Presk",
#     "surname" : "Lis",
#     "gender" : "Male",
#     "list_of_friends" : ['Paul','Nick','Abdul','John']
#     }
# 
# print(online_profile.items())
# 
# print("My friends:")
# 
# if isinstance(online_profile["list_of_friends"],list):
#     for item in online_profile["list_of_friends"]:
#         print(item)

import json

try:
    with open('network.json', 'r') as file:
        network = json.load(file)
except FileNotFoundError:
    network = {}
except json.JSONDecodeError:
    network = {}

network = {
  "Region_A" : {
    "altens": {
      "Van_Fill" : {
          "1" : 12.1,
          "2" : 12.2
          },
      "Site_Shared" : {
        "1" : 0.09,
        "2" : 0.08
        }
      },
    "killingworth": {
      "Van_Fill" : {
          "1" : 12.1,
          "2" : 12.2
          },
      "Site_Shared" : {
        "1" : 0.09,
        "2" : 0.08
        }
      }
    }
  }

def show_van_fill(network_dictionery,site_name):
    for region in network_dictionery:
        print()
        print(region.title())
        for site in network_dictionery[region]:
            if site == site_name:
                print(site.title())
                if "Van_Fill" in network_dictionery[region][site]:
                    print("Van Fill")
                    for week,value in network_dictionery[region][site]["Van_Fill"].items():
                        print(f"WK{week}:{value}")
        

def display_menu():
    print("Menu\n")
    print("1. Show Van Fill\n")
    print("2. Exit\n")

def main():
    while True:
        display_menu()
        choice = input("Please select a valid option from the menu\n")
        if choice == '1':
            branch = input("please input the branch name ").lower()
            show_van_fill(network,branch)
            print()
        elif choice == '2':
            print("Goodbye")
            break
        else:
            print("Invalid choice, please select again")

if __name__ == "__main__":
    print("Welcome JL user\n")
    main()
