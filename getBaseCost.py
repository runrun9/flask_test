import json

# BaseCostを算出
# 引数(エンチャント名, エンチャントレベルの差分, "item"or"book")
def getBaseCost(enchantType, enchantLevelDif, IorB):
    if IorB != "book":
        IorB = "item"

    with open("enchantInfo.json", "r") as f:
         d = json.loads(f.read())

    return d[enchantType][IorB] * enchantLevelDif