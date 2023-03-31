angry = True
bored = False
hungry = True
tired = False

if angry:
  if hungry and bored:
    print("T-Rex eats Triceratops. Nyum! Nyum!")
elif tired and hungry:
  print("T-Rex eats Iguanadon. Nyum! Nyum!")
elif tired:
  print("T-Rex goes to sleep. Zzzzzz...")
elif angry and bored:
  print("T-Rex eats Velociraptor. Nyum! Nyum!")
elif angry or bored:
  print("T-Rex roars. Rawr!")
else:
  print("T-Rex gives toothy smile.")
