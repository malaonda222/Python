from __future__ import annotations
from flask import Flask, jsonify, url_for, requests 
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float) -> None:
        self.id: str = id
        self.name: str = name 
        self.age_years: int = age_years
        self.weight_kg: float = weight_kg

    @abstractmethod
    def species(self):
        pass 

    @abstractmethod
    def daily_food_grams(self):
        pass 

    def info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.age_years,
            "daily_food_grams": self.daily_food_grams()
        }
    
    def bmi_like(self):
        return self.weight_kg / (self.age_years + 1)
    

class Dog(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.breed: str = breed
        self.is_trained: bool = is_trained
    
    def species(self):
        return "dog"
    
    def daily_food_grams(self):
        return round(200 + self.age_years * 50, 2)
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict["breed"] = self.breed
        info_dict["is_trained"] = self.is_trained
        return info_dict
    

class Cat(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, indoor_only: bool, favorite_toy: str) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.indoor_only: bool = indoor_only
        self.favorite_toy: str = favorite_toy

    def species(self) -> str:
        return "cat"
    
    def daily_food_grams(self):
        return round(100+self.age_years*30, 2)
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict["indoor_only"] = self.indoor_only
        info_dict["favorite_toy"] = self.favorite_toy
        return info_dict
    

class Shelter:
    def __init__(self, animals: dict[str, Animal] | None = None, adoptions: dict[str, str] | None = None) -> None:
        self.animals: dict = animals if animals is not None else {}
        self.adoptions: dict = adoptions if adoptions is not None else {}

    def add(self, animal: Animal):
        if animal.id in self.animals:
            raise ValueError("Errore. Id animale già esistente")
        self.animals[animal.id] = animal
    
    def get(self, animal_id: str) -> Animal | None:
        if animal_id not in self.animals:
            return None 
        else:
            return self.animals[animal_id]
    
    def list_all(self) -> list[Animal]:
        return [animal.info() for animal in self.animals.values()]

    def is_adopted(self, animal_id: str) -> bool:
        return animal_id in self.adoptions 
    
    def set_adopted(self, animal_id: str, adopter_name: str):
        self.adoptions[animal_id] = adopter_name