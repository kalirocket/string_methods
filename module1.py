highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"


highlighted_poems_list = highlighted_poems.split(",")


highlighted_poems_stripped = []

for elem in highlighted_poems_list:
  highlighted_poems_stripped.append(elem.strip())

highlighted_poems_details = []

for elem in highlighted_poems_stripped:
  highlighted_poems_details.append(elem.split(":"))

titles = []
poets = []
dates = []
i = 0
new_list = []


for elem in highlighted_poems_details:
    for elem2 in elem:
        new_list.append(elem2)

while i < len(new_list) - 1:
  titles.append(new_list[i])
  poets.append(new_list[i+1])
  dates.append(new_list[i+2])
  i += 3


i = 0
for times in range(len(highlighted_poems_details)):
  if i > len(titles)-1:
    break
  else:
      txt = "The poem {title} was published by {poet} in {date}.".format(title=titles[i], poet=poets[i], date=dates[i])
      print(txt)
      i += 1


