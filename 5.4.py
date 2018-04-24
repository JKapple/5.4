fat_grams = 0.0
carb_grams = 0.0
protien_grams = 00


fat_grams = int(input("How many fat grams have you had today?"))
carb_grams = int(input("How many carb grams have you had today?"))
protien_grams = int(input("How many protien grams have you had today?"))

def get_cal_of_fat():
    calories_of_fat = fat_grams * 9
    print("Your total calories of fat are ",calories_of_fat)

get_cal_of_fat()
#carb
def get_cal_of_carb():
    calories_of_carb = carb_grams * 4
    print("Your total calories of carb are ",calories_of_carb)

get_cal_of_carb()
#protien
def get_cal_of_pro():
    calories_of_pro = protien_grams * 4
    print("Your total calories of protien are ",calories_of_pro)

get_cal_of_pro()



def total():
    total_cal = protien_grams + carb_grams + fat_grams
    print("Your total are ",total_cal)

total()

