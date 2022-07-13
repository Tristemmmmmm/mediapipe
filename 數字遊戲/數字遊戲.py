import random

def main():
    while True:
        level=input("請輸入文字選擇'困難'或'普通'模式 :")
        if(level=='普通'):
            number=random.randint(1,4)
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
                print("運氣不好餒~ 你猜錯了！！")
                print("答案是: ",end="")
                print(number)
                print("請問你是否繼續遊戲(是/否))")
                if not input().lower().startswith('是'):
                    break
        
        
        elif(level=='困難'):
            number=random.randint(1, 14)
        #number = random.randint(1, 4)
            txt = input("請輸入文字猜測是'奇數'或'偶數'：")
            if(number % 2 == 1): 
                answer = "奇數"
            else:
                answer = "偶數"
            if txt == answer:
                print("恭喜你猜對了！！！")
                print("接著猜猜這個數字是多少吧！")
            
                while True:
                    for i in range(1,3):
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
                    guess = input("請輸入數字：")
                    if(int(guess)>int(number)):
                        print("not even close")
                    elif(int(number)<int(guess)):
                        print("not even close")
                    else:
                        print("恭喜你猜對了！！")
                        print("遊戲結束，按任意鍵退出")
                        break
                    
            else:
                print("運氣不好餒~ 你猜錯了！！") #47 71猜機偶
                print("答案是: ",end="")
                print(number)
                print("請問你是否繼續遊戲(是/否))")
                if not input().lower().startswith('是'):
                    break
        else:
            level=input("請輸入文字選擇'困難'或'普通'模式 :")
        
if __name__ == '__main__':
    main()
    
    
    
    
    