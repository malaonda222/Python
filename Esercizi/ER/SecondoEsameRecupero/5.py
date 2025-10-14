def check_security_alarm(s1: bool, s2: bool, s3: bool) -> str:
    if s1 == True and (s2 == False or s3 == False):
        return "Allarme attivato"
    else:
        return "Nessun allarme"
    

def check_security_alarm(s1: bool, s2:bool, s3: bool) -> str:
    if s1 and (not s2 or not s3):
        return "Allarme attivato"
    else:
        return "Nessun allarme"

