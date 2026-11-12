# pyrefly: ignore[missing-import]
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ယုံကြည်စိတ်ချရသော Logo လင့်ခ်များဖြင့် ပြင်ဆင်ထားသော Database
TEAMS_DB = {
    "real madrid": {
        "name": "Real Madrid",
        "badge": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
        "league": "Spanish La Liga",
        "stadium": "Santiago Bernabéu",
        "founded": "1902",
        "description": "Real Madrid Club de Fútbol, commonly known as Real Madrid, is a professional football club based in Madrid, Spain.",
        "recent_matches": []
    },
    "barcelona": {
        "name": "Barcelona",
        "badge": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
        "league": "Spanish La Liga",
        "stadium": "Spotify Camp Nou",
        "founded": "1899",
        "description": "Futbol Club Barcelona, commonly known as Barcelona, is a professional football club based in Barcelona, Catalonia, Spain.",
        "recent_matches": []
    },
    "atletico madrid": {
        "name": "Atletico Madrid",
        "badge": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2024_logo.svg",
        "league": "Spanish La Liga",
        "stadium": "Metropolitano Stadium",
        "founded": "1903",
        "description": "Atlético Madrid is a professional football club based in Madrid, Spain, that plays in La Liga.",
        "recent_matches": []
    },
    "arsenal": {
        "name": "Arsenal",
        "badge": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
        "league": "English Premier League",
        "stadium": "Emirates Stadium",
        "founded": "1886",
        "description": "Arsenal Football Club is a professional football club based in Holloway, North London.",
        "recent_matches": []
    },
    "manchester united": {
        "name": "Manchester United",
        "badge": "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg",
        "league": "English Premier League",
        "stadium": "Old Trafford",
        "founded": "1878",
        "description": "Manchester United Football Club, commonly known as Man Utd, is a professional football club based in Old Trafford, Greater Manchester, England.",
        "recent_matches": []
    },
    "manchester city": {
        "name": "Manchester City",
        "badge": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
        "league": "English Premier League",
        "stadium": "Etihad Stadium",
        "founded": "1880",
        "description": "Manchester City Football Club is an English football club based in Manchester that competes in the Premier League.",
        "recent_matches": []
    },
    "liverpool": {
        "name": "Liverpool",
        "badge": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
        "league": "English Premier League",
        "stadium": "Anfield",
        "founded": "1892",
        "description": "Liverpool Football Club is a professional football club based in Liverpool, England, that competes in the Premier League.",
        "recent_matches": []
    },
    "chelsea": {
        "name": "Chelsea",
        "badge": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
        "league": "English Premier League",
        "stadium": "Stamford Bridge",
        "founded": "1905",
        "description": "Chelsea Football Club is an English professional football club based in Fulham, West London.",
        "recent_matches": []
    },
    "tottenham": {
        "name": "Tottenham Hotspur",
        "badge": "https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg",
        "league": "English Premier League",
        "stadium": "Tottenham Hotspur Stadium",
        "founded": "1882",
        "description": "Tottenham Hotspur Football Club, commonly referred to as Tottenham or Spurs, is based in Tottenham, North London.",
        "recent_matches": []
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/team")
def get_team_info():
    team_name = request.args.get("name", "").strip().lower()
    if not team_name:
        return jsonify({"error": "Team name is required"}), 400

    if team_name in TEAMS_DB:
        return jsonify(TEAMS_DB[team_name])
    else:
        return jsonify({"error": "အသင်းရှာမတွေ့ပါ။ Real Madrid, Arsenal သို့မဟုတ် Liverpool ဟု စမ်းပါ။"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)