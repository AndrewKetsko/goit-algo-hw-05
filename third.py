from enum import Enum
import sys
from pathlib import Path
from typing import Generator
from collections import defaultdict


Level=Enum('Level',['INFO', 'ERROR', 'DEBUG', 'WARNING'])

def parse_input(args:list[str]):
    if len(args)==1:
        raise Exception('path is empty')
    path=Path(args[1])
    if len(args)==2:
        if not path.exists() and not path.is_file():
            raise Exception('path is not for a file or not exists')
        return path,None
    level=args[2].upper()
    if level not in [level.name for level in Level]:
        return path, None
    return path,level


def load_logs(file_path:str)->Generator[str,any,any]:
    try:
        with open(file_path,'r') as file:
            while True:
                line=file.readline()
                if len(line)==0:
                    break
                yield line
            
    except FileNotFoundError:
        raise FileNotFoundError('file not found')
    
    except OSError or IOError:
        raise IOError('cant read file')
    
    
def parse_log_line(line:str)->dict:
    date,time,level,*msg=line.strip().split(' ')
    return {'date':date,'time':time,'level':level,'message':' '.join(msg)}


def display_log_counts(counts):
    print('\nРівень логування | Кількість')
    print('-'*28)
    for key, value in counts.items():
        print(f'{key:<16} | {value:<9}')
    print()


def main():
    try:
        path,entry_level=parse_input(sys.argv)
    except Exception as error:
        print(repr(error))
        return
    
    logs_iterator=load_logs(path)
    levels=defaultdict(int)
    logs_by_entry_level=[]

    while True:
        try:
            line=next(logs_iterator)
            date,time,level,message=parse_log_line(line).values()
            levels[level]+=1
            if entry_level==level:
                logs_by_entry_level.append(f'{date} {time} - {message}\n')
        except StopIteration:
            break

    display_log_counts(levels)
    if entry_level:
        print(f'\nДеталі логів для рівня "{entry_level}":\n') 
        print(''.join(logs_by_entry_level))

if __name__=="__main__":
    main()