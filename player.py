from random import randint;
class Player():
    def __init__(self, name):
        self.info = {
            "name" : name,
            "class" : ["ordinary"],
            "level" : 1,
            "exp" : 0,
            "condition" : ["ok"],
            "affinity" : ["existing"],
        }
        self.stats = {
            "health" : 100,
            "energy" : 100,
            "attack" : randint(1, 10),
            "defense" : randint(1, 10),
            "dexterity" : randint(1, 10),
        }
        self.skills = {
            "quick jab" : {
                "proficiency" : 0,
                "energy" : 10,
                "type" : "active",
                "class" : "physical",
                "desc" : "it's a jab.",
            }
        }
        self.inventory = {
            "health potion" : {
                "amount" : 5,
                "durability" : 1,
                "type" : "potion",
                "class" : "support",
                "creator" : "game",
                "desc" : "restore health easily!",
            }
        }

    def add_stat(self, stat, val):
      try:
        if val < 0:
          return False;
        else:
          self.stat[stat] += val;
          return True;
      except KeyError:
        return False;
        
    def sub_stat(self, stat, val):
      try:
        if val < 0:
          return False;
        else:
          self.stat[stat] -= val;
          return True;
      except KeyError:
        return False;

    def add_skill(self, skill_info):
      if len(skill_info) < 6:
        return False;
      else:
        self.skills.update({
        skill_info[0] : {
          "proficiency" : skill_info[1],
          "energy" : skill_info[2],
          "type" : skill_info[3],
          "class" : skill_info[4],
          "desc" : skill_info[5],
        }
        });
      return True;
        
    def add_item(self, item_info):
      if len(item_info) < 7:
        return False;
      else:
        self.inventory.update({
        item_info[0] : {
          "amount" : item_info[1],
          "durability" : item_info[2],
          "type" : item_info[3],
          "class" : item_info[4],
          "creator" : item_info[5],
          "desc" : item_info[6],
        }
        });
      return True;
    
    def del_skill(self, skill):
      del self.skills[skill];
    
    def del_item(self, item):
      del self.inventory[item];
    
    def get_skill(self, skill):
      return self.skills[skill];
    
    def get_item(self, item):
      return self.inventory[item];
    
    def deal_damage(self, dmg):
      self.sub_stat("health", dmg);
      
    def formatted_info(self):
      out = "[{name}]\n[class] 👉 {_class}\n[level] 👉 {level}\n[exp] 👉 {exp}\n[condition] 👉 {condition}\n[affinity] 👉 {affinity}\n";
      return out.format(name = self.info["name"], _class = ','.join(self.info["class"]), level = self.info["level"],
      exp = self.info["exp"], condition = ','.join(self.info["condition"]), affinity = ','.join(self.info["affinity"]));
      
    def formatted_stats(self):
      out = "[❤️] {health}\n[⚡] {energy}\n[💪] {attack}\n[🛡️] {defense}\n[🏃] {dexterity}\n";
      return out.format(health = self.stats["health"], energy = self.stats["energy"], attack = self.stats["attack"],
      defense = self.stats["defense"], dexterity = self.stats["dexterity"]);
    
    def formatted_basic_skills(self):
      out = "";
      for skill in self.skills:
        out += "[{name}]({proficiency}%)({energy}) {type}, {_class}\n".format(
        name = skill, proficiency = self.get_skill(skill)["proficiency"],
        energy = self.get_skill(skill)["energy"], type = self.get_skill(skill)["type"], _class = self.get_skill(skill)["class"]);
      return out;
    
    def formatted_basic_items(self):
      out = "";
      for item in self.inventory:
        out += "[{name}]({durability}%)({amount}) {type}, {_class}\n".format(
        name = item, durability = self.get_item(item)["durability"],
        amount = self.get_item(item)["amount"], type = self.get_item(item)["type"], _class = self.get_item(item)["class"]);
      return out;
    
    def formatted_all_skills(self):
      out = "";
      for skill in self.skills:
        out += "[{name}]\nproficiency > {proficiency}, energy > {energy}\ncategory > {type}, {_class}\ndescription:\n{desc}".format(
        name = skill, proficiency = self.get_skill(skill)["proficiency"], energy = self.get_skill(skill)["energy"], type = self.get_skill(skill)["type"], _class = self.get_skill(skill)["class"], desc = self.get_skill(skill)["desc"]);
      return out;
      
      