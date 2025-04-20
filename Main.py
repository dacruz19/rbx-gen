import string
import random
import requests
import asyncio

### Values ###
possible_values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Robux Generator Trust")
number = int(input("How many codes do you want to generate??? "))

#### Function #####
async def Generation():
   code = "RI-"
   new_block = ""

   for i in range(0,4):
      code += new_gen(new_block)
      code += "-"
      new_block = ""
   
   val = len(code)
   code = code[:-1] + code[val+1:]
   print(code)

def new_gen(new_block):
   amount_of_numbers = 0
   for i in range(4):
      if len(new_block) < 4:
         ran_val = random.choice(possible_values)
         if ran_val.isnumeric() and amount_of_numbers in [0,1]:
            amount_of_numbers += 1
            new_block += ran_val
         elif ran_val.isnumeric() and amount_of_numbers == 2:
            new_block += random.choice(string.ascii_letters).upper()
         else:
            new_block += ran_val
   return new_block

async def main():
   tasks = [Generation() for num in range(0,number)]
   asyncio.gather(*tasks)

if __name__ == "__main__":
   asyncio.run(main())
