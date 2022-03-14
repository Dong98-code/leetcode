# 堆

堆就是用数组实现的二叉树，所以它没有使用父指针或者子指针。堆根据“堆属性”来排序，“堆属性”决定了树中节点的位置。

## 堆属性

大根堆和小根堆：

大根堆：  父节点的值比每一个子节点的值都要大；
小根堆 反之亦然；

> 注意：堆的根节点中存放的是最大或者最小元素，但是其他节点的排序顺序是未知的。例如，在一个最大堆中，最大的那一个元素总是位于 index 0 的位置，但是最小的元素则未必是最后一个元素。--唯一能够保证的是最小的元素是一个叶节点，但是不确定是哪一个。

## 堆 和 二叉搜索树的区别

1. 节点顺序

AVL 中， 左子节点的值 小于父亲子节点的值； 右子节点的值大于父子节点的值；

在小根堆中， 都比父子节点的值大； 小根堆 反之

2. 内存

普通的树 不仅需要存储节点的值； 还需要存贮节点之间指向的指针；

堆 使用数组来存储数据

3. 平衡。二叉搜索树必须是“平衡”的情况下，其大部分操作的复杂度才能达到O(log n)。你可以按任意顺序位置插入/删除数据，或者使用 AVL 树或者红黑树，但是在堆中实际上不需要整棵树都是有序的。我们只需要满足堆属性即可，所以在堆中平衡不是问题。因为堆中数据的组织方式可以保证O(log n) 的性能

4. 搜索

avl会更快； 堆的主要目的是让堆顶 始终为最大值或者最小值

## 来自数组的树

使用数组存储数据；

![20220313193917](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220313193917.png)


![20220313194039](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220313194039.png)

大根堆中： 

父亲节点的值 始终大于 其子节点的值 

> array[parent(i)] >= array[i]


![20220313194143](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220313194143.png)

堆中形状始终类似与下面这个样子：

![20220313194226](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220313194226.png)


## more math...

堆中有 n个节点， 那么对应的树的高度 为 $floor(log_2(n))$, 

## 堆的作用？

![20220313194742](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220313194742.png)

![20220313194803](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220313194803.png)


## 附录

heap 代码实现：

