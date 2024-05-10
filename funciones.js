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
    };
  };

  //FUNCION DEFINIDA PARA BUSCAR POR ID DE "productoX" ( x=numero --> producto1, producto2), el nombre de la imagen para a partir de ese dato, depurarlo para conseguir que se refleje en el titulo del card
  // LA FUNCION ESTA ARMADA PARA CARGAR CON LA PAGINA Y AUTO OBTIENE EL ID, POR LO CUAL id="productoX" onload="productName(this.id) DEBE SER PUESTO EN TODOS LOS IMGS DE CADA CARD
  function productName(id){
    //constante regular para limpiar de la ruta del archivo, el nombre del producto
    const regex = /\/([^\/]+)\.\w+$/;
    //let nombre busca por id, el src de la imagen y apica la limpieza
    let nombre = document.getElementById(id).getAttribute("src").match(regex)[1];
    //let titulo busca dentro del card el contenedor h5, y escribe como contenido html lo almacenado en la variable nombre
    let titulo = document.getElementById(id).nextElementSibling.firstElementChild;
    titulo.innerHTML = nombre;  
  };
  
  
  

  
