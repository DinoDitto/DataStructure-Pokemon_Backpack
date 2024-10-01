import sys

###class
##pokemon
class Pokemon():
    def __init__(self):
        self.name = ''
        self.per = ''  #per = 個性
        self.attr = '' #attr = 屬性
        self.weight = 0
        self.height = 0
        self.bf = 0
        self.rlink = None
        self.llink = None
        
#avl tree
root_s = None
ptr_s = None
current_s = None
prev_s = None
pivot_s = None
pivot_prev_s = None
nodecount_s = 0

#heap
MAX_h = 100
last_index_h = 0
heap_tree_h = [Pokemon()]*MAX_h

##list
class List_node():
    def __init__(self):
        self.ID = 0      #識別節點
        self.n = 0       #節點內的鍵值數
        self.key = [0]*3    #節點內的鍵值
        self.link = [None]*3  #子節點

##隊伍系統
class Team():
    def __init__(self):
        self.name = ''
        self.amount = 0
        self.head = None
    
    @staticmethod
    def add_pokemon_team(poke):
        global tree_s
        global ptr_ss
        global current_ss
        global prev_ss
        global head_ss
        
        ptr_ss = Pokemon_in_team()
        ptr_ss.name = poke.name
        ptr_ss.per = poke.per
        ptr_ss.attr = poke.attr
        ptr_ss.height = poke.height
        ptr_ss.weight = poke.weight
    
        prev_ss = head_ss
        current_ss = head_ss.rlink
        while current_ss != head_ss and current_ss.name >= ptr_ss.name:
            prev_ss = current_ss
            current_ss = current_ss.rlink
        ptr_ss.rlink = current_ss
        ptr_ss.llink = prev_ss
        prev_ss.rlink = ptr_ss
        current_ss.llink = ptr_ss
    
    @staticmethod    
    def delete_pokemon_team(poke):
        global head_ss
        global current_ss
        global prev_ss
        
        if head_ss.rlink == head_ss:
            print('沒有這隻 Pokemon！ \n')
        else:
            prev_ss = head_ss
            current_ss = head_ss.rlink
            while current_ss != head_ss and poke.name != current_ss.name:
                prev_ss = current_ss
                current_ss = current_ss.rlink
                
            if current_ss != head_ss:
                prev_ss.rlink = current_ss.rlink
                current_ss.rlink.llink = prev_ss
                current_ss = None
                print('\nPokemon < %s > 已被移除出隊伍 \n' %poke.name)
            else:
                print('\n找不到 Pokemon : < %s > \n' %poke.name)

    @staticmethod
    def display_pokemon_team():
        global head_ss
        global current_ss
        
        count = 0
        
        if head_ss.rlink == head_ss:
            print('沒有 Pokemon 的紀錄！ \n')
        else:
            print('{:<8} {:<8} {:<8} {:<8} {:<8}'.format('名稱', '個性', '屬性', '身高(cm)', '體重(kg)'))  
            print('------------------------------------------------------', end = '')
            print()
            current_ss = head_ss.rlink
            while current_ss != head_ss:
                print('{:<11} {:<10} {:<10} {:<10} {:<8}'.format(current_ss.name, current_ss.per, current_ss.attr, current_ss.height, current_ss.weight))
                count += 1
                current_ss = current_ss.rlink
            
            print('------------------------------------------------------', end = '')
            print()
            print('總計 Pokemon : %d' %count)  

#m-way tree
MAX_pl = 3     
ptr_pl = None
root_pl = None
node_pl = None
prev_pl = None
parent_pl = None
replace_pl = None
id_seq_pl = ''

#heap
MAX_h_pl = 100
last_index_h_pl = 0
heap_tree_h_pl = [Team()]*MAX_h_pl
        
class Pokemon_in_team():
  def __init__(self):
      self.name = ''
      self.per = ''
      self.attr = ''
      self.height = 0
      self.weight = 0
        
      self.rlink = None
      self.llink = None
      
#linked list
ptr_ss = None
current_ss = None
prev_ss = None

head_ss = Pokemon_in_team()
head_ss.name = ''
head_ss.per = ''
head_ss.attr = ''
head_ss.height = 0
head_ss.weight = 0

head_ss.rlink = head_ss
head_ss.llink = head_ss



###平衡二元樹(pokemon)-insert, delete
#高度平衡樹 LL, RR, LR, RL 型
def type_ll():
    global root_s
    global pivot_s
    global pivot_prev_s

    pivot_next = pivot_s.llink
    temp = pivot_next.rlink
    
    pivot_next.rlink = pivot_s
    pivot_s.llink = temp
    
    if pivot_s == root_s:
        root_s = pivot_next
    elif pivot_prev_s.llink == pivot_s:
        pivot_prev_s.llink = pivot_next
    else:
        pivot_prev_s.rlink = pivot_next
        
def type_rr():
    global root_s
    global pivot_s
    global pivot_prev_s

    pivot_next = pivot_s.rlink
    temp = pivot_next.llink
    
    pivot_next.llink = pivot_s
    pivot_s.rlink = temp
    
    if pivot_s == root_s:
        root_s = pivot_next
    elif pivot_prev_s.llink == pivot_s:
        pivot_prev_s.llink = pivot_next
    else:
        pivot_prev_s.rlink = pivot_next
        
def type_lr():
    global root_s
    global pivot_s
    global pivot_prev_s

    pivot_next = pivot_s.llink
    temp = pivot_next.rlink
    
    pivot_s.llink = temp.rlink
    pivot_next.rlink = temp.llink
    
    if pivot_s == root_s:
        root_s = temp
    elif pivot_prev_s.llink == pivot_s:
        pivot_prev_s.llink = temp
    else:
        pivot_prev_s.rlink = temp

