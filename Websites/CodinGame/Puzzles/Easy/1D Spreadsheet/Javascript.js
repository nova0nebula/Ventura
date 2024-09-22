let spreadsheet = [];
let indexNotCalculated = [];
const N = parseInt(readline());
for (let i = 0; i < N; i++) {
  var inputs = readline().split(" ");
  let object = {
    operation: inputs[0],
    arg1: inputs[1],
    arg2: inputs[2],
    value: null,
  };
  if (canProcess(object, i)) {
    object.value = process(object);
  } else {
    indexNotCalculated.push(i);
  }
  spreadsheet.push(object);
}
let index = 0;
while (indexNotCalculated.length != 0) {
  let object = spreadsheet[indexNotCalculated[index]];
  if (canProcess(object)) {
    object.value = process(object);
    indexNotCalculated.splice(index, 1);
    index = 0;
  } else {
    index++;
  }
}
for (let i = 0; i < N; i++) {
  console.log(spreadsheet[i].value);
}
function process(object) {
  let valueArg1 = parseInt(object.arg1[0] == "$" ? spreadsheet[parseInt(object.arg1.substring(1))].value : object.arg1);
  let valueArg2 = parseInt(object.arg2[0] == "$" ? spreadsheet[parseInt(object.arg2.substring(1))].value : object.arg2);
  let answer = 0;
  switch (object.operation) {
    case "VALUE":
      answer = valueArg1;
      break;
    case "ADD":
      answer = valueArg1 + valueArg2;
      break;
    case "SUB":
      answer = valueArg1 - valueArg2;
      break;
    case "MULT":
      answer = valueArg1 * valueArg2;
      break;
  }
  if (answer === -0) {
    answer = 0;
  }
  return answer;
}
function canProcess(object, i = -1) {
  let argIsRef = [false, false];
  let process = true;
  if (object.arg1[0] == "$") {
    argIsRef[0] = true;
  }
  if (object.arg2[0] == "$") {
    argIsRef[1] = true;
  }
  if (argIsRef[0] || argIsRef[1]) {
    if (argIsRef[0]) {
      let indexRef = parseInt(object.arg1.substring(1));
      if (indexRef < i || i == -1) {
        if (indexNotCalculated.includes(indexRef)) {
          process = false;
        }
      } else {
        process = false;
      }
    }
    if (argIsRef[1]) {
      let indexRef = parseInt(object.arg2.substring(1));
      if (indexRef < i || i == -1) {
        if (indexNotCalculated.includes(indexRef)) {
          process = false;
        }
      } else {
        process = false;
      }
    }
  }
  return process;
}