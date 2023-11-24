// Recuperar valores seleccionados de localStorage
const option1 = localStorage.getItem("Keys");
const option2 = localStorage.getItem("select_dec_cif");

// Establecer valores seleccionados en los selects
document.getElementById("Keys").value = option1;
document.getElementById("select_dec_cif").value = option2;

// Guardar valores seleccionados en localStorage al enviar el formulario
document.querySelector("form").addEventListener("submit", function () {
    localStorage.setItem("Keys", document.getElementById("Keys").value);
    localStorage.setItem("select_dec_cif", document.getElementById("select_dec_cif").value);
});