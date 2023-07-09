import random
import requests
import json

def game():
    print('\n   ###コマンド一覧###\ni:ステータス確認, help:ゲーム説明, q:終了\n')

    #主人公のステータス
    player_hp = 100
    weapon = None
    armor = None
    get_item = None

    # マップのサイズ
    MAP_WIDTH = 30
    MAP_HEIGHT = 10

    #キャラクターの初期位置
    player_x = random.randint(0, MAP_WIDTH - 1)
    player_y = random.randint(0, MAP_HEIGHT - 1)

    #各アイテムの内容
    tool_list = ['包帯(+10)','薬草(+20)']
    weapon_list = ['勇者の剣(+30)','錆びた剣(+15)','こんぼう(+5)']
    armor_list = ['勇者の盾(+30)','鉄の盾(+20)','鍋の蓋(+10)']

    # 各アイテムの位置
    item_x = random.randint(0, MAP_WIDTH - 1)
    item_y = random.randint(0, MAP_HEIGHT - 1)

    tool_x = random.randint(0, MAP_WIDTH - 1)
    tool_y = random.randint(0, MAP_HEIGHT - 1)

    weapon_x = random.randint(0, MAP_WIDTH -1)
    weapon_y = random.randint(0,MAP_HEIGHT -1)

    armor_x = random.randint(0, MAP_WIDTH -1)
    armor_y = random.randint(0, MAP_HEIGHT -1)

    #敵の位置
    enemy_x = random.randint(0,MAP_WIDTH -1)
    enemy_y = random.randint(0,MAP_HEIGHT -1)

    #敵のステータス
    enemy_hp = 50

    # ゲームループ
    while True:
        # マップの描画
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if x == player_x and y == player_y:
                    print("@", end="")
                elif x == tool_x and y == tool_y:
                    print("T", end="")
                elif x == weapon_x and y == weapon_y:
                    print('W',end="")
                elif x == armor_x and y== armor_y:
                    print('A',end="")
                elif x == enemy_x and y == enemy_y:
                    print('E', end="")
                else:
                    print(".", end="")
            print()
        # ユーザー入力の処理
        print(f'HP:{player_hp} 攻撃力:{weapon} 防御力:{armor}')
        command = input("移動方向を入力してください (w:上, a:左, s:下, d:右): ")

        #プレイヤーと敵の攻撃力をランダム生成
        player_attack = random.randint(10,30)
        enemy_attack = random.randint(40,70)
        print(f'x:{enemy_x} y:{enemy_y}')

        #敵をランダムに動かす
        enemy_x_move = random.randint(-1, 1)
        enemy_y_move = random.randint(-1, 1)
        if enemy_x_move == 0:
            enemy_y = enemy_y + enemy_y_move
        enemy_x = enemy_x + enemy_x_move

        # 入力されたコマンド
        if command == "w" and player_y > 0:
            player_y -= 1
        elif command == "a" and player_x > 0:
            player_x -= 1
        elif command == "s" and player_y < MAP_HEIGHT -1:
            player_y += 1
        elif command == "d" and player_x < MAP_WIDTH -1:
            player_x += 1
        elif command == "help":
            print('\n@が自分自身　Tはツール　Wは武器　Aは防具　Eはモンスター\n')
        elif command == "i":
            print(f' \n === ステータス === \n武器 {weapon}\n防具 {armor}\n道具 {get_item}') 
        elif command == "q":
            break
        
        # 各アイテムの収集
        if player_x == tool_x and player_y == tool_y:
            tool_x = None
            tool_y = None
            get_item = tool_list[random.randint(0, len(tool_list)) -1]
            print(f'\n[・] {get_item}を入手しました')
        elif player_x == weapon_x and player_y == weapon_y:
            weapon_x = None
            weapon_y = None
            weapon = weapon_list[random.randint(0, len(weapon_list)) -1]
            print(f'\n[・] {weapon}を入手しました')
        elif player_x == armor_x and player_y == armor_y:
            armor_x = None
            armor_y = None
            armor = armor_list[random.randint(0, len(armor_list)) -1]
            print(f'\n[・] {armor}を入手しました')


        # 戦闘
        if player_x == enemy_x and player_y == enemy_y:
            enemy_hp -= player_attack
            print(f'\n[・] 敵に{player_attack}ダメージを与えた')
            if enemy_hp <= 0:
                input('おめでとうございます！！勝利しました！')
                break
            player_hp -= enemy_attack
            print(f'\n[・] 敵から{enemy_attack}ダメージを受けた')
            if player_hp <= 0:
                input('敗北しました')
                break

def get_latest_version():
    url = 'https://github.com/iorin006/Rogue_game-py/blob/main/ver.txt'
    response = requests.get(url)
    data = json.loads(response.text)
    colorized_lines = data["payload"]["blob"]["colorizedLines"]
    return colorized_lines[0] if colorized_lines else ""

def update_game():
    url = "https://raw.githubusercontent.com/iorin006/Rogue_game-py/main/game.py"
    response = requests.get(url)
    if response.status_code == 200:
        f = open('game.py', 'w')
        f.write(response.text)
    else:
        print("エラーが発生しました。ステータスコード:", response.status_code)

current_version = '0.1'  # 現在のゲームのバージョン
latest_version = get_latest_version()
if latest_version > current_version:
    print('新しいバージョンが見つかりました。更新します。')
    update_game()
else:
    print('ゲームは最新バージョンです。')
    game()

