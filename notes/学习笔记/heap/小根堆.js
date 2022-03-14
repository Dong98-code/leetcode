class MinHeap {
    constructor(compare = (a, b) => a > b) {
        this.data = [];
        this.size = 0;
        this.compare = compare;
    }

    _swap(i, j) {
        [this.data[i], this.data[j]] = [this.data[j], this.data[i]];
    }

    peek() {
        return this.data[0]; // 堆顶的元素

    }

    isEmpty() {
        return this.data.length === 0;
    }

    _childIndex(index) {
        return (index << 2) + 1;
    }

    _parentIndex(index) {
        return Math.floor((index - 1) / 2);
    }

    _heapifyUp(index) {

        while (this._parentIndex(index) >= 0 && this.compare(this.data[index], this.data[this._parentIndex(index)])) {
            this._swap(this._parentIndex(index), index);
            index = this._parentIndex(index);
        }
    }

    _heapifyDown(index) {
        while (this._childIndex(index) < this.size) {
            let child = this._childIndex(index)
            if (child + 1 < this.size &&
                this.compare(this.data[child + 1], this.data[child])) {
                child = child + 1
            }
            if (this.compare(this.data[index], this.data[child])) {
                break;
            }
                this._swap(index, child)
                index = child
        }
    }

    push(val) {
        this.data.push(val);
        this.size += 1;
        this._heapifyUp(this.size - 1);
    }

    pop() {
        if (this.size === 0) {
            return null;
        }
        this._swap(0, this.size - 1);
        const top = this.data.pop()
        this.size -= 1;
        this._heapifyDown(0);
        // return this.data.pop();
        return top;
    }
}

let pq = new MinHeap((a, b) => a < b);

test_data = [1, 10, 15, 2, 3, 11]

for (let data of test_data) {
    pq.push(data);
}
for (let i = 1; i < 7; i++) {
    console.log(pq.pop());
}
console.log(pq);