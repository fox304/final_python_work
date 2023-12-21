import argparse
from final_certification import *

""""
этот  модуль запускается с консоли
командами, закомментированными  в конце 
"""

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="Запуск с консоли")
parser.add_argument('-type_animal',
                    metavar='a',
                    type=str,
                    help='введите тип животного')
parser.add_argument('-name_animal',
                    metavar='b',
                    type=str,
                    help='введите имя животного')
parser.add_argument('-par',
                    metavar='c',
                    type=int,
                    help='введите параметр животного')
args = parser.parse_args()

if args.type_animal:
    an = AnimalFactory.create_animal(args.type_animal,
                                     args.name_animal, args.par)  # Создание экземпляра животного
    if args.type_animal == "Bird":
        print(an.wing_length())
    elif args.type_animal == "Fish":
        print(an.depth())
    elif args.type_animal == "Mammal":
        print(an.category())
else:
    logger.error("этот  модуль запускается только с консоли")

# python .\from_console.py -type_animal Bird -name Орел -par 200
# python .\from_console.py -type_animal Fish -name Лосось -par 50
# python .\from_console.py -type_animal Mammal -name Слон -par 5000
