class RecipeManager:
    def __init__(self):
        self.ricette = {}

    def create_recipe(self, name:str, ingredients: list):
        if name in self.ricette:
            return ("Errore. La ricetta è già presente nella lista delle ricette.")
        else:
            self.ricette[name] = ingredients
            return {name: ingredients}
        
    def add_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name not in self.ricette:
            return "Errore. Ricetta non presente nella lista."
        if ingredient in self.ricette[recipe_name]:
            return "Ingrediente già presente nella lista associata alla ricetta."
        self.ricette[recipe_name].append(ingredient)
        return {recipe_name: self.ricette[recipe_name]}             
        
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name not in self.ricette:
            return "Errore. Ricetta non presente nella lista."
        if ingredient not in self.ricette[recipe_name]:
            return "Ingrediente non presente nella ricetta, non è possibile rimuoverlo."
        self.ricette[recipe_name].remove(ingredient)
        return {recipe_name: self.ricette[recipe_name]}
                   
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        if recipe_name not in self.ricette:
            return "Errore. Ricetta non presente nella lista."
        
        for i in range(len(self.ricette[recipe_name])):
            if self.ricette[recipe_name][i] == old_ingredient:
                self.ricette[recipe_name][i] = new_ingredient
                return {recipe_name: self.ricette[recipe_name]}
        return "Errore. Ingrediente da sostituire non presente nella ricetta."
            
        
    def list_recipes(self):
        if not self.ricette:
            return "Lista vuota."
        else:
            return list(self.ricette.keys())

    def list_ingredients(self, recipe_name: str):
        if recipe_name not in self.ricette:
            return "Errore. Ricetta non presente nella lista delle ricette."
        else:
            return self.ricette[recipe_name]     
    
    def search_recipe_by_ingredient(self, ingredient: str):
        ricette_trovate = []
        for recipe_name, ingredients in self.ricette.items():
            if ingredient in ingredients:
                ricette_trovate.append(recipe_name)
        if not ricette_trovate:
            return "Errore. L'ingrediente non si trova in nessuna ricetta."
        return {recipe_name: self.ricette[recipe_name]}
        
           
