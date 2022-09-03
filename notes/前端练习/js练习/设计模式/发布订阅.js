let eventEmiter = {
    list: {},//缓存列表对象
    on(event, fn) {
        //wvent事件可能由多个订阅者同时订阅，创建一个列表
        //函数的调用者应该为 eventEmiter 保存this
        let _this = this;
        if (!_this.list[event]) {
            //现在还未存在 这个 event
            _this.list[event] = [];
        }
        _this.list[event].push(fn);// 将fn保存到对应的消息队列中去

    },

    emit() {
        let _this = this;
        let event = [].shift.call(arguments);
        let fns = [...this.list[event]];// 浅拷贝一次
        if (!fns || fns.length === 0) {
            return false; // fns不存在，
        }
        // 遍历执行对应的函数
        fns.forEach((f) => {
            f.apply(_this, arguments);
        })
        return _this; // 返回
    }
}