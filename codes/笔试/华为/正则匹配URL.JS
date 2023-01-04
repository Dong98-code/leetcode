function getUrlObject(url) {
  //首先解析整个字符串我们一点一点对应来看
  //第一个括号(\w+) \w匹配任意asc字符 +号代表一个或多个，这里就是匹配https或者http
  //([\w\.]+)匹配主机地址www.baidu.com
  //(\d+)匹配端口号
  //([\/\w\.]*)匹配url路径
  //(\?[^#]*)匹配query查询字符串
  //(\S*)匹配hash
  var regexp = /(\w+):\/\/([\w\.]+)\:?(\d+)?([\/\w\.]*)?(\?[^#]*)?#?(\S*)?/;
  var par = /(&?(\w*)=([^&]*))+/;
  var mat = url.match(regexp);
  var ob = {};
  ob.source = mat[0];
  ob.protocol = mat[1];
  ob.host = mat[2];
  ob.port = mat[3] || "80";
  ob.path = mat[4];
  ob.query = mat[5] || "";
  ob.hash = mat[6] || "";
  ob.params = {};
  //用&分割查询字符串中的每一个参数
  var params = ob.query.split("&");
  for (var i = 0; i < params.length; i++) {
    if (params[i] !== "") {
      //匹配每一个参数中的键和值。
      var par = params[i].match(/\??(\w+)=(\S+)/);
      // console.log(par);
      ob.params[par[1]] = par[2];
    }
  }
  return ob;
}
var url =
  "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%93%88%E5%93%88#top";
console.log(getUrlObject(url));
