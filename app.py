from flask import Flask, request

app = Flask(__name__)


states = {

    "kerala": {
        "capital": "Thiruvananthapuram",
        "places": [
            "Munnar",
            "Alleppey",
            "Kochi"
        ]
    },

    "andhra pradesh": {
        "capital": "Amaravati",
        "places": [
            "Tirupati",
            "Vizag Beach"
        ]
    }

}


@app.route("/", methods=["GET"])

def home():

    state = request.args.get("state")

    result = ""

    if state:

        state = state.lower()

        if state in states:

            result += f"<h2>Capital: {states[state]['capital']}</h2>"

            result += "<h3>Famous Places:</h3>"

            for place in states[state]["places"]:

                result += f"<p>{place}</p>"

        else:

            result = "<h2>State not found</h2>"


    return f"""

    <h1>India Tourism Project</h1>

    <form>

        <input type='text' name='state' placeholder='Enter State Name'>

        <button type='submit'>Search</button>

    </form>

    {result}

    """


app.run(host="0.0.0.0", port=5000)
