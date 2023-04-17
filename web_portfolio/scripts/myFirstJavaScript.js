function hello() {
    alert("Hello World!");
    console.log("hello");
    var outer = "hello from outer";

    function innerHello() {
        console.log(outer);
    }
    innerHello();
}

var a = [2,8,3,14,5];

const sumArray = function() {
    let sum = 0;
    for (let num of a) {
        sum += num;
    }
    return sum;
}

const funWithArrays = function() {
    console.log(sumArray());
    console.log(findMax());
    console.log(findMin());
}

const plainOldFunction = function(default_val="hello") {
    console.log(default_val);
}

const callback = function() {
    console.log("this is the callback function");
}

const firstFunction = function(aFunction) {
    aFunction();
}

const soManyFunctions = function() {
    plainOldFunction();
    plainOldFunction("This is my parameter");
    firstFunction(callback);
    firstFunction(function() {
        console.log("function written in paramater");
    });
    firstFunction(plainOldFunction);

    const pet_obj = {
        name: "Boomer",
        age: 7,
        pet_type: "dog",
        cute: true,
        puppies: ["pup1","pup2","pup3"]
    }
    console.log(pet_obj);
    console.log(pet_obj.name);
    console.log(pet_obj["age"]);
    console.log(pet_obj['age']);
    


}

// hello();
// innerHello();

