import random
from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent
key_word = "user"
result = []


def random_boolean():
    return random.choice([True, False])



def process():
    file = open(ROOT_DIR / "rockyou.txt")
    counter:int = 0
    finded_counter :int =0
    Writed_counter :int =0
    while True:
        try:
            counter += 1
            line:str = file.readline()
            #print(f'String number {counter}')
            if line.find(key_word) == -1:
               # print("No substring in string")
                continue
            else:
                finded_counter +=1
                #print (f'We find element : {finded_counter}')                
                if random_boolean():
                    #print(f"Number: {counter}  writing...")
                    Writed_counter +=1
                    result.append(line)
                else:
                    print (f"We dont writing this el number: {counter}")
            
        except Exception:
            break
    file.close()
    print(f"total elements: {counter}")
    print(f"Finded elements: {finded_counter}")
    print(f"Write elements{Writed_counter}")
    return result
process()
#for item in  process():
#    print(item)