def type_rl():
    global root_s
    global pivot_s
    global pivot_prev_s

    pivot_next = pivot_s.rlink
    temp = pivot_next.llink
    
    pivot_s.llink = temp.llink
    pivot_next.rlink = temp.rlink
    
    if pivot_s == root_s:
        root_s = temp
    elif pivot_prev_s.llink == pivot_s:
        pivot_prev_s.llink = temp
    else:
        pivot_prev_s.rlink = temp

#平衡樹共同使用的function
def bf_count(trees):
    if trees != None:
        bf_count(trees.llink)     
        bf_count(trees.rlink) 
        #BF值計算方式為左子樹高減去右子樹高
        trees.bf = height_count(trees.llink) -  height_count(trees.rlink)   

def pivot_find():
    global root_s
    global current_s
    global prev_s
    global pivot_s
    global pivot_prev_s
    global nodecount_s
    
    current_s = root_s
    pivot_s = None
    
    for i in range(nodecount_s):
        #當BF值的絕對值.小於等於1，則將Pivot指向此節點
        if current_s.bf < -1 or current_s.bf > 1:
            pivot_s = current_s
            if pivot_s != root_s:
                pivot_prev_s = prev_s
        if current_s.bf > 0: #左子樹較高
            prev_s = current_s
            current_s = current_s.llink
        elif current_s.bf < 0: #右子樹較高
            prev_s = current_s
            current_s = current_s.rlink            
    return pivot_s

def type_find():
    global current_s
    global pivot_s
    
    op_r = 0 
    current_s = pivot_s
    for i in range(2):
        if current_s.bf > 0: #左子樹較高
            current_s = current_s.llink
            if op_r == 0:
                op_r += 10
            else:
                op_r += 1
        elif current_s.bf < 0: #右子樹較高
            current_s = current_s.rlink
            if op_r == 0:
                op_r += 20
            else:
                op_r += 2   
    return op_r

def height_count(trees):
    if trees == None:
        return 0
    elif trees.llink == None and trees.rlink == None:
        return 1
    elif height_count(trees.llink) > height_count(trees.rlink):
        return 1+ height_count(trees.llink)
    else:
        return 1+ height_count(trees.rlink)


##add pokemon
def add_pokemon():
  global nodecount_s
  global MAX_h
  global last_index_h

  name_t = ''
  per_t = ''
  attr_t = ''
  height_t = 0
  weight_t = 0

  print('\n******************** 加入 Pokemon  ********************')
  while True:
      try:
          name_t = input('請輸入 Pokemon 名稱: ')
          EmptyStringError(name_t)
          per_t = input('請輸入 Pokemon 個性: ')
          EmptyStringError(per_t)
          attr_t = input('請輸入 Pokemon 屬性: ')
          EmptyStringError(attr_t)
          height_t = int(input('請輸入 Pokemon 身高: '))
          weight_t = int(input('請輸入 Pokemon 體重: '))
          print('------------------------------------------------------')
          break
      except ValueError:
          print()
          print('輸入的資料類型錯誤，請再輸入一次！')
      except Exception as e:
          print(e)
  
  #建立 avl tree資料
  nodecount_s += 1
  sort_f(name_t, per_t, attr_t, height_t, weight_t)
  
  #建立heap資料(判斷式)
  if last_index_h >= MAX_h-1:
      print('\n背包空間已達上限 : %d!!' %MAX_h-1)
    
def sort_f(name_t, per_t, attr_t, height_t, weight_t):
  global ptr_s
  global root_s
  global current_s
  global prev_s
  global pivot_s

  op = 0
  current_s = root_s

  while current_s != None and name_t != current_s.name:
    if name_t < current_s.name:
      prev_s = current_s
      current_s = current_s.llink
    else:
      prev_s = current_s
      current_s = current_s.rlink
  
  if current_s == None or name_t != current_s.name:
    ptr_s = Pokemon()
    ptr_s.name = name_t
    ptr_s.per = per_t
    ptr_s.attr = attr_t
    ptr_s.height = height_t
    ptr_s.weight = weight_t
    ptr_s.llink = None
    ptr_s.rlink = None
    if root_s == None:
      root_s = ptr_s
    elif ptr_s.name < prev_s.name:
      prev_s.llink = ptr_s
    else:
      prev_s.rlink = ptr_s
    bf_count(root_s)
    pivot_s = pivot_find()
    if pivot_s != None:
      op = type_find()
      if op == 11:
        type_ll()
      elif op == 22:
        type_rr()
      elif op == 12:
        type_lr()
      elif op == 21:
        type_rl()
    bf_count(root_s)
    
    #建立heap資料  
    id_temp = Pokemon()
    id_temp.name = name_t
    id_temp.per = per_t
    id_temp.attr = attr_t
    id_temp.height = height_t
    id_temp.weight = weight_t
    create_pokemon_heap(id_temp) 

    print('Pokemon < %s > 已被加入！ ' % name_t)
  else:
    print('加入 Pokemon 時發生錯誤！ ')
    print('Pokemon < %s > 已經存在！ ' % name_t)
    

