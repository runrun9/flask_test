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
    print(request.form)
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
