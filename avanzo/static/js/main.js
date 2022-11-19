// PRUEBAS DE FUNCIONAMIENTO
var switch_bool = localStorage.getItem('switch_bool');

if (switch_bool == null) {
    localStorage.setItem('switch_bool', 'true');
} else {
    if (switch_bool == 'true') {
        localStorage.setItem('switch_bool', 'false');
    } else {
        localStorage.setItem('switch_bool', 'true');
    }
}
console.log("switch bool = " + switch_bool);

btn_example = document.getElementById("btn-example");
if (btn_example != null) {
    btn_example.addEventListener("click", () => { console.log("example clicked"); });
}

// FORMULARIO DE CREDITOS
var form_submit_btn = document.getElementById("form-submit-btn");
if (form_submit_btn != null) {
    form_submit_btn.addEventListener("click", () => {
        var form = document.getElementById("form-creditos");
        console.log("Form:", form);
        var form_data = new FormData(form);
        var form_data_json = JSON.stringify(Object.fromEntries(form_data));
        console.log("Credito Form",form_data_json);
        /*var xhr = new XMLHttpRequest();
        xhr.open("POST", "/creditos", true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(form_data_json);*/
    });
}