##delete Pokemon
def delete_pokemon():
    global root_s
    global current_s
    global prev_s
    global pivot_s
    global nodecount_s
    global heap_tree_h_pl
    
    clear = None
    name_t = ''
    tempn = ''
    
    id_temp = 0
    del_index = 0

    if root_s == None:
        print('\n沒有 Pokemon 存在！ ')
    else:
        print('\n******************** 刪除 Pokemon ********************')
        print('\nPokemon 一覽表 : ')
        display_pokemon_heap('increase') 
        name_t = input('請輸入你想刪除的 Pokemon : ')
        
        #刪除 Pokemon 時同時刪除隊伍中的 Pokemon
        heap_temp = [i for i in heap_tree_h_pl]
 
        poke_node = search_pokemon_node(name_t)
        for i in range(len(heap_temp)):
            current_list = heap_temp[i]
            current_list.amount -= 1
        current_list.delete_pokemon_team(poke_node)
        
        #刪除Pokemon
        tempn = name_t
        current_s = root_s
        while current_s != None and name_t != current_s.name:
            if name_t < current_s.name:
                prev_s = current_s
                current_s = current_s.llink
            else:
                prev_s = current_s
                current_s = current_s.rlink
                
        if current_s != None and name_t == current_s.name:
            if current_s.llink == None and current_s.rlink == None:
                clear = current_s
                if name_t == root_s.name:
                    root_s = None
                else:
                    if name_t < prev_s.name:
                        prev_s.llink = None
                    else:
                        prev_s.rlink = None
                clear = None
            else:
                if current_s.llink != None:
                    clear = current_s.llink
                    while clear.rlink != None:
                        prev_s = clear
                        clear = clear.rlink
                    current_s.name = clear.name
                    current_s.per = clear.per
                    current_s.attr = clear.attr
                    current_s.height = clear.height
                    current_s.weight = clear.weight
                    if current_s.llink == clear:
                        current_s.llink = clear.llink
                    else:
                        prev_s.rlink = clear.rlink
                else:
                    clear = current_s.rlink
                    while clear.llink != None:
                        prev_s = clear
                        clear = clear.llink
                    current_s.name = clear.name
                    current_s.per = clear.per
                    current_s.attr = clear.attr
                    current_s.height = clear.height
                    current_s.weight = clear.weight
                    if current_s.rlink == clear:
                        current_s.rlink = clear.rlink
                    else:
                        prev_s.llink = clear.rlink
                clear = None
            
            bf_count(root_s)
            if root_s != None:  # Pivot存在，則需改善為AVL-TREE
                pivot_s = pivot_find()
                while pivot_s != None:
                    op = type_find()
                    if op == 11:
                        type_ll()
                    elif op == 22:
                        type_rr()
                    elif op == 12:
                        type_lr()
                    elif op == 21:
                        type_rl()
                    pivot_s = pivot_find()
            nodecount_s -= 1
            
            #heap delete
            id_temp = name_t
            del_index = search_h(id_temp)
            removes_h(del_index)
                        
            print('\nPokemon < %s > 已被刪除 !' % tempn) 
        else:
            print('\n找不到 Pokemon < %s > !' % tempn)        


###m-way tree(team)-insert, delete
#m-way共同使用的function
def search_exist(name):
    global root_pl
    global node_pl
    global prev_pl
    global parent_pl
    
    node_pl = root_pl
    while node_pl != None:
        parent_pl = prev_pl
        prev_pl = node_pl
        i = 1
        done = 0
        while i <= node_pl.n:
            if name == node_pl.key[i].name:
                return i 
            if name < node_pl.key[i].name:
                node_pl = node_pl.link[i-1]
                done = 1
                break
            i += 1
        if done == 0:
            node_pl = node_pl.link[i-1]
    return 0

def find_next(node_temp):
    global node_pl
    global prev_pl
    
    prev_pl = node_pl
    if node_temp != None:
        while node_temp.link[0] != None:
            prev_pl = node_temp
            node_temp = node_temp.link[0]
    return node_temp

def find_prev(node_temp):
    global MAX_pl
    global node_pl
    global prev_pl
    
    prev_pl = node_pl
    if node_temp != None:
        while node_temp.link[MAX_pl-1] != None:
            prev_pl = node_temp
            node_temp = node_temp.link[MAX_pl-1]
    return node_temp

def moveleft(index):
    global node_pl
    for i in range(index, node_pl.n):
        node_pl.key[i] = node_pl.key[i+1]
        node_pl.link[i] = node_pl.link[i+1]
        
##add list
def add_team():
  new_list = Team()
  print('\n****************** 加入隊伍 ******************')
  while True:
      try:
          add_name = input('\n請輸入隊伍名稱 : ')
          EmptyStringError(add_name)
          break
      except Exception as e:
          print(e)
  new_list.name = add_name

  #建立 m-way tree資料
  create(new_list)
  
  #建立heap資料
  create_list_heap(new_list)
  print()

def create(new_list):
  global root_pl
  global ptr_pl
  global node_pl
  global prev_pl

  ans = 0
  i = 0
  if root_pl == None:
    initial() 
    ptr_pl.key[1] = new_list
    ptr_pl.n += 1
    root_pl = ptr_pl
    print('隊伍 < %s > 已被加入！' %new_list.name)
  else:
    ans = search_exist(new_list.name)
    if ans != 0:
      print('隊伍 < %s > 已存在！ ' %new_list.name)
    else:
      node_pl = search_node(new_list.name)
      if node_pl != None:
        i = 1
        while i < MAX_pl-1:
          if new_list.name < node_pl.key[i].name:
            break
          i += 1
        moveright(i , new_list)
      else:
        initial()
        ptr_pl.key[1] = new_list
        ptr_pl.n += 1
        i = 1
        while i < MAX_pl:
          if new_list.name < prev_pl.key[i].name:
            break
          i +=1
        prev_pl.link[i-1] = ptr_pl
      print('已增加隊伍 < %s > ！' %new_list.name)

def initial():
  global MAX_pl
  global ptr_pl

  ptr_pl = List_node()
  for i in range(MAX_pl):
    ptr_pl.link[i] = None
  ptr_pl.n = 0

def search_node(name):
    global MAX_pl
    global root_pl

    node_temp = root_pl
    
    while node_temp != None:
      if node_temp.n < MAX_pl-1:
        return node_temp
      else:
        i = 1
        done = 0
        while i < MAX_pl:
          if node_temp.n < i:
            break
          if name < node_temp.key[i].name:
            node_temp = node_temp.link[i-1]
            done = 1
            break
          i += 1
        if done == 0:
          node_temp = node_temp.link[i-1]
    return node_temp

