# 平衡二叉树

## 定义：

平衡二叉树， 平衡二叉搜索树， AVL树， 具有以下特点：

它是一 棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树

![20220226110845](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220226110845.png)


## 旋转

### 左旋转：

![20220226111103](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220226111103.png)
当右子树的高度 rightHeight - leftHight > 1 ， 不再是 一个 avl树

左旋转

步骤如下：

1. 节点的右子树 代替节点的位置
2. 右孩子的左子树 称为该节点的右子树， 
3. 节点本身百年未右孩子的左子树

### 右旋转： 

和左旋转类似

1. 根节点的左孩子指向 原来左孩子的右孩子， 
2. 原来左孩子右孩子 指向原来的根节点


LR 和 RL

## 代码
```html
<script>
        class AVLTree {
            constructor(num) {
                this.val = num;
                this.leftChild = null;
                this.rightChild = null;
                this.height = 1;
            }

            getHeight(a) {
                return a === null ? 0 : a.height;
            }

            getMax(a, b) {
                let aHeight = (!a) ? 0 : a.height;
                let bHeight = (!b) ? 0 : b.height;
                // let aHeight = getHeight(a);
                // let bHeight = getHeight(b);
                return aHeight > bHeight ? aHeight : bHeight;
            }

            // 计算平衡因子
            getBalance(a, b) {
                let aHeight = (!a) ? 0 : a.height;
                let bHeight = (!b) ? 0 : b.height;

                return aHeight - bHeight;
            }

            RR() {
                // 右子树的右节点 添加新节点
                // 左旋操作
                let a = this;
                let b = this.rightChild;
                a.rightChild = b.leftChild;
                b.leftChild = a;
                // 重新计算 左右子树的高度
                // 孙子辈的子树的高度是没有变化的
                a.height = a.getMax(a.rightChild, a.leftChild) + 1;
                b.height = b.getMax(b.leftChild, b.rightChild) + 1;
                return b;

            }

            LL() {
                // 左子树的左节点 添加新节点
                // 右旋 操作
                let a = this;
                let b = this.leftChild;
                a.leftChild = b.rightChild;
                b.rightChild = a;
                a.height = a.getMax(a.rightChild, a.leftChild) + 1;
                b.height = b.getMax(b.rightChild, b.rightChild) + 1;
                return b;

            }
            // 左孩子的左子树 插入节点
            RL() {
                // 显示 右子节点右旋； 后是根节点 左旋
                let a = this;
                a.rightChild = a.rightChild.LL();
                a = a.RR();
                return a;
            }

            LR() {
                // 左孩子 左旋， 根节点 右旋
                let a = this;
                a.leftChild = a.leftChild.RR();
                a = a.LL();
                return a;
            }

            insertNode(num) {
                // 插入节点
                let node = new AVLTree(num); // 每一个节点都可以看作一个新的树
                let res = this;
                if (node.val > this.val) {
                    // 新值大于根节点的值
                    if (this.rightChild == null) {
                        this.rightChild = node;
                    } else {
                        this.rightChild.insertNode(num);
                    }

                    let balanceFactor = this.getBalance(this.rightChild, this.leftChild); // 该树的平衡因子；
                    if (balanceFactor == 2) {
                        if (node.val > this.rightChild.val) {
                            // rr
                            res = this.RR();
                        } else {
                            res = this.RL();
                        }
                    }
                } else if (point.val < this.val) {
                    // 在左子树上插入
                    if (this.leftChild == null) {
                        this.leftChild = node;
                    } else {
                        this.leftChild.insertNode(num);

                    }

                    let balanceFactor = this.getBalance(this.leftChild, this.rightChild);
                    if (balanceFactor == 2) {
                        if (node.val < this.leftChild.val) {
                            // LL
                            res = this.LL();
                        } else {
                            res = this.LR();
                        }
                    }
                } else {
                    throw "输入了重复的值"
                }

                this.height = this.getMax(this.leftChild, this.rightChild) + 1;
                return res;
            }

            // 删除节点
            delNode(num) {
                let res = this;
                if (num > this.val) {
                    // 在孩子删除
                    res.rightChild = res.rightChild.delNode(num);
                } else if (num < this.val) {
                    res.leftChild = res.leftChild.delNode(num);

                } else {
                    // 删除的是根节点
                    if (num !== this.val) {
                        throw '不存在该值'
                    }
                    if (res.leftChild !== null) {
                        let cur = res.leftChild;
                        // 找到 左子树中的最大值
                        while (tree) {
                            if (cur.rightChild) {
                                cur = cur.rightChild;

                            } else {
                                break;
                            }
                        }
                        // cur此时为 左子树的最大值， 将根节点的值变成左子树的中最大值
                        res.val = cur.val;
                        res.leftChild = res.leftChild.delNode(cur.val); // 删除此时左子树的对应的节点
                    } else if (res.rightChild !== null) {
                        let cur = res.rightChild;
                        while (true) {
                            if (cur.leftChild) {
                                cur = cur.leftChild;
                            } else {
                                break;
                            }

                            res.val = cur.val;
                            res.rightChild = res.rightChild.delNode(cur.val);
                        }
                    } else {
                        console.log('delte' + res); // 最后的叶子节点
                        return null; // 删除这个节点， 将其 变成null 即可
                    }


                }

                // 再平衡二叉树
                if (res.getBalance(res.leftChild, res.rightChild) == 2) {
                    if (res.getHeight(res.leftChild.rightChild) - res.getHeight(res.leftChild.leftChild) == 1) {
                        res = res.LR();
                    } else {
                        res = res.LL();
                    }

                } else if (res.getBalance(res.leftChild, res.rightChild) == -2) {
                    if (res.getHeight(res.rightChild.leftChild) - res.getHeight(res.rightChild.rightChild) == 1) {
                        res = res.RL();
                    } else {
                        res = res.RR();
                    }
                } else {
                    console.log('balanced');
                }

                res.height = this.getMax(this.leftChild, this.rightChild) + 1;
                return res
            }
        }



        //使用方法

        function createTree(arr) {
            let result;
            arr.forEach((child, index) => {
                if (index === 0) {
                    result = new AVLTree(child);
                } else {
                    result = result.insertNode(child);
                }
            })
            return result;
        }
        var arr = [1, 3, 5, 7, 15, 24, 56, 11, 33, 42, 2, 4, 6, 12];
        var tree = createTree(arr);
    </script>
```

