from flask import Flask, request;
from game import Game;
from player import Player;
from location import Location;
from enum import Enum;

import json;

app = Flask(__name__);
game = Game();
town = Location("town");
town.generate_map(["house", "hotel", "cvstore", "gym"]);

class codes(Enum):
  PLAYEREXIST = "-1";
  PLAYERNOTEXIST = "-2";
  REGISTERSUCCESS = "1";
  REGISTERFAIL = "-3";
  MISSINGARGS = "-4";
  
@app.route("/map", methods = ["GET"])
def get_map():
  return town.print_map();
  
@app.route("/<user>/exists", methods = ["GET"])
def player_exists(user):
  if game.player_exists(user):
    return codes.PLAYEREXIST.value;
  else:
    return codes.PLAYERNOTEXIST.value;

@app.route("/register", methods = ["POST"])
def register_player():
  print(request.data);
  data = json.loads(request.data);
  if game.player_exists(data["name"]):
    return codes.PLAYEREXIST.value;
  else:
    try:
      game.add_player(Player(data["name"]), data["passw"]);
    except KeyError :
      return codes.MISSINGARGS.value;
  return codes.REGISTERSUCCESS.value;
  
@app.route("/<user>/<_type>", methods = ["GET", "POST"])
def get_user_info(user, _type):
  match request.method:
    case "GET":
      if game.player_exists(user):
        plr = game.get_player(user)["plr"];
        match _type:
          case "info":
            return json.dumps(plr.info);
          case "stats":
            return json.dumps(plr.stats);
          case "skills":
            return json.dumps(plr.skills);
          case "inventory":
            return json.dumps(plr.inventory);
          case _:
            return "not a valid type";
      else:
        return "username not found";
        
    case "POST":
      if game.player_exists(user):
        plr = game.get_player(user)["plr"];
        data = request.data;
        match _type:
          case "info":
            return plr.info.update(json.loads(data));
          case "stats":
            return plr.stats.update(json.loads(data));
          case "skills":
            return plr.skills.update(json.loads(data));
          case "inventory":
            return plr.inventory.update(json.loads(data));
          case _:
            return "not a valid type";
      else:
        return "username not found";

app.run();