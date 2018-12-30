next_item_num = 3;
let enchant_nums = new Object();

// add enchantボタンを押したときの処理
function add_enchant_event(e){
  if(e.target.item in enchant_nums){
    enchant_nums[e.target.item] += 1;
  }else{
    enchant_nums[e.target.item] = 1;
  }

  // enchant name の追加
  let new_tag = document.createElement("select");
  new_tag.setAttribute("class", "form-control offset-1");
  new_tag.setAttribute("name", e.target.item+"_enchant"+enchant_nums[e.target.item]);
  new_tag.setAttribute("id", e.target.item+"_enchant"+enchant_nums[e.target.item]+"_id");
  document.getElementById(e.target.item+"_inline").insertBefore(new_tag, document.getElementById("add_"+e.target.item+"_enchant_button"));

  for(let i of item_info[document.getElementById(e.target.item+"_id").value]["permissionEnchant"]){
    new_tag = document.createElement("option");
    new_tag.setAttribute("value", i);
    new_tag.textContent = i;
    document.getElementById(e.target.item+"_enchant"+enchant_nums[e.target.item]+"_id").appendChild(new_tag);
  }

  // enchant level の追加
  new_tag = document.createElement("select");
  new_tag.setAttribute("class", "form-control");
  new_tag.setAttribute("name", e.target.item+"_enchant"+enchant_nums[e.target.item]+"_lv");
  new_tag.setAttribute("id", e.target.item+"_enchant"+enchant_nums[e.target.item]+"_lv_id");
  document.getElementById(e.target.item+"_inline").insertBefore(new_tag, document.getElementById("add_"+e.target.item+"_enchant_button"));

  for(let i=1; i<6; i++){ // enchantにより動的レベル帯を変更する必要あり！
    new_tag = document.createElement("option");
    new_tag.setAttribute("value", i);
    new_tag.textContent = i;
    document.getElementById(e.target.item+"_enchant"+enchant_nums[e.target.item]+"_lv_id").appendChild(new_tag);
  }

  // Lv文字列の追加
  new_tag = document.createElement("span");
  new_tag.textContent = "Lv"
  document.getElementById(e.target.item+"_inline").insertBefore(new_tag, document.getElementById("add_"+e.target.item+"_enchant_button"));
}

document.getElementById("add_item1_enchant_button").addEventListener("click", add_enchant_event);
document.getElementById("add_item1_enchant_button").item = "item1";
document.getElementById("add_item2_enchant_button").addEventListener("click", add_enchant_event);
document.getElementById("add_item2_enchant_button").item = "item2";

// add itemボタンを押したときの処理
let add_item_button = document.getElementById("add_item_button");
add_item_button.addEventListener("click", function(){
  let new_tag = document.createElement("div");
  new_tag.setAttribute("class", "form-group");
  add_item_button.parentNode.insertBefore(new_tag, add_item_button);

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

  for(let i of document.getElementsByTagName("select")[0].children){
    new_tag = document.createElement("option");
    new_tag.setAttribute("value", i.value);
    new_tag.textContent = i.value;
    document.getElementById("item"+next_item_num+"_id").appendChild(new_tag);
  }

  new_tag = document.createElement("select");
  new_tag.setAttribute("class", "form-control");
  new_tag.setAttribute("name", "item"+next_item_num+"_prior");
  new_tag.setAttribute("id", "item"+next_item_num+"_prior_id");
  document.getElementById("item"+next_item_num+"_inline").appendChild(new_tag);

  for(let i=0; i<6; i++){
    new_tag = document.createElement("option");
    new_tag.setAttribute("value", i);
    new_tag.textContent = i;
    document.getElementById("item"+next_item_num+"_prior_id").appendChild(new_tag);
  }

  new_tag = document.createElement("button");
  new_tag.setAttribute("id", "add_item"+next_item_num+"_enchant_button");
  new_tag.setAttribute("type", "button");
  new_tag.setAttribute("class", "btn btn-primary");
  new_tag.textContent = "add enchant";
  document.getElementById("item"+next_item_num+"_inline").appendChild(new_tag);
  document.getElementById("add_item"+next_item_num+"_enchant_button").addEventListener("click", add_enchant_event);
  document.getElementById("add_item"+next_item_num+"_enchant_button").item = "item"+next_item_num;

  next_item_num += 1;

});
