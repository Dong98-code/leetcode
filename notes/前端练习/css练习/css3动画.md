# @keyframes

![20220418151953](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220418151953.png)

# animation

将关键帧绑定到dom属性上去；

## name

关键帧的名称

```css
animation-name: keyframename|none;
// keyframename 指定要绑定到选择器的关键帧的名称

```

## animation-duration

```css
animation-duration: time;
// time 指定动画播放完成花费的时间。

```

## animation-timing-function

指定动画将如何完成一个周期

```css
animation-timing-function: value;

```

![20220418152336](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220418152336.png)


## animation-delay 

动画什么时候开始， 单位可以是s或者是ms


```css
animation-delay: time;
// time 定义动画开始前等待的时间，以秒或毫秒计

```

## -iteration-count

```css
animation-iteration-count: value;
//  n 定义应该播放多少次动画
// 	infinite 指定动画应该播放无限次（永远）

```

![20220418152624](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220418152624.png)

![20220418152659](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220418152659.png)

## animation-fill-mode

![20220418152822](https://xd-imgsubmit.oss-cn-beijing.aliyuncs.com/images/20220418152822.png)


# js:动画和css3动画的区别