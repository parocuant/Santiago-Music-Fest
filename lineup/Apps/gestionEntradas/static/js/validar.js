function validar(){
    var nombre,contraseña,telefono,email,apellidos,rcontraseña;
    nombre = document.getElementById("nombre").value;
    telefono= document.getElementById("telefono").value;
    contraseña = document.getElementById("contraseña").value;
    email = document.getElementById("email").value;
    apellidos = document.getElementById("apellidos").value;
    rcontraseña = document.getElementById("rcontraseña").value


    expresion = /\w+@\w+\.+[a-z]/ ;

    if(nombre === "" || telefono === "" || email === "" || contraseña === "" || apellidos === "" || rcontraseña === "")
    {
        alert("Todos los campos son obligatorios");
        return false;
    }
    else if (nombre.length>30)
    {
        alert("El nombre es muy largo");
        return false;
    }
    else if (apellidos.length>30)
    {
        alert("Los apellidos son muy largos");
        return false;
    }
    else if (email.length>30)
    {
        alert("El email es muy largo");
        return false;
    }
    else if(!expresion.test(email)){
        alert("El correo no es valido");
        return false;
    }

    else if (contraseña.length>20)
    {
        alert("La clave no debe exceder los 20 caracteres");
        return false;
    }
    else if (telefono.length>10)
    {
        alert("El telefono es muy largo");
        return false;
    }
    else if (isNaN(telefono))
    {
        alert("El teléfono ingresado no es valido");
        return false;
    }

    if(contraseña != rcontraseña)
    {
        alert("Las contraseñas deben coincidir");
        return false;
    }
}