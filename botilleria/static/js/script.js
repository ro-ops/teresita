function validarCorreo(){
    var correo = document.getElementById("mail").nodeValue;

    if(correo == null || correo.length == 0 || !(/^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3,4})+$/.test(correo))){
        alert("Formato de Correo inválido");
    }
}
$(function() {
    $("#mi-formulario").validate({
      rules: {
        email: {
          required: true,
          email: true
        },
        nombre:{
            required: true,
            email: true

        },
        telefono:{
            required: true,
            email: true

        }
      },

      messages: {
        email: {
          required: 'Ingresa tu correo electrónico' ,
          email: 'Formato de correo no válido'
        },
        nombre: {
          required: 'Ingresa su nombre',
          minlength: 'Largo insuficiente'
        },
        telefono: {
          required: 'Ingresa su telefono',
        }
      }
    });
  });

var today = new Date().toISOString().split('T')[0];
document.getElementsByName("somedate")[0].setAttribute('min', today);