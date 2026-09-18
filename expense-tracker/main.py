print("Welcome to the Daily Expense Tracker!")
print('')
print('Menu:')
print('1. Add a new expense')
print('2. View all expenses')
print('3. Calculate total and average expense')
print('4. Clear all expenses')
print('5. Exit')

ex=[]
hi=True
while hi:
    ch=int(input())
    if ch==5:
        print('Exiting the Daily Expense Tracker. Goodbye!')
        hi=False
        break
    if ch==1:
        new_input=float(input())
        ex.append(new_input)
        print('Expense added successfully!')
    elif ch==2:
        if len(ex)==0:
            print('No expenses recorded yet.')
        else:
            print('Your expenses:')
            ii=1
            for exp in ex:
                print(f'{ii}. {exp}')
                ii+=1
    elif ch==3:
        if len(ex)==0:
            print('No expenses recorded yet.')
        else:
            t=0
            a=0
            for s in ex:
                t=t+s
            a=t/len(ex)
            print(f'Total expense: {t}')
            print(f'Average expense: {a}')
    elif ch==4:
        ex.clear()
        print('All expenses cleared.')
