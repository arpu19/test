
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"model":2004})
thisdict["color"]="red"
thisdict.pop("model")
for v in thisdict:
 print(thisdict)