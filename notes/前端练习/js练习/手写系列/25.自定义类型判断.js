function getType(value) {
    if (value === null) {
        return 'null';
    }
    if (typeof value === "object"){
        let res = Object.prototype.toString.call(value);
        res = res.replace(/\[onject\s(.+)\]/, "$1")
        return res;
    } else {
        return typeof value;
    }
}