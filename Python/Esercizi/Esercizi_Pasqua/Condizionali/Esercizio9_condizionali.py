def rimbalzo() -> None:
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0   
    print(f"Tempo: {tempo} Altezza: {altezza}")
 
    while rimbalzi < 5:
        tempo += 1
        if altezza < 0: 
            altezza *= -0.5
            velocita *= -0.5
            print(f"Tempo: {tempo} Altezza: {altezza}")
 
        else: 
            altezza += velocita
            velocita -= 96
            if altezza < 0:
                rimbalzi += 1
                print(f"Tempo: {tempo} Rimbalzo!")
            else:
                print(f"Tempo: {tempo} Altezza: {altezza}")