# itemクラスの定義
class item:
    def __init__(self, synthesizeProcedure, itemType ,enchantType, enchantLevel, priorWorkPenalty):
        self.synthesizeProcedure = synthesizeProcedure
        self.itemType = itemType
        self.enchantType = enchantType              # listで初期化
        self.enchantLevel = enchantLevel            # listで初期化
        self.priorWorkPenalty = priorWorkPenalty
        self.necessaryExp = 0

    # アイテム情報の表示ppe3
    def showItemInfo(self):
        print("アイテムの種類:" + self.itemType)
        print("エンチャントの種類:" + ','.join(self.enchantType))
        print("各エンチャントレベル:" + ','.join(map(str, self.enchantLevel)))
        print("priorWorkPenalty:" + str(self.priorWorkPenalty))
        print("necessaryExp:" +str(self.necessaryExp))
        print("アイテムの合成手順:" +self.synthesizeProcedure)
        print()
