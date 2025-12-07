import math

def get_valid_number(message):
    while True:
        try:
            user_input = int(input(message))
            
            if user_input <= 0:
                print("正しく入力せよ")
                continue

            else:    
                return  user_input 
        
        except ValueError:
            print("半角数字を入力せよ")

quantity = get_valid_number("製作する個数を入力せよ")
time_per_unit = get_valid_number("1個当たりの所要秒数を入力せよ")

total_minutes = math.ceil((quantity * time_per_unit) / 60)

print(f"製作所要時間は{total_minutes}分")

        
            