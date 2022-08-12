var solveEquation = function (equation) {
    let xishu = 0;
    let const_value = 0;
    equation = equation.replaceAll("-", "+-");
    let [left, right] = equation.split('=');
    left = left.split("+"); //已加号分割，如果包含x,则
    for (let item of left) {
        if (item !== "") {
            if (item.includes("x")) {
                // 包含x的项
                if (item === "x") {
                    xishu += 1;
                } else {
                    xishu += +item.split("x")[0];

                }
            } else {
                const_value -= parseInt(item);
            }
        }

    }
    right = right.split("+");
    for (let item of right) {
        if (item !== "") {
            if (item.includes("x")) {
                if (item === "x") {
                    xishu -= 1;
                } else {
                    xishu -= +item.split("x")[0];

                }
                // 包含x的项
            } else {
                const_value += parseInt(item);
            }
        }

    }
    if (xishu === 0) {
        if (const_value === 0) {
            return "Infinite solutions"

        } else {
            return "No solution"
        }
    }
    let value = parseInt(const_value / xishu);
    return "x=" + value;
};

console.log(solveEquation("-x=-1"));