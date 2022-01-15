var api = "https://web-series-quotes-api.deta.dev/pic"

function make_link() {
    var dis = document.getElementById('dis');
    var c = document.getElementsByName('c')[0].value;
    var src = document.getElementsByName('src')[0].value;
    var s = document.getElementsByName('s')[0].value;
    var id = document.getElementsByName('id')[0].value;
    var font = document.getElementsByName('font')[0].value;
    var link = `${api}/series=${s}&id=${id}&background_img_url=${src}&text_color=${c}&text_size=${font}`
    dis.innerHTML = link;
    dis.style.display = "block"
}

function open_link() {
    var dis = document.getElementById('dis');
    var c = document.getElementsByName('c')[0].value;
    var src = document.getElementsByName('src')[0].value;
    var s = document.getElementsByName('s')[0].value;
    var id = document.getElementsByName('id')[0].value;
    var font = document.getElementsByName('font')[0].value;
    var link = `${api}/image?series=${s}&id=${id}&background_img_url=${src}&text_color=${c}&text_size=${font}`
    dis.innerHTML = link;
    dis.style.display = "block"
    window.open(link)
}

function make_link_2() {
    var dis = document.getElementById('dis');
    var fc = document.getElementsByName('fc')[0].value;
    var bc = document.getElementsByName('bc')[0].value;
    var text = document.getElementsByName('text')[0].value;
    var x = document.getElementsByName('x')[0].value;
    var y = document.getElementsByName('y')[0].value
    var link = `${api}/custom?text_color=${fc}&background_color=${bc}&text=${text}&x=${x}&y=${y}`
    dis.innerHTML = link;
    dis.style.display = "block"
}

function open_link_2() {
    var dis = document.getElementById('dis');
    var fc = document.getElementsByName('fc')[0].value;
    var bc = document.getElementsByName('bc')[0].value;
    var text = document.getElementsByName('text')[0].value;
    var x = document.getElementsByName('x')[0].value;
    var y = document.getElementsByName('y')[0].value
    var link = `${api}/custom?text_color=${fc}&background_color=${bc}&text=${text}&x=${x}&y=${y}`
    dis.innerHTML = link;
    dis.style.display = "block"
    window.open(link)
}

function open_form_1() {
    a = document.getElementById('b1')
    b = document.getElementById('b2')
    a.style.color = "red"
    b.style.color = "white"
    x = document.getElementById('form1');
    y = document.getElementById('form2');
    y.style.display = "none"
    x.style.display = "block";
}

function open_form_2() {
    b = document.getElementById('b2')
    a = document.getElementById('b1')
    b.style.color = "red"
    a.style.color = "white"
    x = document.getElementById('form2');
    y = document.getElementById('form1');
    y.style.display = "none"
    x.style.display = "block"
}
