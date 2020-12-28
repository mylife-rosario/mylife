document.getElementById("p2").style.color = "green";
document.getElementById("p2").style.fontFamily = "Garamond";
document.getElementById("p2").style.fontSize = "larger";
document.getElementById("p3").style.color = "white";
document.getElementById("p5").style.color = "white";
document.getElementById("p5").style.fontFamily = "Brush Script MT";
document.getElementById("p5").style.textAlign = "center";
document.getElementById("p7").style.textAlign = "center";
document.getElementsByName("grupo1").style.color = "white";

function mOver(obj) {
    obj.innerHTML = "¡¡ Vamos contactanos !!"
  }
  
  function mOut(obj) {
    obj.innerHTML = "Contacto"
  }


  function mOver2(obj) {
    obj.innerHTML = "¡¡ Vamos ¿¿ Que es este sitio web!! ??"
  }
  
  function mOut2(obj) {
    obj.innerHTML = "Quienes Somos"
  }

  function mOver3(obj) {
    obj.innerHTML = "¡¡ Vamos inicia o logeate !!"
  }
  
  function mOut3(obj) {
    obj.innerHTML = "Inicio"
  }

  function mOver4(obj) {
    obj.innerHTML = "Salida exitos!!"
  }
  
  function mOut4(obj) {
    obj.innerHTML = "About"
  }


  function mOver5(obj) {
    obj.innerHTML = "Vamos a Ingresar!!"
  }
  
  function mOut5(obj) {
    obj.innerHTML = "Inicia sesion"
  }



  function mOver6(obj) {
    obj.innerHTML = "Vamos a Registrarte es simple !!"
  }
  
  function mOut6(obj) {
    obj.innerHTML = "Registrar Usuario"
  }




  function mOver7(obj) {
    obj.innerHTML = "Vamos a Registrarte es simple !!"
  }
  
  function mOut7(obj) {
    obj.innerHTML = "Registrar Usuario"
  }




document.getElementById("myBtn").addEventListener("click", function() {alert("Hola Inicia session!!");});


function myFunction() {
    var txt;
    var person = prompt("Porfavor ingresa tu nombre:", "-------");
    if (person == null || person == "") {
      txt = "User cancelled the prompt.";
    }
    document.getElementById("p3").innerHTML = txt;
  }









  