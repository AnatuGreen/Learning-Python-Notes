const fromServer = '{"name":"John", "age":30, "city":"New York"}';
// Part the JSON string to JS object
const JSObj = JSON.parse(fromServer);

console.log(JSObj);
// { name: 'John', age: 30, city: 'New York' }
//  Make changes to the parsed data
JSObj.name = "Green";
console.log(JSObj);
// { name: 'Green', age: 30, city: 'New York' }

// Using JSON data in our html
document.getElementById("header").innerHTML = JSObj.city;

const jsonArray = '["Mouse","Goat","Horse","Rabbit"]';
const jsArr = JSON.parse(jsonArray);
console.log(jsArr);
//  [ 'Mouse', 'Goat', 'Horse', 'Rabbit' ]

// Convert JS object back to string to send to server

const fromServer2 = '{"name":"John", "age":30, "city":"New York"}';
// Part the JSON string to JS object
const JSObj2 = JSON.parse(fromServer2);
jsonConv = JSON.stringify(JSObj2);
console.log(jsonConv);
// {"name":"John","age":30,"city":"New York"}

// Stringify a js array:
const MyJsArr = ["Mouse", "Goat", "Horse", "Rabbit"];
const myJSONArr = JSON.stringify(MyJsArr);
console.log(myJSONArr);
// ["Mouse","Goat","Horse","Rabbit"]

jsonDate =
  '{"name":"John","today":"2022-09-06T08:48:15.884Z","city":"New York"}';
jsDate = JSON.parse(jsonDate); //json string including date to javascript
jsDate.today = new Date(jsDate.today); // 2022-09-06T08:48:15.884Z
console.log(jsDate.today);
console.log(new Date());
