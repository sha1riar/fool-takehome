"use strict";

function test(){
    let stockList = document.getElementById('stockList');
    let stocks = [];
    for(let i of stockList.children){
        stocks.push(i);
        stockList.removeChild(i);
    }
    stocks = shuffle(stocks);
    for(let j of stocks){
        stockList.appendChild(j);
    }
}

function shuffle(a) {
    let j, temp, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    return a;
}