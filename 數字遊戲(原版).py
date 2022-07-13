import random

def main():
    while True:
        number = random.randint(1, 100)
        txt = input("請輸入文字猜測是'奇數'或'偶數'：")
        if(number % 2 == 1): 
            answer = "奇數"
        else:
            answer = "偶數"
        if txt == answer:
            print("恭喜你猜對了！！！")
            print("接著猜猜這個數字是多少吧！")
            while True:
                guess = input("請輸入數字：")
                if (int(guess) < int(number)):
                    print("數字再大一點")
                    print("try again")
                elif (int(guess) > int(number)):
                    print("數字在小一點")
                    print("try again")
                else:
                    print("恭喜你猜對了！！")
                    print("遊戲結束，按任意鍵退出")
                    break
            
            
            
        else:
            print("運氣不好餒~ 你猜錯了否！！")
            print("接著猜猜這個數字是多少吧!")
            while True:
                guess = input("請輸入數字：")
                if (int(guess) < int(number)):
                    print("NOT EVEN CLOSE")
                elif (int(guess) > int(number)):
                    print("NOT EVEN CLOSE")
                else:
                    print("恭喜你猜對了！！")
                    print("遊戲結束，按任意鍵退出")
                    break
                    
                
        print("請問你是否繼續遊戲(是/否))")
        if not input().lower().startswith('是'):
            break
        
        
if __name__ == '__main__':
    main()