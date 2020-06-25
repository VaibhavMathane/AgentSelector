import random


def agent_Selector(t):
    available_since1 = [lis[1] for lis in t]
    roles1 = [lis[0] for lis in t]
    temp = min(available_since1)

    issue_type = input("Enter the role for issue \n")
    available=[item[2] for item in t if item[0] == issue_type and item[3] == "Yes"]


    Selection_mode = int(input("Please select the mode \n 1: All available mode \n 2: Least busy \n 3: Random \n"))

    if Selection_mode == 1:
        print(available)

    elif Selection_mode == 2:
        Output = [item[2] for item in t
                  if item[0] == "sales" and item[1] == temp and item[3] == "Yes"]
        print(Output)


    elif Selection_mode == 3:
        random_item = random.choice(available)
        print(random_item)


    else :
        print("Enter correct value")





t = list(
        tuple(map(str, input('Enter role, the time since agent is available in mins, agents name and is_available: ').split()))
        for r in
        range(int(input('enter no of agents : '))))

print(t)
agent_Selector(t)
