//FUNCION DEFINIDA PARA HACER TOOGLE SEGUN SU ID, APLICANDO LA CLASE SHOW Y NOSHOW
function toggleFunc(id) {
    let ele = document.getElementById(id).nextElementSibling;

    if (ele.classList.contains("submenu-noshow")) {
      ele.classList.toggle("submenu-show");
    }
  }