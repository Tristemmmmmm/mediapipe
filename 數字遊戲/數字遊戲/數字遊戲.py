import random

def main():
    while True:
        number = random.randint(1, 100)
        guess = input("請輸入奇數或偶數：")
        if(number % 2 == 1): 
            answer = "奇數"
        else:
            answer = "偶數"
        if guess == answer:
            print("運氣不錯唷~ 恭喜你猜對了！！！")
            print("再來請猜這個數字是多少吧！")
            
            while True:
                num = input("請輸入數字：")
                if (int(num) < int(number)):
                    print("數字再大一點")
                elif (int(num) > int(number)):
                    print("數字在小一點")
                else:
                    print("恭喜你猜對了！！")
                    print("遊戲結束，按任意鍵退出")
                    break
                    
        else:
            print("運氣不好餒~ 你猜錯了！！")
            print(number)
            print("請問你是否繼續遊戲(是/否))")
        if not input().lower().startswith('是'):
            break
        
if __name__ == '__main__':
    main()