def moveright(index, list):
    global node_pl

    i = node_pl.n + 1

    while i > index:
        node_pl.key[i] = node_pl.key[i-1]
        node_pl.link[i] = node_pl.link[i-1]
        i -= 1
    node_pl.key[i] = list

    if node_pl.link[i-1] != None and node_pl.link[i-1].key[0].name > list.name:
        node_pl.link[i-1] = node_pl.link[i-1]
        node_pl.link[i-1] = None
    node_pl.n += 1
  
##delete team
def delete_team():
    global root_pl
    global node_pl
    
    del_name = 0
    ans = 0
    
    if root_pl == None:
        print('\n找不到隊伍~~\n')
    else:
        print('\n****************** 刪除隊伍 ******************')
        print('\n隊伍一覽表 : ')
        display_team_heap('increase') 
        del_name = input('\n請輸入隊伍名稱 : ')
        #搜尋資料是否存在
        ans = search_exist(del_name)
        if ans == 0:
            print('找不到隊伍 < %s >\n' %del_name)
        else:
            removes(node_pl, ans)
            
            #heap delete
            id_temp = del_name
            del_index = search_h_pl(id_temp)
            removes_h_pl(del_index)
            
            print('隊伍 < %s > 已被刪除！ \n' %del_name)

def removes(node_temp, location):
    global root_pl
    global node_pl
    global prev_pl
    global parent_pl
    global replace_pl
    
    node_pl = node_temp
    replace_pl = find_next(node_pl.link[location])
    
    if replace_pl == None:
        replace_pl = find_prev(node_pl.link[location-1])
        if replace_pl == None:
            moveleft(location)
            replace_pl = node_pl
            if node_pl.n == 0:
                if node_pl == root_pl :
                    root_pl = None
                else :
                    for i in range(parent_pl.n+1):
                        if node_pl == parent_pl.link[i]:
                            parent_pl.link[i] = None
                            break
        else:
            node_pl.key[location] = replace_pl.key[replace_pl.n]
            parent_pl = prev_pl
            removes(replace_pl, replace_pl.n)
    else:
        node_pl.key[location] = replace_pl.key[1]
        parent_pl = prev_pl
        removes(replace_pl, 1)

###modify
#共同使用的function
def search_pokemon_node(poke_name): #用poke_name找到物件Pokemon()
    global current_s
    global root_s
    global prev_s
    
    current_s = root_s
    while current_s != None and poke_name != current_s.name:
        if poke_name < current_s.name:
            prev_s = current_s
            current_s = current_s.llink
        else:
            prev_s = current_s
            current_s = current_s.rlink
            
    return current_s

def search_team_node(list_name):
    global root_pl
    global node_pl
    global prev_pl
    global parent_pl
    
    node_pl = root_pl
    while node_pl != None:
        parent_pl = prev_pl
        prev_pl = node_pl
        i = 1
        done = 0
        while i <= node_pl.n:
            if list_name == node_pl.key[i].name:
                return node_pl
            if list_name < node_pl.key[i].name:
                node_pl = node_pl.link[i-1]
                done = 1
                break
            i += 1
        if done == 0:
            node_pl = node_pl.link[i-1]
    return 0


##add pokemon to team      
def add_pokemon_team():
    global root_pl
    global root_s
    
    list_name = ''
    
    if root_pl == None:
        print('\n找不到隊伍~~') 
        print('請新增一個隊伍！')
    else:
        print('\n**************** 將 Pokemon 加到隊伍中 ****************')
        print('\n隊伍一覽表 : ')
        display_team_heap('increase') 
        list_name = input('\n請選擇要將 Pokemon 加入的隊伍名稱 : ')
        list_key = search_exist(list_name) 
    
        if list_key != 0: 
            if root_s != None:
                print('\nPokemon 一覽表 : ')
                display_pokemon_heap('increase')
                pokemon_name = input('\n請輸入 Pokemon 名稱 : ')
     
                pokemon_node = search_pokemon_node(pokemon_name) #找到物件Pokemon()
                list_node = search_team_node(list_name) #找到物件Pokemon_list()
                
                current_list = list_node.key[list_key] 
                current_list.amount += 1
                current_list.add_pokemon_team(pokemon_node)
                print('Pokemon 已加入隊伍中！')
            else:
                print('\n找不到 Pokemon')
                print('請輸入一個 pokemon！')
        else:
            print('隊伍 < %s > 不存在' %list_name)

##delete pokemon in team
def delete_pokemon_in_team():
    global root_pl
    
    list_name = ''
    
    if root_pl == None:
        print('\n找不到隊伍~~\n')
    else:
        print('\n************* 從隊伍中將 Pokemon 移除 *************')
        print('\n隊伍一覽表 : ')
        display_team_heap('increase') 
        list_name = input('\n請選擇要將 Pokemon 刪除的隊伍名稱 : ')
        list_key = search_exist(list_name) 
    
        if list_key != 0: 
            list_node = search_team_node(list_name) #找到物件Team()
            current_list = list_node.key[list_key]
            current_list.display_pokemon_team()
            
            if current_list.amount != 0:
                poke_name = input('\n請輸入 Pokemon 名稱 : ')
                poke_node = search_pokemon_node(poke_name) #找到物件Pokemon()            
                current_list.amount -= 1
                current_list.delete_pokemon_team(poke_node)
                print('Pokemon 已從隊伍中移除！')
            else:
                print('隊伍中已經沒有 Pokemon')
        else:
            print('隊伍 < %s > 不存在！' %list_name)

