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

// CAMBIAR SIGNO DE PESOS
let x = document.querySelectorAll(".money");
for (let i = 0, len = x.length; i < len; i++) {
    let num = Number(x[i].innerHTML)
              .toLocaleString('en');
    x[i].innerHTML = num;
    x[i].classList.add("currSign");
}

// FORMULARIO DE CREDITOS
var form_creditos = document.getElementById("form-create-credito");
if (form_creditos != null) {
    // recuperar datos del formulario
    // incluso si el formulario no se envía (es decir, no hay conexión) se guardan los datos
    form_creditos.addEventListener("submit", (e) => {
        // e.preventDefault();
        var form_data = new FormData(form_creditos);
        var form_data_json = JSON.stringify(Object.fromEntries(form_data));
        localStorage.setItem('credit_create_data', form_data_json); // guardar datos en memoria local
    });
}

// Recuperar datos del formulario
var credit_create_data = localStorage.getItem('credit_create_data');
if (credit_create_data != null) {
    // enviar petición POST a /creditos/creditocreate
    console.log("Se recuperaron datos para enviar", credit_create_data);

    credit_create_data = JSON.parse(credit_create_data);

    var final_form = new FormData();
    final_form.append("monto", credit_create_data.monto);
    final_form.append("cuotas", credit_create_data.cuotas);
    final_form.append("estado", "PENDIENTE");
    final_form.append("csrfmiddlewaretoken", credit_create_data.csrfmiddlewaretoken);
    
    console.log("Modificado", final_form);

    var xhr = new window.XMLHttpRequest();
    xhr.open("POST", "/creditos/creditocreate", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    resp = xhr.send(final_form);
    console.log("Crédito recuperado y enviado");
    console.log(resp);
    // eliminar datos del formulario
} else {
    console.log("No hay datos almacenados para enviar");
}
