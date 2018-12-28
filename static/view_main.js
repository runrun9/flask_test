next_item_num = 3;
let enchant_nums = new Object();

// add enchantボタンを押したときの処理
function add_enchant_event(e){
  if(e.target.item in enchant_nums){
    enchant_nums[e.target.item] += 1;
  }else{
    enchant_nums[e.target.item] = 1;
  }
  let new_tag = document.createElement("select");
  new_tag.setAttribute("class", "form-control");
  new_tag.setAttribute("name", e.target.item+"_enchant"+enchant_nums[e.target.item]);
  new_tag.setAttribute("id", e.target.item+"_enchant"+enchant_nums[e.target.item]+"_id");
  document.getElementById(e.target.item+"_inline").insertBefore(new_tag, document.getElementById("add_"+e.target.item+"_enchant_button"));

  for(i of json_data[document.getElementById(e.target.item+"_id").value]["permissionEnchant"]){
    new_tag = document.createElement("option");
    new_tag.setAttribute("value", i);
    new_tag.textContent = i;
    document.getElementById(e.target.item+"_enchant"+enchant_nums[e.target.item]+"_id").appendChild(new_tag);
  }
}

document.getElementById("add_item1_enchant_button").addEventListener("click", add_enchant_event);
document.getElementById("add_item1_enchant_button").item = "item1";
document.getElementById("add_item2_enchant_button").addEventListener("click", add_enchant_event);
document.getElementById("add_item2_enchant_button").item = "item2";

// add itemボタンを押したときの処理
document.getElementById("add_item_button").addEventListener("click", function(){
  let new_tag = document.createElement("div");
  new_tag.setAttribute("class", "form-group");
  let submit_button = document.getElementById("submit_button");
  submit_button.parentNode.insertBefore(new_tag, submit_button);

  new_tag = document.createElement("div");
  new_tag.setAttribute("class", "col-sm-12 form-inline");
  new_tag.setAttribute("id", "item"+next_item_num+"_inline");
  let parent_element = document.getElementsByClassName("form-group");
  parent_element[parent_element.length-2].appendChild(new_tag);

  new_tag = document.createElement("label");
  new_tag.setAttribute("class", "col-sm-1 control-label");
  new_tag.textContent = "item" + next_item_num;
  document.getElementById("item"+next_item_num+"_inline").appendChild(new_tag);

  new_tag = document.createElement("select");
  new_tag.setAttribute("class", "form-control");
  new_tag.setAttribute("name", "item"+next_item_num+"_name");
  new_tag.setAttribute("id", "item"+next_item_num+"_id");
  document.getElementById("item"+next_item_num+"_inline").appendChild(new_tag);

  new_tag = document.createElement("button");
  new_tag.setAttribute("id", "add_item"+next_item_num+"_enchant_button");
  new_tag.setAttribute("type", "button");
  new_tag.setAttribute("class", "btn btn-primary");
  new_tag.textContent = "add enchant";
  document.getElementById("item"+next_item_num+"_inline").appendChild(new_tag);
  document.getElementById("add_item"+next_item_num+"_enchant_button").addEventListener("click", add_enchant_event);
  document.getElementById("add_item"+next_item_num+"_enchant_button").item = "item"+next_item_num;

  for(let i of document.getElementsByTagName("select")[0].children){
    new_tag = document.createElement("option");
    new_tag.setAttribute("value", i.value);
    new_tag.textContent = i.value;
    document.getElementById("item"+next_item_num+"_id").appendChild(new_tag);
  }

  next_item_num += 1;

});
