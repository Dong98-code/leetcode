// tree扁平化

let arr = [
    {id: 1, name: '1', pid: 0},
    {id: 2, name: '2', pid: 1},
    {id: 3, name: '3', pid: 1},
    {id: 4, name: '4', pid: 3},
    {id: 5, name: '5', pid: 3},
   ]

   let tree = [
    {
        "id": 1,
        "name": "1",
        "pid": 0,
        "children": [
            {
                "id": 2,
                "name": "2",
                "pid": 1,
                "children": []
            },
            {
                "id": 3,
                "name": "3",
                "pid": 1,
                "children": [
                   {
                     "id": 4,
                     "name": "4",
                     "pid": 3,
                     "children": []
                   }
                ]
            }
        ]
    }
]

const treeToArray = function(tree) {
    let res = [];
    for (let item of tree) {
        const { children, ...i } = item;
        if (children && children.length) {
            res = res.concat(treeToArray(children))
        }
        res.push(i);
    }
    return res;
}

console.log(treeToArray(tree));
const getNameById = function (tree, id) {
    let res = -1;
    if (!tree) {
        return;
    }
    for (let item of tree) {
        if (res !== -1) {
            break;
        }
        if (item.id == id) {
            res = item.name;
            break;
        } else if (item.children.length > 0){
            res = getNameById(item.children, id)
        }
    }
    return res;
}

const getNameById_bfs = function (tree, id) {
    let res = -1;
    let q = tree;
    while (q.length > 0) {
        let item = q.shift();
        if (item.id === id) {
            res = item.name;
            break;
        }
        if (item.children.length > 0) {
            q = q.concat(item.children);
        }
    }
    return res;
}
// console.log(getNameById_bfs(tree, 4))

const treeToArray_bfs = function (tree) {
    let res = [];
    let q = tree;
    while (q.length > 0) {
        let item = q.shift();
        let { children, ...i } = item;
        res.push(i)
        if (children.length > 0) {
            q = q.concat(children);
        }
    }
    return res;
}

console.log(treeToArray_bfs(tree));
