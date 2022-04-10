var menu_list = [ {
    id: '1-1',
    menu_name: '权限设置',
    menu_url: 'setting.permission',
    parent_id: '1'
   }, {
    id: '1',
    menu_name: '设置',
    menu_url: 'setting',
    parent_id: 0
   },{
    id: '1-1-1',
    menu_name: '用户管理列表',
    menu_url: 'setting.permission.user_list',
    parent_id: '1-1'
   }, {
    id: '1-1-2',
    menu_name: '用户管理新增',
    menu_url: 'setting.permission.user_add',
    parent_id: '1-1'
   }, {
    id: '1-1-3',
    menu_name: '角色管理列表',
    menu_url: 'setting.permission.role_list',
    parent_id: '1-1'
   }, {
    id: '1-2',
    menu_name: '菜单设置',
    menu_url: 'setting.menu',
    parent_id: '1'
   }, {
    id: '1-2-1',
    menu_name: '菜单列表',
    menu_url: 'setting.menu.menu_list',
    parent_id: '1-2'
   }, {
    id: '1-2-2',
    menu_name: '菜单添加',
    menu_url: 'setting.menu.menu_add',
    parent_id: '1-2'
   }, {
    id: '2',
    menu_name: '订单',
    menu_url: 'order',
    parent_id: 0
   }, {
    id: '2-1',
    menu_name: '报单审核',
    menu_url: 'order.orderreview',
    parent_id: '2'
   }, {
    id: '2-2',
    menu_name: '退款管理',
    menu_url: 'order.refundmanagement',
    parent_id: '2'
   }
 ]

//初始时，数组中的每个元素具有 4 个属性，其中有 id 和 parent_id，现在我们需要根据这两个 id 之间的关系，添加一个 children 属性，使之成为一棵树的结构。
//#region
// function arrToTree(data) {
//     function nodePbj(obj) {
//         return {
//             id: obj.id,
//             menu_name: obj.menu_name,
//             menu_url: obj.menu_url,
//             children:[]
//         }
//     }
//     function getElementById(arr, id) {
//         // 遍历现有的数组
//         for (const ele of arr) {
//             if (ele.id === id) {
//                 return ele;
//             } else {
//                 if (ele.children.length > 0) {
//                     // 在孩子中寻找
//                     const tmp = getElementById(ele.children, id);
//                     if (tmp) {
//                         return tmp;
//                     } else {
//                         continue;
//                     }
//                 }
//             }
//         }
//     }
//     let tree = [];
//     if (!Array.isArray(data)) {
//         return tree;
//     }

//     data.forEach(ele => {
//         if (ele.parent_id === 0) {
//             return tree.push(nodePbj(ele));
//         } else {
//             const obj = getElementById(tree, ele.parent_id);
//             obj && obj.children.push(nodePbj(ele))
//         }
//     })
//     return tree;
// }

// 上述方法中， 要求 arr中的值按照层级顺序排列好了
//#endregion
function arrToTree(arr) {
    let map = {};
    let tree = [];
    arr.forEach(ele => {
        map[ele.id] = ele; // 便于查找id
        if (!ele.children) { // 没有children属性
            ele.children = [];
        }
    });
    arr.forEach(ele => {
        const parent = map[ele.parent_id];
        if (parent) {
            // 父级存在；
            parent.children.push(ele);
        } else {// 根节点
            tree.push(ele);
        }
    })
    return tree;
}
console.log(arrToTree(menu_list));