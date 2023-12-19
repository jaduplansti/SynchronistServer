import bcrypt;

class Game():
    def __init__(self):
      self.players = {};
     
    def add_player(self, player, passw):
      self.players.update({
        player.info["name"] : {
          "plr" : player,
          "passw" : passw,
        },
      });
    
    def encrypt_passw(self, passw):
      return bcrypt.hashpw(passw.encode(), bcrypt.gensalt());
      
    def check_passw(self, passw, name):
      if bcrypt.checkpw(passw.encode(), game.get_player(name)["passw"]):
        return True;
      else:
        return False;
        
    def player_exists(self, name):
      try:
        self.players[name];
        return True;
      except KeyError:
        return False;
    
    def get_player(self, name):
      try:
        return self.players[name];
      except KeyError:
        return False;
    
    def remove_player(self, name):
      del self.players[name];
        
