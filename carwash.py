from time import sleep

def pricing():
    print('Enter "1" for Car wash : Inside and Outside = Rs.1000')
    print('Enter "2" for Car wash : Inside only = Rs.700')
    print('Enter "3" for Car wash : Outside only = Rs.300')
    val = int(input('WHICH SERVICE: '))
    print()
    select_service(val)
    total_cost(val)
    payment(val)

def select_service(n):
    match n:
        case 1:
            print('Starting Car Wash.....')
            sleep(2)
            print('EXTERIOR DONE!')
            sleep(2)
            print('INTERIOR DONE!')
            sleep(1)
            print('GETTING YOUR RIDE READY')
            sleep(1)
            print('YOUR ARE ALL SET TO GO')
            print()            

        case 2: 
            print('Starting Car Wash.....')
            sleep(3)
            print('INTERIOR DONE!')
            sleep(1)
            print('GETTING YOUR RIDE READY')
            sleep(2)
            print('YOUR ARE ALL SET TO GO')
            print()
        case 3:
            print('Starting Car Wash.....')
            sleep(3)
            print('EXTERIOR DONE!')
            sleep(1)
            print('GETTING YOUR RIDE READY')
            sleep(2)
            print('YOUR ARE ALL SET TO GO')
            print()


def total_cost(n):
    match n:
        case 1:
            print('TOTAL COST OF YOUR SERCVICE IS Rs.1000')
            print()
            sleep(1)
        case 2:
            print('TOTAL COST OF YOUR SERCVICE IS Rs.700')
            print()
            sleep(1)
        case 3:
            print('TOTAL COST OF YOUR SERCVICE IS Rs.300')
            print()
            sleep(1)


def payment(opt):
    print('WHICH PAYMENT METHOD YOU LIKE TO CHOOSE ?')
    print('ENTER "1" FOR CASH')
    print('ENTER "2" FOR CARD')
    val = int(input('WHICH METHOD: '))
    match val:
        case 1:
            billing(opt)
            print('PLEASE VISIT AGAIN!')

        case 2:
            name = input('ENTER CARD HOLDER NAME: ')
            card_num = int(input('ENTER CARD NUMBER: '))
            print()
            print('Redirecting to the bank......')
            sleep(1)
            print('processing payment....')
            sleep(2)
            billing(opt)
            print('PLEASE VISIT AGAIN!')

def billing(n):
    match n:
        case 1:
            print('Payment of Rs.1000 has been done!')

        case 2:
            print('Payment of Rs.700 has been done!')
            
        case 3:
            print('Payment of Rs.300 has been done!')


pricing()
            






            

    