def modify_team_name():
    if root_pl == None:
        print('\n找不到隊伍~~\n')
    else:
        print('\n*************** 編輯隊伍名稱 ***************')
        print('\n隊伍一覽表 : ')
        display_team_heap('increase') 
        list_name = input('\n請選擇要編輯的隊伍名稱 : ')
        list_key = search_exist(list_name)
        
        if list_key != 0: 
            list_node = search_team_node(list_name) #找到物件Team()
            current_list = list_node.key[list_key]
            new_list_name = input('請輸入新的隊伍名稱 : ')
            current_list.name = new_list_name
            print('隊伍名稱已改為 < %s >' %new_list_name)
        else:
            print('隊伍 < %s > 不存在！' %list_name)          


###道具
#佇列
MAX_q = 5
queu_q = ['']*MAX_q
front_q = MAX_q-1
rear_q = MAX_q-1
tag_q = 0     #當tag為0時，表示沒有存放資料；若未1，則表示有存放資料
count = 0

def init_queue():
    global MAX_q
    global queu_q
    global front_q
    global rear_q
    global tag_q
    global count
    
    queu_q = ['']*MAX_q
    front_q = MAX_q-1
    rear_q = MAX_q-1
    tag_q = 0
    count = 0

#加入道具
def insert_item(): #enqueue
    global MAX_q
    global queu_q
    global front_q
    global rear_q
    global tag_q
    global count
    
    print('\n********* 新增道具 *********\n')
    if front_q == rear_q and tag_q == 1:  #佇列已滿
        print("\n背包已滿")
    else:
        rear_q = (rear_q+1) % MAX_q
        queu_q[rear_q] = input('\n請輸入要新增的道具: ')
        count += 1
        if front_q == rear_q:
            tag_q = 1    

#刪除道具
def delete_item():
    global MAX_q
    global queu_q
    global front_q
    global rear_q
    global tag_q
    global count
    
    global MAX_q
    global front_q
    global queu_q
    global rear_q
    global tag_q
    global count
    
    if front_q == rear_q and tag_q == 0:
        print("沒有道具哦 !")
    else:
        front_q = (front_q+1)%MAX_q
        print("\n< %s > 已被刪除" %queu_q[front_q])
        count -= 1
    
        if front_q == rear_q:
            tag_q = 0
            
def search_item(item_name):
    global MAX_q
    global queu_q
    global front_q
    global rear_q
    global tag_q
    
    i = (front_q+1) % MAX_q
    while i != rear_q+1:
        if queu_q[i] == item_name:
            return (queu_q[i], i)
        i = (i+1) % MAX_q
    print('\n背包中找不到 < %s > \n' %item_name) 
    return (0,0)    

#移除所有道具                
def remove_all_item():
    init_queue()
    print('\n已清空背包！ \n')

def show_item():
    global MAX_q
    global queu_q
    global front_q
    global rear_q
    global tag_q
    global count
    
    ptr = None
    
    if front_q== rear_q and tag_q == 0:
        print('\n沒有道具喔！ \n')
    else:
        print('\n********* 道具一覽表 *********\n')
        print('--------------------------------------------')
        i = (front_q+1) % MAX_q
        while i != rear_q:
            ptr = queu_q[i]
            print(ptr)
            i = (i+1) % MAX_q
        print(queu_q[i])
        print('--------------------------------------------')
        print('目前道具總數 : %d' %count)


###show - heap
#show共同使用的function
def exchange(arr, id1, id2):
    id_temp = arr[id1]
    arr[id1] = arr[id2]
    arr[id2] = id_temp

