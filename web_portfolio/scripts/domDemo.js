console.log(document);

const depositSavings = function() {
    var td_node = document.getElementById("savingsBalance");
    console.log(td_node);
    var balance_str = td_node.textContent;
    var balance_num = Number(balance_str);
    balance_num += 100;
    td_node.textContent = balance_num;
}