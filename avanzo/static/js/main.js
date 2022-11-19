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

var form_creditos = document.getElementById("form-create-credito");
if (form_creditos != null) {
    form_creditos.addEventListener("submit", (e) => {
        e.preventDefault();
        var form_data = new FormData(form_creditos);
        var form_data_json = JSON.stringify(Object.fromEntries(form_data));
        console.log(form_data_json);
        localStorage.setItem('credit_create_data', form_data_json);
        window.location.href = "/creditos/";
    });
}
