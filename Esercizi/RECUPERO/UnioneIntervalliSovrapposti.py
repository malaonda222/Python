#ordinare in ordine crescente rispetto all'indice 0

'''se abbiamo una lista di tre intervalli che non si sovrappongono allora:
se il primo non si sovrappone con il secondo allora il primo non si sovrappone con il terzo'''

# def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
#     intervals.sort()

#     if intervals == []:
#         return list()
    
#     if len(intervals) == 1:
#         interval = intervals[0]
#         if not isinstance(intervals, list) or len(interval) != 2:
#             raise ValueError("Intervallo non valido.")
#         if not all(isinstance(x, int) for x in interval):
#             raise ValueError("Intervallo non valido.")
#         if interval[0] > interval[1]:
#             raise ValueError("Intervallo non valido")
#         return [interval]

   
#     for intervallo_attuale in intervals[1:]:
#         if not isinstance(intervals, list) or len(interval) != 2:
#             raise ValueError("Intervallo non valido.")  
#         if not all(isinstance(x, int) for x in interval):
#             raise ValueError("Intervallo non valido.")
#         if interval[0] > interval[1]:
#             raise ValueError("Intervallo non valido")
#         else:
#             new_list = [intervals[0]]
#             intervallo_ultimo = intervallo_attuale[-1]
#             if intervallo_attuale[0] <= intervallo_ultimo[1]:
#                 intervallo_ultimo[1] = max(intervallo_ultimo[1], intervallo_attuale[1])
#             else:
#                 new_list.append(intervallo_attuale)


def merge_intervals(intervals: list[list[int]]):
    intervals.sort()
    if not intervals:
        return []
    if len(intervals) == 1:
        return [intervals]
    
    unione = [intervals[0]]
    for inter_attuale in intervals[1:]:
        ultimo_intervallo = unione[-1]
        if inter_attuale[0] > inter_attuale[1]:
            raise ValueError(f"Intervallo non valido: [{inter_attuale[0]}, {inter_attuale[1]}]")
        if inter_attuale[0] <= ultimo_intervallo[1]:
            ultimo_intervallo[1] = max(ultimo_intervallo[1], inter_attuale[1])
        
        # oppure 
            # massimo = ultimo_intervallo[1]
            # if inter_attuale[1] > massimo:
            #     massimo = inter_attuale[1]
        else: 
            unione.append(inter_attuale)
    return unione

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 2], [2, 6], [5, 7], [15, 18]]
print(merge_intervals(intervals))
print(merge_intervals(intervals2)) # restituisce [[1, 6], [8, 10], [15, 18]]


