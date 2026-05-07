states = {

    "andhra pradesh": {
        "formed": "1956",
        "named_by": "Named after Andhra region and Pradesh means state",
        "capital": "Amaravati",

        "places": [
            "Tirupati",
            "Araku Valley",
            "Vizag Beach",
            "Amaravati"
        ]
    },

    "telangana": {
        "formed": "2014",
        "named_by": "Telangana word came from Telugu Angana",
        "capital": "Hyderabad",

        "places": [
            "Charminar",
            "Golconda Fort",
            "Ramoji Film City",
            "Warangal"
        ]
    },

    "karnataka": {
        "formed": "1956",
        "named_by": "Derived from Karunadu meaning elevated land",
        "capital": "Bangalore",

        "places": [
            "Mysore Palace",
            "Coorg",
            "Hampi",
            "Bangalore Palace"
        ]
    },
     
        "tamil nadu": {
        "formed": "1956",
        "named_by": "Tamil people land",
        "capital": "Chennai",

        "places": [
            "Marina Beach",
            "Ooty",
            "Meenakshi Temple",
            "Kodaikanal"
        ]
    },

    "kerala": {
        "formed": "1956",
        "named_by": "Derived from Kera meaning coconut",
        "capital": "Thiruvananthapuram",

        "places": [
            "Munnar",
            "Alleppey",
            "Kochi",
            "Wayanad"
        ]
    },

    "maharashtra": {
        "formed": "1960",
        "named_by": "Derived from Maha meaning great and Rashtra meaning nation",
        "capital": "Mumbai",

        "places": [
            "Gateway of India",
            "Lonavala",
            "Ajanta Ellora Caves",
            "Shirdi"
        ]
    },

    "goa": {
        "formed": "1987",
        "named_by": "Derived from ancient Sanskrit word Gomantak",
        "capital": "Panaji",

        "places": [
            "Baga Beach",
            "Calangute Beach",
            "Dudhsagar Falls",
            "Fort Aguada"
        ]
    },

    "gujarat": {
        "formed": "1960",
        "named_by": "Named after Gurjara people",
        "capital": "Gandhinagar",

        "places": [
            "Statue of Unity",
            "Gir National Park",
            "Somnath Temple",
            "Kutch"
        ]
    }

}

def show_state_info():

    while True:

        print("\nAvailable States:")

        for state_name in states:
            print("-", state_name.title())

        state = input("\nEnter State Name: ").lower()

        if state in states:

            print("\nState Information")
            print("----------------------")

            print("Formation Year :", states[state]["formed"])
            print("Named By       :", states[state]["named_by"])
            print("Capital        :", states[state]["capital"])

            print("\nFamous Places:")

            for place in states[state]["places"]:
                print("-", place)

        else:
            print("\nState not found")
            print("Please enter correct state name")
            continue


        again = input("\nDo you want to search another state? (yes/no): ").lower()

        if again != "yes":
            print("\nThank You")
            break


show_state_info()
