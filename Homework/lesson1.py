Tyeshela_Crew = ['Gio Gagnidze', 'Luka Kevkhishvili', 'Jemiko Kaxidze', 'Luka Turadze', 'Davit Meparishvili', 'Luka Tevzadze', 'Alexandre Katsarava']
name = Tyeshela_Crew[4]
for member in Tyeshela_Crew:
    if len(member) == len(name):
      Tyeshela_Crew.remove(member)
print(Tyeshela_Crew)