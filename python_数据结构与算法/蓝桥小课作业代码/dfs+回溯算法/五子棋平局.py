def is_win(player, rows, cols, diag1, diag2, anti_diag):
    # 检查行
    for r in rows:
        if r == player * 5:
            return True
    # 检查列
    for c in cols:
        if c == player * 5:
            return True
    # 检查主对角线
    if diag1 == player * 5 or anti_diag == player * 5:  # 注意：在5x5棋盘上，反对角线和主对角线有重叠，但这里为了通用性分开处理
        return True
    # 检查副对角线（非5x5棋盘上可能与主对角线不同）
    diag2_check = sum(mp[i][4-i] for i in range(5))  # 直接计算，不依赖外部变量
    if diag2_check == player * 5:
        return True
    return False

def dfs(depth, player, rows, cols, diag1, diag2_count, anti_diag_count, count_player, count_opponent):
    global ans
    
    # 棋盘已满，检查是否平局
    if depth == 25:
        if not is_win(1, rows, cols, diag1, diag2_count, anti_diag_count) and not is_win(-1, rows, cols, diag1, diag2_count, anti_diag_count):
            ans += 1
        return
    
    # 剪枝：如果当前玩家已经不可能胜利（比如没有空位可以形成连续五个棋子），则剪枝
    # 这里还可以加入更复杂的剪枝逻辑，比如检查对手是否接近胜利等
    if all(r < 4 for r in rows if r != -player*5) and all(c < 4 for c in cols if c != -player*5) and diag1 < 4 and (4-depth if player==1 else depth) not in {diag2_count-4, anti_diag_count-4}:  # 简单的剪枝条件示例
        return
    
    # 尝试在当前深度放置棋子
    for i in range(5):
        for j in range(5):
            if not rows[i] and not cols[j] and (i == j and not diag1) and (abs(i - j) == 4 and (diag2_count if player == 1 else anti_diag_count) < 4):  # 额外的剪枝条件：不放置会导致立即输掉的棋子
                # 标记当前位置为已占用，并更新相关变量
                rows[i] = cols[j] = player
                if i == j:
                    diag1 += player
                elif i + j == 4:
                    diag2_count += player  # 使用计数器而不是布尔变量，以便在5x5以外的棋盘上使用
                else:
                    anti_diag_count += player  # 同上
                
                # 递归调用DFS
                dfs(depth + 1, -player, rows[:], cols[:], diag1, diag2_count, anti_diag_count, count_player + 1, count_opponent if player == 1 else count_player)
                
                # 回溯：标记当前位置为未占用，并更新相关变量
                rows[i] = cols[j] = 0
                if i == j:
                    diag1 -= player
                elif i + j == 4:
                    diag2_count -= player
                else:
                    anti_diag_count -= player

# 初始化全局变量和棋盘状态（这里不使用全局棋盘mp，而是直接在rows和cols中跟踪状态）
ans = 0
rows = [0] * 5
cols = [0] * 5
diag1 = 0
diag2_count = 0  # 使用计数器来跟踪副对角线的状态（在5x5棋盘上也可以只用布尔值，但为了通用性使用计数器）
anti_diag_count = 0  # 同上，跟踪反对角线的状态

# 开始DFS搜索
dfs(0, 1, rows, cols, diag1, diag2_count, anti_diag_count, 0, 0)  # 从第一个位置开始，玩家1（白棋）先下

# 输出结果（注意：这个结果可能需要很长时间才能得到，因为五子棋的状态空间非常巨大）
print(ans)
