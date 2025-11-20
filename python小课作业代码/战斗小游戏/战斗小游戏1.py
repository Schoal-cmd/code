#战斗小游戏之数据类型转换版
import time,random

while True:  #设置循环，以实现再来一局
    print('游戏开始，该游戏为三局两胜制')
    player_score=0  #计分法
    enemy_score=0
    
    for i in range(3):
        
        time.sleep(2)   # 让局与局之间有较明显的有时间间隔
        print(f"现在是第{i+1}局")   # 作为局的标记

        player_life = random.randint(100,150) 
        player_attack = random.randint(30,50) 
        enemy_life = random.randint(100,150) 
        enemy_attack = random.randint(30,50) 
        
        # 展示双方角色的属性
        print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
        print('------------------------')
        time.sleep(1)
        print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
        print('------------------------')
        time.sleep(1)
        
        # 双方PK
        while (player_life >0) and (enemy_life > 0):
            player_life = player_life - enemy_attack 
            enemy_life = enemy_life - player_attack 
            print('你发起了攻击，【敌人】剩余血量'+str(enemy_life))
            print('敌人向你发起了攻击，【玩家】剩余血量'+str(player_life))
            print('------------------------')
            time.sleep(1.5)
    
        #打印单局战果
        if player_life <= 0 and enemy_life > 0:
            print('玩家失败，敌人获胜')
            enemy_score=enemy_score+1
        elif enemy_life <= 0 and player_life > 0:
            print('敌人失败，玩家获胜')
            player_score=player_score+1
        else:
            print('玩家与敌人平局')    
    time.sleep(2)
    
    #打印最终战果
    if player_score>enemy_score:
        print('三局结束，恭喜玩家获胜~~')
    elif player_score<enemy_score:
        print('三局结束，悲催玩家你被打败了')
    else:
        print('wow玩家你和敌人平局哦')
    
    #是否再来一局
    again=input('要继续游戏吗？请输入‘n’退出，输入其他键继续')
    if again=='n':
        break
print('游戏结束')