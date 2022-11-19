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

example = () => {
    console.log("example clicked");
}

btn_example.addEventListener("click", example);



