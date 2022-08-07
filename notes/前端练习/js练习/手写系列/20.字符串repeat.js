let str = "sf"
function repeat(object, n) {
    return (new Array(n + 1)).join(object);
}

let res = repeat(str, 2)
console.log(res);