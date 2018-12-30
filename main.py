from flask import Flask, render_template, request
from synthesizeItem import synthesizeItem
import itemClass
import json

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "konti"

@app.route("/test", methods=["POST"])
def test():
    item_count = 0
    for i in request.form:
        if i[-4:] == "name":
            item_count += 1

    items = []
    for i in range(1, item_count+1):
        enchant_count = 0
        for j in request.form:
            if (j[4] == str(i)) and (j.split("_")[1][:-1] == "enchant"):
                enchant_count += 1
        
        enchants = [[],[]]
        for j in range(1, enchant_count//2+1):
            enchants[0].append(request.form["item"+str(i)+"_enchant"+str(j)])
            enchants[1].append(request.form["item"+str(i)+"_enchant"+str(j)+"_lv"])
            
        items.append(itemClass.item("item"+str(i), request.form["item"+str(i)+"_name"], enchants[0], enchants[1], request.form["item"+str(i)+"_prior"]))

    print(items[0].showItemInfo())
    return "hai"

@app.route("/", methods=["GET", "POST"])
def top():
    if request.method == "GET":
        with open("itemInfo.json", "r") as f:
            item_info = json.load(f)
        with open("enchantInfo.json", "r") as f:
            enchant_info = json.load(f)
        return render_template("main.html", item_info=item_info, enchant_info=enchant_info)

    else:
        data1 = json.loads(request.form["item1"])
        data2 = json.loads(request.form["item2"])
        hogeSword = itemClass.item(data1["itemType"], data1["enchantType"], data1["enchantLevel"], data1["priorWorkPenalty"])
        hugaBook = itemClass.item(data2["itemType"], data2["enchantType"], data2["enchantLevel"], data2["priorWorkPenalty"])
        res = synthesizeItem(hogeSword, hugaBook)
        print(res)
        return render_template("response.html", data1=res[0], data2=res[1])

if __name__ == "__main__":
    app.run()
