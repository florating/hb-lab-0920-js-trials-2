"use strict";


// 1. printIndices
function printIndices(items) {
  for (let i = 0; i < items.length; i += 1) {
    console.log("${items[i]} ${i}");
  } 
}
// for i in range(len(items)):
// print(f'{items[i]} {i}')


// 2. everyOtherItem
function everyOtherItem(items) {
  const result = [];
  for (let i = 0; i < items.length; i += 1) {
    if (i % 2 === 0) {
      result.push(items[i]);
    }
  console.log(result);
  }
}
// result = []

// for i in range(len(items)):
//     if i % 2 == 0:
//         result.append(items[i])

// print(result)

// 3. smallestNItems
function smallestNItems(items, n) {
  const sortedItems = items.sort();
  let sortedNItems = sortedItems.slice(0, n);
}
