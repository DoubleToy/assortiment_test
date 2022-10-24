window.onload = function (){
    var d = document.querySelector('#id_selectionoperation_set-0-operation');
    d.onchange = async function (e) {
        console.log(e.target.value)
        let url = 'http://127.0.0.1:8000/technologist/operations/';
        let response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
                "id": e.target.value
            }),
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            }
        });

        let period = await response.json();
        console.log(period)

        var t = document.querySelector('#id_selectionoperation_set-0-time');
        t.value = period.time
    }
    var a = document.querySelector('#id_selectionoperation_set-1-operation');
    a.onchange = async function (b) {
        console.log(b.target.value)
        let url = 'http://127.0.0.1:8000/technologist/operations/';
        let response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
                "id": b.target.value
            }),
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            }
        });

        let period = await response.json();
        console.log(period)

        var t = document.querySelector('#id_selectionoperation_set-1-time');
        t.value = period.time
    }
    var c = document.querySelector('#id_selectionoperation_set-2-operation');
    c.onchange = async function (h) {
        console.log(h.target.value)
        let url = 'http://127.0.0.1:8000/technologist/operations/';
        let response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
                "id": h.target.value
            }),
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            }
        });

        let period = await response.json();
        console.log(period)

        var t = document.querySelector('#id_selectionoperation_set-2-time');
        t.value = period.time
    }

    let n = null;
    let inter = setInterval(() => {
        n = document.querySelector('.add-inline-link');
        if (n){
            nIsRaddy(n)
            clearInterval(inter);
        }
    }, 100);

}

function nIsRaddy(elem){
    var l = 2;
    var q = 2;
    elem.onclick = function (e) {
        l += 1;
        q += 1;
        var k = 'id_selectionoperation_set--operation';
        var w = 'id_selectionoperation_set--time';
        k = '#id_selectionoperation_set-' + l + '-operation';
        w = '#id_selectionoperation_set-' + q + '-time';
        console.log(k)
        console.log(w)
        var m = document.querySelector(k);
        m.onchange = async function (v) {
            console.log(v);
            let url = 'http://127.0.0.1:8000/technologist/operations/';
            let response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
                "id": v.target.value
            }),
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            }
        });

        let period = await response.json();
        console.log(period)

        var t = document.querySelector(w);
        t.value = period.time
        }
    }
}