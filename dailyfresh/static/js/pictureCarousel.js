$(function () {
    var time = 0;
    //初始化
    var size = $(".img li").size();  //获取图片的个数
    for (var i = 1; i <= size; i++) {	//创建图片个数相对应的底部数字个数
        var li;
        if (i == 1) {
            var li = "<li class='selected' href='#'><a></a></li>";	//创建li标签，并插入到页面中
        } else {
            var li = "<li href='#'><a></a></li>";
        }
        $(".num").append(li);
    }

    //手动控制图片轮播
    $(".img li").eq(0).show();	//显示第一张图片
    $(".num li").eq(0).addClass("active");	//第一张图片底部相对应的数字列表添加active类
    $(".num li").mouseover(function () {
        $(this).addClass("selected").siblings().removeClass("selected");  //鼠标在哪个数字上那个数字添加class为active
        var index = $(this).index();  //定义底部数字索引值
        i = index;  //底部数字索引值等于图片索引值
        $(".img li").eq(index).stop().fadeIn(2000).siblings().stop().fadeOut(2000);	//鼠标移动到的数字上显示对应的图片
    })

    //自动控制图片轮播
    var i = 0;  //初始i=0
    var t = setInterval(move, 2500);  //设置定时器，2.5秒切换下一站轮播图
    //向左切换函数
    function moveL() {
        i--;
        if (i == -1) {
            i = size - 1;  //如果这是第一张图片再按向左的按钮则切换到最后一张图
        }
        $(".num li").eq(i).addClass("selected").siblings().removeClass("selected");  //对应底部数字添加背景
        $(".img li").eq(i).fadeIn(2000).siblings().fadeOut(2000);  //对应图片切换
    }

    //向右切换函数
    function move() {
        i++;
        if (i == size) {
            i = 0;  //如果这是最后一张图片再按向右的按钮则切换到第一张图
        }
        $(".num li").eq(i).addClass("selected").siblings().removeClass("selected");  //对应底部数字添加背景
        $(".img li").eq(i).fadeIn(2000).siblings().fadeOut(2000);  //对应图片切换
    }

    $(".btn").mouseover(function () {
        //实现透明渐变，阻止冒泡
        $(this).css("background", "rgba(0,0,0,0.5)");
        return false;
    })
    $(".btn").mouseleave(function () {
        //实现透明渐变，阻止冒泡
        $(this).css("background", "rgba(0,0,0,0.3)");
        return false;
    })
    //左按钮点击事件	(在动画完成前多次点击只有一次有效)
    $(".out .left").click(function () {

        //判断计时器是否处于关闭状态
        if (time == 0) {
            time = 2; //设定间隔时间（秒）	对应淡入淡出(动画)时间

            //启动计时器，倒计时time秒后自动关闭计时器。
            var index = setInterval(function () {
                time--;
                if (time == 0) {
                    clearInterval(index);
                }
            }, 1000);

            moveL();	//点击左键调用向左切换函数
        } else {
            return;
        }


    })
    //右按钮点击事件	(在动画完成前多次点击只有一次有效)
    $(".out .right").click(function () {
        //判断计时器是否处于关闭状态
        if (time == 0) {
            time = 2; //设定间隔时间（秒）	对应淡入淡出(动画)时间

            //启动计时器，倒计时time秒后自动关闭计时器。
            var index = setInterval(function () {
                time--;
                if (time == 0) {
                    clearInterval(index);
                }
            }, 1000);

            move();    //点击右键调用向右切换函数
        } else {
            return;
        }

    })
    //定时器开始与结束
    $(".out").hover(function () {
        clearInterval(t);	//鼠标放在轮播区域上时，清除定时器
    }, function () {
        t = setInterval(move, 2500);  //鼠标移开时定时器继续
    })
})