document.addEventListener("DOMContentLoaded", function() {
  // Obtener el mensaje de error del atributo "data-error" del elemento HTML
  var errorMessage = document.getElementById("error-message").getAttribute("data-error");

  // Mostrar el mensaje de error en rojo con letras blancas cuando ocurra un error
  if (errorMessage) {
    var errorElement = document.getElementById("error-message");
    errorElement.innerText = errorMessage;
    errorElement.style.display = "block";

    // Desaparecer el mensaje de error después de 8 segundos
    setTimeout(function() {
      errorElement.style.display = "none";
    }, 8000);
  } else {
    // Ocultar el mensaje de error si no hay ningún error
    var errorElement = document.getElementById("error-message");
    errorElement.style.display = "none";
  }
});
