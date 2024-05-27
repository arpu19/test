import json
x={
"a":"name",
"s":"sucess",
"dress":[
         {"colour":"Red","style":"western","pattern":"kurti"},
         {"colour":"yellow","style":"western","pattern":"tops"},
         {"colour":"black","style":"western","pattern":"crops Tops"}       
             ]

}
print(json.dumps(x,indent=4))

