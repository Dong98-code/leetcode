/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
 var findAllRecipes = function(recipes, ingredients, supplies) {
    let ans = new Array();
    while (supplies.length !== 0) {
        let s = supplies.shift();

        for (let i=0;i<ingredients.length;i++) {
            let ingredient = ingredients[i];
            if (ingredient.length === 0) {
                continue;
            }
            if (ingredient.includes(s)) {
                let index = ingredient.indexOf(s);
                ingredient.splice(index, 1);
            }
            if (ingredient.length === 0) {
                ans.push(recipes[i]);
                supplies.push(recipes[i]);
            }
        }
    }
    return ans;
};
recipes = ["bread"], ingredients = [["yeast", "flour"]], supplies = ["yeast", "flour", "corn"]
console.log(findAllRecipes(recipes, ingredients, supplies))