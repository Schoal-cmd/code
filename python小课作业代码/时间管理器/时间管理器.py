import datetime,time

input("欢迎使用“时间管理器”！请按回车继续。")

while True: 

    #开启循环并收集任务信息
    task_name = input('请输入任务名：')
    task_time = float(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始计时：'%(task_name,task_time))
    
    #开始计算并打印时间
    start_time = datetime.datetime.now()
    print(start_time)
    
    #倒计时实时显示时间
    count=0
    task_times=task_time*60
    while count<task_times:
        surplus=task_times-count
        print('任务的剩余时间：%d秒'%(surplus))
        count+=60
        time.sleep(60)
    
    #结束任务
    task_status = input('请在任务完成后按输入y:')
    if task_status == 'y':

        #计算实际时长
        end_time=datetime.datetime.now()
        actual_time=end_time-start_time

        #追加文件（使用反馈）
        with open('timelog2.txt','a', encoding = 'utf-8') as f:
                f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
                f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟\n')
       
        #是否开启新任务
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':            
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

#结束语
print('愿被你善待的时光，予你美好的回赠。')

