def seconds_since_noon(ora:int, minuto:int, secondo:int) -> int:
    secondi_totali = (ora - 0) * (60 * 60) + minuto * 60 + secondo
    return secondi_totali

def time_difference(ora1:int, minuto1:int, secondo1:int, ora2:int, minuto2:int, secondo2:int) -> int:
    time1 = seconds_since_noon(ora1, minuto1, secondo1)
    time2 = seconds_since_noon(ora2, minuto2, secondo2)
    differenza = time1 - time2
    if differenza < 0:
        return differenza * -1
    else:
        return differenza
    
    # oppure

    abs(time1 - time2)