来源： [datastructures-js/heap](https://github.com/datastructures-js/heap/blob/master/src/heap.js)

```js
/**
 * @license MIT
 * @copyright 2020 Eyas Ranjous <eyas.ranjous@gmail.com>
 *
 * @class
 */
class Heap {
  /**
   * @param {function} compare
   * @param {array} [values]
   * @param {number|string|object} [leaf]
   */
  constructor(compare, values, leaf) {
    if (typeof compare !== 'function') {
      throw new Error('Heap constructor expects a compare function');
    }
    this._compare = compare; // compare 用于 确定优先级 大根堆 还是小根堆
    this._nodes = Array.isArray(values) ? values : []; // ? 数组形式存储数据；如果传入的值 就是数组形式 那么 this._nodes = array；否则初始化一个空数组；
    this._leaf = leaf || null; // ?
  }

  /**
   * Checks if a parent has a left child
   * @private
   */
  _hasLeftChild(parentIndex) {
    const leftChildIndex = (parentIndex * 2) + 1; // 如果有左子节点 那么 其idx为 2*parentIndex+1
    return leftChildIndex < this.size();
  }

  /**
   * Checks if a parent has a right child
   * @private
   */
  _hasRightChild(parentIndex) {
    const rightChildIndex = (parentIndex * 2) + 2;
    return rightChildIndex < this.size();
  }

  /**
   * Compares two nodes
   * @private
   */
  _compareAt(i, j) {
      // 传入的为索引值 idx.
    return this._compare(this._nodes[i], this._nodes[j]);
  }

  /**
   * Swaps two nodes in the heap
   * @private
   */
  _swap(i, j) {
    // 数组交换
    // [this._nodes[j], this._nodes[i]] = [this._nodes[j], this._nodes[i]]
    const temp = this._nodes[i];
    this._nodes[i] = this._nodes[j];
    this._nodes[j] = temp;
  }

  /**
   * Checks if parent and child should be swapped
   * @private
   */
  _shouldSwap(parentIndex, childIndex) {
      // 先判断 父亲和孩子节点是否是有效的 index
    if (parentIndex < 0 || parentIndex >= this.size()) {
      return false;
    }

    if (childIndex < 0 || childIndex >= this.size()) {
      return false;
    }
    // 根据传入的compare函数 来判断 小根堆； 和大根堆 的区别
    return this._compareAt(parentIndex, childIndex) > 0;
  }

  /**
   * Compares children of a parent
   * @private
   */
  _compareChildrenOf(parentIndex) {
    if (!this._hasLeftChild(parentIndex) && !this._hasRightChild(parentIndex)) {
      return -1;
    }

    const leftChildIndex = (parentIndex * 2) + 1;
    const rightChildIndex = (parentIndex * 2) + 2;

    if (!this._hasLeftChild(parentIndex)) {
      return rightChildIndex;
    }

    if (!this._hasRightChild(parentIndex)) {
      return leftChildIndex;
    }

    const compare = this._compareAt(leftChildIndex, rightChildIndex);
    return compare > 0 ? rightChildIndex : leftChildIndex;
  }

  /**
   * Compares two children before a position
   * @private
   */
  _compareChildrenBefore(index, leftChildIndex, rightChildIndex) {
    const compare = this._compareAt(rightChildIndex, leftChildIndex);

    if (compare <= 0 && rightChildIndex < index) {
      return rightChildIndex;
    }

    return leftChildIndex;
  }

  /**
   * Recursively bubbles up a node if it's in a wrong position
   * @private
   */
  _heapifyUp(startIndex) {
    // 从开始的位置上浮
    let childIndex = startIndex;
    let parentIndex = Math.floor((childIndex - 1) / 2); // 改idx的父亲节点的位置

    while (this._shouldSwap(parentIndex, childIndex)) {
    // 使用shouldSwap来判断是否需要 交换 两个索引位置处的值
      this._swap(parentIndex, childIndex);
      childIndex = parentIndex;
      parentIndex = Math.floor((childIndex - 1) / 2);
    }
  }

  /**
   * Recursively bubbles down a node if it's in a wrong position
   * @private
   */
  _heapifyDown(startIndex) {
    let parentIndex = startIndex;
    let childIndex = this._compareChildrenOf(parentIndex);

    while (this._shouldSwap(parentIndex, childIndex)) {
      this._swap(parentIndex, childIndex);
      parentIndex = childIndex;
      childIndex = this._compareChildrenOf(parentIndex);
    }
  }

  /**
   * Recursively bubbles down a node before a given index
   * @private
   */
  _heapifyDownUntil(index) {
    let parentIndex = 0;
    let leftChildIndex = 1;
    let rightChildIndex = 2;
    let childIndex;

    while (leftChildIndex < index) {
      childIndex = this._compareChildrenBefore(
        index,
        leftChildIndex,
        rightChildIndex
      );

      if (this._shouldSwap(parentIndex, childIndex)) {
        this._swap(parentIndex, childIndex);
      }

      parentIndex = childIndex;
      leftChildIndex = (parentIndex * 2) + 1;
      rightChildIndex = (parentIndex * 2) + 2;
    }
  }

  /**
   * Inserts a new value into the heap
   * @public
   * @param {number|string|object} value
   * @returns {Heap}
   */
  insert(value) {
    this._nodes.push(value);
    this._heapifyUp(this.size() - 1);
    if (this._leaf === null || this._compare(value, this._leaf) > 0) {
      this._leaf = value;
    }
    return this;
  }

  /**
   * Removes and returns the root node in the heap
   * @public
   * @returns {number|string|object}
   */
  extractRoot() {
    if (this.isEmpty()) {
      return null;
    }

    const root = this.root();// root 为根节点的值
    this._nodes[0] = this._nodes[this.size() - 1]; // 数组的最后一个位置 到最有一个点
    this._nodes.pop(); // 删除_nodes的最后一个值
    this._heapifyDown(0); // 从 0idx 下沉

    if (root === this._leaf) {
        // 如果原来的 leaf的值 为 root的值 更显此时 leaf的值
      this._leaf = this.root();
    }

    return root;
  }

  /**
   * Applies heap sort and return the values sorted by priority
   * @public
   * @returns {array}
   */
  sort() {
    for (let i = this.size() - 1; i > 0; i -= 1) {
      this._swap(0, i);
      this._heapifyDownUntil(i);
    }
    return this._nodes;
  }

  /**
   * Fixes node positions in the heap
   * @public
   * @returns {Heap}
   */
  fix() {
    for (let i = 0; i < this.size(); i += 1) {
      this._heapifyUp(i);
    }
    return this;
  }

  /**
   * Verifies that all heap nodes are in the right position
   * @public
   * @returns {boolean}
   */
  isValid() {
    const isValidRecursive = (parentIndex) => {
      let isValidLeft = true;
      let isValidRight = true;

      if (this._hasLeftChild(parentIndex)) {
        const leftChildIndex = (parentIndex * 2) + 1;
        if (this._compareAt(parentIndex, leftChildIndex) > 0) {
          return false;
        }
        isValidLeft = isValidRecursive(leftChildIndex);
      }

      if (this._hasRightChild(parentIndex)) {
        const rightChildIndex = (parentIndex * 2) + 2;
        if (this._compareAt(parentIndex, rightChildIndex) > 0) {
          return false;
        }
        isValidRight = isValidRecursive(rightChildIndex);
      }

      return isValidLeft && isValidRight;
    };

    return isValidRecursive(0);
  }

  /**
   * Returns a shallow copy of the heap
   * @public
   * @returns {Heap}
   */
  clone() {
    return new Heap(this._compare, this._nodes.slice(), this._leaf);
  }

  /**
   * Returns the root node in the heap
   * @public
   * @returns {number|string|object}
   */
  root() {
    if (this.isEmpty()) {
      return null;
    }

    return this._nodes[0];
  }

  /**
   * Returns a leaf node in the heap
   * @public
   * @returns {number|string|object}
   */
  leaf() {
    return this._leaf;
  }

  /**
   * Returns the number of nodes in the heap
   * @public
   * @returns {number}
   */
  size() {
    return this._nodes.length;
  }

  /**
   * Checks if the heap is empty
   * @public
   * @returns {boolean}
   */
  isEmpty() {
    return this.size() === 0;
  }

  /**
   * Clears the heap
   * @public
   */
  clear() {
    this._nodes = [];
    this._leaf = null;
  }

  /**
   * Builds a heap from a array of values
   * @public
   * @static
   * @param {array} values
   * @param {function} compare
   * @returns {Heap}
   */
  static heapify(values, compare) {
    if (!Array.isArray(values)) {
      throw new Error('Heap.heapify expects an array of values');
    }

    if (typeof compare !== 'function') {
      throw new Error('Heap.heapify expects a compare function');
    }

    return new Heap(compare, values).fix();
  }

  /**
   * Checks if a list of values is a valid heap
   * @public
   * @static
   * @param {array} values
   * @param {function} compare
   * @returns {boolean}
   */
  static isHeapified(values, compare) {
    return new Heap(compare, values).isValid();
  }
}

exports.Heap = Heap;

```

# priority-queue 优先队列


```js

/**
 * @copyright 2020 Eyas Ranjous <eyas.ranjous@gmail.com>
 * @license MIT
 */

const { CustomHeap } = require('@datastructures-js/heap');

/**
 * @class PriorityQueue
 */
class PriorityQueue {
  /**
   * Creates a priority queue
   * @public
   * @params {object} [options]
   */
  constructor(options = {}) {
    const { priority, compare } = options;
    if (compare) {
      if (typeof compare !== 'function') {
        throw new Error('.constructor expects a valid compare function');
      }
      this._compare = compare;
      this._heap = new CustomHeap(this._compare);
    } else {
      if (priority !== undefined && typeof priority !== 'function') {
        throw new Error('.constructor expects a valid priority function');
      }

      this._priority = priority || ((el) => +el);
    }
  }

  /**
   * @private
   * @returns {object}
   */
  _getElementWithPriority(node) {
    return {
      priority: node.key,
      element: node.value
    };
  }

  /**
   * @public
   * @returns {number}
   */
  size() {
    return this._heap.size();
  }

  /**
   * @public
   * @returns {boolean}
   */
  isEmpty() {
    return this._heap.isEmpty();
  }

  /**
   * Returns an element with highest priority in the queue
   * @public
   * @returns {object}
   */
  front() {
    if (this.isEmpty()) return null;

    if (this._compare) {
      return this._heap.root();
    }

    return this._getElementWithPriority(this._heap.root());
  }

  /**
   * Returns an element with lowest priority in the queue
   * @public
   * @returns {object}
   */
  back() {
    if (this.isEmpty()) return null;

    if (this._compare) {
      return this._heap.leaf();
    }

    return this._getElementWithPriority(this._heap.leaf());
  }

  /**
   * Adds an element to the queue
   * @public
   * @param {any} element
   * @param {number} p - priority
   * @throws {Error} if priority is not a valid number
   */
  enqueue(element, p) {
    if (this._compare) {
      this._heap.insert(element);
      return this;
    }

    if (p && Number.isNaN(+p)) {
      throw new Error('.enqueue expects a numeric priority');
    }

    if (Number.isNaN(+p) && Number.isNaN(this._priority(element))) {
      throw new Error(
        '.enqueue expects a numeric priority '
        + 'or a constructor callback that returns a number'
      );
    }

    const priority = !Number.isNaN(+p) ? p : this._priority(element);
    this._heap.insert(+priority, element);
    return this;
  }

  /**
   * Removes and returns an element with highest priority in the queue
   * @public
   * @returns {object}
   */
  dequeue() {
    if (this.isEmpty()) return null;

    if (this._compare) {
      return this._heap.extractRoot();
    }

    return this._getElementWithPriority(this._heap.extractRoot());
  }

  /**
   * Returns a sorted list of elements from highest to lowest priority
   * @public
   * @returns {array}
   */
  toArray() {
    if (this._compare) {
      return this._heap.clone().sort().reverse();
    }

    return this._heap
      .clone()
      .sort()
      .map((n) => this._getElementWithPriority(n))
      .reverse();
  }

  /**
   * Clears the queue
   * @public
   */
  clear() {
    this._heap.clear();
  }
}

exports.PriorityQueue = PriorityQueue;
```