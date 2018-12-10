
import getBaseCost
import json

### こいつどうすんねん
priorWorkPenaltyCostInfo = {0: 0, 1: 1, 2: 3, 3: 7, 4: 15, 5: 31}
###

# 2つのアイテムを合成
# 引数(itemClassインスタンス, itemClassインスタンス,)
def synthesizeItem(leftItem, rightItem):

    # enchantInfo.jsonの読み込み
    enchantInfoFile = open("enchantInfo.json","r")
    enchantInfoJson = json.load(enchantInfoFile)

    # 合成後アイテムを定義, leftItemを基準
    newItem = leftItem

    # 必要コストを格納
    baseCost = 0


    # エンチャント合成処理
    # 右側アイテムのエンチャントを見ていく
    for rightEnchantIndex, rightEnchant in enumerate(rightItem.enchantType):

        # 同一エンチャントの有無を格納
        sameEnchantFlag = False

        #左側アイテムのエンチャントを見ていく
        for leftEnchantIndex, leftEnchant in enumerate(leftItem.enchantType):

            # 同一エンチャントがあった場合
            if rightEnchant == leftEnchant:
                sameEnchantFlag = True

                # 右側アイテムのエンチャントレベルが高かった場合
                if rightItem.enchantLevel[rightEnchantIndex] > leftItem.enchantLevel[leftEnchantIndex]:
                    baseCost += getBaseCost.getBaseCost(rightEnchant, rightItem.enchantLevel[rightEnchantIndex] - leftItem.enchantLevel[leftEnchantIndex], rightItem.itemType)
                    newItem.enchantLevel[leftEnchantIndex] = rightItem.enchantLevel[rightEnchantIndex]
                # 左右アイテムのエンチャントレベルが等しかった場合
                elif rightItem.enchantLevel[rightEnchantIndex] == leftItem.enchantLevel[leftEnchantIndex]:
                    # エンチャントの上限レベルを超えないかチェック
                    if rightItem.enchantLevel[rightEnchantIndex] < enchantInfoJson[rightEnchant]["max"]:
                        baseCost += getBaseCost.getBaseCost(rightEnchant, 1, rightItem.itemType)
                        newItem.enchantLevel[leftEnchantIndex] += 1

        # 同一エンチャントがなかった場合
        if sameEnchantFlag == False:
            baseCost += getBaseCost.getBaseCost(rightEnchant, rightItem.enchantLevel[rightEnchantIndex], rightItem.itemType)
            newItem.enchantType.append(rightEnchant)
            newItem.enchantLevel.append(rightItem.enchantLevel[rightEnchantIndex])


    # priorWorkPenaltyCostを算出
    priorWorkPenaltyCost = priorWorkPenaltyCostInfo[leftItem.priorWorkPenalty] + priorWorkPenaltyCostInfo[rightItem.priorWorkPenalty]

    # 合成後アイテムのpriorWorkPenaltyを算出
    if leftItem.priorWorkPenalty >= rightItem.priorWorkPenalty:
        newItem.priorWorkPenalty += 1
    else :
        newItem.priorWorkPenalty = rightItem.priorWorkPenalty + 1


    # 合成結果, 必要コストを表示
    newItem.showItemInfo()
    print("BaseCost: {}".format(baseCost))
    print("PriorWorkPenaltyCost: {}".format(priorWorkPenaltyCost))
    print("TotalCost: {}".format(baseCost + priorWorkPenaltyCost))

    return [baseCost, priorWorkPenaltyCost]


# テスト
if __name__ == "__main__":
    hogeSword = itemClass.item("book", ["smite", "unbreaking"], [2, 2], 2)
    hugaBook = itemClass.item("book", ["knockback", "unbreaking", "smite"], [1, 2, 4], 4)

    synthesizeItem(hogeSword, hugaBook)