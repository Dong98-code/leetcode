 # bfc和ifc

 定义： 所谓BFC就是块级格式化上下文, Block Formatting Context，在常规流中竖着排列
IFC就是行内格式化上下文, Inline Formatting Content，在常规流中横着排列

## BFC 布局规则

内部的Box会在垂直方向，一个接一个的放置
同一个BFC内，垂直方向的盒子上下margin会重叠
每个元素的margin box的左边，与包含块border box的左边连接（对于从右往左的布局，则相反）即使存在浮动也是如此
子BFC的区域不会与float box重叠
BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素，反之也如此。
计算BFC的高度时，浮动元素也参与计算（故也可以达到所谓清除浮动的效果，只要将包裹层转变为BFC）

## 将块级元素转换为bfc

1. 具有除了float:none的其他浮动属性
2. 定位为absolute或者fixed
3. dispaly为block、inline-block、table-cell、table-caption、flex、inline-flex
4. overflow不为visible（除非该值已经传播到视口，入html body会将overflow的值传播到视口，故此情况下，该属性不能建立BFC）


## IFC

IFC的line box（线框高度由其包含行内元素中最高的实际高度计算而来（不受到竖直方向的padding/margin影响）

IFC的inline box一般左右都贴紧整个IFC，但是因为float元素二扰乱。float元素会位于IFC与line box之间，使得line box宽度缩短。同个IFC下的多个line box高度会不同。IFC中不可能有块级元素，当插入块级元素时（如p中插入div）会产生两个匿名快与div分隔开，即产生两个IFC，每个IFC对外表现为块级元素，与div垂直排列。

