##########multilevel inheritance###########
#child class->look immediate father->not found->above heirarchy

class dad:
    basketball=6

class son(dad):
    dance=5
#    basketball=9
    def is_dance(self):
        return f"yes i can {self.dance} types of dance "
class grandson(son):
    dance=3
    basketball = 17
 #   def is_dance(self):
 #       return f"yes,i dance {self.dance} types of unique style "

harivansh=dad()
amitabh=son()
abhishek=grandson()
print(abhishek.is_dance())
print(abhishek.basketball)
print(amitabh.basketball)