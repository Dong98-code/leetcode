var numUniqueEmails = function(emails) {
    let res = new Set();

    for (let email of emails) {
        // 去掉. 和 + 
        let [name, domain] = email.split('@');
        // 找到 +的索引位置
        let idx = name.indexOf("+");
        let new_name = idx === -1 ? name:name.slice(0, name.indexOf('+'));
        new_name = new_name.replaceAll(".", "")
        res.add(new_name+"@"+domain);
    }
    return res.size;
};
let emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
console.log(numUniqueEmails(emails));