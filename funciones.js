//FUNCION DEFINIDA PARA HACER TOOGLE SEGUN SU ID, APLICANDO LA CLASE SHOW Y NOSHOW
function toggleFunc(id) {
  let ele = document.getElementById(id).nextElementSibling;
  let child = document.getElementById(id).firstElementChild;
  if (ele.classList.contains("submenu-noshow")) {
    ele.classList.toggle("submenu-show");
    child.classList.toggle("rotate");
  } else {
    ele.classList.toggle("submenu-noshow");
    child.classList.toggle("rotate");
  }
}

//FUNCION DEFINIDA PARA BUSCAR POR ID, el nombre de la imagen para a partir de ese dato, depurarlo para conseguir que se refleje en el titulo del card
// LA FUNCION ESTA ARMADA PARA CARGAR CON LA PAGINA Y AUTO OBTIENE EL ID,
function productName(id) {
  //constante regular para limpiar de la ruta del archivo, el nombre del producto
  const regex = /\/([^\/]+)\.\w+$/;
  //let nombre busca por id, el src de la imagen y apica la limpieza
  let nombre = document.getElementById(id).getAttribute("src").match(regex)[1];
  //let titulo busca dentro del card el contenedor h5, y escribe como contenido html lo almacenado en la variable nombre
  let titulo = document.getElementById(id).nextElementSibling.firstElementChild;
  titulo.innerHTML = nombre;
};
//FUNCION PARA GENERAR UN NUMERO ALEATORIO Y RETORNAR EL VALOR PARA PODER SER UTILIZADO
function numeroRandom() {
  let nrandom = Math.floor(Math.random() * 2000 + 1);
  return nrandom.toString(); // Convertir el número en una cadena
};
//FUNCION QUE GENERA UN ID EN BASE A LA FUNCION numeroRandom(), ACCEDE A LOS ELEMENTOS DE CLASE CARD, PARA LUEGO RECORRERLOS Y ACCEDER A CADA ELEMENTO DE IMG Y H6, EN EL ELEMENTO IMG INSERTA EL ATRIBUTO ID Y EN EL ELEMENTO H6 INSERTA EL PRECIO.
function idRandom() {
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let img = cards[i].querySelector("img");
    if (img) {
      let randomId = numeroRandom();
      img.setAttribute("id", randomId);
      let h6 = cards[i].querySelector("h6");
      if (h6) {
        let precio = parseInt(randomId) * 1050;
        h6.textContent = "Precio: $" + precio;
      }      
    }
  }

}

//FUNCION DE VALIDACION DE FORMULARIO
function validarFormulario(event){
  const regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  let nombre = document.getElementById("nombre").value;
  let apellido = document.getElementById("apellido").value;
  let email = document.getElementById("email").value;

  if(nombre.length < 2){
    alert("El nombre debe contener al menos 2 caracteres.");
    event.preventDefault();
    return false;    
  }

  if(apellido.length < 1){
    alert("El apellido debe contener al menos 1 caracter.");
    event.preventDefault();
    return false;    
  }

  if(!regex.test(email)){
    alert("Email invalido.");
    event.preventDefault();
    return false;   
  }


  return true;
};
a