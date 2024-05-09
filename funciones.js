//FUNCION DEFINIDA PARA HACER TOOGLE SEGUN SU ID, APLICANDO LA CLASE SHOW Y NOSHOW
  function toggleFunc(id) {
    let ele = document.getElementById(id).nextElementSibling;
    let child = document.getElementById(id).firstElementChild;
    console.log(child)

    if (ele.classList.contains("submenu-noshow")) {
      ele.classList.toggle("submenu-show");
      child.classList.toggle("rotate");
    } else {
      ele.classList.toggle("submenu-noshow");
      child.classList.toggle("rotate");
    };
  };

  