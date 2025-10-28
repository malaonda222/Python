class Esercizio:
    # inizializzo esercizio
    def __init__(self, name: str, difficulty: str) -> None:
        self.name: str = name 
        self.difficulty: str = difficulty
        self.completed: bool = False 

    def mark_completed(self) -> None:
        self.completed = True
    
    def __str__(self) -> str:
        return f"{self.name} ({self.difficulty})"
    

class Allenamento:
    def __init__(self, workout_id: str, workout_name: str) -> None:
        self.workout_id: str = workout_id
        self.workout_name: str = workout_name
        self.esercizi: list[Esercizio] = [] # lista di istanze di Esercizio

    # se esercizio non è già nella lista esercizi, allora aggiugilo
    def add_exercise(self, exercise: Esercizio) -> None:
        if exercise not in self.esercizi:
            self.esercizi.append(exercise)
        else:
            print(f"L'esercizio è già presente nell'allenamento")
    
    # ritorna la lista degli esercizi (lista, no dict quindi non c'è bisogno di fare .keys())
    def list_exercises(self):
        if not self.esercizi: 
            print(f"La lista degli esercizi è vuota")
        else:
            print(", ".join([str(esercizio) for esercizio in self.esercizi]))


class Membro:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name 
        self.allenamenti_iscritti: list[Allenamento]= [] # lista di allenamenti a cui il membro è iscritto
    
    # segna il membro a un allenamento se non è già iscritto all'allenamento
    def enroll_in_workout(self, workout: Allenamento) -> None:
        if workout not in self.allenamenti_iscritti:
            self.allenamenti_iscritti.append(workout)
        else:
            print(f"Il membro è già iscritto a questo allenamento.")
    
    # segna un esercizio come completato 
    def mark_exercise_completed(self, workout: Allenamento, exercise_name: str) -> None:
        if workout in self.allenamenti_iscritti: # controllo che l'allenamento sia tra gli allenamenti iscritti del membro
            for exercise in workout.esercizi: # itero sulla lista di esercizi dell'istanza workout(Allenamento)
                if exercise.name == exercise_name: # controllo che il nome dell'esercizio corrisponda all'esercizio del workout (workout.exercise)
                    exercise.mark_completed() # richiamo il metodo di Esercizio che segna l'esercizio come completato
                    return
            print(f"'{exercise_name}' non trovato in questo allenamento")
    
    def __str__(self) -> str:
        return f"{self.name} - {self.member_id}"
    

class PalestraDigitale:
    def __init__(self) -> None:
        self.allenamenti: dict[str, Allenamento] = {} # inizializzo dizionario di allenamenti
        self.membri: dict[str, Membro] = {} # inizializzo dizionario di membri
    
    # aggiungo workout al dizionario allenamenti
    def add_workout(self, workout_id: str, workout_name: str) -> None:
        if workout_id not in self.allenamenti:
            self.allenamenti[workout_id] = Allenamento(workout_id, workout_name)
    
    # aggiungo l'esercizio a un allenamento
    def add_exercise_to_workout(self, workout_id: str, exercise_name: str, difficulty: str) -> None:
        if workout_id in self.allenamenti: # controllo che workout_id sia già all'interno del dizionario allenamenti
            exercise = Esercizio(exercise_name, difficulty) # se c'è allora crea l'esercizio con i parametri di Esercizio
            self.allenamenti[workout_id].add_exercise(exercise) # estrapolo il workout_id dal dizionario e uso il metodo della classe Allenamento (add_exercise())
        else:
            print("Esercizio non presente nel dizionario")
    
    # aggiungo un membro al dizionario membri
    def register_member(self, member_id: str, name: str) -> None:
        if member_id not in self.membri:
            self.membri[member_id] = Membro(member_id, name)
        else:
            print(f"Membro già iscritto in questa palestra")
    
    # iscrivo il membro nell'allenamento
    def enroll_member_in_workout(self, member_id: str, workout_id: str) -> None:
        if member_id in self.membri and workout_id in self.allenamenti:
            membro = self.membri[member_id]
            workout = self.allenamenti[workout_id]
            membro.enroll_in_workout(workout)
        else:
            return "Membro o workout non trovati"
    
    def mark_exercise_completed_for_member(self, member_id: str, workout_id: str, exercise_name: str) -> None:
        if member_id in self.membri and workout_id in self.allenamenti:
            membro = self.membri[member_id]
            workout = self.allenamenti[workout_id]
            membro.mark_exercise_completed(workout, exercise_name)
        else:
            return "Membro o workout non trovato"
        
    def list_member_workouts(self, member_id: str) -> None: 
        #  Mostra tutti gli allenamenti a cui un membro è iscritto.
        if member_id in self.membri:
            member = self.membri[member_id]
            return [workout.workout_name for workout in member.allenamenti_iscritti]
        else:
            print("Il membro non è iscritto")
 
    def list_member_exercises(self, member_id: str, workout_id: str) -> None: 
        # Mostra tutti gli esercizi di un allenamento a cui un membro è iscritto, con il loro stato (completato/non completato).
        if member_id in self.membri and workout_id in self.allenamenti:
            member = self.membri[member_id]
            workout = self.allenamenti[workout_id]
            
            if workout not in member.allenamenti_iscritti:
                print("Il membro non è iscritto a questo workout")
            
            if not workout.esercizi:
                print("Lista degli esercizi vuota.")

            for esercizio in workout.esercizi:
                stato = "Completato" if esercizio.completed else "Non completato"
                print(f"{esercizio.name}, {esercizio.difficulty} - {stato}")
                
    def list_completed_exercises(self, member_id: str) -> None:
        if member_id in self.membri:
            member = self.membri[member_id]
            nuova_lista = []
            for workout in member.allenamenti_iscritti:
                for esercizio in workout.esercizi:
                    if esercizio.completed:
                        nuova_lista.append(workout.workout_name, esercizio.name)

            if not nuova_lista:
                print("Ancora non è stato completato nessun esercizio.")
            
            print(f"\nEsercizi completati da {member.name}:")
            for workout_name, esercizio in nuova_lista:
                print(f"- {esercizio.name} da {workout_name}")
        

palestra = PalestraDigitale()


esercizio = Esercizio("Push-up", "Facile")
esercizio1 = Esercizio("Addominali", "Difficile")

palestra.add_exercise_to_workout("1", "Push-up", "Facile")
palestra.add_exercise_to_workout("1", "Stacchi", "Difficile")

palestra.add_member("1001", "Mauro")

palestra.enroll_member_in_workout("1001", "1")

palestra.mark_exercise_completed_for_member("1001", "1", "Push-up")

allenamento = Allenamento("1", "Funzionale")
allenamento.add_exercise(esercizio)
allenamento.add_exercise(esercizio1)

palestra.add_workout("1", "Funzionale")

allenamento.list_exercises()
