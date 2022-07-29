setTimeout(() => {
    console.log("a");
})

Promise.resolve().then(() => {
    console.log("b");
}).then(
    () => {
        const data = Promise.resolve("c");
        setTimeout(() => {
            console.log("d");
        });
        console.log("f");
        return data;
    }
).then(data => {
    console.log(data);
})