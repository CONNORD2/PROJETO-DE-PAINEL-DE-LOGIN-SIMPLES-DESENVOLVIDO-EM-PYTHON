document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    var usuario = document.getElementById("usuario").value;
    var senha = document.getElementById("senha").value;

    // Simulação de verificação (em um caso real, você faria uma requisição AJAX para o servidor)
    if (usuario.toUpperCase() === "ADMINISTRADOR" && senha === "love you") {
        alert("Acesso concedido!");
        window.location.href = "/dashboard"; // Redirecionar para outra página (exemplo)
    } else {
        document.getElementById("error-message").style.display = "block";
    }
});
