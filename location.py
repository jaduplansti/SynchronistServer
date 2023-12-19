from random import randint, choice;
from player import Player;

class House(): # its a house
  def __init__(self):
    self.info = {
      "owned" : False,
      "owner" : "",
      "players" : {},
    }
    self.appliances= { # TODO: add appliances
      "bed" : None,
    }

class Hotel(): # hotel or motel?
  def __init__(self):
    self.info = {
      "owner" : False,
      "players" : {},
    }
    self.rooms = { # rooms
      
    }
    
class CVStore(): # aka convenience store
  def __init__(self):
    self.info = {
      "players" : {},
    }
    self.items = { # TODO: add items
      "bread" : None
    }

class Gym(): # lets hit it brahs!
  def __init__(self):
    self.info = {
      "owner" : {},
      "players" : {},
    }
    self.equipment = { # gym equipment
      
    }
class Location():
  def __init__(self, name):
    self.name = name;
    self.players = {};
    self.map = [None for n in range (64)];
  
  def pick_option(self, options):
    return choice(options);
  
  def check(self, index):
    if index > 63 or index < 0:
      return False;
    elif self.map[index] == None:
      return True;
    else:
      return False;
  
  def arrivable(self, n):
    if self.check(n + 8) and self.check(n - 8) and self.check(n + 1) and self.check(n - 1):
      return True;
    else:
      return False;
      
  def generate_map(self, contents):
    for n in range(0, 64):
      if self.arrivable(n):
        match self.pick_option(contents):
          case "house":
            self.map[n] = House();
          case "cvstore":
            self.map[n] = CVStore();
          case "hotel":
            self.map[n] = Hotel();
          case "gym":
            self.map[n] = Gym();
      else:
        continue;
  
  def print_map(self):
    map = "";
    for n, tile in enumerate(self.map):
      if n % 8 == 0 and n != 0:
        map += "\n";
        
      if isinstance(tile, House):
        map += "🏠";
      elif isinstance(tile, CVStore):
        map += "🏪";
      elif isinstance(tile, Hotel):
        map += "🏨";
      elif isinstance(tile, Gym):
        map += "🛖";
      elif tile == None:
        map += "  •  ";
      
    return map;