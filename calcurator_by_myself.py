import math

def get_valid_number(message):
    while True:
        try:
            user_input = int(input(message))
            
            if user_input <= 0:
                print("エラー：0以下の数字が入力されています")
                continue
    
            return  user_input 
        
        except ValueError:
            print("エラー：半角数字を入力してください")

quantity = get_valid_number("製作する個数を入力してください")
time_per_unit = get_valid_number("1個当たりの所要秒数を入力してください")

total_minutes = math.ceil((quantity * time_per_unit) / 60)

print(f"製作所要時間は{total_minutes}分です")

        
            