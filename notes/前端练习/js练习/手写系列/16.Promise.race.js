Promise.myrace = function (promiseList) {
    return new Promise((resolve, reject) => {
        let list;
        try {
            list = [...promiseList]
        } catch (e) {
            throw new TypeError(TypeError(`${promiseList} is not iterable (cannot read property Symbol(Symbol.iterator))`))
        }
        for (let [i, p] of list) {
            Promise.resolve(p).then(
                (result) => {resolve(result)},
                (reason) => {reject(reason)}
            )
        }

    })
}