def adjust_d(temp, index1, index2):
    id_temp = temp[index1]
    index_temp = index1 * 2
    
    while index_temp <= index2:
        if index_temp < index2 and temp[index_temp].name < temp[index_temp+1].name:
            index_temp += 1
        if id_temp.name >= temp[index_temp].name:
            break
        else:
            temp[index_temp//2].name = temp[index_temp].name
            index_temp *= 2
    temp[index_temp//2] = id_temp

def adjust_u(temp, index):
    while (index > 1):
        if temp[index].name >= temp[index//2].name:
            break
        else:
            exchange(temp, index, index//2)
        index //= 2

def search_h(id_temp):
    global heap_tree_h
    
    for c_index in range(1, len(heap_tree_h)):
        if id_temp == heap_tree_h[c_index].name:
            return c_index
    return 0

def create_pokemon_heap(id_temp): 
    global last_index_h
    global heap_tree_h
    
    last_index_h += 1
    heap_tree_h[last_index_h] = id_temp

    adjust_u(heap_tree_h, last_index_h)


def removes_h(index_temp):
    global last_index_h
    global heap_tree_h
    
    heap_tree_h[index_temp] = heap_tree_h[last_index_h]
    heap_tree_h[last_index_h] = Pokemon()
    last_index_h -= 1
    
    if last_index_h > 1:
        if heap_tree_h[index_temp].name > heap_tree_h[index_temp//2].name and index_temp > 1:
            adjust_u(heap_tree_h, index_temp)
        else:
            adjust_d(heap_tree_h, index_temp, last_index_h-1)

def search_h_pl(id_temp):
    global heap_tree_h_pl
    
    for c_index in range(1, len(heap_tree_h_pl)):
        if id_temp == heap_tree_h_pl[c_index].name:
            return c_index
    return 0

def create_list_heap(node):
    global last_index_h_pl
    global heap_tree_h_pl
    last_index_h_pl += 1
    heap_tree_h_pl[last_index_h_pl] = node
    adjust_u(heap_tree_h_pl, last_index_h_pl)

def removes_h_pl(index_temp):
    global last_index_h_pl
    global heap_tree_h_pl
    
    heap_tree_h_pl[index_temp] = heap_tree_h_pl[last_index_h_pl]
    heap_tree_h_pl[last_index_h_pl] = Team()
    last_index_h_pl -= 1
    
    if last_index_h_pl > 1:
        if heap_tree_h_pl[index_temp].name > heap_tree_h_pl[index_temp//2].name and index_temp > 1:
            adjust_u(heap_tree_h_pl, index_temp)
        else:
            adjust_d(heap_tree_h_pl, index_temp, last_index_h_pl-1)

##show Pokemon
def show_pokemon():
    display_pokemon_heap('ask')

def display_pokemon_heap(ask_or_increase): 
    if ask_or_increase == 'ask':
        op = ask_order_h_pokemon()
    elif ask_or_increase == 'increase':
        op = '2'
    if op != '0':    
        show_heap_pokemon(op)
        
def ask_order_h_pokemon():
    global last_index_h
    option = ''
    
    if last_index_h < 1:
        print('\n無資料可顯示 \n') 
        option = '0'
    else:
        while True:
            print()
            print('<1> From A to Z')
            print('<2> From Z to A')
            
            try:
                option = input('\n請輸入功能 : ')
                OptionError(option, '1', '2')
                break
            except ValueError:
                print()
                print('查無此功能，請再輸入一次！\n')
            except Exception as e:
                print(e)
            if(option == '1' or option == '2'):
                break
    return option

def show_heap_pokemon(op):
    global last_index_h
    global heap_tree_h
    
    heap_temp = []
    
    heap_temp = [i for i in heap_tree_h]
    c_index = last_index_h - 1
    
    while c_index > 0:
        exchange(heap_temp, 1, c_index+1)
        adjust_d(heap_temp, 1, c_index)
        c_index -= 1
    print('{:<8} {:<8} {:<8} {:<8} {:<8}'.format("名稱", "個性", "屬性", "身高(cm)", "體重(kg)"))
    print('======================================================')
    
    if op == '2':
        for c_index in range(1, last_index_h+1):
            print('{:<11}'.format(heap_temp[c_index].name), end = '')
            print('{:<10}'.format(heap_temp[c_index].per), end = '') 
            print('{:<10}'.format(heap_temp[c_index].attr), end = '') 
            print('{:<10}'.format(heap_temp[c_index].height), end = '')
            print('{:<8}'.format(heap_temp[c_index].weight))
    elif op == '1':
        c_index = last_index_h
        
        while c_index > 0:
            print('{:<11}'.format(heap_temp[c_index].name), end = '')
            print('{:<10}'.format( heap_temp[c_index].per), end = '') 
            print('{:<10}'.format(heap_temp[c_index].attr), end = '') 
            print('{:<10}'.format(heap_temp[c_index].height), end = '')
            print('{:<8}'.format(heap_temp[c_index].weight))
            c_index -= 1
            
    print('------------------------------------------------------')
    print('Pokemon 總數 : ', last_index_h, '\n')
          
##show Team
def show_team():
    display_team_heap('ask') 

def display_team_heap(ask_or_increase): 
    if ask_or_increase == 'ask':
        op = ask_order_h_pl() 
    elif ask_or_increase == 'increase':
        op = '1'
    if op != '0':
        show_heap_team(op)

def ask_order_h_pl():
    global last_index_h_pl
    option = ''
    
    if last_index_h_pl < 1:
        print('\n無資料可顯示 \n')
        option = '0'
    else:
        while True:
            print()
            print('<1> From A to Z')
            print('<2> From Z to A')
        
            try:
                option = input('\n請輸入功能 : ')
                OptionError(option, '1', '2')
                break
            except ValueError:
                print()
                print('查無此功能，請再輸入一次！\n')
            except Exception as e:
                print(e)
            if(option == '1' or option == '2'):
                break
    return option

def show_heap_team(op):
    global last_index_h_pl
    global heap_tree_h_pl
    heap_temp = []

    heap_temp = [i for i in heap_tree_h_pl]        
    c_index = last_index_h_pl - 1
    while c_index > 0:
        exchange(heap_temp, 1, c_index+1)
        adjust_d(heap_temp, 1, c_index)
        c_index -= 1
    print('\n{:<8} {:<8}' .format('隊伍名稱', 'Pokemon 數量'))
    print('-----------------------------------------------------')
    
    
    if op == '2':
        for c_index in range(1, last_index_h_pl +1):
            print('{:<12} {:<8}' .format(heap_temp[c_index].name, heap_temp[c_index].amount))
    elif op == '1' :
        c_index = last_index_h_pl
        while c_index > 0:
            print('{:<12} {:<8}'.format(heap_temp[c_index].name, heap_temp[c_index].amount))
            c_index -= 1
            
    print('-----------------------------------------------------')
    print('隊伍總數 : ', last_index_h_pl, '\n')

##show Pokemon in Team
def show_pokemon_team():
    global root_pl
    
    list_name = ''
    
    if root_pl == None:
        print('\n無資料可顯示 \n')
    else:
        print('\n隊伍一覽表 : ')
        display_team_heap('increase') 
        list_name = input('\n請選擇要展示的隊伍 : ')
        list_key = search_exist(list_name) 
    
        if list_key != 0:
            list_node = search_team_node(list_name) #找到物件Team()
            current_list = list_node.key[list_key] #找到物件Team()
            current_list.display_pokemon_team()
        else:
            print('隊伍 < %s > 不存在！' %list_name)
            
            
            
###search
##binary tree及Stack要用的class及變數
#binary tree
class BT:
    def __init__(self):
        self.name = ''
        self.per = ''  #per = 個性
        self.attr = '' #attr = 屬性
        self.weight = 0
        self.height = 0
        self.llink = None
        self.rlink = None
    
root_bt = None
count_bt = 0

def init_BT():
    global root_bt
    global count_bt
    root_bt = None
    count_bt = 0

#stack
MAX_st = 100
st_st = [''] * MAX_st
top_st = -1

def init_stack():
    global MAX_st
    global st_st
    global top_st
    st_st = [''] * MAX_st
    top_st = -1
    
    
##search_pokemon_by
def search_pokemon_by(sort):
    global root_s
    global root_pl
    global rear_q
    global MAX_st
    global st_st
    global top_st

#操作:一個一個節點跑 -> 判斷此節點是否符合 -> 符合者加入二元樹/堆疊 -> 列出二元樹/堆疊內容    
    if sort == 'Pokemon' or sort == 'Attribute':
        #若以Pokemon或Attribute搜尋，以queue處理
        if root_s == None:
            print('\n無資料可搜尋 \n')
            return
        print('\n********************** 搜尋 Pokemon 或隊伍 ***********************')
        search_temp = input('請輸入關鍵字 :' )
        inorder_search_bt(search_temp, root_s, sort) #sort:尋找依據(Pokemon/Attribute)
        show_bt()
        init_BT() #把二元樹清空
    
    elif sort == 'Team':
        if root_pl == None:
            print('\n無資料可搜尋 \n')
            return
        #若以Team搜尋，以stack處理
        print('\n********************** 搜尋 Pokemon 或隊伍 ***********************')
        search_temp = input('請輸入關鍵字 :' )
        preorder_search_3way(search_temp, root_pl)
        list_stack()
        init_stack() #把堆疊清空


##佇列queue-搜尋pokemon或attribute時
#對二元樹用中序的方式一個一個節點進行符不符合關鍵字的判斷
def inorder_search_bt(word, node_temp, sort):
    if node_temp != None:
        inorder_search_bt(word, node_temp.llink, sort)
        run_search_bt(word, node_temp, sort) #進行判斷
        inorder_search_bt(word, node_temp.rlink, sort)

#進行pokemon或attribute的關鍵字判斷
def run_search_bt(word, node_temp, sort):
    l = len(word)
    ans = 0
    target = node_temp #target設為現在傳入的節點
    
    if sort == 'Pokemon':
        if len(target.name) >= len(word):
            for i in range(l): #i代表關鍵字的字數
                if word[i] == target.name[i]: #把關鍵字的第i個字和pokemon名的第i個字做判斷
                    ans = 1
                else:
                    ans = 0  
        else:
            for i in range(len(target.name)):
                if word[i] == target.name[i]: #把關鍵字的第i個字和pokemon名的第i個字做判斷
                    ans = 1
                else:
                    ans = 0  
    elif sort == 'Attribute':
        if len(target.attr) >= len(word):
            for i in range(l): #i代表關鍵字的字數
                if word[i] == target.attr[i]: #把關鍵字的第i個字和attribute名的第i個字做判斷
                    ans = 1
                else:
                    ans = 0  
        else:
            for i in range(len(target.attr)):
                if word[i] == target.attr[i]: #把關鍵字的第i個字和attribute名的第i個字做判斷
                    ans = 1
                else:
                    ans = 0
    
    if ans == 1: #如果最後的結果為1
        insert_bt(target) #就把這個節點加入二元樹

#加入二元樹
def insert_bt(node):
    global root_bt
    ptr = None
    prev = None
    
    if search_bt(node.name) != None:    #檢查此名字是否已經存在
        print('已搜尋到 Pokemon < %s > ' %node.name)
        return
    
    ptr = BT()
    ptr.name = node.name
    ptr.per = node.per
    ptr.attr = node.attr
    ptr.height = node.height
    ptr.weight = node.weight
    ptr.llink = None    #事實上llink及rlink已在Ｐokemon()時定義為None了
    ptr.rlink = None    #重新指定只是增加可讀性
    if root_bt == None:
        root_bt = ptr
    else:
        node = root_bt
        while node != None:
            prev = node
            if ptr.name < node.name:
                node = node.llink
            else:
                node = node.rlink
        if ptr.name < prev.name:
            prev.llink = ptr
        else:
            prev.rlink = ptr

def search_bt(target):
    global root_bt
    node = root_bt
    while node != None:
        if target == node.name:
            return node
        elif target < node.name:
            node = node.llink
        elif target > node.name:
            node = node.rlink
    return node

#列出二元樹
def show_bt():
    global root_bt
    global count_bt
    if root_bt == None:
        print('\n無資料顯示~~ \n')
        return
    print('\n{:<8} {:<8} {:<8} {:<8} {:<8}'.format("名稱", "個性", "屬性", "身高(cm)", "體重(kg)"))
    print('-----------------------------------------------------')
    inorder(root_bt)
    print('-----------------------------------------------------')
    print('Pokemon 總數 : %d' %count_bt)
    
def inorder(node):
    global count_bt
    if node != None:
        inorder(node.llink)
        print('{:<10} {:<9} {:<10} {:<9} {:<8}'.format(node.name, node.per, node.attr, node.height, node.weight))
        count_bt += 1
        inorder(node.rlink)
  
      
##堆疊Stack-搜尋team時
#對m-way樹用前序的方式一個一個資料進行符不符合關鍵字的判斷
def preorder_search_3way(word, tree):
    if tree != None:
        for i in range(1, tree.n+1): #到達某一節點時，先對節點內的資料作判斷
            run_search_3way(word, tree.key[i])
        for i in range (tree.n+1):
            preorder_search_3way(word, tree.link[i]) #判斷完結點內資料再依序跑子節點

#進行team的關鍵字判斷
def run_search_3way(word, node):
    if type(node) is Team :
        l = len(word)
        ans = 0
    
        if len(node.name) >= len(word):
            for i in range(l): #i代表關鍵字的字數
                if word[i] == node.name[i]: #把關鍵字的第i個字和pokemon名的第i個字做判斷
                    ans = 1
                else:
                    ans = 0  
        else:
            for i in range(len(node.name)):
                if word[i] == node.name[i]: #把關鍵字的第i個字和pokemon名的第i個字做判斷
                    ans = 1
                else:
                    ans = 0 
        if ans == 1: #如果最後的結果為1
            push_st(node) #就把這個節點加入佇列

def push_st(node):
    global MAX_st
    global st_st
    global top_st
    
    #當堆疊已滿(符合條件的結果太多)，則要求重新搜尋
    if top_st >= MAX_st-1:
        print('\n     ... 資料太多無法顯示 ...     ')
        print('... 請再輸入更多關鍵字！ ...')
        search_pokemon_by('Team')
    else: 
        if type(node) is Team:
            top_st += 1
            st_st[top_st] = node

def list_stack():
    global st_st
    global top_st
    
    count = 0
    
    if top_st<0:
        print('\n無資料顯示~~ ')
    else:
        print('\n%-10s %s' %('隊伍名稱', 'Pokemon 總數'))
        print('-----------------------------------------------------')
        i = top_st
        while i >= 0:
            if type(st_st[i]) is Team:
                print('%-10s %d' %(st_st[i].name, st_st[i].amount))
                count += 1
            i -= 1
        print('-----------------------------------------------------')
        print('Pokemon 總數 : %d' %count)
        
    
###錯誤訊息
def OptionError(op, op1, op2):
    if op < op1 or op > op2:
        raise Exception("查無此功能，請再輸入一次！")
        
def EmptyStringError(st):
    if st == '':
        raise Exception("不能輸入空字串喔，請再輸入一次！")

        

###main
def main():
    option = 0
    
    while True:
        print('\n請選擇要使用下列何種功能 : ')
        print('<1> 新增  ')
        print('<2> 刪除  ')
        print('<3> 編輯  ')
        print('<4> 道具  ')
        print('<5> 展示  ')
        print('<6> 搜尋  ')
        print('<7> 離開  ')
        print('-----------------------------------------------------')
        
        try:
            option = int(input('功能:'))
            OptionError(option, 1, 7)
        except ValueError:
            print()
            print('查無此功能，請再輸入一次！')
        except Exception as err:
            print(err)
            
        if option == 1:
            
            choice = 0
    
            while True:
              print('\n<1> 新增 Pokemon')
              print('<2> 新增隊伍')
              print('-----------------------------------------------------')
            
              try:
                    choice = int(input('功能:'))
                    OptionError(choice, 1, 2)
                    break
              except ValueError:
                    print()
                    print('查無此功能，請再輸入一次！')
              except Exception as err :
                    print(err)
                
            if choice == 1:
                  add_pokemon()
            elif choice == 2:
                  add_team()
                
        elif option == 2:
            
            choice = 0
    
            while True:
              print('\n<1> 刪除 Pokemon')
              print('<2> 刪除隊伍')
              print('-----------------------------------------------------')
            
              try:
                    choice = int(input('功能:'))
                    OptionError(choice, 1, 2)
                    break
              except ValueError:
                    print()
                    print('查無此功能，請再輸入一次！')
              except Exception as err :
                    print(err)
            if choice == 1:
                delete_pokemon()
            elif choice == 2:
                delete_team()
        
        elif option == 3:
            
            choice = 0
    
            while True:
              print('\n<1> 將 Pokemon 新增到隊伍中')
              print('<2> 將 Pokemon 從隊伍中刪除')
              print('<3> 編輯隊伍名稱')
              print('-----------------------------------------------------')
            
              try:
                    choice = int(input('功能:'))
                    OptionError(choice, 1, 3)
                    break
              except ValueError:
                    print()
                    print('查無此功能，請再輸入一次！')
              except Exception as err:
                    print(err)
                  
            if choice == 1:
                add_pokemon_team()
            elif choice == 2:
                delete_pokemon_in_team()
            elif choice == 3:
                modify_team_name()
        
        elif option == 4:
             
            choice = 0
    
            while True: 
              print('\n<1> 新增道具')
              print('<2> 刪除即期道具')
              print('<3> 列出所有道具')
              print('<4> 刪除所有道具')
              print('-----------------------------------------------------')
            
              try:
                    choice = int(input('功能:'))
                    OptionError(choice, 1, 4)
                    break
              except ValueError:
                    print()
                    print('查無此功能，請再輸入一次！')
              except Exception as err:
                    print(err)
            
            if choice == 1:
                insert_item()
            elif choice == 2:
                delete_item()
            elif choice == 3:
                show_item()
            elif choice == 4:
                remove_all_item()


        elif option == 5:
            
            choice = 0
    
            while True: 
              print('\n<1> 列出所有 Pokemon')
              print('<2> 列出所有隊伍')
              print('<3> 列出隊伍中的 Pokemon')
              print('-----------------------------------------------------')
            
              try:
                    choice = int(input('功能:'))
                    OptionError(choice, 1, 3)
                    break
              except ValueError:
                    print()
                    print('查無此功能，請再輸入一次！')
              except Exception as err:
                    print(err)
            
            if choice == 1:
                show_pokemon()
            elif choice == 2:
                show_team()
            elif choice == 3:
                show_pokemon_team()

        elif option == 6:
            
            choice = 0
    
            while True:
              print('\n<1> 利用名稱搜尋 Pokemon')
              print('<2> 利用屬性搜尋 Pokemon')
              print('<3> 搜尋隊伍')
              print('-----------------------------------------------------')
            
              try:
                    choice = int(input('功能:'))
                    OptionError(choice, 1, 3)
                    break
              except ValueError:
                    print()
                    print('查無此功能，請再輸入一次！')
              except Exception as err:
                    print(err)
            
            if choice == 1:
                  search_pokemon_by('Pokemon')   
            elif choice == 2:
                  search_pokemon_by('Attribute') 
            elif choice == 3:
                  search_pokemon_by('Team')

        elif option == 7:
            sys.exit(0)
            
main()