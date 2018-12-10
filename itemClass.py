# itemクラスの定義
class item:
    def __init__(self, itemType ,enchantType, enchantLevel, priorWorkPenalty):
        self.itemType = itemType
        self.enchantType = enchantType              # listで初期化
        self.enchantLevel = enchantLevel            # listで初期化
        self.priorWorkPenalty = priorWorkPenalty

    # アイテム情報の表示
    def showItemInfo(self):
        print("アイテムの種類:" + self.itemType)
        print("エンチャントの種類:" + ','.join(self.enchantType))
        print("各エンチャントレベル:" + ','.join(map(str, self.enchantLevel)))
        print("priorWorkPenalty:" + str(self.priorWorkPenalty))