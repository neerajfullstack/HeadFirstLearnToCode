balance = 10500
camera_on = True

def steal(acc_balance, amount):
    global camera_on
    camera_on = False
    if(amount < acc_balance):
        global balance
        balance = acc_balance - amount
        camera_on = True
    return amount
    

proceeds = steal(balance, 10000)
print('Criminal: You stole', proceeds)

