import os
import random

list_days = random.sample(range(1, 500), 350) 

def make_commit(days: int):
    if days in list_days:
        dates = f'{days} days ago'

        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

        #Staging
        os.system('git add data.txt')
        #Commit
        os.system('git commit --date="'+dates+'" -m "first commit"')

        return days * make_commit(days - 1)

    else:
        return os.system("git push")
        
        
make_commit(500)
